"""Converters used for Europa-Clipper CCSDS packets."""
import logging
import math

import bitstring
from ccsdspy import converters

logger = logging.getLogger(__name__)

SF_SIZE_BITS: int = 64
sample_count = None


# TODO: Work in progress, the converter is not finalized, needs to be fully migrated to CCSDSpy environment
class RICEDecompressor(converters):
    """Converter to de-compress RICE encoded field."""

    def rice_decode(self, in_bit_stream: bitstring.ConstBitStream, n_bits, rice_k):
        """Decode the dat field."""
        # get the q value encoded as unary
        rice_q = 0
        while in_bit_stream.read(1).uint == 0:
            rice_q += 1

        if rice_q == 47:  # limit beyond which residuals are encoded as binary
            return in_bit_stream.read(n_bits + 2).int
        else:
            if rice_q & 0x1:  # odd
                rice_q = int(-((rice_q + 1) >> 1))
            else:  # even
                rice_q = int(rice_q >> 1)

            rice_r = in_bit_stream.read(rice_k + 1).uint
            return (rice_q << (rice_k + 1)) + rice_r

    def constant(
        self, in_bit_stream: bitstring.ConstBitStream, n_bits=12, sf_size=SF_SIZE_BITS
    ):
        """Constant stream, specific decoding algorithm."""
        output = []
        try:
            sample = in_bit_stream.read(n_bits).uint
            for _ in range(sf_size):
                output.append(sample)
            return output
        except IndexError:
            logger.debug("input stream is finished")

    def verbatim(
        self, in_bit_stream: bitstring.ConstBitStream, n_bits=12, sf_size=SF_SIZE_BITS
    ):
        """Uncompressed data stream."""
        output = []
        try:
            for _ in range(sf_size):
                sample = in_bit_stream.read(n_bits).uint
                output.append(sample)
                return output
        except IndexError:
            logger.debug("input stream is finished")

    def rice_decode_linear(
        self,
        in_bit_stream: bitstring.ConstBitStream,
        n_bits=12,
        sf_size=SF_SIZE_BITS,
        rice_k_bits=4,
        linear_number=1,
    ):
        """RICE compressed data stream."""
        output = []
        try:
            rice_k = in_bit_stream.read(rice_k_bits).uint

            for _ in range(linear_number):
                sample = in_bit_stream.read(n_bits).uint
                output.append(sample)

            while len(output) < sf_size:
                residual = self.rice_decode(in_bit_stream, n_bits, rice_k)
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

    def convert(
        self, in_bit_stream: bitstring.ConstBitStream
    ) -> bitstring.ConstBitStream:
        """RICE decompression."""
        output = []
        n_bits = 12

        rice_k_bits = math.ceil(math.log2(n_bits))

        try:
            while len(output) < sample_count:
                # read piece of SF_SIZE values
                frame = []
                predictor = in_bit_stream.read(2).uint
                if predictor == 0b00:  # Constant
                    frame = self.constant(
                        in_bit_stream, n_bits=n_bits, sf_size=SF_SIZE_BITS
                    )
                elif predictor == 0b01:  # Verbatim
                    frame = self.verbatim(
                        in_bit_stream, n_bits=n_bits, sf_size=SF_SIZE_BITS
                    )
                elif predictor == 0b10:  # Linear Predictor #1
                    frame = self.rice_decode_linear(
                        in_bit_stream,
                        n_bits=n_bits,
                        sf_size=SF_SIZE_BITS,
                        rice_k_bits=rice_k_bits,
                        linear_number=1,
                    )
                elif predictor == 0b11:  # Linear Predictor #2
                    frame = self.rice_decode_linear(
                        in_bit_stream,
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
            # convert list to binary string
            out_bin_str = "".join([bin(v)[2:].zfill(12) for v in output])
            return bitstring.ConstBitStream("0b" + out_bin_str)

        except IndexError:
            logger.debug("input stream is finished")
