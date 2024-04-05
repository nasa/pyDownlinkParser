"""HS header fields re-used for multiple instruments."""
import ccsdspy

hs_header_fields = [
    ccsdspy.PacketField(name="MSCLK Seconds", bit_length=32, data_type="uint"),
    ccsdspy.PacketField(name="MSCLK Subseconds", bit_length=16, data_type="uint"),
    # operational status
    ccsdspy.PacketField(name="Subseconds Pre-zero", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="IF Type", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="Selected Interface", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="Busy", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="Panic", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="Instrument Mode", bit_length=3, data_type="uint"),
    ccsdspy.PacketField(
        name="Operational Status Spare", bit_length=1, data_type="uint"
    ),
    # command status
    ccsdspy.PacketField(name="Command Accepted Cnt", bit_length=8, data_type="uint"),
    ccsdspy.PacketField(name="Command Executed Cnt", bit_length=8, data_type="uint"),
    ccsdspy.PacketField(name="Command Rejected Count", bit_length=8, data_type="uint"),
    ccsdspy.PacketField(
        name="Most Recent Command's Sequence Count", bit_length=5, data_type="uint"
    ),
    ccsdspy.PacketField(
        name="Most Recent Command's Status", bit_length=3, data_type="uint"
    ),
    ccsdspy.PacketField(
        name="Most Recent Command's Opcode", bit_length=16, data_type="uint"
    ),
    ccsdspy.PacketField(
        name="2nd Most Recent Command's  Sequence Count", bit_length=5, data_type="uint"
    ),
    ccsdspy.PacketField(
        name="2nd Most Recent Command's Status", bit_length=3, data_type="uint"
    ),
    ccsdspy.PacketField(
        name="2nd Most Recent Command's Opcode", bit_length=16, data_type="uint"
    ),
    ccsdspy.PacketField(
        name="3rd Most Recent Command's  Sequence Count", bit_length=5, data_type="uint"
    ),
    ccsdspy.PacketField(
        name="3rd Most Recent Command's Status", bit_length=3, data_type="uint"
    ),
    ccsdspy.PacketField(
        name="3rd Most Recent Command's Opcode", bit_length=16, data_type="uint"
    ),
    ccsdspy.PacketField(
        name="4th Most Recent Command's  Sequence Count", bit_length=5, data_type="uint"
    ),
    ccsdspy.PacketField(
        name="4th Most Recent Command's Status", bit_length=3, data_type="uint"
    ),
    ccsdspy.PacketField(
        name="4th Most Recent Command's Opcode", bit_length=16, data_type="uint"
    ),
    ccsdspy.PacketField(
        name="5th Most Recent Command's  Sequence Count", bit_length=5, data_type="uint"
    ),
    ccsdspy.PacketField(
        name="5th Most Recent Command's Status", bit_length=3, data_type="uint"
    ),
    ccsdspy.PacketField(
        name="5th Most Recent Command's Opcode", bit_length=16, data_type="uint"
    ),
    # uart status
    ccsdspy.PacketField(name="Error Count", bit_length=8, data_type="uint"),
    ccsdspy.PacketField(name="UART Spare", bit_length=14, data_type="uint"),
    # error bits (guides SC fault response)
    ccsdspy.PacketField(
        name="Req_SC_Power_Off (Requests instrument shutdown)",
        bit_length=1,
        data_type="uint",
    ),
    ccsdspy.PacketField(
        name="Req_SC_Power_Cycle (OK to attempt instrument restart)",
        bit_length=1,
        data_type="uint",
    ),
    # source data, derived parameters
    ccsdspy.PacketField(
        name="Source Data Derived Parameters SPARE", bit_length=24, data_type="uint"
    ),
    ccsdspy.PacketField(name="CLOCKS_LAST_1PPS", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="FG1_HTR_AVG", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="FG2_HTR_AVG", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="FG3_HTR_AVG", bit_length=24, data_type="uint"),
    ccsdspy.PacketField(name="FG1_DRIVE_PHASE", bit_length=8, data_type="uint"),
    ccsdspy.PacketField(name="FG2_DRIVE_PHASE", bit_length=8, data_type="uint"),
    ccsdspy.PacketField(name="FG3_DRIVE_PHASE", bit_length=8, data_type="uint"),
    ccsdspy.PacketField(name="SPARE", bit_length=2, data_type="uint"),
    ccsdspy.PacketField(name="I_TP_IN1", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="I_TP_IN2", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="I_FPGA_ID0", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="I_FPGA_ID1", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="I_FPGA_ID2", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="I_FPGA_ID3", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="FG_GENERAL_REGISTERS", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="VERSION", bit_length=24, data_type="uint"),
]
