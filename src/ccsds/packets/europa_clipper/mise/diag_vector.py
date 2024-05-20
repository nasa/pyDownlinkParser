"""Diagnostic Vector packet definition."""
import ccsdspy
from ccsds.packets.europa_clipper.common.ccsds_header_footer import CRC_FOOTER
from ccsds.packets.europa_clipper.common.ccsds_header_footer import SECONDARY_HEADER

diagnostic_vector_pkt = ccsdspy.VariableLength(
    [
        *SECONDARY_HEADER,
        ccsdspy.PacketArray(
            name="Data", bit_length=32, data_type="uint", array_shape="expand"
        ),
        ccsdspy.PacketField(name="Pad", bit_length=8 * 2, data_type="fill"),
        CRC_FOOTER,
    ]
)
diagnostic_vector_pkt.name = "diagnostic_vector"
diagnostic_vector_pkt.apid = 1395
