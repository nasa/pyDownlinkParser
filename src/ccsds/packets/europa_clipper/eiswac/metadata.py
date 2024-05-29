"""ECM Metadata packet structure."""
import ccsdspy
from ccsds.packets.europa_clipper.common import METADATA_FIELDS

metadata_eiswac = ccsdspy.VariableLength(METADATA_FIELDS)
metadata_eiswac.name = "adp_metadata_eiswac"
metadata_eiswac.apid = 1665
