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
from .mise import ancillary_data_pkt
from .mise import comp_frame_pkt
from .mise import dark_histogram
from .mise import diagnostic_count_pkt
from .mise import diagnostic_flag_pkt
from .mise import diagnostic_vector_pkt
from .mise import frame_support_pkt
from .mise import last_frame_packet
from .mise import standard_frame_pkt
from .suda import catalog
from .suda import catalog_entries
from .suda import catalog_header
from .suda import catalog_list
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
    1392: default_pkt,
    1393: comp_frame_pkt,
    1394: frame_support_pkt,
    1395: diagnostic_vector_pkt,
    1396: diagnostic_count_pkt,
    1397: diagnostic_flag_pkt,
    1398: dark_histogram,
}


def is_metadata(decision_value):
    """Identify which packet APID 1424 is an event header (metadata)."""
    return decision_value == 0x1


N = 0


def sequence():
    """Simple counter to identify packets APID 1392."""
    global N
    N += 1
    if N <= 90:
        return "90th"
    if N == 91:
        return "91st"
    else:
        N = 0
        return "92nd"


current_aid = None


def is_new_header(aid):
    """Identify if the packet is a catalog header or entries for APID 1426."""
    global current_aid
    if current_aid is None or current_aid != aid:
        current_aid = aid
        return True
    else:
        return False


apid_multi_pkt = {
    1424: dict(
        decision_field="SCI0TYPE",
        decision_fun=is_metadata,
        pkts={True: event_wf_transmit_metadata, False: event_wf_transmit_data},
    ),
    1426: dict(
        decision_field="CATHDRAID",
        decision_fun=is_new_header,
        pkts={True: catalog_header, False: catalog_entries},
    ),
    1392: dict(
        decision_fun=sequence,
        pkts={
            "90th": standard_frame_pkt,
            "91st": last_frame_packet,
            "92nd": ancillary_data_pkt,
        },
    ),
}
