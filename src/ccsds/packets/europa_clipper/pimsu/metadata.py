"""ECM Metadata packet structure."""
import ccsdspy
from ccsds.packets.europa_clipper.common import METADATA_FIELDS

metadata_pimsu = ccsdspy.VariableLength(METADATA_FIELDS)
metadata_pimsu.name = "adp_metadata_pimsu"
metadata_pimsu.apid = 1089
