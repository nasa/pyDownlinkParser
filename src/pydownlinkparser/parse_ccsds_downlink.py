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
        return [decision_fun() for _ in range(0, len(parsed_apids))]


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
    # with open(ccsds_file, "rb") as mixed_file:
    stream_by_apid = ccsdspy.utils.split_by_apid(ccsds_file)

    dfs = {}
    for apid, streams in stream_by_apid.items():
        # copy the input stream because the load function alters it
        stream1 = copy.deepcopy(streams)
        pkt = apid_packets.get(apid, default_pkt)
        multi_parsed_df = pd.DataFrame
        parsed_apids = pkt.load(streams, include_primary_header=True)
        df = pd.DataFrame.from_dict(parsed_apids)
        df['APID'] = apid
        multi_parsed_apids = {}
        if apid in apid_multi_pkt:
            keys = get_sub_packet_keys(parsed_apids, apid_multi_pkt[apid])
            buffer = distritbute_packets(keys, stream1)
            for key, minor_pkt in apid_multi_pkt[apid]["pkts"].items():
                multi_parsed_apids[key] = minor_pkt.load(
                    buffer[key], include_primary_header=True
                )
            multi_parsed_df = pd.DataFrame.from_dict(multi_parsed_apids)
            multi_parsed_df['APID'] = apid
            combined_df = pd.concat([df, multi_parsed_df])
            dfs[apid] = combined_df
        else:
            dfs[apid] = df

    return dfs
