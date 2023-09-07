import ccsdspy
import io
import copy
import pandas as pd
from pydownlinkparser.europa_clipper.apid_packet_structures import apid_packets
from pydownlinkparser.util import default_pkt
from pydownlinkparser.europa_clipper.apid_packet_structures import apid_multi_pkt


def get_sub_packet_keys(parsed_apids, sub_apid: dict):
    decision_fun = sub_apid["decision_fun"]
    if "decision_field" in sub_apid:
        decision_field = sub_apid["decision_field"]
        return [
            decision_fun(decision_value)
            for decision_value in list(parsed_apids[decision_field])
        ]
    else:
        first_key = list(parsed_apids.keys())[0]
        return [decision_fun() for _ in range(0, len(parsed_apids[first_key]))]


def distritbute_packets(keyss, stream1):
    buffers = {}
    rows = ccsdspy.utils.split_packet_bytes(stream1)
    for i in range(0, len(keyss)):
        if keyss[i] not in buffers:
            buffers[keyss[i]] = bytes()
        buffers[keyss[i]] += rows[i]
    buffers = {k: io.BytesIO(v) for k, v in buffers.items()}
    return buffers


def parse_ccsds_file(ccsds_file: str):
    """ """
    stream_by_apid = ccsdspy.utils.split_by_apid(ccsds_file)
    dfs = {}
    for apid, streams in stream_by_apid.items():
        # copy the input stream because the load function alters it
        stream1 = copy.deepcopy(streams)
        pkt = apid_packets.get(apid, default_pkt)
        parsed_apids = pkt.load(streams, include_primary_header=True)
        multi_parsed_apids = {}
        if apid in apid_multi_pkt:
            keys = get_sub_packet_keys(parsed_apids, apid_multi_pkt[apid])
            buffer = distritbute_packets(keys, stream1)
            for key, minor_pkt in apid_multi_pkt[apid]["pkts"].items():
                multi_parsed_apids[key] = minor_pkt.load(
                    buffer[key], include_primary_header=True
                )
                name = get_tab_name(apid, minor_pkt, dfs.keys())
                dfs[name] = pd.DataFrame.from_dict(
                    multi_parsed_apids[key]
                )
        else:
            name = get_tab_name(apid, pkt, dfs.keys())
            dfs[name] = pd.DataFrame.from_dict(
                parsed_apids
            )

    return dfs


def get_tab_name(apid, pkt_def, existing_names):
    if hasattr(pkt_def, 'name'):
        name = f"{apid} {pkt_def.name}"
    else:
        name = f"{apid} {pkt_def.__class__.__name__}"
    # we need that in case the name is used twice so that data is not overridden
    n = 1
    while name in existing_names:
        name = f"{name} ({n})"
    return name
