"""ECM Register Read packet structures."""
import ccsdspy
from ccsdspy.converters import StringifyBytesConverter

read_reg_structure = ccsdspy.VariableLength(
    [
        ccsdspy.PacketField(
            name="Instrument SCLK Time second", bit_length=32, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="Instrument SCLK Time subsec", bit_length=16, data_type="uint"
        ),
        ccsdspy.PacketField(name="Accountability ID", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(
            name="Register Read Start Address", bit_length=8, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="Register Read End Address", bit_length=8, data_type="uint"
        ),
        ccsdspy.PacketArray(
            name="REG", bit_length=16, data_type="uint", array_shape="expand"
        ),
        ccsdspy.PacketField(name="CRC", bit_length=16, data_type="uint"),
    ]
)

read_reg_structure.add_converted_field(
    "REG", "REG_HEX", StringifyBytesConverter(format="hex")
)
read_reg_structure.name = "read_reg_structure"
read_reg_structure.apid = 1232
