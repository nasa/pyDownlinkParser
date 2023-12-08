"""Definition of the Europa-Clipper CCSDS packets."""
from pydownlinkparser.util import default_pkt

from .ecm import fg1_high
from .ecm import fg1_low
from .ecm import fg2_high
from .ecm import fg2_low
from .ecm import fg3_high
from .ecm import fg3_low
from .ecm import hs_ecm
from .ecm import metadata_ecm
from .ecm import read_reg_structure
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
from .suda import catalog
from .suda import catalog_list
from .suda import event_wf_fetch
from .suda import event_wf_transmit
from .suda import event_wf_transmit_data
from .suda import event_wf_transmit_metadata

# for each supported APID, define a ccsdspy.VariableLength packet definition
apid_packets = {
    # ECM
    1232: read_reg_structure,
    1216: hs_ecm,
    1218: fg1_low,
    1219: fg1_high,
    1222: fg2_low,
    1223: fg2_high,
    1226: fg3_low,
    1227: fg3_high,
    1217: metadata_ecm,
    # SUDA
    1419: catalog_list,
    1424: event_wf_transmit,
    1426: catalog,
    # MISE
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
        pkts={True: event_wf_transmit_metadata, False: event_wf_transmit_data},
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
