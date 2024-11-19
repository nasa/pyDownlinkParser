"""UVS packet structure for APID 1540."""
import ccsdspy
from ccsds.packets.europa_clipper.common import CRC_FOOTER
from ccsds.packets.europa_clipper.common import SECONDARY_HEADER
from ccsdspy.constants import BITS_PER_BYTE

# specifically for UVS metadata packetm the following 2 fields are swapped,
# unlike the metadata packets for all the other instruments
uvs_fields = [
    *SECONDARY_HEADER,
    ccsdspy.PacketArray(
        name="data",
        data_type="uint",
        bit_length=BITS_PER_BYTE,
        array_shape="expand",
    ),
    CRC_FOOTER,
]

apid_1540_uvs = ccsdspy.VariableLength(uvs_fields)
apid_1540_uvs.name = "adp_uvs_1540"
apid_1540_uvs.apid = 1540
