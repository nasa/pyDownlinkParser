import ccsdspy
import bitstring

filename_ecm = '/Users/nischayn/PycharmProjects/ccsdspyParse/data/ecm_0406193095-0283151.DAT'
filename_suda = '/Users/nischayn/PycharmProjects/ccsdspyParse/data/suda_0409517390-0283787_cleansplit.dat'
filename_mise = '/Users/nischayn/PycharmProjects/ccsdspyParse/data/mise_1951_32offsets.bin'


# def parse_file_ecm(filename_ecm):
#     i = 0
#     with open(filename_ecm, 'rb') as f:
#         bit_stream = bitstring.ConstBitStream(f)
#
#         buffer = bytes()
#
#         while bit_stream.pos < bit_stream.length:
#             control_word = bit_stream.read('uintle:32')
#             sse_length = control_word
#             packet_data = bit_stream.read(sse_length * 8)
#             print(f'{i}. {sse_length}')
#             i = i + 1
#             buffer += packet_data
#
#         return buffer


# buffer_ecm = parse_file_ecm(filename_ecm)
#
# newfile_ecm = '/Users/nischayn/PycharmProjects/ccsdspyParse/data/ecm_removed_header2.bin'
#
# with open(newfile_ecm, 'wb') as f:
#     f.write(buffer_ecm)


def parse_file_suda(filename_suda):
    i = 0
    with open(filename_suda, 'rb') as f:
        bit_stream = bitstring.ConstBitStream(f)
        buffer = bytes()
        while bit_stream.pos < bit_stream.length:
            packet_header = bit_stream.read(48)
            packet_length = packet_header[-16:].uint
            packet_data = bit_stream.read(packet_length * 8)
            crc = bit_stream.read(8)
            # print(f'{i}, {packet_length}')
            i = i + 1
            buffer += packet_header.tobytes() + packet_data.tobytes() + crc.tobytes()

        return buffer


buffer_suda = parse_file_suda(filename_suda)

# newfile_suda = '/Users/nischayn/PycharmProjects/ccsdspyParse/data/suda_removed_header1.bin'
#
# with open(newfile_suda, 'wb') as f:
#     f.write(buffer_suda)

# def parse_file_mise(filename_mise):
#     i = 0
#     with open(filename_mise, 'rb') as f:
#         bit_stream = bitstring.ConstBitStream(f)
#         buffer = bytearray()
#
#         while bit_stream.pos < bit_stream.length:
#             offset = bit_stream.read(1)
#             message_header = bit_stream.read(32)
#             ccsds_header = bit_stream.read(48)
#             packet_length = ccsds_header[-16:].uint
#             packet_data = bit_stream.read(packet_length * 8)
#             buffer += ccsds_header + packet_data
#
#         return buffer
#
#
# newfile_mise = '/Users/nischayn/PycharmProjects/ccsdspyParse/data/mise_removed_header1.bin'
# buffer_mise = parse_file_mise(filename_mise)
#
# with open(newfile_mise, 'wb') as f:
#     f.write(buffer_mise)
