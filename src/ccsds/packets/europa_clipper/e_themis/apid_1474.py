"""Dummy packet description for E-THEMIS datasets, APID 1474."""
import ccsdspy
from ccsds.packets.europa_clipper.common import CRC_FOOTER
from ccsds.packets.europa_clipper.common import SECONDARY_HEADER

e_themis_1474 = ccsdspy.VariableLength(
    [
        *SECONDARY_HEADER,
        ccsdspy.PacketArray(
            name="Data", bit_length=8, data_type="uint", array_shape="expand"
        ),
        CRC_FOOTER,
    ]
)

e_themis_1474.name = "apid 1474"
