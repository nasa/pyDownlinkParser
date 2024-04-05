"""Definition of the Europa-Clipper CCSDS packets."""
from pydownlinkparser.util import default_pkt

from .e_themis import e_themis_1474
from .ecm import fg1_high
from .ecm import fg1_low
from .ecm import fg2_high
from .ecm import fg2_low
from .ecm import fg3_high
from .ecm import fg3_low
from .ecm import hs_ecm
from .ecm import metadata_ecm
from .ecm import read_reg_structure
from .mise import comp_frame_pkt
from .mise import dark_histogram
from .mise import diagnostic_count_pkt
from .mise import diagnostic_flag_pkt
from .mise import diagnostic_vector_pkt
from .mise import frame_support_pkt
from .suda import catalog
from .suda import catalog_list
from .suda import event_wf_transmit

# for each supported APID, define a ccsdspy.VariableLength packet definition
# OBSOLETE, keep it until validation is done.
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
    # E-THEMIS
    1474: e_themis_1474,
}
