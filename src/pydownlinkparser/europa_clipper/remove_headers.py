import bitstring

BYTE_SIZE_IN_BITS = 8


def parse_bdsem_with_headers(filename_ecm):
    buffer = bytes()
    # TODO: don't harcode file papth
    newfile_bdsem = "/Users/nischayn/PycharmProjects/ccsdspyParse/data/ecm_new_1.bin"
    with open(filename_ecm, "rb") as f:
        bit_stream = bitstring.ConstBitStream(f)

        while bit_stream.pos < bit_stream.length:
            control_word = bit_stream.read("uintle:32")
            sse_length = control_word

            # skipping 32 bits of unused
            _ = bit_stream.read(32)
            sse_length -= 4

            packet_data = bit_stream.read(sse_length * 8)
            buffer += packet_data.tobytes()

    f.close()
    # TODO keep the buffer as result, don't write on file system
    with open(newfile_bdsem, "wb") as f:
        f.write(buffer)
        f.close()
    return newfile_bdsem


def parse_bdsem_without_headers(filename_suda):
    buffer = bytes()
    newfile_bdsem_n = "/Users/nischayn/PycharmProjects/ccsdspyParse/data/suda_new_6.bin"
    with open(filename_suda, "rb") as f:
        bit_stream = bitstring.ConstBitStream(f)
        while bit_stream.pos < bit_stream.length:
            packet_header = bit_stream.read(48)
            packet_length = packet_header[-16:].uint
            packet_data = bit_stream.read(packet_length * 8)
            crc = bit_stream.read(8)
            buffer += packet_header.tobytes() + packet_data.tobytes() + crc.tobytes()

    f.close()
    with open(newfile_bdsem_n, "wb") as f:
        f.write(buffer)
        f.close()
    return newfile_bdsem_n


def parse_raw_with_headers(filename_mise):
    header_size = 4
    ccsds_header_size = 6
    byte_size = 8
    offset_size = 1
    buffer = bytes()
    newfile_raw = "/Users/nischayn/PycharmProjects/ccsdspyParse/data/mise_new_1"
    with open(filename_mise, "rb") as f:
        raw_data = f.read()
        starting_idx = []

        for i in range(0, len(raw_data[:-byte_size])):
            if start_sequence(raw_data[i : i + byte_size]):
                starting_idx.append(i)

        for s in starting_idx:
            hdr_start = s + header_size
            hdr_end = hdr_start + ccsds_header_size
            ccsds_header = raw_data[hdr_start:hdr_end]
            pkt_len = int.from_bytes(ccsds_header[-2:], byteorder="big") + offset_size
            data = raw_data[hdr_start : hdr_end + pkt_len]
            buffer += data

    f.close()
    with open(newfile_raw, "wb") as f:
        f.write(buffer)
        f.close()
    return newfile_raw


def start_sequence(seq):
    return seq[1] == 0xF0 and seq[0] == seq[2] == seq[3] != 0x00
