"""Frame support packet for ancillary data of the compressed frames."""
import ccsdspy
from ccsds.packets.europa_clipper.common import CRC_FOOTER
from ccsds.packets.europa_clipper.common import SECONDARY_HEADER

from .ancillary_fields import ANCILLARY_DATA_FIELDS

# Table 59, MISE Flight Software Specification 7489-9100 Revision B
frame_support_pkt = ccsdspy.VariableLength(
    [
        *SECONDARY_HEADER,
        ccsdspy.PacketField(name="Time (MS)", bit_length=8 * 4, data_type="uint"),
        ccsdspy.PacketField(name="Time (LS)", bit_length=8 * 4, data_type="uint"),
        ccsdspy.PacketField(name="Reserved", bit_length=6 * 32, data_type="fill"),
        *ANCILLARY_DATA_FIELDS,
        ccsdspy.PacketField(name="Pad", bit_length=8 * 2, data_type="fill"),
        CRC_FOOTER,
    ]
)

frame_support_pkt.name = "frame_support"
frame_support_pkt.apid = 1394
