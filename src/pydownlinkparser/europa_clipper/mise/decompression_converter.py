"""Fast loose-less decompression converter."""
import logging

import numpy as np
from bitstring import ConstBitStream
from bitstring import ReadError
from ccsdspy.converters import Converter

logger = logging.getLogger(__name__)


class MISEDecompressionConverter(Converter):
    """Converter user to uncompress the MISE packets using fast loose-less compression."""

    compressed_block_size = 16
    packet_header_length_bits = 80

    def __init__(
        self,
        uncompressed_item_mask=0x3FFF,
        data_length_without_frame_bytes=0,
        default_initial_value=None,
        differences_stored=False,
        width_encoding_bits=4,
    ):
        """Initialization of the decompressor with parameters depending on the configuration of the compression.

        @param uncompressed_item_mask:
        @param data_length_without_frame_bytes:
        @param default_initial_value: when there is no default value found at the beginning of the compressed stream.
        @param differences_stored:
        @param width_encoding_bits:
        """
        self.uncompressed_item_mask = uncompressed_item_mask
        self.data_length_without_frame_bytes = data_length_without_frame_bytes
        self.default_initial_value = default_initial_value
        self.differences_stored = differences_stored
        self.width_encoding_bits = width_encoding_bits

    def convert(self, *args):
        """Convert."""
        compressed_fields = args[0]
        if len(args) == 3:
            window_columns_lst = args[1]
            column_binning_lst = args[2]
            column_number_lst = window_columns_lst / 2**column_binning_lst
        elif len(args) == 1:
            column_number_lst = np.full((len(compressed_fields),), 320)

        uncompressed_fields = []
        for column_number, compressed_field in zip(
            column_number_lst, compressed_fields
        ):

            compressed_stream = ConstBitStream(bytearray(compressed_field))

            if self.default_initial_value is None:
                initial_value = compressed_stream.read(14).uint
            else:
                initial_value = self.default_initial_value

            uncompressed_field = self.mise_decomp(
                compressed_stream,
                initial_value=initial_value,
                row_number=4,
                column_number=int(column_number),
            )
            uncompressed_fields.append(uncompressed_field)
        return uncompressed_fields

    def unpack_value(self, delta_code, ref_value=None):
        """Unpack a single compressed value.

        param: ref_value value of the previous reference pixel
        param: delta_code binary code of the difference with the previous reference pixel
        returns: the current pixel value
        """
        delta_int = int(delta_code, base=2)

        if self.differences_stored:
            delta_value = ~(delta_int >> 1) if delta_int & 0x01 else delta_int >> 1
            # errata sent by John Hayes on 2023/-2/14
            # see https://wiki.jpl.nasa.gov/display/jeowiki/SDS+MISE+Meetings, - becomes a +
            return (ref_value + delta_value) & self.uncompressed_item_mask
        else:
            return delta_int & self.uncompressed_item_mask

    def mise_decomp(
        self,
        seq: ConstBitStream,
        initial_value: int,
        row_number: int,
        column_number: int,
    ):
        """Fast loose-less decompression.

        Implements the following uncompression algorithm, in pseudo-C
        See specification in MISE Flight Software Specification 7489-9100, 8.3.1.2
        pp = read(14bits) // first pixel

        for each row in strip
            for each code block in row
                w = read(4bits)
                for each value in block // 16 values, 1-16 in last
                    ∆code = read(w bits)
                    ∆f = (∆code & 0x01) ? ~(∆code >> 1): (∆code >> 1)
                // errata sent by John Hayes on 2023/-2/14
                // see https://wiki.jpl.nasa.gov/display/jeowiki/SDS+MISE+Meetings, - becomes a +
                p[i, j] = (pp + ∆f) & 0x3fff
                pp = p[i, j]

            pp = p[i, 0]

        Where read(n) is a function that reads next n bits
        Note: read(0) returns 0.

        @param seq: compressed stream as a ConstBitStream
        @param initial_value: initial value
        @param row_number: number of rows in each block (default 4)
        @param column_number: number of column in each block.
        @return: the decompressed stream a list of values.
        """
        value = initial_value
        decompressed_data: list(int) = []

        try:
            for _ in range(row_number):
                # each block codes 16 values, except the last one which contains the remaining values
                for block_start in range(0, column_number, self.compressed_block_size):
                    w = seq.read(f"uint:{self.width_encoding_bits}")
                    block_end = min(
                        block_start + self.compressed_block_size, column_number
                    )
                    for bit_packet_value_j in range(block_start, block_end):
                        # this line implements  --> Note: read(0) returns 0 in the pseudo code above
                        delta_code = seq.read(w) if w > 0 else ConstBitStream("0b0")
                        value = self.unpack_value(delta_code.bin, ref_value=value)
                        # first value of the row is used as a reference for the upper-row first value
                        if bit_packet_value_j == 0:
                            pi0 = value
                        decompressed_data.append(value)
                value = pi0  # noqa
        except ReadError as e:
            logger.error("error while reading compressed frame", e)
            raise e

        return decompressed_data
