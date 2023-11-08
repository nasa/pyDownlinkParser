"""Definition of the Europa-Clipper CCSDS packets."""
from pydownlinkparser.util import default_pkt

from .ecm_config import adp_metadata_ecm
from .ecm_config import get_fgx_freq_pkt
from .ecm_config import hs_ecm
from .ecm_config import read_reg_structure
from .mise_config import adp_metadata_mise
from .mise_config import alarm_pkt
from .mise_config import ancillary_data_pkt
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
from .mise_config import hs_mise
from .mise_config import last_frame_packet
from .mise_config import macro_chksum_pkt
from .mise_config import macro_dump_pkt
from .mise_config import mem_chksum_pkt
from .mise_config import mon_limits_pkt
from .mise_config import param_pkts
from .mise_config import standard_frame_pkt
from .mise_config import status_pkt
from .mise_config import text_pkt
from .mise_config import uncomp_frame_pkt
from .suda_config import adc_register_pkt
from .suda_config import adp_metadata_suda
from .suda_config import catalog_list
from .suda_config import catalog_list_pkt
from .suda_config import command_log_pkt
from .suda_config import dwell_pkt
from .suda_config import event_log_pkt
from .suda_config import event_message_pkt
from .suda_config import event_wf_fetch
from .suda_config import event_wf_transmit
from .suda_config import event_wf_transmit_with_md
from .suda_config import flash_table_dump_pkt
from .suda_config import hardware_centric_pkt
from .suda_config import hs_suda
from .suda_config import mem_dump_pkt
from .suda_config import postmortem_log_pkt
from .suda_config import software_centric_pkt

# for each supported APID, define a ccsdspy.VariableLength packet definition
apid_packets = {
    1419: catalog_list,
    1232: read_reg_structure,
    1216: hs_ecm,
    1218: get_fgx_freq_pkt(1, "low"),
    1219: get_fgx_freq_pkt(1, "high"),
    1222: get_fgx_freq_pkt(2, "low"),
    1223: get_fgx_freq_pkt(2, "high"),
    1226: get_fgx_freq_pkt(3, "low"),
    1227: get_fgx_freq_pkt(3, "high"),
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
    """Identify which packet APID 1424 is an event header (metadata)."""
    return decision_value == 0x1


N = 0


def sequence():
    """Simple counter to identify packets APID 1392."""
    global N
    N += 1
    if N < 90:
        return "90th"
    if N == 90:
        return "91st"
    else:
        N = 0
        return "92nd"


apid_multi_pkt = {
    1424: dict(
        decision_field="SCI0TYPE",
        decision_fun=is_metadata,
        pkts={True: event_wf_transmit, False: event_wf_transmit_with_md},
    ),
    1392: dict(
        decision_fun=sequence,
        pkts={
            "90th": standard_frame_pkt,
            "91st": ancillary_data_pkt,
            "92nd": last_frame_packet,
        },
    ),
}
