"""ECM Metadata packet structure."""
import ccsdspy
from ccsds.packets.europa_clipper.common import METADATA_FIELDS

metadata_ecm = ccsdspy.VariableLength(METADATA_FIELDS)
metadata_ecm.name = "adp_metadata_ecm"
metadata_ecm.apid = 1217
