"""Uncompressed frame standard packet definition (0-89)."""
import ccsdspy
from ccsds.packets.europa_clipper.common import CRC_FOOTER
from ccsds.packets.europa_clipper.common import SECONDARY_HEADER

# see specification in MISE Flight Software Specification 7489-9100, section 8.3.1.1
standard_frame_pkts = [
    *SECONDARY_HEADER,
    ccsdspy.PacketArray(
        name="Data", data_type="uint", bit_length=16, array_shape="expand"
    ),
    ccsdspy.PacketField(name="Pad", bit_length=16, data_type="uint"),
    CRC_FOOTER,
]

standard_frame_pkt = ccsdspy.VariableLength(standard_frame_pkts)
standard_frame_pkt.name = "standard_frame_pkt"
standard_frame_pkt.apid = 1392
standard_frame_pkt.sub_apid = "90th"
