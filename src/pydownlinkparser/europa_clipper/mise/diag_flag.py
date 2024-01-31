"""Diagnostic Flag packet definition."""
import ccsdspy
from pydownlinkparser.europa_clipper.common import CRC_FOOTER
from pydownlinkparser.europa_clipper.common import SECONDARY_HEADER

from .decompression_converter import MISEDecompressionConverter

diagnostic_flag_pkt = ccsdspy.VariableLength(
    [
        *SECONDARY_HEADER,
        ccsdspy.PacketArray(
            name="Comp Data", bit_length=8, data_type="uint", array_shape="expand"
        ),
        CRC_FOOTER,
    ]
)

diagnostic_flag_pkt.name = "diagnostic flag"

converter = MISEDecompressionConverter(
    uncompressed_item_mask=0x1,
    data_length_without_frame_bytes=0,
    default_initial_value=0,
    width_encoding_bits=1,
)

diagnostic_flag_pkt.add_converted_field(("Comp Data"), "Uncomp Data", converter)
