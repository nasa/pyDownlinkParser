"""Uncompressed frame, pre-parsing packet."""
import ccsdspy
from ccsdspy.constants import BITS_PER_BYTE

frame_uncompressed_preparser = ccsdspy.VariableLength(
    [
        ccsdspy.PacketArray(
            name="data",
            data_type="uint",
            bit_length=BITS_PER_BYTE,
            array_shape="expand",
        )
    ]
)

frame_uncompressed_preparser.apid = 1392
frame_uncompressed_preparser.name = "MISE uncompressed frame pre-parser"

N = 0


def sequence():
    """Simple counter to identify packets APID 1392."""
    global N
    N += 1
    if N <= 90:
        return "90th"
    if N == 91:
        return "91st"
    else:
        N = 0
        return "92nd"


frame_uncompressed_preparser.decision_fun = sequence
