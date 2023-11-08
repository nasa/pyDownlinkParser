"""ECM packet structures."""
import copy

import ccsdspy
from ccsdspy.converters import Converter
from ccsdspy.converters import StringifyBytesConverter

from .common_config import hs_header

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
        # ccsdspy.PacketField(name = "Spare", bit_length = 0, data_type='uint'),
        ccsdspy.PacketField(name="CRC", bit_length=16, data_type="uint"),
    ]
)
# packet_structure.add_converted_field("Spare", "Spare_Hex", StringifyBytesConverter(format="hex"))
# packet_structure.add_converted_field("Register Read Start Address", "Register Read Start Address_Hex", StringifyBytesConverter(format="hex"))
# packet_structure.add_converted_field("Register Read End Address", "Register Read End Address_Hex", StringifyBytesConverter(format="hex"))
read_reg_structure.add_converted_field(
    "REG", "REG_HEX", StringifyBytesConverter(format="hex")
)
read_reg_structure.name = "read_reg_structure"

hs_fields = [
    ccsdspy.PacketField(
        name="Source Data, Fault Detection", bit_length=32, data_type="uint"
    ),
    ccsdspy.PacketField(name="FPGA_+3_I", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="PS_+15V", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="FPGA_+5_I", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="PS_-15V", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="FPGA_TEMP", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="+15V_I", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="1.5V_LDO_Current", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="-15V_I", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="FPGA_IO_I", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="HK1_2VREF", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="HK2_1VREF", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="HK1_1VREF", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="3.3V_LDO_Current", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="FG12_TEMP", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="FG1_HTR_I", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="FG1_SNS_PRT", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="FG2_HTR_I", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="FG2_SNS_PRT", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="1.5V_LDO_V", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="PS_+5V", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="FPGA_LDO_V", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="PS_+3.3V", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="FG3_HTR_I", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="HK1_MUX_CH11", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="FPGA_+3_3V", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="HK1_MUX_CH12", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="HK2_2VREF", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="HK1_MUX_CH13", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="FG23_TEMP", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="HK1_MUX_CH14", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="FG3_SNS_PRT", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="HK1_MUX_CH15", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(
        name="32-bit word zero padding", bit_length=16, data_type="uint"
    ),
]

hs_ecm = ccsdspy.VariableLength(hs_header + hs_fields)
hs_ecm.name = "hs_ecm"

fgx_pkt = ccsdspy.VariableLength(
    [
        ccsdspy.PacketField(
            name="Instrument SCLK Time second", bit_length=32, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="Instrument SCLK Time subsec", bit_length=16, data_type="uint"
        ),
        ccsdspy.PacketField(name="Accountability ID", bit_length=32, data_type="uint"),
        # shape is 3 bytes * 3 channels * number of samples
        # 255, 237, 147]
        ccsdspy.PacketArray(
            name="FGX_CHANNELS_8bits",
            data_type="uint",
            bit_length=8,
            array_shape="expand",
        ),
        ccsdspy.PacketField(name="FGx_-4.7VHK", bit_length=24, data_type="int"),
        ccsdspy.PacketField(name="FGx_+4.7VHK", bit_length=24, data_type="int"),
        ccsdspy.PacketField(name="FGx_2VREF", bit_length=24, data_type="int"),
        ccsdspy.PacketField(name="FGx_1VREF", bit_length=24, data_type="int"),
        ccsdspy.PacketField(name="FGx_DRV_SNS", bit_length=24, data_type="int"),
        ccsdspy.PacketField(name="FGx_OP_PRTA", bit_length=24, data_type="int"),
        ccsdspy.PacketField(name="FGx_FBX", bit_length=24, data_type="int"),
        ccsdspy.PacketField(name="FGx_FBY", bit_length=24, data_type="int"),
        ccsdspy.PacketField(name="FGx_FBZ", bit_length=24, data_type="int"),
        ccsdspy.PacketField(name="FGx_BPFX", bit_length=24, data_type="int"),
        ccsdspy.PacketField(name="FGx_BPFY", bit_length=24, data_type="int"),
        ccsdspy.PacketField(name="FGx_BPFZ", bit_length=24, data_type="int"),
        ccsdspy.PacketField(name="FGx_+4.7_I", bit_length=24, data_type="int"),
        ccsdspy.PacketField(name="FGx_-4.7_I", bit_length=24, data_type="int"),
        ccsdspy.PacketField(name="FGx_HK_CH14", bit_length=24, data_type="int"),
        ccsdspy.PacketField(name="FGx_HK_CH15", bit_length=24, data_type="int"),
        ccsdspy.PacketField(name="Register 80", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(name="PEC (CRC-16-CCITT)", bit_length=16, data_type="uint"),
    ]
)


class BytesTo24BitInts(Converter):
    """Convert from array of bytes to arrays of 24bits (3 bytes) integer."""

    def __init__(self):
        """Does nothing."""
        pass

    def convert(self, field_array):
        """Convert list of arrays of bytes to list of arrays of int, each from 3 bytes."""
        fgx_channels_24bits_list = []
        for fgx_channels in field_array:
            fgx_channels_24bits = []
            for i in range(0, len(fgx_channels), 3):
                meas_3bytes = bytes(fgx_channels[i : i + 3])
                meas_int = int.from_bytes(meas_3bytes, "big", signed=True)
                fgx_channels_24bits.append(meas_int)
            fgx_channels_24bits_list.append(fgx_channels_24bits)
        return fgx_channels_24bits_list


def get_fgx_freq_pkt(sensor, frequency):
    """Prepare a properly named packet structure for ECM FG packets."""
    pkt = copy.copy(fgx_pkt)
    pkt.name = f"fg{sensor}_{frequency}"
    pkt.add_converted_field(
        "FGX_CHANNELS_8bits", "FGX_CHANNELS_24bits", BytesTo24BitInts()
    )
    return pkt


adp_metadata_ecm = ccsdspy.VariableLength(
    [
        # secondary header
        ccsdspy.PacketField(name="MSCLK Seconds", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(
            name="Subseconds Pre-zero", bit_length=16, data_type="uint"
        ),
        ccsdspy.PacketField(name="AID", bit_length=32, data_type="uint"),
        # ADP Metadata
        ccsdspy.PacketField(name="CTRL = START | END", bit_length=5, data_type="uint"),
        ccsdspy.PacketField(name="ADP Major APID", bit_length=5, data_type="uint"),
        ccsdspy.PacketField(name="ADP Minor APID", bit_length=6, data_type="uint"),
        ccsdspy.PacketField(name="SCLK", bit_length=48, data_type="uint"),
        ccsdspy.PacketField(
            name="Source Sequence Count", bit_length=14, data_type="uint"
        ),
        ccsdspy.PacketField(name="Spare", bit_length=2, data_type="uint"),
        ccsdspy.PacketField(
            name="CTRL==END ? Count : Spare", bit_length=32, data_type="uint"
        ),
        # PEC
        ccsdspy.PacketField(name="PEC (CRC-16-CCITT)", bit_length=16, data_type="uint"),
    ]
)
adp_metadata_ecm.name = "adp_metadata_ecm"
