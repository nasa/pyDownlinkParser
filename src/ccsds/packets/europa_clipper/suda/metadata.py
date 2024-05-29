"""ECM Metadata packet structure."""
import ccsdspy
from ccsds.packets.europa_clipper.common import METADATA_FIELDS

metadata_suda = ccsdspy.VariableLength(METADATA_FIELDS)
metadata_suda.name = "adp_metadata_suda"
metadata_suda.apid = 1409
