"""
...
"""
import ccsdspy
from ccsdspy.constants import BITS_PER_BYTE

from .ecm_config import adp_metadata_ecm
from .ecm_config import fg1_high_pkt
from .ecm_config import fg1_low_pkt
from .ecm_config import fg2_high_pkt
from .ecm_config import fg2_low_pkt
from .ecm_config import fg3_high_pkt
from .ecm_config import fg3_low_pkt
from .ecm_config import hs_ecm
from .ecm_config import read_reg_structure
from .mise_config import alarm_pkt
from .mise_config import boot_status_pkt
from .mise_config import ceu_reg_dump_pkt
from .mise_config import command_echo_pkt
from .mise_config import comp_frame_pkt
from .mise_config import deferred_cmd_echo_pkt
from .mise_config import diag_flag_pkt
from .mise_config import flash_error_pkt
from .mise_config import fpie_reg_dump_pkt
from .mise_config import fpie_reg_settings_pkt
from .mise_config import fpmc_mem_chksum_pkt
from .mise_config import fpmc_mem_dump_pkt
from .mise_config import frame_support_pkt
from .mise_config import macro_chksum_pkt
from .mise_config import macro_dump_pkt
from .mise_config import mem_chksum_pkt
from .mise_config import mem_dump_pkt
from .mise_config import adp_metadata_mise
from .mise_config import hs_mise
from .mise_config import mon_limits_pkt
from .mise_config import param_pkts
from .mise_config import status_pkt
from .mise_config import text_pkt
from .mise_config import uncomp_frame_pkt
from .suda_config import adc_register_pkt
from .suda_config import adp_metadata_suda
from .suda_config import catalog_list_pkt
from .suda_config import command_log_pkt
from .suda_config import dwell_pkt
from .suda_config import event_log_pkt
from .suda_config import event_message_pkt
from .suda_config import flash_table_dump_pkt
from .suda_config import hardware_centric_pkt
from .suda_config import hs_suda
from .suda_config import mem_dump_pkt
from .suda_config import postmortem_log_pkt
from .suda_config import software_centric_pkt
from .suda_config import catalog_list
from .suda_config import event_wf_transmit
from .suda_config import event_wf_fetch
from .suda_config import event_wf_transmit_with_md
from pydownlinkparser.util import default_pkt

# for each supported APID, define a ccsdspy.VariableLength packet definition
apid_packets = {
    1419: catalog_list,
    1232: read_reg_structure,
    1216: hs_ecm,
    1218: fg1_low_pkt,
    1219: fg1_high_pkt,
    1222: fg2_low_pkt,
    1223: fg2_high_pkt,
    1226: fg3_low_pkt,
    1227: fg3_high_pkt,
    1217: adp_metadata_ecm,
    1408: hs_suda,
    1409: adp_metadata_suda,
    1410: event_log_pkt,
    1411: postmortem_log_pkt,
    1412: command_log_pkt,
    1413: hardware_centric_pkt,
    1414: software_centric_pkt,
    1415: mem_dump_pkt,
    1416: flash_table_dump_pkt,
    1417: dwell_pkt,
    1418: event_message_pkt,
    1420: adc_register_pkt,
    1424: event_wf_transmit,
    1426: event_wf_fetch,
    1432: catalog_list_pkt,
    1344: hs_mise,
    1345: adp_metadata_mise,
    1346: command_echo_pkt,
    1347: alarm_pkt,
    1348: mem_chksum_pkt,
    1349: status_pkt,
    1350: boot_status_pkt,
    1351: macro_dump_pkt,
    1352: macro_chksum_pkt,
    1354: mon_limits_pkt,
    1355: param_pkts,
    1356: text_pkt,
    1357: fpie_reg_settings_pkt,
    1360: ceu_reg_dump_pkt,
    1361: fpie_reg_dump_pkt,
    1376: fpmc_mem_chksum_pkt,
    1377: fpmc_mem_dump_pkt,
    1378: flash_error_pkt,
    1379: deferred_cmd_echo_pkt,
    1380: uncomp_frame_pkt,
    1381: comp_frame_pkt,
    1382: frame_support_pkt,
    1385: diag_flag_pkt,
    1392: default_pkt,
}


def is_metadata(decision_value):
    return decision_value == 0x1


apid_multi_pkt = {
    1424: dict(
        decision_field="SCI0TYPE",
        decision_fun=is_metadata,
        pkts={
            True: event_wf_transmit,
            False: event_wf_transmit_with_md
        }
    )
}

# TODO we could also add a name attribute to all the VariableLength structures, by creating in the core package a
#  NamedVariableLength object. the name would be a property of the object, we would not need to manage the
#  dictionnary after we also need a fall off case where the object will be a VariableLength object with no name,
#  we would then use the object name by introspection and add a sequence number to avoid collisions