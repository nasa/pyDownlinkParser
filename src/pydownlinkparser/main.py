import ccsdspy
import pandas as pd
import argparse
from europa_clipper.apid_packet_structures import default_pkt, apid_packets, apid_names
from europa_clipper.remove_headers import buffer_suda


def export_xlsx(dfs):
    with pd.ExcelWriter('suda_with_defaultpkt.xlsx') as writer:
        for apid, df in dfs.items():
            if apid in apid_packets.keys():
                name = apid_names[apid]
                df.to_excel(writer, sheet_name=name, index=True)


parser = argparse.ArgumentParser(description="Parse ECM")
# parser.add_argument("--file", help="Input File")
parser.add_argument("--mode", help="Mode")


args = parser.parse_args()

new_filename = '/Users/nischayn/PycharmProjects/ccsdspyParse/data/suda_new9.bin'

if args.mode == "BDSEM":
    with open(new_filename,'wb') as fp:
        fp.write(buffer_suda)

with open(new_filename, 'rb') as mixed_file:
    stream_by_apid = ccsdspy.utils.split_by_apid(mixed_file)

output = {}
dfs = {}

for apid, stream in stream_by_apid.items():
    pkt = apid_packets.get(apid, default_pkt)
    try:
        parsed_apid = pkt.load(stream, include_primary_header=True)
        df = pd.DataFrame.from_dict(parsed_apid)
        df['APID'] = apid
        dfs[apid] = df
        print(df)
        output[apid] = pd.DataFrame.from_dict(parsed_apid)
    except Exception as e:
        print(f'Skipping {apid}, {str(e)}')

export_xlsx(dfs)
