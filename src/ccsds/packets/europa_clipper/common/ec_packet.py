"""Shared definition for Europa-Clipper packets."""
import ccsdspy

from .ccsds_header_footer import SECONDARY_HEADER


ec_regular_packet = ccsdspy.VariableLength(
    [
        *SECONDARY_HEADER,
        ccsdspy.PacketArray(
            name="data",
            data_type="uint",
            bit_length=8,
            array_shape="expand",
        ),
        ccsdspy.PacketField(name="PEC_CRC_16_CCITT", bit_length=16, data_type="uint"),
    ]
)

ec_jumbo_packet = ccsdspy.VariableLength(
    [
        *SECONDARY_HEADER,
        ccsdspy.PacketArray(
            name="data",
            data_type="uint",
            bit_length=8,
            array_shape="expand",
        ),
        ccsdspy.PacketField(name="PEC_CRC_32_CCITT", bit_length=32, data_type="uint"),
    ]
)
