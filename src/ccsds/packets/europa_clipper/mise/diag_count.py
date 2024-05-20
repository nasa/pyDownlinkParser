"""Diagnostic count packet definition."""
import ccsdspy
from ccsds.packets.europa_clipper.common import CRC_FOOTER
from ccsds.packets.europa_clipper.common import SECONDARY_HEADER

from .decompression_converter import MISEDecompressionConverter

diagnostic_count_pkt = ccsdspy.VariableLength(
    [
        *SECONDARY_HEADER,
        ccsdspy.PacketArray(
            name="Comp Data", bit_length=8, data_type="uint", array_shape="expand"
        ),
        CRC_FOOTER,
    ]
)

diagnostic_count_pkt.name = "diagnositic count"
diagnostic_count_pkt.apid = 1396

converter = MISEDecompressionConverter(
    uncompressed_item_mask=0x3F,
    data_length_without_frame_bytes=0,
    default_initial_value=0,
    width_encoding_bits=3,
)

diagnostic_count_pkt.add_converted_field(("Comp Data"), "Uncomp Data", converter)
