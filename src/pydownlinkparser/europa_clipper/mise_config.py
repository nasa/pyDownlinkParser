import ccsdspy
from ccsdspy.converters import StringifyBytesConverter

CRC_FIELD_NAME = "PEC (CRC-16-CCITT)"

MISE_MAJOR_APID = 0x15

SECOND_LENGTH_BYTES = 4  # Seconds
SUBSECOND_LENGTH_BYTES = 2
AID_LENGTH_BYTES = 4
CHECKSUM_LENGTH_BYTES = 2
DATA_ELEMENT_SIZE_BITS = 16
bit_length = ANALOG_TWELVE_BIT_LENGTH = 12
DIGITAL_RESERVED1_BIT_LENGTH = 9
IFC_POWER_DOWN_BIT_LENGTH = 1
IFC_RUN_BIT_LENGTH = 1
DIGITAL_RESERVED2_BIT_LENGTH = 1
CEU_DRIVE_BIT_LENGTH = 1
IFC_POWER__BIT_LENGTH = 1
FPIE_POWER__BIT_LENGTH = 1
FPMC_POWER_BIT_LENGTH = 1
CEU_CONT_TEMP_BIT_LENGTH = 16
CEU_AUX_TEMP_BIT_LENGTH = 16
CEU_PI_OUT_BIT_LENGTH = 16
CEU_PEAK_BUS_VOLTAGE_BIT_LENGTH = 16
CUE_BUS_CURRENT_BIT_LENGTH = 16
CEU_BUS_VOLTAGE__BIT_LENGTH = 16
DIGITAL_RESERVED3_BIT_LENGTH = 13
CEU_TEMP_SENSOR_BIT_LENGTH = 1
CEU_MODE_BIT_LENGTH = 1
CEU_H_BRIDGE_BIT_LENGTH = 1
CEU_MOTOR_A_PEAK_POS_V_BIT_LENGTH = 16
CEU_MOTOR_A_PEAK_NEG_V_BIT_LENGTH = 16
CEU_MOTOR_B_PEAK_POS_V_BIT_LENGTH = 16
CEU_MOTOR_B_PEAK_NEG_V_BIT_LENGTH = 16
STATUS_INT_BIT_LENGTH = 16
MACRO_BLOCKS_BIT_LENGTH = 16
TLM_VOL_BIT_LENGTH = 16
WATCH_ADDR_BIT_LENGTH = 16
WATCH_MEM_BIT_LENGTH = 8
WATCH_DATA_BIT_LENGTH = 16
SW_VERSION_BIT_LENGTH = 8
SW_TIME_BIT_LENGTH = 32
ALARM_ID_BIT_LENGTH = 8
ALRAM_TYPE_BIT_LENGTH = 1
ALARM_COUNT_BIT_LENGTH = 7
CMD_EXEC_BIT_LENGTH = 8
CMD_REJECT_BIT_LENGTH = 8
MAC_EXEC_BIT_LENGTH = 8
MAC_REJECT_BIT_LENGTH = 8
MACRO_ID_BIT_LENGTH = 8
MACRO_LEARN_BIT_LENGTH = 1
MONITOR_RESPONSE_BIT_LENGTH = 1
WRITE_ENB_BIT_LENGTH = 1
SCAN_DIAG_ENB_BIT_LENGTH = 1
COOLER_STATE_BIT_LENGTH = 4
SAFING_TIME_BIT_LENGTH = 16
COOLER_TEMP_GOAL_BIT_LENGTH = 16
CURRENT_ANGLE_BIT_LENGTH = 32
GOAL_ANGLE_BIT_LENGTH = 32
SLEW_ANGLE_BIT_LENGTH = 32
OFFSET_ANGLE_BIT_LENGTH = 32
OFFSET_RATE_BIT_LENGTH = 32
OFFSET_ADJUSTMENT_BIT_LENGTH = 1
CRYOCOOLER_HEATER_CONTROL_BIT_LENGTH = 2
SCAN_LOOP_MODE_BIT_LENGTH = 2
SCAN_MODE_BIT_LENGTH = 3
SCAN_POS_MODE_BIT_LENGTH = 1
PRIMARY_WINDING_BIT_LENGTH = 1
SECONDARY_WINDING_BIT_LENGTH = 1
TIMELINE_ENB_BIT_LENGTH = 1
OBSERVE_BIT_LENGTH = 1
FPMC_STATUS_VALID_BIT_LENGTH = 1
CRYOCOOLER_HEATER_BIT_LENGTH = 1
SCAN_FALLBACK_BIT_LENGTH = 1
SCAN_STABILITY_ERROR_RATE_BIT_LENGTH = 16
TARGET_ID_BIT_LENGTH = 32
OBSERVE_MACRO_ID_BIT_LENGTH = 8
SCAN_STALL_BIT_LENGTH = 1
SOFTWARE_STATUS_RESERVED_BIT_LENGTH = 2
PROFILE_ID_BIT_LENGTH = 5
PROFILE_TIME_SECONDS_BIT_LENGTH = 32
PROFILE_TIME_SUBSECONDS_BIT_LENGTH = 16
LOG_USED_BIT_LENGTH = 32
FLASH_BANK_A_USED_BIT_LENGTH = 32
FLASH_BANK_B_USED_BIT_LENGTH = 32
CURR_CUBE_BIT_LENGTH = 8
FPMC_RESERVED1_BIT_LENGTH = 16
FPMC_SW_VERSION_BIT_LENGTH = 8
FPMC_SW_TIME_BIT_LENGTH = 32
CURR_AID_BIT_LENGTH = 32
FPMC_WRITE_ENB_BIT_LENGTH = 1
CURR_FILTER_ID_BIT_LENGTH = 4
ROW_ORIGIN_BIT_LENGTH = 9
COLUMN_ORIGIN_BIT_LENGTH = 9
WINDOW_ROWS_BIT_LENGTH = 9
WINDOW_COLUMNS_BIT_LENGTH = 9
ROW_BINNING_BIT_LENGTH = 2
COLUMN_BINNING_BIT_LENGTH = 2
ROW_REORDER_BIT_LENGTH = 2
FPMC_RESERVED2_BIT_LENGTH = 17
SCAN_ERROR_BIT_LENGTH = 32
RESERVED_1_BIT_LENGTH = 8 * 8
RESERVED_2_BIT_LENGTH = 8 * 8
RESERVED_3_BIT_LENGTH = 824 * 8

