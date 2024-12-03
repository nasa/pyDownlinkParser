"""ECM Health and Safety packet structure."""
import ccsdspy
from ccsds.packets.europa_clipper.common import hs_header_fields


hs_ecm_fields = [
    ccsdspy.PacketField(
        name="Source Data, Fault Detection", bit_length=32, data_type="uint"
    ),
    ccsdspy.PacketField(name="FPGA_+3_I", bit_length=24, data_type="int"),
    ccsdspy.PacketField(name="PS_+15V", bit_length=24, data_type="int"),
    ccsdspy.PacketField(name="FPGA_+5_I", bit_length=24, data_type="int"),
    ccsdspy.PacketField(name="PS_-15V", bit_length=24, data_type="int"),
    ccsdspy.PacketField(name="FPGA_TEMP", bit_length=24, data_type="int"),
    ccsdspy.PacketField(name="+15V_I", bit_length=24, data_type="int"),
    ccsdspy.PacketField(name="1.5V_LDO_Current", bit_length=24, data_type="int"),
    ccsdspy.PacketField(name="-15V_I", bit_length=24, data_type="int"),
    ccsdspy.PacketField(name="FPGA_IO_I", bit_length=24, data_type="int"),
    ccsdspy.PacketField(name="HK1_2VREF", bit_length=24, data_type="int"),
    ccsdspy.PacketField(name="HK2_1VREF", bit_length=24, data_type="int"),
    ccsdspy.PacketField(name="HK1_1VREF", bit_length=24, data_type="int"),
    ccsdspy.PacketField(name="3.3V_LDO_Current", bit_length=24, data_type="int"),
    ccsdspy.PacketField(name="FG12_TEMP", bit_length=24, data_type="int"),
    ccsdspy.PacketField(name="FG1_HTR_I", bit_length=24, data_type="int"),
    ccsdspy.PacketField(name="FG1_SNS_PRT", bit_length=24, data_type="int"),
    ccsdspy.PacketField(name="FG2_HTR_I", bit_length=24, data_type="int"),
    ccsdspy.PacketField(name="FG2_SNS_PRT", bit_length=24, data_type="int"),
    ccsdspy.PacketField(name="1.5V_LDO_V", bit_length=24, data_type="int"),
    ccsdspy.PacketField(name="PS_+5V", bit_length=24, data_type="int"),
    ccsdspy.PacketField(name="FPGA_LDO_V", bit_length=24, data_type="int"),
    ccsdspy.PacketField(name="PS_+3.3V", bit_length=24, data_type="int"),
    ccsdspy.PacketField(name="FG3_HTR_I", bit_length=24, data_type="int"),
    ccsdspy.PacketField(name="HK1_MUX_CH11", bit_length=24, data_type="int"),
    ccsdspy.PacketField(name="FPGA_+3_3V", bit_length=24, data_type="int"),
    ccsdspy.PacketField(name="HK1_MUX_CH12", bit_length=24, data_type="int"),
    ccsdspy.PacketField(name="HK2_2VREF", bit_length=24, data_type="int"),
    ccsdspy.PacketField(name="HK1_MUX_CH13", bit_length=24, data_type="int"),
    ccsdspy.PacketField(name="FG23_TEMP", bit_length=24, data_type="int"),
    ccsdspy.PacketField(name="HK1_MUX_CH14", bit_length=24, data_type="int"),
    ccsdspy.PacketField(name="FG3_SNS_PRT", bit_length=24, data_type="int"),
    ccsdspy.PacketField(name="HK1_MUX_CH15", bit_length=24, data_type="int"),
    ccsdspy.PacketField(
        name="32-bit word zero padding", bit_length=16, data_type="uint"
    ),
]

hs_ecm = ccsdspy.VariableLength(hs_header_fields + hs_ecm_fields)
hs_ecm.name = "hs_ecm"
hs_ecm.apid = 1216
