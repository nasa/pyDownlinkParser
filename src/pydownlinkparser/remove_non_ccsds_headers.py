"""Remove non CCSDS binary code from input streams."""
import io
import logging

import bitstring
from tqdm import tqdm

logger = logging.getLogger(__name__)

BYTE_SIZE_IN_BITS = 8
CCSDS_HEADER_LENGTH_BYTES = 8


def remove_bdsem_and_message_headers(f):
    """Removes extra headers provided by the BDSEM data generation.

    @param f: file handler
    @return: file handler
    """
    buffer = io.BytesIO()

    bit_stream = bitstring.ConstBitStream(f)

    n_pkts = 0
    logger.info("Remove BDSEM wrappers and message headers.")
    pbar = tqdm(total=bit_stream.length)
    while bit_stream.pos < bit_stream.length:
        pbar.update(bit_stream.pos)
        control_word = bit_stream.read("uintle:32")
        sse_length = control_word

        # skipping 32 bits of unused
        _ = bit_stream.read(32)
        packet_length = sse_length - 4  # remove the unused bytes

        n_pkts += 1
        logger.debug("read packet %i", n_pkts)
        packet_data = bit_stream.read(packet_length * 8)
        packet_data_bytes = packet_data.tobytes()
        # read CCSDS header to double check the length of the packet
        ccsds_packet_length = int.from_bytes(
            packet_data_bytes[4:6], byteorder="big", signed=False
        )
        if ccsds_packet_length - 1 == packet_length - CCSDS_HEADER_LENGTH_BYTES:
            buffer.write(packet_data_bytes)
        else:
            apid = (
                int.from_bytes(packet_data_bytes[0:2], byteorder="big", signed=False)
                & 0b0000011111111111
            )
            sequence_cnt = (
                int.from_bytes(packet_data_bytes[2:3], byteorder="big", signed=False)
                & 0b0011111111111111
            )
            logger.warning(
                "Skip packet apid %i, sequence count %i: length did not match with the packet length specified in the message header",
                apid,
                sequence_cnt,
            )

    buffer.seek(0)
    return buffer


def remove_bdsem(f):
    """Remove BDSEM headers."""
    buffer = io.BytesIO()

    bit_stream = bitstring.ConstBitStream(f)
    logger.info("Remove BDSEM wrappers.")
    pbar = tqdm(total=bit_stream.length)
    while bit_stream.pos < bit_stream.length:
        pbar.update(bit_stream.pos)
        packet_header = bit_stream.read(48)
        packet_length = packet_header[-16:].uint
        packet_data = bit_stream.read(packet_length * 8)
        crc = bit_stream.read(8)
        buffer.write(packet_header.tobytes() + packet_data.tobytes() + crc.tobytes())

    buffer.seek(0)

    return buffer


def remove_mise_and_headers(f):
    """Remove packet markers from Raw mode file."""
    header_size = 4
    ccsds_header_size = 6
    offset_size = 1
    buffer = io.BytesIO()

    raw_data = f.read()
    starting_idx = []

    logger.info("Remove packet markers.")
    logger.info("Get starting indices.")
    for i in tqdm(range(0, len(raw_data[:-header_size]))):
        if start_sequence(raw_data[i : i + header_size]):
            starting_idx.append(i)

    logger.info("Rebuild the binary stream skipping the markers")
    for s in tqdm(starting_idx):
        hdr_start = s + header_size
        hdr_end = hdr_start + ccsds_header_size
        ccsds_header = raw_data[hdr_start:hdr_end]
        pkt_len = int.from_bytes(ccsds_header[-2:], byteorder="big") + offset_size
        data = raw_data[hdr_start : hdr_end + pkt_len]
        buffer.write(data)

    buffer.seek(0)

    return buffer


def start_sequence(seq):
    """Returns True if seq is on the beginning of a marker between CCSDS packets."""
    return seq[1] == 0xF0 and seq[0] == seq[2] == seq[3] != 0x00


def strip_non_ccsds_headers(
    file_handler, is_bdsem: bool, has_pkt_header: bool, has_json_header: bool
):
    """Remove all cases of non CCSDS headers which can occur in Europa-Clipper SDS inputs, mostly in test cases.

    @param filename: input binary filename
    @param is_bdsem: file coming from BDSEM, else RAW
    @param has_pkt_header:
    @param has_json_header:
    @return: the file handler where the CCSDS packets start
    """
    if has_json_header:
        logger.info("Skip json header.")
        file_handler.readline()

    if is_bdsem:
        if has_pkt_header:
            return remove_bdsem_and_message_headers(file_handler)
        else:
            return remove_bdsem(file_handler)
    else:
        if has_pkt_header:
            return remove_mise_and_headers(file_handler)
        else:
            return file_handler