hs_mise = ccsdspy.VariableLength([
    ccsdspy.PacketField(name="MSCLK Seconds", bit_length=32, data_type='uint'),
    ccsdspy.PacketField(name="MSCLK Subseconds", bit_length=16, data_type='uint'),
    # operational status
    ccsdspy.PacketField(name="Subseconds Pre-zero", bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name="IF Type", bit_length=1, data_type='uint'),
    ccsdspy.PacketField(name="Selected Interface", bit_length=1, data_type='uint'),
    ccsdspy.PacketField(name="Busy", bit_length=1, data_type='uint'),
    ccsdspy.PacketField(name="Panic", bit_length=1, data_type='uint'),
    ccsdspy.PacketField(name="Instrument Mode", bit_length=3, data_type='uint'),
    ccsdspy.PacketField(name="Operational Status Spare", bit_length=1, data_type='uint'),
    # command status
    ccsdspy.PacketField(name="Command Accepted Cnt", bit_length=8, data_type='uint'),
    ccsdspy.PacketField(name="Command Executed Cnt", bit_length=8, data_type='uint'),
    ccsdspy.PacketField(name="Command Rejected Count", bit_length=8, data_type='uint'),
    ccsdspy.PacketField(name="Most Recent Command's Sequence Count", bit_length=5, data_type='uint'),
    ccsdspy.PacketField(name="Most Recent Command's Status", bit_length=3, data_type='uint'),
    ccsdspy.PacketField(name="Most Recent Command's Opcode", bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name="2nd Most Recent Command's  Sequence Count", bit_length=5, data_type='uint'),
    ccsdspy.PacketField(name="2nd Most Recent Command's Status", bit_length=3, data_type='uint'),
    ccsdspy.PacketField(name="2nd Most Recent Command's Opcode", bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name="3rd Most Recent Command's  Sequence Count", bit_length=5, data_type='uint'),
    ccsdspy.PacketField(name="3rd Most Recent Command's Status", bit_length=3, data_type='uint'),
    ccsdspy.PacketField(name="3rd Most Recent Command's Opcode", bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name="4th Most Recent Command's  Sequence Count", bit_length=5, data_type='uint'),
    ccsdspy.PacketField(name="4th Most Recent Command's Status", bit_length=3, data_type='uint'),
    ccsdspy.PacketField(name="4th Most Recent Command's Opcode", bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name="5th Most Recent Command's  Sequence Count", bit_length=5, data_type='uint'),
    ccsdspy.PacketField(name="5th Most Recent Command's Status", bit_length=3, data_type='uint'),
    ccsdspy.PacketField(name="5th Most Recent Command's Opcode", bit_length=16, data_type='uint'),
    # uart status
    ccsdspy.PacketField(name="Error Count", bit_length=8, data_type='uint'),
    ccsdspy.PacketField(name="UART Spare", bit_length=14, data_type='uint'),
    # error bits (guides SC fault response)
    ccsdspy.PacketField(name="Req_SC_Power_Off (Requests instrument shutdown)", bit_length=1, data_type='uint'),
    ccsdspy.PacketField(name="Req_SC_Power_Cycle (OK to attempt instrument restart)", bit_length=1, data_type='uint'),
    # source data, derived parameters
    ccsdspy.PacketField(name="Source Data Derived Parameters SPARE", bit_length=24, data_type='uint'),
    ccsdspy.PacketField(name="CLOCKS_LAST_1PPS", bit_length=24, data_type='uint'),
    ccsdspy.PacketField(name="FG1_HTR_AVG", bit_length=24, data_type='uint'),
    ccsdspy.PacketField(name="FG2_HTR_AVG", bit_length=24, data_type='uint'),
    ccsdspy.PacketField(name="FG3_HTR_AVG", bit_length=24, data_type='uint'),
    ccsdspy.PacketField(name="FG1_DRIVE_PHASE", bit_length=8, data_type='uint'),
    ccsdspy.PacketField(name="FG2_DRIVE_PHASE", bit_length=8, data_type='uint'),
    ccsdspy.PacketField(name="FG3_DRIVE_PHASE", bit_length=8, data_type='uint'),
    ccsdspy.PacketField(name="SPARE", bit_length=2, data_type='uint'),
    ccsdspy.PacketField(name="I_TP_IN1", bit_length=1, data_type='uint'),
    ccsdspy.PacketField(name="I_TP_IN2", bit_length=1, data_type='uint'),
    ccsdspy.PacketField(name="I_FPGA_ID0", bit_length=1, data_type='uint'),
    ccsdspy.PacketField(name="I_FPGA_ID1", bit_length=1, data_type='uint'),
    ccsdspy.PacketField(name="I_FPGA_ID2", bit_length=1, data_type='uint'),
    ccsdspy.PacketField(name="I_FPGA_ID3", bit_length=1, data_type='uint'),
    ccsdspy.PacketField(name="FG_GENERAL_REGISTERS", bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name="VERSION", bit_length=24, data_type='uint'),
    # source data zero pad
    ccsdspy.PacketField(name="Source Data and Padding (Bits)", bit_length=16, data_type='uint'
                        ),
    # PEC
    ccsdspy.PacketField(name=CRC_FIELD_NAME, bit_length=16, data_type='uint'),
])

adp_metadata_mise = ccsdspy.VariableLength([
    ccsdspy.PacketField(name="MSCLK Seconds", bit_length=32, data_type='uint'),
    ccsdspy.PacketField(name="Subseconds Pre-zero", bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name="AID", bit_length=32, data_type='uint'),
    # ADP Metadata
    ccsdspy.PacketField(name="CTRL = START | END", bit_length=5, data_type='uint'),
    ccsdspy.PacketField(name="ADP Major APID", bit_length=5, data_type='uint'),
    ccsdspy.PacketField(name="ADP Minor APID", bit_length=6, data_type='uint'),
    ccsdspy.PacketField(name="SCLK", bit_length=48, data_type='uint'),
    ccsdspy.PacketField(name="Source Sequence Count", bit_length=14, data_type='uint'),
    ccsdspy.PacketField(name="Spare", bit_length=2, data_type='uint'),
    ccsdspy.PacketField(name="CTRL==END ? Count : Spare", bit_length=32, data_type='uint'),
    # PEC
    ccsdspy.PacketField(name=CRC_FIELD_NAME, bit_length=16, data_type='uint'),
])

command_echo_pkt = ccsdspy.VariableLength([
    ccsdspy.PacketField(name="Source Data", bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name=CRC_FIELD_NAME, bit_length=16, data_type='uint')
])

