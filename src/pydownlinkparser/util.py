"""Utilities shared."""
import ccsdspy
from ccsdspy.constants import BITS_PER_BYTE

default_pkt = ccsdspy.VariableLength(
    [
        ccsdspy.PacketArray(
            name="data",
            data_type="uint",
            bit_length=BITS_PER_BYTE,
            array_shape="expand",
        )
    ]
)
