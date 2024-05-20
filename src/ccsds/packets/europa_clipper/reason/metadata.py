"""ECM Metadata packet structure."""
import ccsdspy
from ccsds.packets.europa_clipper.common import METADATA_FIELDS

metadata_reason = ccsdspy.VariableLength(METADATA_FIELDS)
metadata_reason.name = "adp_metadata_reason"
metadata_reason.apid = 1601
