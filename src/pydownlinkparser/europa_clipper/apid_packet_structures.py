"""
...
"""
import ccsdspy
from ccsdspy.constants import BITS_PER_BYTE

from .ecm_config import adp_pkt
from .ecm_config import FG1_HIGH_PKT
from .ecm_config import FG1_LOW_PKT
from .ecm_config import FG2_HIGH_PKT
from .ecm_config import FG2_LOW_PKT
from .ecm_config import FG3_HIGH_PKT
from .ecm_config import FG3_LOW_PKT
from .ecm_config import hs_pkt_structure
from .ecm_config import read_reg_structure
from .mise_config import ALARM_PKT
from .mise_config import BOOT_STATUS_PKT
from .mise_config import CEU_REG_DUMP_PKT
from .mise_config import COMMAND_ECHO_PKT
from .mise_config import COMP_FRAME_PKT
from .mise_config import DEFERRED_CMD_ECHO_PKT
from .mise_config import DIAG_FLAG_PKT
from .mise_config import FLASH_ERROR_PKT
from .mise_config import FPIE_REG_DUMP_PKT
from .mise_config import FPIE_REG_SETTINGS_PKT
from .mise_config import FPMC_MEM_CHKSUM_PKT
from .mise_config import FPMC_MEM_DUMP_PKT
from .mise_config import FRAME_SUPPORT_PKT
from .mise_config import MACRO_CHKSUM_PKT
from .mise_config import MACRO_DUMP_PKT
from .mise_config import MEM_CHKSUM_PKT
from .mise_config import MEM_DUMP_PKT
from .mise_config import mise_adp
from .mise_config import mise_hs
from .mise_config import MON_LIMITS_PKT
from .mise_config import PARAM_PKTS
from .mise_config import STATUS_PKT
from .mise_config import TEXT_PKT
from .mise_config import UNCOMP_FRAME_PKT
from .suda_config import ADC_REGISTER_PKT
from .suda_config import adp_suda
from .suda_config import CATALOG_LIST_PKT
from .suda_config import COMMAND_LOG_PKT
from .suda_config import DWELL_PKT
from .suda_config import EVENT_LOG_PKT
from .suda_config import EVENT_MESSAGE_PKT
from .suda_config import FLASH_TABLE_DUMP_PKT
from .suda_config import HARDWARE_CENTRIC_PKT
from .suda_config import hs_suda
from .suda_config import MEM_DUMP_PKT
from .suda_config import POSTMORTEM_LOG_PKT
from .suda_config import SOFTWARE_CENTRIC_PKT
from .suda_config import SudaCatalogListStructure
from .suda_config import SudaWaveformPacketStructure
from .suda_config import SudaWaveformPacketStructureWithMD
from pydownlinkparser.util import default_pkt

# for each supported APID, define a ccsdspy.VariableLength packet definition
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
    1385: DIAG_FLAG_PKT,
    1392: default_pkt,
}


def is_metadata(decision_value):
    return decision_value == 0x1


# N = 0
# def sequence(decision_value):
#     N += 1
#     if N < 90:
#         return "90firsts"
#     if N == 90:
#         return "91st"
#     else:
#         return "92nd"


apid_multi_pkt = {
    1424: dict(
        decision_field="SCI0TYPE",
        decision_fun=is_metadata,
        pkts={
            True: SudaWaveformPacketStructure,
            False: SudaWaveformPacketStructureWithMD,
        },
    ),
    # 1392: dict(
    #     decision_fun=sequence,
    #     pkts={
    #         "90firsts": ...
    #         "91st": ...
    #         ...
    #     }
    # )
}

# TODO we could also add a name attribute to all the VariableLength structures, by creating in the core package a NamedVariableLength object.
# the name would be a property of the object, we would not need to manage the dictionnary after
# we also need a fall off case where the object will be a VariableLength object with no name,
# we would then use the object name by introspection and add a sequence number to avoid collisions

multi_apid_names = {1424: "SudaWF"}

apid_names = {
    1232: "read_reg_structure",
    1216: "hs_pkt_structure",
    1218: "FG1_LOW_PKT",
    1219: "FG1_HIGH_PKT",
    1222: "FG2_LOW_PKT",
    1223: "FG2_HIGH_PKT",
    1226: "FG3_LOW_PKT",
    1227: "FG3_HIGH_PKT",
    1217: "adp_pkt",
    1344: "mise_hs",
    1346: "COMMAND_ECHO_PKT",
    1350: "BOOT_STATUS_PKT",
    # 1392: 'MISEUncompFramePacketStructureFactory',
    1408: "hs_suda",
    1409: "adp_suda",
    1410: "EVENT_LOG_PKT",
    1411: "POSTMORTEM_LOG_PKT",
    1412: "COMMAND_LOG_PKT",
    1413: "HARDWARE_CENTRIC_PKT",
    1414: "SOFTWARE_CENTRIC_PKT",
    1415: "MEM_DUMP_PKT",
    1416: "FLASH_TABLE_DUMP_PKT",
    1417: "DWELL_PKT",
    1418: "EVENT_MESSAGE_PKT",
    1419: "SudaCatalogListStructure",
    1420: "ADC_REGISTER_PKT",
    1432: "CATALOG_LIST_PKT",
}