alarm_pkt = ccsdspy.VariableLength([
    ccsdspy.PacketField(name="Source Data", bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name=CRC_FIELD_NAME, bit_length=16, data_type='uint')
])

mem_chksum_pkt = ccsdspy.VariableLength([
    ccsdspy.PacketField(name="Source Data", bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name=CRC_FIELD_NAME, bit_length=16, data_type='uint')
])

mem_dump_pkt = ccsdspy.VariableLength([
    ccsdspy.PacketField(name="Source Data", bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name=CRC_FIELD_NAME, bit_length=16, data_type='uint')
])

status_pkt = ccsdspy.VariableLength([
    ccsdspy.PacketField(name="Source Data", bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name=CRC_FIELD_NAME, bit_length=16, data_type='uint')
])

boot_status_pkt = ccsdspy.VariableLength([
    ccsdspy.PacketField(name="Source Data", bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name=CRC_FIELD_NAME, bit_length=16, data_type='uint')
])

macro_dump_pkt = ccsdspy.VariableLength([
    ccsdspy.PacketField(name="Source Data", bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name=CRC_FIELD_NAME, bit_length=16, data_type='uint')
])

macro_chksum_pkt = ccsdspy.VariableLength([
    ccsdspy.PacketField(name="Source Data", bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name=CRC_FIELD_NAME, bit_length=16, data_type='uint')
])

mon_limits_pkt = ccsdspy.VariableLength([
    ccsdspy.PacketField(name="Source Data", bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name=CRC_FIELD_NAME, bit_length=16, data_type='uint')
])

param_pkts = ccsdspy.VariableLength([
    ccsdspy.PacketField(name="Source Data", bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name=CRC_FIELD_NAME, bit_length=16, data_type='uint')
])

text_pkt = ccsdspy.VariableLength([
    ccsdspy.PacketField(name="Source Data", bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name=CRC_FIELD_NAME, bit_length=16, data_type='uint')
])

fpie_reg_settings_pkt = ccsdspy.VariableLength([
    ccsdspy.PacketField(name="Source Data", bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name=CRC_FIELD_NAME, bit_length=16, data_type='uint')
])

ceu_reg_dump_pkt = ccsdspy.VariableLength([
    ccsdspy.PacketField(name="Source Data", bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name=CRC_FIELD_NAME, bit_length=16, data_type='uint')
])

fpie_reg_dump_pkt = ccsdspy.VariableLength([
    ccsdspy.PacketField(name="Source Data", bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name=CRC_FIELD_NAME, bit_length=16, data_type='uint')
])

fpmc_mem_chksum_pkt = ccsdspy.VariableLength([
    ccsdspy.PacketField(name="Source Data", bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name=CRC_FIELD_NAME, bit_length=16, data_type='uint')
])

fpmc_mem_dump_pkt = ccsdspy.VariableLength([
    ccsdspy.PacketField(name="Source Data", bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name=CRC_FIELD_NAME, bit_length=16, data_type='uint')
])

flash_error_pkt = ccsdspy.VariableLength([
    ccsdspy.PacketField(name="Source Data", bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name=CRC_FIELD_NAME, bit_length=16, data_type='uint')
])

deferred_cmd_echo_pkt = ccsdspy.VariableLength([
    ccsdspy.PacketField(name="Source Data", bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name=CRC_FIELD_NAME, bit_length=16, data_type='uint')
])
sequence_count: int = 0
PAD_LENGTH_BYTES = 2

