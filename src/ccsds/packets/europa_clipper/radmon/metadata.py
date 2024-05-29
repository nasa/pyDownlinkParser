"""ECM Metadata packet structure."""
import ccsdspy
from ccsds.packets.europa_clipper.common import METADATA_FIELDS

metadata_radmon = ccsdspy.VariableLength(METADATA_FIELDS)
metadata_radmon.name = "adp_metadata_radmon"
metadata_radmon.apid = 1025
