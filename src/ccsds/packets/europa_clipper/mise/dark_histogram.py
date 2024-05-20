"""Dark histogram packet definition."""
import ccsdspy
from ccsds.packets.europa_clipper.common import CRC_FOOTER
from ccsds.packets.europa_clipper.common import SECONDARY_HEADER

dark_histogram = ccsdspy.VariableLength(
    [
        *SECONDARY_HEADER,
        ccsdspy.PacketArray(
            name="Data", bit_length=32, data_type="uint", array_shape="expand"
        ),
        ccsdspy.PacketField(name="Pad", bit_length=16, data_type="fill"),
        CRC_FOOTER,
    ]
)

dark_histogram.name = "dark_histogram"
dark_histogram.apid = 1398
