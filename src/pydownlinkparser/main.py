import argparse
import copy
import io
import os.path

import ccsdspy
import pandas as pd
from europa_clipper import remove_headers
from europa_clipper.apid_packet_structures import apid_multi_pkt
from europa_clipper.apid_packet_structures import apid_packets
from europa_clipper.apid_packet_structures import default_pkt


def get_parser():
    parser = argparse.ArgumentParser(description="Parse Files")
    parser.add_argument("--file", type=str, required=True, help="Input File")
    parser.add_argument("--bdsem", action="store_true", help="Mode BDSEM")
    parser.add_argument("--header", action="store_true", help="Header Status")
    return parser


# TODO: move to a module 'remove_non_ccsds_headers.py' to strip headers together with remove_headers
def strip_non_ccsds_headers(filename: str, is_bdsem: bool, has_header: bool):
    if is_bdsem:
        if has_header:
            return remove_headers.parse_bdsem_with_headers(filename)
        else:
            return remove_headers.parse_bdsem_without_headers(filename)
    else:
        if has_header:
            return remove_headers.parse_raw_with_headers(filename)
        else:
            return filename


# TODO: change the order of the arguments
def export_dfs_to_xlsx(filename1, dfs):
    with pd.ExcelWriter(filename1) as writer:
        for name, df in dfs.items():
            df.to_excel(writer, sheet_name=name, index=True)


# TODO move to a parse_ccsds_downlink.py module
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


# TODO move to a parse_ccsds_downlink.py module
def distritbute_packets(keyss, stream1):
    buffers = {}
    rows = ccsdspy.utils.split_packet_bytes(stream1)
    for i in range(0, len(keyss)):
        if keyss[i] not in buffers:
            buffers[keyss[i]] = bytes()
        buffers[keyss[i]] += rows[i]
    buffers = {k: io.BytesIO(v) for k, v in buffers.items()}
    return buffers


# TODO move to a parse_ccsds_downlink.py module
def parse_ccsds_file(ccsds_file: str):
    """ """
    with open(ccsds_file, "rb") as mixed_file:
        stream_by_apid = ccsdspy.utils.split_by_apid(mixed_file)

    dfs = {}
    for apid, streams in stream_by_apid.items():
        # copy the input stream becasue the load function alters it
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
                dfs[f"{apid} {minor_pkt.__class__.__name__}"] = pd.DataFrame.from_dict(
                    multi_parsed_apids
                )
        else:
            dfs[f"{apid} {pkt.__class__.__name__}"] = pd.DataFrame.from_dict(
                parsed_apids
            )

    return dfs


# TODO: rename main to downlink_to_excel.py
def export_ccsds_to_excel(ccsds_file, outut_filename):
    dfs = parse_ccsds_file(ccsds_file)
    export_dfs_to_xlsx(outut_filename, dfs)


def main():
    parser = get_parser()
    args = parser.parse_args()

    ccsds_file = strip_non_ccsds_headers(args.file, args.bdsem, args.header)

    file_base, _ = os.path.splitext(args.file)
    xlsx_filename = file_base + ".xlsx"
    export_ccsds_to_excel(ccsds_file, xlsx_filename)


if __name__ == "__main__":
    main()
