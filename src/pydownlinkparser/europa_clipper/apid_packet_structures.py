import ccsdspy as ccsdspy
from ccsdspy.constants import BITS_PER_BYTE
from pydownlinkparser.europa_clipper.suda_config import SudaCatalogListStructure, hs_suda, adp_suda, EVENT_LOG_PKT, \
    COMMAND_LOG_PKT, HARDWARE_CENTRIC_PKT, SOFTWARE_CENTRIC_PKT, MEM_DUMP_PKT, FLASH_TABLE_DUMP_PKT, DWELL_PKT, \
    CATALOG_LIST_PKT, ADC_REGISTER_PKT, EVENT_MESSAGE_PKT, SudaWaveformPacketStructure, POSTMORTEM_LOG_PKT, \
    SudaWaveformPacketStructureWithMD

from pydownlinkparser.europa_clipper.ecm_config import hs_pkt_structure, read_reg_structure, FG1_LOW_PKT, FG1_HIGH_PKT, \
    FG2_LOW_PKT, FG3_LOW_PKT, FG2_HIGH_PKT, FG3_HIGH_PKT, adp_pkt

from pydownlinkparser.europa_clipper.mise_config import mise_hs, mise_adp, COMMAND_ECHO_PKT, ALARM_PKT, MEM_CHKSUM_PKT, \
    MEM_DUMP_PKT, STATUS_PKT, BOOT_STATUS_PKT, MACRO_CHKSUM_PKT, MACRO_DUMP_PKT, MON_LIMITS_PKT, PARAM_PKTS, TEXT_PKT, \
    FPIE_REG_DUMP_PKT, CEU_REG_DUMP_PKT, FPIE_REG_SETTINGS_PKT, FPMC_MEM_DUMP_PKT, FPMC_MEM_CHKSUM_PKT, FLASH_ERROR_PKT, \
    DEFERRED_CMD_ECHO_PKT, UNCOMP_FRAME_PKT, COMP_FRAME_PKT, FRAME_SUPPORT_PKT, DIAG_FLAG_PKT

apid_packets = {
    1419: SudaCatalogListStructure(),
    1232: read_reg_structure,
    1216: hs_pkt_structure,
    1218: FG1_LOW_PKT,
    1219: FG1_HIGH_PKT,
    1222: FG2_LOW_PKT,
    1223: FG2_HIGH_PKT,
    1226: FG3_LOW_PKT,
    1227: FG3_HIGH_PKT,
    1217: adp_pkt,
    1408: hs_suda,
    1409: adp_suda,
    1410: EVENT_LOG_PKT,
    1411: POSTMORTEM_LOG_PKT,
    1412: COMMAND_LOG_PKT,
    1413: HARDWARE_CENTRIC_PKT,
    1414: SOFTWARE_CENTRIC_PKT,
    1415: MEM_DUMP_PKT,
    1416: FLASH_TABLE_DUMP_PKT,
    1417: DWELL_PKT,
    1418: EVENT_MESSAGE_PKT,
    1420: ADC_REGISTER_PKT,
    1424: SudaWaveformPacketStructure,
    1432: CATALOG_LIST_PKT,
    1344: mise_hs,
    1345: mise_adp,
    1346: COMMAND_ECHO_PKT,
    1347: ALARM_PKT,
    1348: MEM_CHKSUM_PKT,
    1349: STATUS_PKT,
    1350: BOOT_STATUS_PKT,
    1351: MACRO_DUMP_PKT,
    1352: MACRO_CHKSUM_PKT,
    1354: MON_LIMITS_PKT,
    1355: PARAM_PKTS,
    1356: TEXT_PKT,
    1357: FPIE_REG_SETTINGS_PKT,
    1360: CEU_REG_DUMP_PKT,
    1361: FPIE_REG_DUMP_PKT,
    # 1371, 1392
    1376: FPMC_MEM_CHKSUM_PKT,
    1377: FPMC_MEM_DUMP_PKT,
    1378: FLASH_ERROR_PKT,
    1379: DEFERRED_CMD_ECHO_PKT,
    1380: UNCOMP_FRAME_PKT,
    1381: COMP_FRAME_PKT,
    1382: FRAME_SUPPORT_PKT,
    1385: DIAG_FLAG_PKT
}

default_pkt = ccsdspy.VariableLength(
    [
        ccsdspy.PacketArray(
            name="data", data_type="uint", bit_length=BITS_PER_BYTE, array_shape="expand"
        )
    ]
)


def is_metadata(decision_value):
    return decision_value == 0x1


apid_multi_pkt = {
    1424: dict(
        decision_field='SCI0TYPE',
        decision_fun=is_metadata,
        pkts={
            True: SudaWaveformPacketStructure,
            False: SudaWaveformPacketStructureWithMD
        }
    )
}

multi_apid_names = {
    1424: 'SudaWF'
}

apid_names = {
    1232: 'read_reg_structure',
    1216: 'hs_pkt_structure',
    1218: 'FG1_LOW_PKT',
    1219: 'FG1_HIGH_PKT',
    1222: 'FG2_LOW_PKT',
    1223: 'FG2_HIGH_PKT',
    1226: 'FG3_LOW_PKT',
    1227: 'FG3_HIGH_PKT',
    1217: 'adp_pkt',
    1344: 'mise_hs',
    1346: 'COMMAND_ECHO_PKT',
    1350: 'BOOT_STATUS_PKT',
    1408: 'hs_suda',
    1409: 'adp_suda',
    1410: 'EVENT_LOG_PKT',
    1411: 'POSTMORTEM_LOG_PKT',
    1412: 'COMMAND_LOG_PKT',
    1413: 'HARDWARE_CENTRIC_PKT',
    1414: 'SOFTWARE_CENTRIC_PKT',
    1415: 'MEM_DUMP_PKT',
    1416: 'FLASH_TABLE_DUMP_PKT',
    1417: 'DWELL_PKT',
    1418: 'EVENT_MESSAGE_PKT',
    1419: 'SudaCatalogListStructure',
    1420: 'ADC_REGISTER_PKT',
    1432: 'CATALOG_LIST_PKT',
}
