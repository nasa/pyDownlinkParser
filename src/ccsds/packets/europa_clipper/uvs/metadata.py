"""ECM Metadata packet structure."""
import copy

import ccsdspy
from ccsds.packets.europa_clipper.common import METADATA_FIELDS

# specifically for UVS metadata packetm the following 2 fields are swapped,
# unlike the metadata packets for all the other instruments
uvs_metadata_fields = copy.copy(METADATA_FIELDS)
uvs_metadata_fields[7] = METADATA_FIELDS[8]
uvs_metadata_fields[8] = METADATA_FIELDS[7]

metadata_uvs = ccsdspy.VariableLength(uvs_metadata_fields)
metadata_uvs.name = "adp_metadata_uvs"
metadata_uvs.apid = 1537
