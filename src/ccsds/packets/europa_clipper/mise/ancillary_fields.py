"""Ancillary fields used for both in uncompressed and compressed frames."""
import ccsdspy


def analog_fields_lvps():
    """Create LVPS_{i}_{j} fields."""
    fields = []
    for i in range(1, 5):
        for j in range(0, 6):
            fields.append(
                ccsdspy.PacketField(
                    name=f"LVPS_{i}_{j}", bit_length=12, data_type="uint"
                )
            )

    # the LVPS_4* unlike the previous has up to 7 entries
    for j in range(6, 8):
        fields.append(
            ccsdspy.PacketField(name=f"LVPS_4_{j}", bit_length=12, data_type="uint")
        )

    return fields


def analog_fields_ifc():
    """Create IFC_0_{i} fields."""
    fields = []
    for i in range(0, 12):
        field = ccsdspy.PacketField(name=f"IFC_0_{i}", bit_length=12, data_type="uint")
        fields.append(field)

    # 12,13,14 are not added but 15 is added
    fields.append(ccsdspy.PacketField(name="IFC_0_15", bit_length=12, data_type="uint"))
    return fields


ANCILLARY_DATA_FIELDS = [
    # Ancillary Data - Analog
    *analog_fields_lvps(),
    *analog_fields_ifc(),
    ccsdspy.PacketField(name="Analog_Reserved", bit_length=12, data_type="uint"),
    # Ancillary Data - Digital
    ccsdspy.PacketField(name="Digital_Reserved1", bit_length=9, data_type="uint"),
    ccsdspy.PacketField(name="IFC_Power_Down", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="IFC_Run", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="Digital_Reserved2", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="CEU_Drive", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="IFC_Power", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="FPIE_Power", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="FPMC_Power", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="CEU_Cont._Temp.", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="CEU_Aux._Temp.", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="CEU_PI_Out", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="CEU_Peak_Bus_Voltage", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="CEU_Bus_Current", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="CEU_Bus_Voltage", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="Digital_Reserved3", bit_length=13, data_type="uint"),
    ccsdspy.PacketField(name="CEU_Temp_Sensor", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="CEU_Mode_", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="CEU_H-_Bridge", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="CEU_Motor_A_Peak_POS_V", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="CEU_Motor_A_Peak_NEG_V", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="CEU_Motor_B_Peak_POS_V", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="CEU_Motor_B_Peak_NEG_V", bit_length=16, data_type="uint"),
    # Ancillary Data - Software
    ccsdspy.PacketField(name="Status_Int", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="Macro_Blocks", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="Tlm_Vol", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="Watch_Addr", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="Watch_Mem", bit_length=8, data_type="uint"),
    ccsdspy.PacketField(name="Watch_Data", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="SW_Version", bit_length=8, data_type="uint"),
    ccsdspy.PacketField(name="SW_Time", bit_length=32, data_type="uint"),
    ccsdspy.PacketField(name="Alarm_ID", bit_length=8, data_type="uint"),
    ccsdspy.PacketField(name="Alarm_Type", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="Alarm_Count", bit_length=7, data_type="uint"),
    ccsdspy.PacketField(name="Cmd_Exec", bit_length=8, data_type="uint"),
    ccsdspy.PacketField(name="Cmd_Reject", bit_length=8, data_type="uint"),
    ccsdspy.PacketField(name="Mac_Exec", bit_length=8, data_type="uint"),
    ccsdspy.PacketField(name="Mac_Reject", bit_length=8, data_type="uint"),
    ccsdspy.PacketField(name="Macro_Id", bit_length=8, data_type="uint"),
    ccsdspy.PacketField(name="Macro_Learn", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="Monitor_Response", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="Write_Enb", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="Scan_Diag_Enb", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="Cooler_State", bit_length=4, data_type="uint"),
    ccsdspy.PacketField(name="Safing_Time", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="Cooler_Temp_Goal", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="Current_Angle", bit_length=32, data_type="int"),
    ccsdspy.PacketField(name="Goal_Angle", bit_length=32, data_type="int"),
    ccsdspy.PacketField(name="Slew_Angle", bit_length=32, data_type="int"),
    ccsdspy.PacketField(name="Offset_Angle", bit_length=32, data_type="int"),
    ccsdspy.PacketField(name="Offset_Rate", bit_length=32, data_type="int"),
    ccsdspy.PacketField(name="Offset_Adjustment", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(
        name="Cryocooler_Heater_Control", bit_length=2, data_type="uint"
    ),
    ccsdspy.PacketField(name="Scan_Loop_Mode", bit_length=2, data_type="uint"),
    ccsdspy.PacketField(name="Scan_Mode", bit_length=3, data_type="uint"),
    ccsdspy.PacketField(name="Scan_Pos_Mode", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="Primary_Winding", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="Secondary_Winding", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="Timeline_Enb", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="Observe", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="FPMC_Status_Valid", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="Cryocooler_Heater", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="Scan_Fallback", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(
        name="Scan_Stability_Error_Rate", bit_length=16, data_type="uint"
    ),
    ccsdspy.PacketField(name="Target_ID", bit_length=32, data_type="uint"),
    ccsdspy.PacketField(name="Observe_Macro_ID", bit_length=8, data_type="uint"),
    ccsdspy.PacketField(name="Scan_Stall", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="Software_Reserved", bit_length=2, data_type="uint"),
    ccsdspy.PacketField(name="Profile_ID", bit_length=5, data_type="uint"),
    ccsdspy.PacketField(name="Profile_Time_Seconds", bit_length=32, data_type="uint"),
    ccsdspy.PacketField(
        name="Profile_Time_Subseconds", bit_length=16, data_type="uint"
    ),
    # Ancillary Data - FPMC
    ccsdspy.PacketField(name="Log_used", bit_length=32, data_type="uint"),
    ccsdspy.PacketField(name="Flash_Bank_A_Used", bit_length=32, data_type="uint"),
    ccsdspy.PacketField(name="Flash_Bank_B_Used", bit_length=32, data_type="uint"),
    ccsdspy.PacketField(name="Curr._Cube", bit_length=8, data_type="uint"),
    ccsdspy.PacketField(name="FPMC_Reserved1", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="FPMC_SW_Version", bit_length=8, data_type="uint"),
    ccsdspy.PacketField(name="FPMC_SW_Time", bit_length=32, data_type="uint"),
    ccsdspy.PacketField(name="Curr._AID", bit_length=32, data_type="uint"),
    ccsdspy.PacketField(name="FPMC_Write_Enb", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="Curr._Filter_ID", bit_length=4, data_type="uint"),
    ccsdspy.PacketField(name="Row_Origin", bit_length=9, data_type="uint"),
    ccsdspy.PacketField(name="Column_Origin", bit_length=9, data_type="uint"),
    ccsdspy.PacketField(name="Window_Rows", bit_length=9, data_type="uint"),
    ccsdspy.PacketField(name="Window_Columns", bit_length=9, data_type="uint"),
    ccsdspy.PacketField(name="Row_Binning", bit_length=2, data_type="uint"),
    ccsdspy.PacketField(name="Column_Binning", bit_length=2, data_type="uint"),
    ccsdspy.PacketField(name="Row_reorder", bit_length=2, data_type="uint"),
    ccsdspy.PacketField(name="FPMC_Reserved2", bit_length=17, data_type="uint"),
    # Ancillary Data - Reserved 1
    ccsdspy.PacketField(name="Reserved_1", bit_length=8 * 8, data_type="uint"),
    # Ancillary Data - Software Part 2
    ccsdspy.PacketField(name="Scan_Error", bit_length=32, data_type="uint"),
    # Ancillary Data - Reserved 2
    ccsdspy.PacketField(name="Reserved_2", bit_length=8 * 8, data_type="uint"),
    # Ancillary Data - Reserved 3
    ccsdspy.PacketField(name="Reserved_3", bit_length=824 * 8, data_type="fill"),
]
