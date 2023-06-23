import io

import ccsdspy
import numpy as np
from collections import defaultdict
from ccsdspy.constants import BITS_PER_BYTE, PRIMARY_HEADER_NUM_BYTES

packet_bytes = ccsdspy.utils.split_packet_bytes('ecm_0406193095-0283151.DAT')

for i in range(5):
    print(packet_bytes[i].hex())

num_packets, missing_bytes = ccsdspy.utils.count_packets(
    'ecm_0406193095-0283151.DAT',
    return_missing_bytes=True
)

print(f"There are {num_packets} complete packets in this file")

if missing_bytes > 0:
    print(f"The last packet is incomplete. {missing_bytes} bytes "
          "would need to be added to complete the last packet")

with open('ecm_0406193095-0283151.DAT', 'rb') as mixed_file:
    # dictionary mapping integer apid to BytesIO
    stream_by_apid = ccsdspy.utils.split_by_apid(mixed_file)

header_list = []

hs_packet = ccsdspy.VariableLength(
    [
        ccsdspy.PacketField(name="MSCLK Seconds", bit_length=32, data_type='uint'),
        ccsdspy.PacketField(name="MSCLK Subseconds", bit_length=16, data_type='uint'),
        # operational status
        ccsdspy.PacketField(name="Subseconds Pre-zero", bit_length=16, data_type='uint'),
        ccsdspy.PacketField(name="IF Type", bit_length=1, data_type='uint'),
        ccsdspy.PacketField(name="Selected Interface", bit_length=1, data_type='uint'),
        ccsdspy.PacketField(name="Busy", bit_length=1, data_type='uint'),
        ccsdspy.PacketField(name="Panic", bit_length=1, data_type='uint'),
        ccsdspy.PacketField(name="Instrument Mode", bit_length=3, data_type='uint'),
        ccsdspy.PacketField(name="Operational Status Spare", bit_length=1, data_type='uint'),
        # command status
        ccsdspy.PacketField(name="Command Accepted Cnt", bit_length=8, data_type='uint'),
        ccsdspy.PacketField(name="Command Executed Cnt", bit_length=8, data_type='uint'),
        ccsdspy.PacketField(name="Command Rejected Count", bit_length=8, data_type='uint'),
        ccsdspy.PacketField(name="Most Recent Command's Sequence Count", bit_length=5, data_type='uint'),
        ccsdspy.PacketField(name="Most Recent Command's Status", bit_length=3, data_type='uint'),
        ccsdspy.PacketField(name="Most Recent Command's Opcode", bit_length=16, data_type='uint'),
        ccsdspy.PacketField(name="2nd Most Recent Command's  Sequence Count", bit_length=5, data_type='uint'),
        ccsdspy.PacketField(name="2nd Most Recent Command's Status", bit_length=3, data_type='uint'),
        ccsdspy.PacketField(name="2nd Most Recent Command's Opcode", bit_length=16, data_type='uint'),
        ccsdspy.PacketField(name="3rd Most Recent Command's  Sequence Count", bit_length=5, data_type='uint'),
        ccsdspy.PacketField(name="3rd Most Recent Command's Status", bit_length=3, data_type='uint'),
        ccsdspy.PacketField(name="3rd Most Recent Command's Opcode", bit_length=16, data_type='uint'),
        ccsdspy.PacketField(name="4th Most Recent Command's  Sequence Count", bit_length=5, data_type='uint'),
        ccsdspy.PacketField(name="4th Most Recent Command's Status", bit_length=3, data_type='uint'),
        ccsdspy.PacketField(name="4th Most Recent Command's Opcode", bit_length=16, data_type='uint'),
        ccsdspy.PacketField(name="5th Most Recent Command's  Sequence Count", bit_length=5, data_type='uint'),
        ccsdspy.PacketField(name="5th Most Recent Command's Status", bit_length=3, data_type='uint'),
        ccsdspy.PacketField(name="5th Most Recent Command's Opcode", bit_length=16, data_type='uint'),
        # uart status
        ccsdspy.PacketField(name="Error Count", bit_length=8, data_type='uint'),
        ccsdspy.PacketField(name="UART Spare", bit_length=14, data_type='uint'),
        # error bits (guides SC fault response)
        ccsdspy.PacketField(name="Req_SC_Power_Off (Requests instrument shutdown)", bit_length=1, data_type='uint'),
        ccsdspy.PacketField(name="Req_SC_Power_Cycle (OK to attempt instrument restart)", bit_length=1,
                            data_type='uint'),
        # source data, derived parameters
        ccsdspy.PacketField(name="Source Data Derived Parameters SPARE", bit_length=24, data_type='uint'),
        ccsdspy.PacketField(name="CLOCKS_LAST_1PPS", bit_length=24, data_type='uint'),
        ccsdspy.PacketField(name="FG1_HTR_AVG", bit_length=24, data_type='uint'),
        ccsdspy.PacketField(name="FG2_HTR_AVG", bit_length=24, data_type='uint'),
        ccsdspy.PacketField(name="FG3_HTR_AVG", bit_length=24, data_type='uint'),
        ccsdspy.PacketField(name="FG1_DRIVE_PHASE", bit_length=8, data_type='uint'),
        ccsdspy.PacketField(name="FG2_DRIVE_PHASE", bit_length=8, data_type='uint'),
        ccsdspy.PacketField(name="FG3_DRIVE_PHASE", bit_length=8, data_type='uint'),
        ccsdspy.PacketField(name="SPARE", bit_length=2, data_type='uint'),
        ccsdspy.PacketField(name="I_TP_IN1", bit_length=1, data_type='uint'),
        ccsdspy.PacketField(name="I_TP_IN2", bit_length=1, data_type='uint'),
        ccsdspy.PacketField(name="I_FPGA_ID0", bit_length=1, data_type='uint'),
        ccsdspy.PacketField(name="I_FPGA_ID1", bit_length=1, data_type='uint'),
        ccsdspy.PacketField(name="I_FPGA_ID2", bit_length=1, data_type='uint'),
        ccsdspy.PacketField(name="I_FPGA_ID3", bit_length=1, data_type='uint'),
        ccsdspy.PacketField(name="FG_GENERAL_REGISTERS", bit_length=16, data_type='uint'),
        ccsdspy.PacketField(name="VERSION", bit_length=24, data_type='uint'),
        # source data zero pad
        ccsdspy.PacketArray(name="Source Data and Padding (Bits)", bit_length=BITS_PER_BYTE, array_shape="expand"),
        # PEC
        ccsdspy.PacketField(name="PEC (CRC-16-CCITT)", bit_length=16, data_type='uint'),
    ])

default_pkt = ccsdspy.VariableLength(
    [
        ccsdspy.PacketArray(
            name="unused", data_type="uint", bit_length=BITS_PER_BYTE, array_shape="expand"
        )
    ]
)

d = {
    0: hs_packet
}

output = {}
result = []
pkt_length = 1024

for apid, stream in stream_by_apid.items():
    pkt = d.get(apid, default_pkt)

    offset = 0
    data = stream.getvalue()
    packet_data = []

    while offset < len(data):
        packet_data.append(data[offset:offset+pkt_length])
        offset += pkt_length

    results = []
    for pd in packet_data:
        result = pkt.load(data)
        results.append(result)

    output[apid] = result

print(output)

# except Exception as e:
#     print(f"Error for apid {apid}")
#     print(f"stream {stream}")
#     print(f"Packet {pkt}")
# output[apid] = pkt.load(stream)


# header_arrays = ccsdspy.utils.read_primary_headers('apid00567.tlm')
#
# for i in range(3):
#     print(f"Packet {i + 1} has APID {header_arrays['CCSDS_APID'][i]}")
