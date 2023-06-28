import ccsdspy


class SudaCatalogListStructure:
    def __init__(self):
        super().__init__(
        )
        self.CATALOG_LIST_MIN_SUFFIX = 0
        self.CATALOG_LIST_MAX_SUFFIX = 223
        self.fields = []
        self._add_beginning_fields()
        self._add_middle_fields(self.CATALOG_LIST_MIN_SUFFIX,
                                self.CATALOG_LIST_MAX_SUFFIX)
        self._add_ending_fields()

    def _add_beginning_fields(self):
        self.fields.extend([
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
        ])

    def _middle_fields(self, num: int) -> list[ccsdspy.PacketField]:
        return [
                ccsdspy.PacketField(name=f'CATLISTAID{num}', bit_length=32, data_type='int'),
                ccsdspy.PacketField(name=f'CATLISTPROC{num}', bit_length=1, data_type='int'),
                ccsdspy.PacketField(name=f'CATLSTBLKCNT{num}', bit_length=15, data_type='int'),
                ccsdspy.PacketField(name=f'CATLISTEVTCNT{num}', bit_length=16, data_type='int'),
                ccsdspy.PacketField(name=f'CATLSTBLKSTRT{num}', bit_length=16, data_type='int'),
                ccsdspy.PacketField(name=f'CATLSTBLKEND{num}', bit_length=16, data_type='int'),
                ccsdspy.PacketField(name=f'CATLISTSTRTTM{num}', bit_length=32, data_type='int'),
        ]

    def _add_middle_fields(self, min, max):
        for i in range(min,max):
                self.fields.extend(self._middle_fields(i))

    def _add_ending_fields(self):
        self.fields.extend([
            ccsdspy.PacketField(name='SYNCCATLISTPKT', bit_length=16, data_type='int'),
            ccsdspy.PacketField(name='CRCCATLISTPKT', bit_length=16, data_type='int'),
        ])