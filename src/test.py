import ccsdspy
# from pydownlinkparser.europa_clipper.mise_config import mise_hs, mise_adp, COMMAND_ECHO_PKT, ALARM_PKT, MEM_CHKSUM_PKT, \
#     MEM_DUMP_PKT, STATUS_PKT, BOOT_STATUS_PKT, MACRO_CHKSUM_PKT, MACRO_DUMP_PKT, MON_LIMITS_PKT, PARAM_PKTS, TEXT_PKT, \
#     FPIE_REG_DUMP_PKT, CEU_REG_DUMP_PKT, FPIE_REG_SETTINGS_PKT, FPMC_MEM_DUMP_PKT, FPMC_MEM_CHKSUM_PKT, FLASH_ERROR_PKT, \
#     DEFERRED_CMD_ECHO_PKT, UNCOMP_FRAME_PKT, COMP_FRAME_PKT, FRAME_SUPPORT_PKT, DIAG_FLAG_PKT
# from ccsdspy.constants import BITS_PER_BYTE
import bitstring
#
from src.pydownlinkparser.europa_clipper.apid_packet_structures import apid_packets, default_pkt

# # import pandas as pd
# # from ccsdspy.converters import StringifyBytesConverter
# # from ccsdspy.constants import BITS_PER_BYTE
# #
# # filename = "/Users/nischayn/PycharmProjects/ccsdspyParse/data/ecm_raw2.bin"
# #
# # with open(filename, 'rb') as mixed_file:
# #     # dictionary mapping integer apid to BytesIO
# #     stream_by_apid = ccsdspy.utils.split_by_apid(mixed_file)
# #
# default_pkt = ccsdspy.VariableLength(
#     [
#         ccsdspy.PacketArray(
#             name="unused", data_type="uint", bit_length=BITS_PER_BYTE, array_shape="expand"
#         )
#     ]
# )
# #
# # class FGXPacketStructure(ccsdspy.VariableLength):
# #
# #     def __init__(self, time_sample_per_packet: int):
# #         super().__init__([
# #             ccsdspy.PacketField(name="Instrument SCLK Time second", bit_length=32, data_type='uint'),
# #             ccsdspy.PacketField(name="Instrument SCLK Time subsec", bit_length=16, data_type='uint'),
# #             ccsdspy.PacketField(name="Accountability ID", bit_length=32, data_type='uint'),
# #         ])
# #
# #         self._add_channel_samples(time_sample_per_packet)
# #         self._add_support_fields()
# #
# #     def _add_channel_samples(self, time_sample_per_packet: int):
# #         for i in range(time_sample_per_packet):
# #             for c in range(3, 0, -1):
# #                 self._fields.append(
# #                     ccsdspy.PacketField(f"FGx_CH{c}_{i}", bit_length=24, data_type='int')
# #                 )
# #
# #     def _add_support_fields(self):
# #         self._fields.extend([
# #             ccsdspy.PacketField(name="FGx_-4.7VHK", bit_length=24, data_type='int'),
# #             ccsdspy.PacketField(name="FGx_+4.7VHK", bit_length=24, data_type='int'),
# #             ccsdspy.PacketField(name="FGx_2VREF", bit_length=24, data_type='int'),
# #             ccsdspy.PacketField(name="FGx_1VREF", bit_length=24, data_type='int'),
# #             ccsdspy.PacketField(name="FGx_DRV_SNS", bit_length=24, data_type='int'),
# #             ccsdspy.PacketField(name="FGx_OP_PRTA", bit_length=24, data_type='int'),
# #             ccsdspy.PacketField(name="FGx_FBX", bit_length=24, data_type='int'),
# #             ccsdspy.PacketField(name="FGx_FBY", bit_length=24, data_type='int'),
# #             ccsdspy.PacketField(name="FGx_FBZ", bit_length=24, data_type='int'),
# #             ccsdspy.PacketField(name="FGx_BPFX", bit_length=24, data_type='int'),
# #             ccsdspy.PacketField(name="FGx_BPFY", bit_length=24, data_type='int'),
# #             ccsdspy.PacketField(name="FGx_BPFZ", bit_length=24, data_type='int'),
# #             ccsdspy.PacketField(name="FGx_+4.7_I", bit_length=24, data_type='int'),
# #             ccsdspy.PacketField(name="FGx_-4.7_I", bit_length=24, data_type='int'),
# #             ccsdspy.PacketField(name="FGx_HK_CH14", bit_length=24, data_type='int'),
# #             ccsdspy.PacketField(name="FGx_HK_CH15", bit_length=24, data_type='int'),
# #             ccsdspy.PacketField(name="Register 80", bit_length=16, data_type='uint'),
# #             ccsdspy.PacketField(name="PEC (CRC-16-CCITT)", bit_length=16, data_type='uint'),
# #         ])
# #
# #
# # TIME_SAMPLE_PER_HF_PACKET = 160
# # TIME_SAMPLE_PER_LF_PACKET = 60
# #
# # FG1_LOW_PKT = FGXPacketStructure(TIME_SAMPLE_PER_LF_PACKET)
# # FG1_HIGH_PKT = FGXPacketStructure(TIME_SAMPLE_PER_HF_PACKET)
# # FG2_LOW_PKT = FGXPacketStructure(TIME_SAMPLE_PER_LF_PACKET)
# # FG2_HIGH_PKT = FGXPacketStructure(TIME_SAMPLE_PER_HF_PACKET)
# # FG3_LOW_PKT = FGXPacketStructure(TIME_SAMPLE_PER_LF_PACKET)
# # FG3_HIGH_PKT = FGXPacketStructure(TIME_SAMPLE_PER_HF_PACKET)
# #
# #
# #
# #
# # apid_packets = {
# #     1218: FG1_LOW_PKT,
# #     1219: FG1_HIGH_PKT,
# #     1222: FG2_LOW_PKT,
# #     1223: FG2_HIGH_PKT,
# #     1226: FG3_LOW_PKT,
# #     1227: FG3_HIGH_PKT
# # }
# #
# # output = {}
# # frames = []
# # dfs = {}
# #
# # for apid, stream in stream_by_apid.items():
# #     pkt = apid_packets.get(apid, default_pkt)
# #     parsed_apid = pkt.load(stream, include_primary_header=True)
# #     df = pd.DataFrame.from_dict(parsed_apid)
# #     df['APID'] = apid
# #     dfs[apid] = df
# #     frames.append(df)
# #     output[apid] = pd.DataFrame.from_dict(parsed_apid)
# #
# # output_df = pd.concat(frames, ignore_index=True)
# # print(output_df)
# #
# #
# # def export_xlsx(dfs):
# #     with pd.ExcelWriter('output_3.xlsx') as writer:
# #         for apid, df in dfs.items():
# #             df.to_excel(writer, sheet_name=f'APID_{apid}', index=True)
# #
# #
# # export_xlsx(dfs)
#
#
# apid_packets = {
#     # 1419: SudaCatalogListStructure(),
#     # 1232: read_reg_structure,
#     # 1216: hs_pkt_structure,
#     # 1218: FG1_LOW_PKT,
#     # 1219: FG1_HIGH_PKT,
#     # 1222: FG2_LOW_PKT,
#     # 1223: FG2_HIGH_PKT,
#     # 1226: FG3_LOW_PKT,
#     # 1227: FG3_HIGH_PKT,
#     # 1217: adp_pkt,
#     # 1408: hs_suda,
#     # 1409: adp_suda,
#     # 1410: EVENT_LOG_PKT,
#     # 1411: POSTMORTEM_LOG_PKT,
#     # 1412: COMMAND_LOG_PKT,
#     # 1413: HARDWARE_CENTRIC_PKT,
#     # 1414: SOFTWARE_CENTRIC_PKT,
#     # 1415: MEM_DUMP_PKT,
#     # 1416: FLASH_TABLE_DUMP_PKT,
#     # 1417: DWELL_PKT,
#     # 1418: EVENT_MESSAGE_PKT,
#     # 1420: ADC_REGISTER_PKT,
#     # 1424: SudaWaveformPacketStructure,
#     # 1432: CATALOG_LIST_PKT,
#     1344: mise_hs,
#     1345: mise_adp,
#     1346: COMMAND_ECHO_PKT,
#     1347: ALARM_PKT,
#     1348: MEM_CHKSUM_PKT,
#     1349: STATUS_PKT,
#     1350: BOOT_STATUS_PKT,
#     1351: MACRO_DUMP_PKT,
#     1352: MACRO_CHKSUM_PKT,
#     1354: MON_LIMITS_PKT,
#     1355: PARAM_PKTS,
#     1356: TEXT_PKT,
#     1357: FPIE_REG_SETTINGS_PKT,
#     1360: CEU_REG_DUMP_PKT,
#     1361: FPIE_REG_DUMP_PKT,
#     1376: FPMC_MEM_CHKSUM_PKT,
#     1377: FPMC_MEM_DUMP_PKT,
#     1378: FLASH_ERROR_PKT,
#     1379: DEFERRED_CMD_ECHO_PKT,
#     1380: UNCOMP_FRAME_PKT,
#     1381: COMP_FRAME_PKT,
#     1382: FRAME_SUPPORT_PKT,
#     1385: DIAG_FLAG_PKT
# }
#
# filename = "/Users/nischayn/PycharmProjects/ccsdspyParse/data/suda_0409517390-0283787_cleansplit.dat"
#
# with open(filename, 'rb') as mixed_file:
#     # dictionary mapping integer apid to BytesIO
#     stream_by_apid = ccsdspy.utils.split_by_apid(mixed_file)
#
# for apid, stream in stream_by_apid.items():
#     # print(apid)
#     pkt = apid_packets.get(apid, default_pkt)
#     try:
#         parsed_apid = pkt.load(stream, include_primary_header=True)
#         print(f'Parsed  {apid}')
#     except:
#         print(f'Skipping {apid}')
#


