import ccsdspy
from ccsdspy.constants import BITS_PER_BYTE

suda_packet = ccsdspy.VariableLength(
    [
            ccsdspy.PacketField(name='SHCOARSE', bit_length=32, data_type='int'),
            ccsdspy.PacketField(name='SHFINE', bit_length=16, data_type='int'),
            ccsdspy.PacketField(name='LISTRGN', bit_length=32, data_type='int'),
            ccsdspy.PacketField(name='LISTOFFSET', bit_length=32, data_type='int'),
            ccsdspy.PacketField(name='LISTTOTLEN', bit_length=32, data_type='int'),
            ccsdspy.PacketField(name='LISTVLDCNT', bit_length=32, data_type='int'),
            ccsdspy.PacketField(name='LISTFLSLOC', bit_length=32, data_type='int'),
            ccsdspy.PacketField(name='LISTHDRSP1', bit_length=32, data_type='int'),
            ccsdspy.PacketField(name='LISTHDRSP2', bit_length=32, data_type='int'),
            ccsdspy.PacketField(name='LISTRESERV', bit_length=32, data_type='int'),
            # ccsdspy.PacketField(name=f'CATLISTAID{num}', bit_length=32, data_type='int'),
            # ccsdspy.PacketField(name=f'CATLISTPROC{num}', bit_length=1, data_type='int'),
            # ccsdspy.PacketField(name=f'CATLSTBLKCNT{num}',bit_length=15, data_type='int'),
            # ccsdspy.PacketField(name=f'CATLISTEVTCNT{num}', bit_length=16, data_type='int'),
            # ccsdspy.PacketField(name=f'CATLSTBLKSTRT{num}', bit_length=16, data_type='int'),
            # ccsdspy.PacketField(name=f'CATLSTBLKEND{num}', bit_length=16, data_type='int'),
            # ccsdspy.PacketField(name=f'CATLISTSTRTTM{num}', bit_length=32, data_type='int'),
            ccsdspy.PacketField(name='SYNCCATLISTPKT', bit_length=16, data_type='int'),
            ccsdspy.PacketField(name='CRCCATLISTPKT', bit_length=16, data_type='int'),

    ]
)