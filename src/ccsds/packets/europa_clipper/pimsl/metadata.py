"""ECM Metadata packet structure."""
import ccsdspy
from ccsds.packets.europa_clipper.common import METADATA_FIELDS

metadata_pimsl = ccsdspy.VariableLength(METADATA_FIELDS)
metadata_pimsl.name = "adp_metadata_pimsl"
metadata_pimsl.apid = 1153
