"""Uncompressed frame, last frame data packet definition (90th)."""
import ccsdspy
from pydownlinkparser.europa_clipper.common import CRC_FOOTER
from pydownlinkparser.europa_clipper.common import SECONDARY_HEADER

# see specification in MISE Flight Software Specification 7489-9100, section 8.3.1.1
last_frame_packets = [
    *SECONDARY_HEADER,
    ccsdspy.PacketArray(
        name="Data", data_type="uint", bit_length=16, array_shape="expand"
    ),
    ccsdspy.PacketField(name="Time (MS)", data_type="uint", bit_length=4 * 8),
    ccsdspy.PacketField(name="Time (LS)", data_type="uint", bit_length=4 * 8),
    ccsdspy.PacketField(name="Pad", bit_length=8 * 8, data_type="fill"),
    CRC_FOOTER,
]

last_frame_packet = ccsdspy.VariableLength(last_frame_packets)
last_frame_packet.name = "last_frame_packet"
