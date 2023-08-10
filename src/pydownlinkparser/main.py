import ccsdspy
import pandas as pd
import argparse
from europa_clipper.apid_packet_structures import default_pkt, apid_packets, apid_names, apid_multi_pkt
# from europa_clipper.remove_headers import buffer_suda
import copy
import io
import pickle


def export_xlsx(filename1, dfs):
    with pd.ExcelWriter(filename1) as writer:
        for apid, df in dfs.items():
            if apid in apid_packets.keys():
                name = apid_names[apid]
                df.to_excel(writer, sheet_name=name, index=True)

def export_xlsx2(filename1, dfs):
    with pd.ExcelWriter(filename1) as writer:
        for apid, df in dfs.items():
            if apid in apid_packets.keys():
                name = apid_names[apid]
                df.to_excel(writer, sheet_name=name, index=True)


# parser = argparse.ArgumentParser(description="Parse ECM")
# parser.add_argument("--file", help="Input File")
# parser.add_argument("--mode", help="Mode")
# parser.add_argument("--header", help="Header Status")
# args = parser.parse_args()

new_filename = '/Users/nischayn/PycharmProjects/ccsdspyParse/data/suda_new_6.bin'

# if args.mode == "BDSEM":
#     with open(new_filename, 'wb') as fp:
#         fp.write(buffer_suda)

with open(new_filename, 'rb') as mixed_file:
    stream_by_apid = ccsdspy.utils.split_by_apid(mixed_file)

output = {}
dfs = {}
dfs2 = {}
dfs2_true = {}
dfs2_false = {}
dfs_combined = pd.DataFrame()


def parse_multi(keyss, stream1):
    buffers = {}
    rows = ccsdspy.utils.split_packet_bytes(stream1)
    for i in range(0, len(keyss)):
        if keyss[i] not in buffers:
            buffers[keys[i]] = bytes()
        buffers[keyss[i]] += rows[i]
    buffers[True] = io.BytesIO(buffers[True])
    buffers[False] = io.BytesIO(buffers[False])
    return buffers


# for apid, stream in stream_by_apid.items():
#     pkt = apid_packets.get(apid, default_pkt)
#     try:
#         parsed_apids = pkt.load(stream, include_primary_header=True)
#         multi_parsed_apids = {}
#         if apid in apid_multi_pkt:
#             buffer = {}
#             for key, pkt in apid_multi_pkt[apid]['pkts'].items():
#                 buffer[key] = []
#             decision_fun = apid_multi_pkt[apid]['decision_fun']
#             decision_field = apid_multi_pkt[apid]['decision_field']
#             keys = [decision_fun(decision_value) for decision_value in list(parsed_apids[decision_field])]
#             buffer = parse_multi(buffer, keys, stream)
#             for key, minor_pkt in apid_multi_pkt[apid]['pkts'].items():
#                 multi_parsed_apids = minor_pkt.load(buffer[key])
#             df2 = pd.DataFrame.from_dict(multi_parsed_apids)
#             df2['APID'] = apid
#             dfs2[apid] = df2
#         df = pd.DataFrame.from_dict(parsed_apids)
#         df['APID'] = apid
#         dfs[apid] = df
#
#         output[apid] = pd.DataFrame.from_dict(parsed_apids)
#     except Exception as e:
#         print(f'Skipping {apid}, {str(e)}')


# for apid, stream in stream_by_apid.items():
#     pkt = apid_packets.get(apid, default_pkt)
#     parsed_apid = pkt.load(stream, include_primary_header=True)
#     df = pd.DataFrame.from_dict(parsed_apid)
#     df['APID'] = apid
#     dfs[apid] = df
#     print(apid)
#     output[apid] = pd.DataFrame.from_dict(parsed_apid)

for apid, streams in stream_by_apid.items():
    stream1 = copy.deepcopy(streams)
    pkt = apid_packets.get(apid, default_pkt)
    parsed_apids = pkt.load(streams, include_primary_header=True)
    multi_parsed_apids = {}
    if apid in apid_multi_pkt:
        decision_fun = apid_multi_pkt[apid]['decision_fun']
        decision_field = apid_multi_pkt[apid]['decision_field']
        keys = [decision_fun(decision_value) for decision_value in list(parsed_apids[decision_field])]
        buffer = parse_multi(keys, stream1)
        for key, minor_pkt in apid_multi_pkt[apid]['pkts'].items():
            multi_parsed_apids[key] = minor_pkt.load(buffer[key], include_primary_header=True)
        df2_true = pd.DataFrame.from_dict(multi_parsed_apids[True])
        df2_false = pd.DataFrame.from_dict(multi_parsed_apids[False])
        df2_true['APID'] = apid
        dfs2_true[apid] = df2_true
        df2_true['APID'] = apid
        dfs2_false[apid] = df2_false
    df = pd.DataFrame.from_dict(parsed_apids)
    df['APID'] = apid
    dfs[apid] = df

    output[apid] = pd.DataFrame.from_dict(parsed_apids)

export_xlsx('suda_new_13.xlsx', dfs)
export_xlsx2('suda_new_14.xlsx', dfs2_true)
export_xlsx2('suda_new_15.xlsx',dfs2_false)
