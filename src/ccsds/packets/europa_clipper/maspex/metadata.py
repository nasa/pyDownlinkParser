"""ECM Metadata packet structure."""
import ccsdspy
from ccsds.packets.europa_clipper.common import METADATA_FIELDS

metadata_maspex = ccsdspy.VariableLength(METADATA_FIELDS)
metadata_maspex.name = "adp_metadata_maspex"
metadata_maspex.apid = 1281
