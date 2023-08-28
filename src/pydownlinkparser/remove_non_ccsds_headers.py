import io

import bitstring

BYTE_SIZE_IN_BITS = 8


def remove_bdsem_and_message_headers(filename):
    buffer = bytes()
    with open(filename, "rb") as f:
        bit_stream = bitstring.ConstBitStream(f)

        while bit_stream.pos < bit_stream.length:
            control_word = bit_stream.read("uintle:32")
            sse_length = control_word

            # skipping 32 bits of unused
            _ = bit_stream.read(32)
            sse_length -= 4

            packet_data = bit_stream.read(sse_length * 8)
            buffer += packet_data.tobytes()

    return io.BytesIO(buffer)


def remove_bdsem(filename):
    buffer = bytes()
    with open(filename, "rb") as f:
        bit_stream = bitstring.ConstBitStream(f)
        while bit_stream.pos < bit_stream.length:
            packet_header = bit_stream.read(48)
            packet_length = packet_header[-16:].uint
            packet_data = bit_stream.read(packet_length * 8)
            crc = bit_stream.read(8)
            buffer += packet_header.tobytes() + packet_data.tobytes() + crc.tobytes()

    return io.BytesIO(buffer)


def remove_mise_and_headers(filename):
    header_size = 4
    ccsds_header_size = 6
    byte_size = 8
    offset_size = 1
    buffer = bytes()
    with open(filename, "rb") as f:
        raw_data = f.read()
        starting_idx = []

        for i in range(0, len(raw_data[:-byte_size])):
            if start_sequence(raw_data[i: i + byte_size]):
                starting_idx.append(i)

        for s in starting_idx:
            hdr_start = s + header_size
            hdr_end = hdr_start + ccsds_header_size
            ccsds_header = raw_data[hdr_start:hdr_end]
            pkt_len = int.from_bytes(ccsds_header[-2:], byteorder="big") + offset_size
            data = raw_data[hdr_start: hdr_end + pkt_len]
            buffer += data

    return io.BytesIO(buffer)


def start_sequence(seq):
    return seq[1] == 0xF0 and seq[0] == seq[2] == seq[3] != 0x00


def strip_non_ccsds_headers(filename: str, is_bdsem: bool, has_header: bool):
    if is_bdsem:
        if has_header:
            return remove_bdsem_and_message_headers(filename)
        else:
            return remove_bdsem(filename)
    else:
        if has_header:
            return remove_mise_and_headers(filename)
        else:
            return filename
