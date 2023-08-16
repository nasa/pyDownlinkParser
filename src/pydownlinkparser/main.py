import os.path
import sys

import ccsdspy
import pandas as pd
import argparse
from europa_clipper.apid_packet_structures import default_pkt, apid_packets, apid_names, apid_multi_pkt, \
    multi_apid_names
import copy
import io
from europa_clipper import remove_headers

parser = argparse.ArgumentParser(description="Parse Files")
parser.add_argument("--file", help="Input File")
parser.add_argument("--mode", help="Mode")
parser.add_argument("--header", help="Header Status")
args = parser.parse_args()

filename = args.file
mode = args.mode
header_status = args.header

if mode == "BDSEM" and header_status == "Y":
    new_file = remove_headers.parse_bdsem_with_headers(filename)
elif mode == "BDSEM" and (header_status == "N" or not header_status):
    new_file = remove_headers.parse_bdsem_without_headers(filename)
elif mode == "RAW" and header_status == "Y":
    new_file = remove_headers.parse_raw_with_headers(filename)
else:
    print('Please refer README.TXT on how to enter the configuration')
    sys.exit()

with open(new_file, 'rb') as mixed_file:
    stream_by_apid = ccsdspy.utils.split_by_apid(mixed_file)

dfs = {}
multi_dfs = []
dfs_combined = pd.DataFrame()


def export_xlsx(filename1, dfs):
    with pd.ExcelWriter(filename1) as writer:
        i = 0
        for apid, df in dfs.items():
            if apid in multi_apid_names.keys():
                name = multi_apid_names[apid] + str(i)
                i = i + 1
            elif apid in apid_names.keys():
                name = apid_names[apid]
            df.to_excel(writer, sheet_name=name, index=True)


def parse_multi(keyss, stream1):
    buffers = {}
    rows = ccsdspy.utils.split_packet_bytes(stream1)
    for i in range(0, len(keyss)):
        if keyss[i] not in buffers:
            buffers[keys[i]] = bytes()
        buffers[keyss[i]] += rows[i]
    buffers = {k: io.BytesIO(v) for k, v in buffers.items()}
    return buffers


for apid, streams in stream_by_apid.items():
    stream1 = copy.deepcopy(streams)
    pkt = apid_packets.get(apid, default_pkt)
    parsed_apids = pkt.load(streams, include_primary_header=True)
    multi_parsed_df = pd.DataFrame
    multi_parsed_apids = {}
    if apid in apid_multi_pkt:
        decision_fun = apid_multi_pkt[apid]['decision_fun']
        decision_field = apid_multi_pkt[apid]['decision_field']
        keys = [decision_fun(decision_value) for decision_value in list(parsed_apids[decision_field])]
        buffer = parse_multi(keys, stream1)
        for key, minor_pkt in apid_multi_pkt[apid]['pkts'].items():
            multi_parsed_apids[key] = minor_pkt.load(buffer[key], include_primary_header=True)
        multi_parsed_df = pd.DataFrame.from_dict(multi_parsed_apids)
        multi_parsed_df['APID'] = apid
    df = pd.DataFrame.from_dict(parsed_apids)
    df['APID'] = apid
    if apid in apid_multi_pkt:
        combined_df = pd.concat([df, multi_parsed_df])
        dfs[apid] = combined_df
    else:
        dfs[apid] = df

file_base, _ = os.path.splitext(filename)
xlsx_filename = file_base + ".xlsx"
export_xlsx(xlsx_filename, dfs)
