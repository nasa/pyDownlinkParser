"""Converters used for Europa-Clipper CCSDS packets."""
import logging
import math
from enum import IntEnum

import bitstring
import pandas
from ccsdspy.converters import Converter
from tqdm import tqdm

logger = logging.getLogger(__name__)

SF_SIZE_BITS: int = 64
sample_count = None


class SCIOType(IntEnum):
    """Enumeration of the waveform types."""

    EVT_HDR = 0x01
    TOF_HG = 0x02
    TOF_LG = 0x04
    TOF_MG = 0x08
    CSA_QV = 0x10
    CSA_QT = 0x20
    CSA_QI = 0x40


LOW_RESOLUTION_BITS = 10
HIGH_RESOLUTION_BITS = 12


# TODO: Work in progress, the converter is not finalized, needs to be fully migrated to CCSDSpy environment
class RICEDecompressor(Converter):
    """Converter to de-compress RICE encoded field."""

    data_resolution_bits = {
        SCIOType.EVT_HDR: None,
        SCIOType.TOF_HG: LOW_RESOLUTION_BITS,
        SCIOType.TOF_LG: LOW_RESOLUTION_BITS,
        SCIOType.TOF_MG: LOW_RESOLUTION_BITS,
        SCIOType.CSA_QV: HIGH_RESOLUTION_BITS,
        SCIOType.CSA_QT: HIGH_RESOLUTION_BITS,
        SCIOType.CSA_QI: HIGH_RESOLUTION_BITS,
    }

    def __init__(self):
        """Initialization."""
        self.latest_hs_pre = None
        self.latest_hs_post = None
        self.latest_ls_pre = None
        self.latest_ls_post = None

    @classmethod
    def get_elt_size(cls, sciotype: SCIOType):
        """Get the size of waveform elements, either low or high resolution.

        :param sciotype: SCIOTYPE property in the current packet
        :return: the size (resolution) of the elements stored the data field of the packet as described in `SUDA FSW Science Packets White Paper`, section 1
        """
        return cls.data_resolution_bits[sciotype]

    def rice_decode(self, data_stream: bitstring.ConstBitStream, n_bits, rice_k):
        """Decode the dat field."""
        # get the q value encoded as unary
        rice_q = 0
        while data_stream.read(1).uint == 0:
            rice_q += 1

        if rice_q == 47:  # limit beyond which residuals are encoded as binary
            return data_stream.read(n_bits + 2).int
        else:
            if rice_q & 0x1:  # odd
                rice_q = int(-((rice_q + 1) >> 1))
            else:  # even
                rice_q = int(rice_q >> 1)

            rice_r = data_stream.read(rice_k + 1).uint
            return (rice_q << (rice_k + 1)) + rice_r

    def constant(
        self, data_stream: bitstring.ConstBitStream, n_bits=12, sf_size=SF_SIZE_BITS
    ):
        """Constant stream, specific decoding algorithm."""
        output = []
        try:
            sample = data_stream.read(n_bits).uint
            for _ in range(sf_size):
                output.append(sample)
            return output
        except IndexError:
            logger.debug("input stream is finished")

    def verbatim(
        self, data_stream: bitstring.ConstBitStream, n_bits=12, sf_size=SF_SIZE_BITS
    ):
        """Uncompressed data stream."""
        output = []

        try:
            for _ in range(sf_size):
                sample = data_stream.read(n_bits).uint
                output.append(sample)
                return output
        except IndexError:
            logger.debug("input stream is finished")

    def rice_decode_linear(
        self,
        data_stream: bitstring.ConstBitStream,
        n_bits=12,
        sf_size=SF_SIZE_BITS,
        rice_k_bits=4,
        linear_number=1,
    ):
        """RICE compressed data stream."""
        output = []
        try:
            rice_k = data_stream.read(rice_k_bits).uint

            for _ in range(linear_number):
                sample = data_stream.read(n_bits).uint
                output.append(sample)

            while len(output) < sf_size:
                residual = self.rice_decode(data_stream, n_bits, rice_k)
                slope = output[-1] - output[-2] if linear_number == 2 else 0
                output.append(output[-1] + slope + residual)
            return output
        except IndexError:
            logger.debug("input stream is finished")

    @staticmethod
    def check_overflow(output):
        """Check if the data element do not overflow what is expected in the RICE compression."""
        for v in output:
            if v > 2**12 or v < -(2**12):
                # logger.error(f"output overflow {v}")
                return True
        return False

    @classmethod
    def compute_sample_count(cls, size: int, pre, post):
        """Compute the number of samples.

        @param size: in bits
        @param pre: from the block metadata section
        @param post: from the block metadata section
        @return: the number of samples expected
        """
        return size * (pre + 1 + post + 1)

    def get_current_sample_count(self, type: SCIOType):
        """Return the number of sample expected for a given packets.

        Return the number of sample expected for a given packets using its
        SCIOTYPE and the block sizes found in the preceding metadata packet

        @param type: SCIOTYPE of the current packet
        @return: the number of sample expected
        """
        if type == SCIOType.TOF_HG:
            self.latest_hs_pre = next(self.hs_pre)
            self.latest_hs_post = next(self.hs_post)
            self.latest_ls_pre = next(self.ls_pre)
            self.latest_ls_post = next(self.ls_post)

        if type in {SCIOType.TOF_HG, SCIOType.TOF_LG, SCIOType.TOF_MG}:
            sample_count = self.compute_sample_count(
                512, self.latest_hs_pre, self.latest_hs_post
            )
        elif type in {SCIOType.CSA_QV, SCIOType.CSA_QT, SCIOType.CSA_QI}:
            sample_count = self.compute_sample_count(
                8, self.latest_ls_pre, self.latest_ls_post
            )

        return sample_count

    def convert(self, sciotype, sciofrag, data_array):
        """Decompress all the data of all the packets.

        @param sciotype: list of the sciotype values
        @param sciofrag: list of the sciofrag values
        @param data_array: list of the compressed data fields
        @return: the list of the uncompressed data fields
        """
        decompressed_data = []
        data_buffer = []

        for wf_data, wf_type, wf_frag in tqdm(
            zip(data_array, sciotype, sciofrag), total=len(sciotype)
        ):

            if wf_frag == 1:
                # we don't decompress the data in this packet
                data_buffer += wf_data.tolist()
                decompressed_data.append([])
            else:
                wf_data = data_buffer + wf_data.tolist()
                data_buffer = []
                wf_type = SCIOType(wf_type)
                elt_size_bits = self.get_elt_size(wf_type)
                sample_count = self.get_current_sample_count(wf_type)
                decompressed_field = self.convert_row(
                    wf_data, elt_size_bits, sample_count
                )
                decompressed_data.append(decompressed_field)

        return decompressed_data

    def convert_row(self, data: list, n_bits: int, sample_count: int) -> list:
        """RICE decompression."""
        output = []
        data_stream = bitstring.ConstBitStream(bytes=bytearray(data))

        rice_k_bits = math.ceil(math.log2(n_bits))

        try:
            while len(output) < sample_count:
                # read piece of SF_SIZE values
                frame = []
                predictor = data_stream.read(2).uint
                if predictor == 0b00:  # Constant
                    frame = self.constant(
                        data_stream, n_bits=n_bits, sf_size=SF_SIZE_BITS
                    )
                elif predictor == 0b01:  # Verbatim
                    frame = self.verbatim(
                        data_stream, n_bits=n_bits, sf_size=SF_SIZE_BITS
                    )
                elif predictor == 0b10:  # Linear Predictor #1
                    frame = self.rice_decode_linear(
                        data_stream,
                        n_bits=n_bits,
                        sf_size=SF_SIZE_BITS,
                        rice_k_bits=rice_k_bits,
                        linear_number=1,
                    )
                elif predictor == 0b11:  # Linear Predictor #2
                    frame = self.rice_decode_linear(
                        data_stream,
                        n_bits=n_bits,
                        sf_size=SF_SIZE_BITS,
                        rice_k_bits=rice_k_bits,
                        linear_number=2,
                    )
                else:
                    logger.error(
                        "Unexpected predictor in suda event uncompressed data stream"
                    )

                output.extend(frame)

                if self.check_overflow(frame):
                    logger.error(
                        f"overflow in frame produced with predictor {predictor}"
                    )
            return output

        except IndexError:
            logger.debug("input stream is finished")

    def set_pre_post(self, df: pandas.DataFrame):
        """Set the ls/hs pre/post attributes used to compute the size of the waveform."""
        self.ls_post = iter(df["NBLOCKS_LS_POST"].to_list())
        self.ls_pre = iter(df["NBLOCKS_LS_POST"].to_list())
        self.hs_post = iter(df["NBLOCKS_HS_POST"].to_list())
        self.hs_pre = iter(df["NBLOCKS_HS_PRE"].to_list())
