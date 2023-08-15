import ccsdspy
import bitstring

BYTE_SIZE_IN_BITS = 8


def parse_file_ecm(filename_ecm):
    buffer = bytes()
    newfile_ecm = '/Users/nischayn/PycharmProjects/ccsdspyParse/data/ecm_new_1.bin'
    with open(filename_ecm, 'rb') as f:
        bit_stream = bitstring.ConstBitStream(f)

        while bit_stream.pos < bit_stream.length:
            control_word = bit_stream.read('uintle:32')
            sse_length = control_word
            packet_data = bit_stream.read(sse_length * 8)
            buffer += packet_data.tobytes()

    f.close()
    with open(newfile_ecm, 'wb') as f:
        f.write(buffer)
        f.close()
    return newfile_ecm


def parse_file_suda(filename_suda):
    buffer = bytes()
    newfile_suda = '/Users/nischayn/PycharmProjects/ccsdspyParse/data/suda_new_6.bin'
    with open(filename_suda, 'rb') as f:
        bit_stream = bitstring.ConstBitStream(f)
        while bit_stream.pos < bit_stream.length:
            packet_header = bit_stream.read(48)
            packet_length = packet_header[-16:].uint
            packet_data = bit_stream.read(packet_length * 8)
            crc = bit_stream.read(8)
            buffer += packet_header.tobytes() + packet_data.tobytes() + crc.tobytes()

    f.close()
    with open(newfile_suda, 'wb') as f:
        f.write(buffer)
        f.close()
    return newfile_suda


def parse_file_mise(filename_mise):
    header_size = 4
    ccsds_header_size = 6
    byte_size = 8
    offset_size = 1
    buffer = bytes()
    newfile_mise = '/Users/nischayn/PycharmProjects/ccsdspyParse/data/mise_new_1'
    with open(filename_mise, 'rb') as f:
        raw_data = f.read()
        starting_idx = []

        for i in range(0, len(raw_data[:-byte_size])):
            if start_sequence(raw_data[i:i + byte_size]):
                starting_idx.append(i)

        for s in starting_idx:
            hdr_start = s + header_size
            hdr_end = hdr_start + ccsds_header_size
            ccsds_header = raw_data[hdr_start:hdr_end]
            pkt_len = int.from_bytes(ccsds_header[-2:], byteorder='big') + offset_size
            data = raw_data[hdr_start:hdr_end + pkt_len]
            buffer += data

    f.close()
    with open(newfile_mise, 'wb') as f:
        f.write(buffer)
        f.close()
    return newfile_mise


def start_sequence(seq):
    return seq[1] == 0xF0 and seq[0] == seq[2] == seq[3] != 0x00
