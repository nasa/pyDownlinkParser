"""Compressed frame packet definition."""
import ccsdspy
from ccsds.packets.europa_clipper.common import CRC_FOOTER
from ccsds.packets.europa_clipper.common import SECONDARY_HEADER

from .decompression_converter import MISEDecompressionConverter

# offset_count = 48 + 32 + 16 + 32 + 9*4 + 4 + 14
comp_frame_pkt = ccsdspy.VariableLength(
    [
        *SECONDARY_HEADER,
        ccsdspy.PacketField(name="Row Origin", bit_length=9, data_type="uint"),
        ccsdspy.PacketField(name="Column Origin", bit_length=9, data_type="uint"),
        ccsdspy.PacketField(name="Window Rows", bit_length=9, data_type="uint"),
        ccsdspy.PacketField(name="Window Columns", bit_length=9, data_type="uint"),
        ccsdspy.PacketField(name="Row Binning", bit_length=2, data_type="uint"),
        ccsdspy.PacketField(name="Column Binning", bit_length=2, data_type="uint"),
        # initial value (14bits), compressed frame and padding fields are including in this field
        # to make sure the fields is aligned on bytes.
        ccsdspy.PacketArray(
            name="Comp Data", bit_length=8, data_type="uint", array_shape="expand"
        ),
        CRC_FOOTER,
    ]
)

converter = MISEDecompressionConverter(
    uncompressed_item_mask=0x3FFF,
    data_length_without_frame_bytes=4 * 9 + 2 * 2 + 14,
    differences_stored=True,
)

comp_frame_pkt.add_converted_field(
    ("Comp Data", "Window Columns", "Column Binning"), "Uncomp Data", converter
)
comp_frame_pkt.name = "comp_frame_pkt"
comp_frame_pkt.apid = 1393
