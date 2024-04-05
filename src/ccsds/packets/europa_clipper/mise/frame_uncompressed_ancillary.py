"""Uncompressed frame, ancillary data packet definition (91th, last)."""
import ccsdspy
from ccsds.packets.europa_clipper.common import CRC_FOOTER
from ccsds.packets.europa_clipper.common import SECONDARY_HEADER

from .ancillary_fields import ANCILLARY_DATA_FIELDS

# see specification in MISE Flight Software Specification 7489-9100, Table 55. Ancillary Data
ancillary_data_pkts = [
    *SECONDARY_HEADER,
    ccsdspy.PacketField(name="Spare", bit_length=8 * 16, data_type="fill"),
    *ANCILLARY_DATA_FIELDS,
    ccsdspy.PacketField(name="Pad", bit_length=2 * 8, data_type="fill"),
    CRC_FOOTER,
]


ancillary_data_pkt = ccsdspy.VariableLength(ancillary_data_pkts)
ancillary_data_pkt.name = "ancillary_data_pkt"
ancillary_data_pkt.apid = 1392
ancillary_data_pkt.sub_apid = "92nd"
