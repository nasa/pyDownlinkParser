import ccsdspy
import pandas as pd
from ccsdspy.constants import BITS_PER_BYTE
from pydownlinkparser.europa_clipper.suda_config import SudaCatalogListStructure
from pydownlinkparser.europa_clipper.ecm_config import hs_pkt_structure, read_reg_structure, FG1_LOW_PKT, FG1_HIGH_PKT, FG2_LOW_PKT, FG3_LOW_PKT, FG2_HIGH_PKT, FG3_HIGH_PKT, adp_pkt
import argparse

parser = argparse.ArgumentParser(description="Parse ECM")
parser.add_argument("--file", help="Input File")

args = parser.parse_args()

with open(args.file, 'rb') as mixed_file:
    # dictionary mapping integer apid to BytesIO
    stream_by_apid = ccsdspy.utils.split_by_apid(mixed_file)

header_list = []

default_pkt = ccsdspy.VariableLength(
    [
        ccsdspy.PacketArray(
            name="unused", data_type="uint", bit_length=BITS_PER_BYTE, array_shape="expand"
        )
    ]
)

apid_packets = {
    1419: SudaCatalogListStructure(),
    1232: read_reg_structure,
    1216: hs_pkt_structure,
    1218: FG1_LOW_PKT,
    1219: FG1_HIGH_PKT,
    1222: FG2_LOW_PKT,
    1223: FG2_HIGH_PKT,
    1226: FG3_LOW_PKT,
    1227: FG3_HIGH_PKT,
    1217: adp_pkt
}

output = {}
frames = []
dfs = {}

for apid, stream in stream_by_apid.items():
    # print(apid)
    pkt = apid_packets.get(apid, default_pkt)
    parsed_apid = pkt.load(stream, include_primary_header = True)
    df = pd.DataFrame.from_dict(parsed_apid)
    df['APID'] = apid
    dfs[apid] = df
    frames.append(df)
    output[apid] = pd.DataFrame.from_dict(parsed_apid)

output_df = pd.concat(frames, ignore_index=True)
print(output_df)

def export_xlsx(dfs):
    with pd.ExcelWriter('output10.xlsx') as writer:
        for apid, df in dfs.items():
            df.to_excel(writer, sheet_name = f'APID_{apid}', index = True)

export_xlsx(dfs)

