"""ECM Metadata packet structure."""
import ccsdspy
from ccsds.packets.europa_clipper.common import METADATA_FIELDS

metadata_mise = ccsdspy.VariableLength(METADATA_FIELDS)
metadata_mise.name = "adp_metadata_mise"
metadata_mise.apid = 1345