# filename = "/Users/nischayn/PycharmProjects/ccsdspyParse/data/ecm_removed_header1.bin"
#
# with open(filename, 'rb') as mixed_file:
#     # dictionary mapping integer apid to BytesIO
#     stream_by_apid = ccsdspy.utils.split_by_apid(mixed_file)
#
# for apid, streams in stream_by_apid.items():
#     pkt = apid_packets.get(apid, default_pkt)
#     parsed_apids = pkt.load(streams)
#     print(parsed_apids)
#
# rows1 = []
# for apid, stream in stream_by_apid.items():
#     print(apid)


newfile_ecm = '/Users/nischayn/PycharmProjects/ccsdspyParse/data/ecm_new_1.bin'
filename_ecm = '/Users/nischayn/PycharmProjects/ccsdspyParse/data/ecm_mag_testcase6_cmds_split_out.log'


def parse_file_ecm(filename_ecm):
    with open(filename_ecm, 'rb') as f:
        bit_stream = bitstring.ConstBitStream(f)

        buffer = bytes()

        while bit_stream.pos < bit_stream.length:
            control_word = bit_stream.read('uintle:32')
            sse_length = control_word

            # skipping 32 bits of unused
            _ = bit_stream.read(32)
            sse_length -= 4

            packet_data = bit_stream.read(sse_length * 8)
            buffer += packet_data.tobytes()

        return buffer


ecm_buffer = parse_file_ecm(filename_ecm)
with open(newfile_ecm, 'wb') as f:
    f.write(ecm_buffer)
    f.close()

with open(newfile_ecm, 'rb') as mixed_file:
    stream_by_apid = ccsdspy.utils.split_by_apid(mixed_file)

for apid, stream in stream_by_apid.items():
    print(apid)

for apid, streams in stream_by_apid.items():
    pkt = apid_packets.get(apid, default_pkt)
    parsed_apids = pkt.load(streams)

rows1 = []
