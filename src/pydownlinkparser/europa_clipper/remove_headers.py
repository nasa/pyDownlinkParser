import ccsdspy
import bitstring

#
filename_ecm = '/Users/nischayn/PycharmProjects/ccsdspyParse/data/ecm_0406193095-0283151.DAT'
filename_suda = '/Users/nischayn/PycharmProjects/ccsdspyParse/data/suda_0409517390-0283787_cleansplit.dat'
filename_mise = '/Users/nischayn/PycharmProjects/ccsdspyParse/data/FM_TLM_20221107T1951.bin'

BYTE_SIZE_IN_BITS = 8


def parse_file_ecm(filename_ecm):
    i = 0
    with open(filename_ecm, 'rb') as f:
        bit_stream = bitstring.ConstBitStream(f)

        buffer = bytes()

        while bit_stream.pos < bit_stream.length:
            control_word = bit_stream.read('uintle:32')
            sse_length = control_word
            packet_data = bit_stream.read(sse_length * 8)
            print(f'{i}. {sse_length}')
            i = i + 1
            buffer += packet_data
            print(buffer)

        return buffer


# buffer_ecm = parse_file_ecm(filename_ecm)

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


# buffer_suda = parse_file_suda(filename_suda)
#
# newfile_suda = '/Users/nischayn/PycharmProjects/ccsdspyParse/data/suda_new_6.bin'
#
# with open(newfile_suda, 'wb') as f:
#     f.write(buffer_suda)


def parse_file_mise(filename_mise):
    i = 0
    with open(filename_mise, 'rb') as f:
        bit_stream = bitstring.ConstBitStream(f)
        buffer = bytes()
        positions = []

        while bit_stream.pos < bit_stream.length - BYTE_SIZE_IN_BITS * 4:
            b1 = bit_stream.read(BYTE_SIZE_IN_BITS)
            b2 = bit_stream.read(BYTE_SIZE_IN_BITS)
            b3 = bit_stream.read(BYTE_SIZE_IN_BITS)
            b4 = bit_stream.read(BYTE_SIZE_IN_BITS)
            if b2 == 0xF0 and b1 == b3 == b4 != 0x00:
                packet_header = bit_stream.read(BYTE_SIZE_IN_BITS * 6)
                packet_length = packet_header[-16:].uint + 1
                packet_data = bit_stream.read(packet_length * BYTE_SIZE_IN_BITS)
                buffer += packet_header.tobytes() + packet_data.tobytes()
                positions.append(bit_stream.pos)
                i += 1
                # print(buffer)
            # Move back by 3 bytes and recheck
            bit_stream.pos -= 3 * BYTE_SIZE_IN_BITS
            # else:
            #     continue
        print(i)
        return buffer

# def parse_file_mise(filename_mise):
#     header_size = 4
#     ccsds_header_size = 6
#     byte_size = 8
#     offset_size = 8
#
#     with open(filename_mise, 'rb') as f:
#         raw_data = f.read()
#         possible_starts = []
#
#         for i in range(0, len(raw_data) - byte_size):
#             if start_sequence(raw_data[i: i + byte_size]):
#                 possible_starts.append(i)
#
#         starting_idxs = [possible_starts[0]]
#         pkt_len = 0
#
#         for s in possible_starts[1:]:
#             hdr_start = starting_idxs[-1] + header_size
#             hdr_end = hdr_start + ccsds_header_size
#             pkt_len += (offset_size + header_size + ccsds_header_size)
#
#             if (s - starting_idxs[-1]) >= pkt_len:
#                 starting_idxs.append(s)
#     with open(filename_suda, 'rb') as f:
#         bit_stream = bitstring.ConstBitStream(f)
#         buffer = bytes()
#
#         for idx in starting_idxs:
#             bit_stream.pos = idx * byte_size
#             header = bit_stream.read(32)
#             ccsds_header = bit_stream.read(48)
#             packet_length = ccsds_header[-16:].uint
#             packet_data = bit_stream.read(packet_length * byte_size + offset_size)
#             buffer += ccsds_header.tobytes() + packet_data.tobytes()
#     return buffer



def start_sequence(seq):
    return seq[1] == 0xF0 and seq[0] == seq[2] == seq[3] != 0x00


newfile_mise = '/Users/nischayn/PycharmProjects/ccsdspyParse/data/mise_removed_header_file51_7.bin'
buffer_mise = parse_file_mise(filename_mise)

with open(newfile_mise, 'wb') as f:
    f.write(buffer_mise)
