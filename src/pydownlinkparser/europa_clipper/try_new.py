import ccsdspy
from pydownlinkparser.europa_clipper.apid_packet_structures import default_pkt, apid_packets
import bitstring

filename = '/Users/nischayn/PycharmProjects/ccsdspyParse/data/suda_new9.bin'

with open(filename, 'rb') as mixed_file:
    stream_by_apid = ccsdspy.utils.split_by_apid(mixed_file)

wf_data = stream_by_apid[1424]

ccsds_packet_bytes = ccsdspy.utils.iter_packet_bytes(wf_data)

fields_before_data = [
    ccsdspy.PacketField(name='SHCOARSE', bit_length=32, data_type='uint'),
    ccsdspy.PacketField(name='SHFINE', bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name='SCI0AID', bit_length=32, data_type='uint'),
    ccsdspy.PacketField(name='SCI0TYPE', bit_length=8, data_type='uint'),
    ccsdspy.PacketField(name='SCI0CONT', bit_length=8, data_type='uint'),
    ccsdspy.PacketField(name='SCI0SPARE1', bit_length=13, data_type='uint'),
    ccsdspy.PacketField(name='SCI0PACK', bit_length=1, data_type='uint'),
    ccsdspy.PacketField(name='SCI0FRAG', bit_length=1, data_type='uint'),
    ccsdspy.PacketField(name='SCI0COMP', bit_length=1, data_type='uint'),
    ccsdspy.PacketField(name='SCI0EVTNUM', bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name='SCI0CAT', bit_length=8, data_type='uint'),
    ccsdspy.PacketField(name='SCI0QUAL', bit_length=8, data_type='uint'),
    ccsdspy.PacketField(name='SCI0FRAGOFF', bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name='SCI0VER', bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name='SCI0TIMECOARSE', bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name='SCI0TIMEFINE', bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name='SCI0SPARE2', bit_length=32, data_type='uint'),
    ccsdspy.PacketField(name='SCI0SPARE3', bit_length=32, data_type='uint'),
    ccsdspy.PacketField(name='SCI0SPARE4', bit_length=32, data_type='uint')
]

fields_after_data = [
    ccsdspy.PacketField(name='SYNCSCI0PKT', bit_length=16, data_type='uint'),
    ccsdspy.PacketField(name='CRCSCI0PKT', bit_length=16, data_type='uint'),
]

i = 0

pkt_1 = ccsdspy.VariableLength(
    [
        ccsdspy.PacketArray(
            name="data", data_type="uint", bit_length=8, array_shape="expand"
        )
    ]
)

for byte in ccsds_packet_bytes:
    print(f'{i}, {byte}')
    i = i+1

print(i)