uncomp_frame_pkt = ccsdspy.VariableLength([
    ccsdspy.PacketField(name="Instrument SCLK Time second", bit_length=SECOND_LENGTH_BYTES * 8,
                        data_type='uint'),
    ccsdspy.PacketField(name="Instrument SCLK Time subsec", bit_length=SUBSECOND_LENGTH_BYTES * 8,
                        data_type='uint'),
    ccsdspy.PacketField(name="Accountability ID", bit_length=AID_LENGTH_BYTES * 8, data_type='uint'),
    # PacketListField(
    #     "Data", 3376*8, data_type.LIST, data_type = 'uint'BE,
    #     bit_length = DATA_ELEMENT_SIZE_BITS
    # ),
    # ccsdspy.PacketField(name="Pad", bit_length=PAD_LENGTH_BYTES*8, data_type.PADDING),
    ccsdspy.PacketField(
        name=CRC_FIELD_NAME,
        bit_length=CHECKSUM_LENGTH_BYTES * 8,
        data_type='uint'),
    ccsdspy.PacketField(name="Instrument SCLK Time second", bit_length=SECOND_LENGTH_BYTES * 8,
                        data_type='uint'),
    ccsdspy.PacketField(name="Instrument SCLK Time subsec", bit_length=SUBSECOND_LENGTH_BYTES * 8,
                        data_type='uint'),
    ccsdspy.PacketField(name="Accountability ID", bit_length=AID_LENGTH_BYTES * 8, data_type='uint'),
    # PacketListField("Data", 3360*8, data_type.LIST, data_type = 'uint'BE,
    #     bit_length = DATA_ELEMENT_SIZE_BITS
    # ),
    ccsdspy.PacketField(name="Time", bit_length=16 * 8, data_type='uint'),
    # ccsdspy.PacketField(name="Pad", PAD_LENGTH_BYTES*8, data_type.PADDING),
    ccsdspy.PacketField(
        name=CRC_FIELD_NAME,
        bit_length=CHECKSUM_LENGTH_BYTES * 8,
        data_type='uint'),

    # see specification in MISE Flight Software Specification 7489-9100, Table 55. Ancillary Data
    ccsdspy.PacketField(name="Instrument SCLK Time second", bit_length=SECOND_LENGTH_BYTES * 8,
                        data_type='uint'),
    ccsdspy.PacketField(name="Instrument SCLK Time subsec", bit_length=SUBSECOND_LENGTH_BYTES * 8,
                        data_type='uint'),
    ccsdspy.PacketField(name="Accountability ID", bit_length=AID_LENGTH_BYTES * 8, data_type='uint'),
    # ccsdspy.PacketField(name="Spare", 8 * 16, data_type.PADDING),

    # Ancillary Data - Analog
    ccsdspy.PacketField(name="LVPS_1_0", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="LVPS_1_1", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="LVPS_1_2", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="LVPS_1_3", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="LVPS_1_4", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="LVPS_1_5", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="LVPS_2_0", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="LVPS_2_1", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="LVPS_2_2", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="LVPS_2_3", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="LVPS_2_4", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="LVPS_2_5", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="LVPS_3_0", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="LVPS_3_1", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="LVPS_3_2", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="LVPS_3_3", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="LVPS_3_4", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="LVPS_3_5", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="LVPS_4_0", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="LVPS_4_1", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="LVPS_4_2", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="LVPS_4_3", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="LVPS_4_4", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="LVPS_4_5", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="LVPS_4_6", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="LVPS_4_7", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="IFC_0_0", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="IFC_0_1", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="IFC_0_2", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="IFC_0_3", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="IFC_0_4", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="IFC_0_5", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="IFC_0_6", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="IFC_0_7", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="IFC_0_8", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="IFC_0_9", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="IFC_0_10", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="IFC_0_11", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="IFC_0_15", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Analog_Reserved", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),

    # Ancillary Data - Digital
    ccsdspy.PacketField(name="Digital_Reserved1", bit_length=DIGITAL_RESERVED1_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="IFC_Power_Down", bit_length=IFC_POWER_DOWN_BIT_LENGTH, data_type='int'),
    ccsdspy.PacketField(name="IFC_Run", bit_length=IFC_RUN_BIT_LENGTH, data_type='int'),
    ccsdspy.PacketField(name="Digital_Reserved2", bit_length=DIGITAL_RESERVED2_BIT_LENGTH, data_type='int'),
    ccsdspy.PacketField(name="CEU_Drive", bit_length=CEU_DRIVE_BIT_LENGTH, data_type='int'),
    ccsdspy.PacketField(name="IFC_Power", bit_length=IFC_POWER__BIT_LENGTH, data_type='int'),
    ccsdspy.PacketField(name="FPIE_Power", bit_length=FPIE_POWER__BIT_LENGTH, data_type='int'),
    ccsdspy.PacketField(name="FPMC_Power", bit_length=FPMC_POWER_BIT_LENGTH, data_type='int'),
    ccsdspy.PacketField(name="CEU_Cont._Temp.", bit_length=CEU_CONT_TEMP_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="CEU_Aux._Temp.", bit_length=CEU_AUX_TEMP_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="CEU_PI_Out", bit_length=CEU_PI_OUT_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="CEU_Peak_Bus_Voltage", bit_length=CEU_PEAK_BUS_VOLTAGE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="CEU_Bus_Current", bit_length=CUE_BUS_CURRENT_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="CEU_Bus_Voltage", bit_length=CEU_BUS_VOLTAGE__BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Digital_Reserved3", bit_length=DIGITAL_RESERVED3_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="CEU_Temp_Sensor", bit_length=CEU_TEMP_SENSOR_BIT_LENGTH, data_type='int'),
    ccsdspy.PacketField(name="CEU_Mode_", bit_length=CEU_MODE_BIT_LENGTH, data_type='int'),
    ccsdspy.PacketField(name="CEU_H-_Bridge", bit_length=CEU_H_BRIDGE_BIT_LENGTH, data_type='int'),
    ccsdspy.PacketField(name="CEU_Motor_A_Peak_POS_V", bit_length=CEU_MOTOR_A_PEAK_POS_V_BIT_LENGTH,
                        data_type='uint'),
    ccsdspy.PacketField(name="CEU_Motor_A_Peak_NEG_V", bit_length=CEU_MOTOR_A_PEAK_NEG_V_BIT_LENGTH,
                        data_type='uint'),
    ccsdspy.PacketField(name="CEU_Motor_B_Peak_POS_V", bit_length=CEU_MOTOR_B_PEAK_POS_V_BIT_LENGTH,
                        data_type='uint'),
    ccsdspy.PacketField(name="CEU_Motor_B_Peak_NEG_V", bit_length=CEU_MOTOR_B_PEAK_NEG_V_BIT_LENGTH,
                        data_type='uint'),

    # Ancillary Data - Software
    ccsdspy.PacketField(name="Status_Int", bit_length=STATUS_INT_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Macro_Blocks", bit_length=MACRO_BLOCKS_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Tlm_Vol", bit_length=TLM_VOL_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Watch_Addr", bit_length=WATCH_ADDR_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Watch_Mem", bit_length=WATCH_MEM_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Watch_Data", bit_length=WATCH_DATA_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="SW_Version", bit_length=SW_VERSION_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="SW_Time", bit_length=SW_TIME_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Alarm_ID", bit_length=ALARM_ID_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Alarm_Type", bit_length=ALRAM_TYPE_BIT_LENGTH, data_type='int'),
    ccsdspy.PacketField(name="Alarm_Count", bit_length=ALARM_COUNT_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Cmd_Exec", bit_length=CMD_EXEC_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Cmd_Reject", bit_length=CMD_REJECT_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Mac_Exec", bit_length=MAC_EXEC_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Mac_Reject", bit_length=MAC_REJECT_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Macro_Id", bit_length=MACRO_ID_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Macro_Learn", bit_length=MACRO_LEARN_BIT_LENGTH, data_type='int'),
    ccsdspy.PacketField(name="Monitor_Response", bit_length=MONITOR_RESPONSE_BIT_LENGTH, data_type='int'),
    ccsdspy.PacketField(name="Write_Enb", bit_length=WRITE_ENB_BIT_LENGTH, data_type='int'),
    ccsdspy.PacketField(name="Scan_Diag_Enb", bit_length=SCAN_DIAG_ENB_BIT_LENGTH, data_type='int'),
    ccsdspy.PacketField(name="Cooler_State", bit_length=COOLER_STATE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Safing_Time", bit_length=SAFING_TIME_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Cooler_Temp_Goal", bit_length=COOLER_TEMP_GOAL_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Current_Angle", bit_length=CURRENT_ANGLE_BIT_LENGTH, data_type='int'),
    ccsdspy.PacketField(name="Goal_Angle", bit_length=GOAL_ANGLE_BIT_LENGTH, data_type='int'),
    ccsdspy.PacketField(name="Slew_Angle", bit_length=SLEW_ANGLE_BIT_LENGTH, data_type='int'),
    ccsdspy.PacketField(name="Offset_Angle", bit_length=OFFSET_ANGLE_BIT_LENGTH, data_type='int'),
    ccsdspy.PacketField(name="Offset_Rate", bit_length=OFFSET_RATE_BIT_LENGTH, data_type='int'),
    # ccsdspy.PacketField(name="Offset_Adjustment", bit_length = OFFSET_ADJUSTMENT_BIT_LENGTH, data_type = 'int'),
    ccsdspy.PacketField(name="Cryocooler_Heater_Control", bit_length=CRYOCOOLER_HEATER_CONTROL_BIT_LENGTH,
                        data_type='uint'),
    ccsdspy.PacketField(name="Scan_Loop_Mode", bit_length=SCAN_LOOP_MODE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Scan_Mode", bit_length=SCAN_MODE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Scan_Pos_Mode", bit_length=SCAN_POS_MODE_BIT_LENGTH, data_type='int'),
    ccsdspy.PacketField(name="Primary_Winding", bit_length=PRIMARY_WINDING_BIT_LENGTH, data_type='int'),
    ccsdspy.PacketField(name="Secondary_Winding", bit_length=SECONDARY_WINDING_BIT_LENGTH, data_type='int'),
    ccsdspy.PacketField(name="Timeline_Enb", bit_length=TIMELINE_ENB_BIT_LENGTH, data_type='int'),
    ccsdspy.PacketField(name="Observe", bit_length=OBSERVE_BIT_LENGTH, data_type='int'),
    ccsdspy.PacketField(name="FPMC_Status_Valid", bit_length=FPMC_STATUS_VALID_BIT_LENGTH, data_type='int'),
    ccsdspy.PacketField(name="Cryocooler_Heater", bit_length=CRYOCOOLER_HEATER_BIT_LENGTH, data_type='int'),
    ccsdspy.PacketField(name="Scan_Fallback", bit_length=SCAN_FALLBACK_BIT_LENGTH, data_type='int'),
    ccsdspy.PacketField(name="Scan_Stability_Error_Rate", bit_length=SCAN_STABILITY_ERROR_RATE_BIT_LENGTH,
                        data_type='uint'),
    ccsdspy.PacketField(name="Target_ID", bit_length=TARGET_ID_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Observe_Macro_ID", bit_length=OBSERVE_MACRO_ID_BIT_LENGTH, data_type='uint'),
    # ccsdspy.PacketField(name="Scan_Stall", bit_length = SCAN_STALL_BIT_LENGTH, data_type = ),
    ccsdspy.PacketField(name="Software_Reserved", bit_length=SOFTWARE_STATUS_RESERVED_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Profile_ID", bit_length=PROFILE_ID_BIT_LENGTH, data_type='int'),
    ccsdspy.PacketField(name="Profile_Time_Seconds", bit_length=PROFILE_TIME_SECONDS_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Profile_Time_Subseconds", bit_length=PROFILE_TIME_SUBSECONDS_BIT_LENGTH,
                        data_type='uint'),

    # Ancillary Data - FPMC
    ccsdspy.PacketField(name="Log_used", bit_length=LOG_USED_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Flash_Bank_A_Used", bit_length=FLASH_BANK_A_USED_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Flash_Bank_B_Used", bit_length=FLASH_BANK_B_USED_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Curr._Cube", bit_length=CURR_CUBE_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="FPMC_Reserved1", bit_length=FPMC_RESERVED1_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="FPMC_SW_Version", bit_length=FPMC_SW_VERSION_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="FPMC_SW_Time", bit_length=FPMC_SW_TIME_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Curr._AID", bit_length=CURR_AID_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="FPMC_Write_Enb", bit_length=FPMC_WRITE_ENB_BIT_LENGTH, data_type='int'),
    ccsdspy.PacketField(name="Curr._Filter_ID", bit_length=CURR_FILTER_ID_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Row_Origin", bit_length=ROW_ORIGIN_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Column_Origin", bit_length=COLUMN_ORIGIN_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Window_Rows", bit_length=WINDOW_ROWS_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Window_Columns", bit_length=WINDOW_COLUMNS_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Row_Binning", bit_length=ROW_BINNING_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Column_Binning", bit_length=COLUMN_BINNING_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="Row_reorder", bit_length=ROW_REORDER_BIT_LENGTH, data_type='uint'),
    ccsdspy.PacketField(name="FPMC_Reserved2", bit_length=FPMC_RESERVED2_BIT_LENGTH, data_type='uint'),

    # Ancillary Data - Reserved 1
    ccsdspy.PacketField(name="Reserved_1", bit_length=RESERVED_1_BIT_LENGTH, data_type='uint'),

    # Ancillary Data - Software Part 2
    ccsdspy.PacketField(name="Scan_Error", bit_length=SCAN_ERROR_BIT_LENGTH, data_type='uint'),

    # Ancillary Data - Reserved 2
    ccsdspy.PacketField(name="Reserved_2", bit_length=RESERVED_2_BIT_LENGTH, data_type='uint'),

    # Ancillary Data - Reserved 3
    ccsdspy.PacketField(name="Reserved_3", bit_length=RESERVED_3_BIT_LENGTH, data_type='uint'),

    # ccsdspy.PacketField(name="Pad", 8 * PAD_LENGTH_BYTES, data_type.PADDING),

    ccsdspy.PacketField(name=CRC_FIELD_NAME,
                        bit_length=CHECKSUM_LENGTH_BYTES * 8,
                        data_type='uint'),
])

uncomp_frame_pkt.add_converted_field("Time", "Time_BIN", StringifyBytesConverter(format="bin"))

data_length_without_frame = 4 * 9 + 2 * 2 + 14

comp_frame_pkt = ccsdspy.VariableLength([
    ccsdspy.PacketField(name="Instrument SCLK Time second", bit_length=8 * SECOND_LENGTH_BYTES, data_type='uint'),
    ccsdspy.PacketField(name="Instrument SCLK Time subsec", bit_length=8 * SUBSECOND_LENGTH_BYTES, data_type='uint'),
    ccsdspy.PacketField(name="Accountability ID", bit_length=8 * AID_LENGTH_BYTES, data_type='uint'),
    ccsdspy.PacketField(name="Row Origin", bit_length=9, data_type='uint'),
    ccsdspy.PacketField(name="Column Origin", bit_length=9, data_type='uint'),
    ccsdspy.PacketField(name="Window Rows", bit_length=9, data_type='uint'),
    ccsdspy.PacketField(name="Window Columns", bit_length=9, data_type='uint'),
    ccsdspy.PacketField(name="Row Binning", bit_length=2, data_type='uint'),
    ccsdspy.PacketField(name="Column Binning", bit_length=2, data_type='uint'),
    ccsdspy.PacketField(name="P0,0", bit_length=14, data_type='uint'),
    ccsdspy.PacketField(name=CRC_FIELD_NAME, bit_length=16, data_type='uint')
])

frame_support_pkt = ccsdspy.VariableLength([
    ccsdspy.PacketField(name="Source Data", bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name=CRC_FIELD_NAME, bit_length=16, data_type='uint')
])

DIAG_COUNT_PKT = ccsdspy.VariableLength([
    ccsdspy.PacketField(name="Instrument SCLK Time second", bit_length=8 * SECOND_LENGTH_BYTES, data_type='uint'),
    ccsdspy.PacketField(name="Instrument SCLK Time subsec", bit_length=8 * SUBSECOND_LENGTH_BYTES, data_type='uint'),
    ccsdspy.PacketField(name="Accountability ID", bit_length=8 * AID_LENGTH_BYTES, data_type='uint'),
    ccsdspy.PacketField(name=CRC_FIELD_NAME, bit_length=16, data_type='uint')
])

diag_flag_pkt = ccsdspy.VariableLength([
    ccsdspy.PacketField(name="Instrument SCLK Time second", bit_length=8 * SECOND_LENGTH_BYTES, data_type='uint'),
    ccsdspy.PacketField(name="Instrument SCLK Time subsec", bit_length=8 * SUBSECOND_LENGTH_BYTES, data_type='uint'),
    ccsdspy.PacketField(name="Accountability ID", bit_length=8 * AID_LENGTH_BYTES, data_type='uint'),
    ccsdspy.PacketField(name=CRC_FIELD_NAME, bit_length=16, data_type='uint')
])

SECOND_LENGTH_BYTES = 4
SUBSECOND_LENGTH_BYTES = 2
AID_LENGTH_BYTES = 4
CHECKSUM_LENGTH_BYTES = 2
DIGITAL_RESERVED1_BIT_LENGTH = 9
IFC_POWER_DOWN_BIT_LENGTH = 1
IFC_RUN_BIT_LENGTH = 1
DIGITAL_RESERVED2_BIT_LENGTH = 1
CEU_DRIVE_BIT_LENGTH = 1
IFC_POWER__BIT_LENGTH = 1
FPIE_POWER__BIT_LENGTH = 1
FPMC_POWER_BIT_LENGTH = 1
CEU_CONT_TEMP_BIT_LENGTH = 16
CEU_AUX_TEMP_BIT_LENGTH = 16
CEU_PI_OUT_BIT_LENGTH = 16
CEU_PEAK_BUS_VOLTAGE_BIT_LENGTH = 16
CUE_BUS_CURRENT_BIT_LENGTH = 16
CEU_BUS_VOLTAGE__BIT_LENGTH = 16
DIGITAL_RESERVED3_BIT_LENGTH = 13
CEU_TEMP_SENSOR_BIT_LENGTH = 1
CEU_MODE_BIT_LENGTH = 1
CEU_H_BRIDGE_BIT_LENGTH = 1
CEU_MOTOR_A_PEAK_POS_V_BIT_LENGTH = 16
CEU_MOTOR_A_PEAK_NEG_V_BIT_LENGTH = 16
CEU_MOTOR_B_PEAK_POS_V_BIT_LENGTH = 16
CEU_MOTOR_B_PEAK_NEG_V_BIT_LENGTH = 16
STATUS_INT_BIT_LENGTH = 16
MACRO_BLOCKS_BIT_LENGTH = 16
TLM_VOL_BIT_LENGTH = 16
WATCH_ADDR_BIT_LENGTH = 16
WATCH_MEM_BIT_LENGTH = 8
WATCH_DATA_BIT_LENGTH = 16
SW_VERSION_BIT_LENGTH = 8
SW_TIME_BIT_LENGTH = 32
ALARM_ID_BIT_LENGTH = 8
ALRAM_TYPE_BIT_LENGTH = 1
ALARM_COUNT_BIT_LENGTH = 7
CMD_EXEC_BIT_LENGTH = 8
CMD_REJECT_BIT_LENGTH = 8
MAC_EXEC_BIT_LENGTH = 8
MAC_REJECT_BIT_LENGTH = 8
MACRO_ID_BIT_LENGTH = 8
MACRO_LEARN_BIT_LENGTH = 1
MONITOR_RESPONSE_BIT_LENGTH = 1
WRITE_ENB_BIT_LENGTH = 1
SCAN_DIAG_ENB_BIT_LENGTH = 1
COOLER_STATE_BIT_LENGTH = 4
SAFING_TIME_BIT_LENGTH = 16
COOLER_TEMP_GOAL_BIT_LENGTH = 16
CURRENT_ANGLE_BIT_LENGTH = 32
GOAL_ANGLE_BIT_LENGTH = 32
SLEW_ANGLE_BIT_LENGTH = 32
OFFSET_ANGLE_BIT_LENGTH = 32
OFFSET_RATE_BIT_LENGTH = 32
CRYOCOOLER_HEATER_CONTROL_BIT_LENGTH = 2
SCAN_LOOP_MODE_BIT_LENGTH = 2
SCAN_MODE_BIT_LENGTH = 3
SCAN_POS_MODE_BIT_LENGTH = 1
PRIMARY_WINDING_BIT_LENGTH = 1
SECONDARY_WINDING_BIT_LENGTH = 1
TIMELINE_ENB_BIT_LENGTH = 1
OBSERVE_BIT_LENGTH = 1
FPMC_STATUS_VALID_BIT_LENGTH = 1
CRYOCOOLER_HEATER_BIT_LENGTH = 1
SCAN_FALLBACK_BIT_LENGTH = 1
SCAN_STABILITY_ERROR_RATE_BIT_LENGTH = 16
TARGET_ID_BIT_LENGTH = 32
OBSERVE_MACRO_ID_BIT_LENGTH = 8
SOFTWARE_STATUS_RESERVED_BIT_LENGTH = 2
PROFILE_ID_BIT_LENGTH = 5
PROFILE_TIME_SECONDS_BIT_LENGTH = 32
PROFILE_TIME_SUBSECONDS_BIT_LENGTH = 16
LOG_USED_BIT_LENGTH = 32
FLASH_BANK_A_USED_BIT_LENGTH = 32
FLASH_BANK_B_USED_BIT_LENGTH = 32
CURR_CUBE_BIT_LENGTH = 8
FPMC_RESERVED1_BIT_LENGTH = 16
FPMC_SW_VERSION_BIT_LENGTH = 8
FPMC_SW_TIME_BIT_LENGTH = 32
CURR_AID_BIT_LENGTH = 32
FPMC_WRITE_ENB_BIT_LENGTH = 1
CURR_FILTER_ID_BIT_LENGTH = 4
ROW_ORIGIN_BIT_LENGTH = 9
COLUMN_ORIGIN_BIT_LENGTH = 9
WINDOW_ROWS_BIT_LENGTH = 9
WINDOW_COLUMNS_BIT_LENGTH = 9
ROW_BINNING_BIT_LENGTH = 2
COLUMN_BINNING_BIT_LENGTH = 2
ROW_REORDER_BIT_LENGTH = 2
FPMC_RESERVED2_BIT_LENGTH = 17
SCAN_ERROR_BIT_LENGTH = 32
RESERVED_1_BIT_LENGTH = 8 * 8
RESERVED_2_BIT_LENGTH = 8 * 8
RESERVED_3_BIT_LENGTH = 824 * 8

# MISEUncompFramePacketStructureFactory = ccsdspy.VariableLength([
#     ccsdspy.PacketField(name="Instrument SCLK Time second", bit_length=8 * SECOND_LENGTH_BYTES,
#                         data_type='uint'),
#     ccsdspy.PacketField(name="Instrument SCLK Time subsec", bit_length=8 * SUBSECOND_LENGTH_BYTES,
#                         data_type='uint'),
#     ccsdspy.PacketField(name="Accountability ID", bit_length=8 * AID_LENGTH_BYTES, data_type='uint'),
#     # PacketListField(
#     #     "Data", 3376*8, data_type.LIST, data_type = 'uint'BE,
#     #     DATA_ELEMENT_SIZE_BITS
#     # ),
#     # ccsdspy.PacketField(name = "Pad", bit_length=8 * PAD_LENGTH_BYTES, data_type.PADDING),
#     ccsdspy.PacketField(
#         name=CRC_FIELD_NAME,
#         bit_length=8 * CHECKSUM_LENGTH_BYTES,
#         data_type='uint'),
#     ccsdspy.PacketField(name="Instrument SCLK Time second", bit_length=8 * SECOND_LENGTH_BYTES,
#                         data_type='uint'),
#     ccsdspy.PacketField(name="Instrument SCLK Time subsec", bit_length=8 * SUBSECOND_LENGTH_BYTES,
#                         data_type='uint'),
#     ccsdspy.PacketField(name="Accountability ID", bit_length=8 * AID_LENGTH_BYTES, data_type='uint'),
#     # PacketListField("Data", 3360 * 8, data_type.LIST, data_type = 'uint'BE,
#     #                 DATA_ELEMENT_SIZE_BITS
#     #                 ),
#     ccsdspy.PacketField(name="Time", bit_length=16 * 8, data_type='uint'),
#     # ccsdspy.PacketField(name = "Pad", bit_length=8 * PAD_LENGTH_BYTES, data_type.PADDING),
#     ccsdspy.PacketField(
#         name=CRC_FIELD_NAME,
#         bit_length=8 * CHECKSUM_LENGTH_BYTES,
#         data_type='uint'),
#     ccsdspy.PacketField(name="Instrument SCLK Time second", bit_length=8 * SECOND_LENGTH_BYTES,
#                         data_type='uint'),
#     ccsdspy.PacketField(name="Instrument SCLK Time subsec", bit_length=8 * SUBSECOND_LENGTH_BYTES,
#                         data_type='uint'),
#     ccsdspy.PacketField(name="Accountability ID", bit_length=8 * AID_LENGTH_BYTES, data_type='uint'),
#     # ccsdspy.PacketField(name = "Spare", 8 * 16, data_type.PADDING),
#
#     # Ancillary Data - Analog
#     ccsdspy.PacketField(name="LVPS_1_0", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="LVPS_1_1", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="LVPS_1_2", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="LVPS_1_3", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="LVPS_1_4", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="LVPS_1_5", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="LVPS_2_0", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="LVPS_2_1", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="LVPS_2_2", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="LVPS_2_3", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="LVPS_2_4", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="LVPS_2_5", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="LVPS_3_0", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="LVPS_3_1", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="LVPS_3_2", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="LVPS_3_3", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="LVPS_3_4", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="LVPS_3_5", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="LVPS_4_0", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="LVPS_4_1", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="LVPS_4_2", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="LVPS_4_3", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="LVPS_4_4", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="LVPS_4_5", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="LVPS_4_6", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="LVPS_4_7", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="IFC_0_0", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="IFC_0_1", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="IFC_0_2", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="IFC_0_3", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="IFC_0_4", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="IFC_0_5", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="IFC_0_6", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="IFC_0_7", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="IFC_0_8", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="IFC_0_9", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="IFC_0_10", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="IFC_0_11", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="IFC_0_15", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Analog_Reserved", bit_length=ANALOG_TWELVE_BIT_LENGTH, data_type='uint'),
#
#     # Ancillary Data - Digital
#     ccsdspy.PacketField(name="Digital_Reserved1", bit_length=DIGITAL_RESERVED1_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="IFC_Power_Down", bit_length=IFC_POWER_DOWN_BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="IFC_Run", bit_length=IFC_RUN_BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="Digital_Reserved2", bit_length=DIGITAL_RESERVED2_BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="CEU_Drive", bit_length=CEU_DRIVE_BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="IFC_Power", bit_length=IFC_POWER__BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="FPIE_Power", bit_length=FPIE_POWER__BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="FPMC_Power", bit_length=FPMC_POWER_BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="CEU_Cont._Temp.", bit_length=CEU_CONT_TEMP_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="CEU_Aux._Temp.", bit_length=CEU_AUX_TEMP_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="CEU_PI_Out", bit_length=CEU_PI_OUT_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="CEU_Peak_Bus_Voltage", bit_length=CEU_PEAK_BUS_VOLTAGE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="CEU_Bus_Current", bit_length=CUE_BUS_CURRENT_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="CEU_Bus_Voltage", bit_length=CEU_BUS_VOLTAGE__BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Digital_Reserved3", bit_length=DIGITAL_RESERVED3_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="CEU_Temp_Sensor", bit_length=CEU_TEMP_SENSOR_BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="CEU_Mode_", bit_length=CEU_MODE_BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="CEU_H-_Bridge", bit_length=CEU_H_BRIDGE_BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="CEU_Motor_A_Peak_POS_V", bit_length=CEU_MOTOR_A_PEAK_POS_V_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="CEU_Motor_A_Peak_NEG_V", bit_length=CEU_MOTOR_A_PEAK_NEG_V_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="CEU_Motor_B_Peak_POS_V", bit_length=CEU_MOTOR_B_PEAK_POS_V_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="CEU_Motor_B_Peak_NEG_V", bit_length=CEU_MOTOR_B_PEAK_NEG_V_BIT_LENGTH, data_type='uint'),
#
#     # Ancillary Data - Software
#     ccsdspy.PacketField(name="Status_Int", bit_length=STATUS_INT_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Macro_Blocks", bit_length=MACRO_BLOCKS_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Tlm_Vol", bit_length=TLM_VOL_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Watch_Addr", bit_length=WATCH_ADDR_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Watch_Mem", bit_length=WATCH_MEM_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Watch_Data", bit_length=WATCH_DATA_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="SW_Version", bit_length=SW_VERSION_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="SW_Time", bit_length=SW_TIME_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Alarm_ID", bit_length=ALARM_ID_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Alarm_Type", bit_length=ALRAM_TYPE_BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="Alarm_Count", bit_length=ALARM_COUNT_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Cmd_Exec", bit_length=CMD_EXEC_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Cmd_Reject", bit_length=CMD_REJECT_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Mac_Exec", bit_length=MAC_EXEC_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Mac_Reject", bit_length=MAC_REJECT_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Macro_Id", bit_length=MACRO_ID_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Macro_Learn", bit_length=MACRO_LEARN_BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="Monitor_Response", bit_length=MONITOR_RESPONSE_BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="Write_Enb", bit_length=WRITE_ENB_BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="Scan_Diag_Enb", bit_length=SCAN_DIAG_ENB_BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="Cooler_State", bit_length=COOLER_STATE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Safing_Time", bit_length=SAFING_TIME_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Cooler_Temp_Goal", bit_length=COOLER_TEMP_GOAL_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Current_Angle", bit_length=CURRENT_ANGLE_BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="Goal_Angle", bit_length=GOAL_ANGLE_BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="Slew_Angle", bit_length=SLEW_ANGLE_BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="Offset_Angle", bit_length=OFFSET_ANGLE_BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="Offset_Rate", bit_length=OFFSET_RATE_BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="Offset_Adjustment", bit_length=OFFSET_ADJUSTMENT_BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="Cryocooler_Heater_Control", bit_length=CRYOCOOLER_HEATER_CONTROL_BIT_LENGTH,
#                         data_type='uint'),
#     ccsdspy.PacketField(name="Scan_Loop_Mode", bit_length=SCAN_LOOP_MODE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Scan_Mode", bit_length=SCAN_MODE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Scan_Pos_Mode", bit_length=SCAN_POS_MODE_BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="Primary_Winding", bit_length=PRIMARY_WINDING_BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="Secondary_Winding", bit_length=SECONDARY_WINDING_BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="Timeline_Enb", bit_length=TIMELINE_ENB_BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="Observe", bit_length=OBSERVE_BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="FPMC_Status_Valid", bit_length=FPMC_STATUS_VALID_BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="Cryocooler_Heater", bit_length=CRYOCOOLER_HEATER_BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="Scan_Fallback", bit_length=SCAN_FALLBACK_BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="Scan_Stability_Error_Rate", bit_length=SCAN_STABILITY_ERROR_RATE_BIT_LENGTH,
#                         data_type='uint'),
#     ccsdspy.PacketField(name="Target_ID", bit_length=TARGET_ID_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Observe_Macro_ID", bit_length=OBSERVE_MACRO_ID_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Scan_Stall", bit_length=SCAN_STALL_BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="Software_Reserved", bit_length=SOFTWARE_STATUS_RESERVED_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Profile_ID", bit_length=PROFILE_ID_BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="Profile_Time_Seconds", bit_length=PROFILE_TIME_SECONDS_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Profile_Time_Subseconds", bit_length=PROFILE_TIME_SUBSECONDS_BIT_LENGTH,
#                         data_type='uint'),
#
#     # Ancillary Data - FPMC
#     ccsdspy.PacketField(name="Log_used", bit_length=LOG_USED_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Flash_Bank_A_Used", bit_length=FLASH_BANK_A_USED_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Flash_Bank_B_Used", bit_length=FLASH_BANK_B_USED_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Curr._Cube", bit_length=CURR_CUBE_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="FPMC_Reserved1", bit_length=FPMC_RESERVED1_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="FPMC_SW_Version", bit_length=FPMC_SW_VERSION_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="FPMC_SW_Time", bit_length=FPMC_SW_TIME_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Curr._AID", bit_length=CURR_AID_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="FPMC_Write_Enb", bit_length=FPMC_WRITE_ENB_BIT_LENGTH, data_type='int'),
#     ccsdspy.PacketField(name="Curr._Filter_ID", bit_length=CURR_FILTER_ID_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Row_Origin", bit_length=ROW_ORIGIN_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Column_Origin", bit_length=COLUMN_ORIGIN_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Window_Rows", bit_length=WINDOW_ROWS_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Window_Columns", bit_length=WINDOW_COLUMNS_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Row_Binning", bit_length=ROW_BINNING_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Column_Binning", bit_length=COLUMN_BINNING_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="Row_reorder", bit_length=ROW_REORDER_BIT_LENGTH, data_type='uint'),
#     ccsdspy.PacketField(name="FPMC_Reserved2", bit_length=FPMC_RESERVED2_BIT_LENGTH, data_type='uint'),
#
#     # Ancillary Data - Reserved 1
#     ccsdspy.PacketField(name="Reserved_1", bit_length=RESERVED_1_BIT_LENGTH, data_type='uint'),
#
#     # Ancillary Data - Software Part 2
#     ccsdspy.PacketField(name="Scan_Error", bit_length=SCAN_ERROR_BIT_LENGTH, data_type='uint'),
#
#     # Ancillary Data - Reserved 2
#     ccsdspy.PacketField(name="Reserved_2", bit_length=RESERVED_2_BIT_LENGTH, data_type='uint'),
#
#     # Ancillary Data - Reserved 3
#     ccsdspy.PacketField(name="Reserved_3", bit_length=RESERVED_3_BIT_LENGTH, data_type='uint'),
#
#     # ccsdspy.PacketField(name = "Pad", bit_length=8 * PAD_LENGTH_BYTES, data_type.PADDING),
#
#     ccsdspy.PacketField(name=CRC_FIELD_NAME,
#                         bit_length=8 * CHECKSUM_LENGTH_BYTES,
#                         data_type='uint'),
#
# ])

# MISEUncompFramePacketStructureFactory.add_converted_field("Time", "Time_BIN", StringifyBytesConverter(format="bin"))
