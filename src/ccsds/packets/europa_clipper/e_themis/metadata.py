"""ECM Metadata packet structure."""
import ccsdspy
from ccsds.packets.europa_clipper.common import METADATA_FIELDS

metadata_ethemis = ccsdspy.VariableLength(METADATA_FIELDS)
metadata_ethemis.name = "adp_metadata_ethemis"
metadata_ethemis.apid = 1473
