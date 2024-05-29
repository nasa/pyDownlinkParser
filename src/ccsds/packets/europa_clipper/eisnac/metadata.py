"""ECM Metadata packet structure."""
import ccsdspy
from ccsds.packets.europa_clipper.common import METADATA_FIELDS

metadata_eisnac = ccsdspy.VariableLength(METADATA_FIELDS)
metadata_eisnac.name = "adp_metadata_eisnac"
metadata_eisnac.apid = 1729
