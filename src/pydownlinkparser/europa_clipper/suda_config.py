"""Packet definitions for SUDA instrument."""
import ccsdspy
from ccsdspy.converters import StringifyBytesConverter

Major_APID = 0x16


class SudaCatalogListStructure(ccsdspy.VariableLength):
    """Catalog List packet structure definition."""

    name = "catalog_list"

    def __init__(self):
        """Constructor."""
        super().__init__(
            [
                ccsdspy.PacketField(name="SHCOARSE", bit_length=32, data_type="int"),
                ccsdspy.PacketField(name="SHFINE", bit_length=16, data_type="int"),
                ccsdspy.PacketField(name="LISTRGN", bit_length=32, data_type="int"),
                ccsdspy.PacketField(name="LISTOFFSET", bit_length=32, data_type="int"),
                ccsdspy.PacketField(name="LISTTOTLEN", bit_length=32, data_type="int"),
                ccsdspy.PacketField(name="LISTVLDCNT", bit_length=32, data_type="int"),
                ccsdspy.PacketField(name="LISTFLSLOC", bit_length=32, data_type="int"),
                ccsdspy.PacketField(name="LISTHDRSP1", bit_length=32, data_type="int"),
                ccsdspy.PacketField(name="LISTHDRSP2", bit_length=32, data_type="int"),
                ccsdspy.PacketField(name="LISTRESERV", bit_length=32, data_type="int"),
            ]
        )
        self.CATALOG_LIST_MIN_SUFFIX = 0
        self.CATALOG_LIST_MAX_SUFFIX = 223
        self._fields = []
        # self._add_beginning_fields()
        self._add_middle_fields(
            self.CATALOG_LIST_MIN_SUFFIX, self.CATALOG_LIST_MAX_SUFFIX
        )
        self._add_ending_fields()

    def _middle_fields(self, num: int) -> list[ccsdspy.PacketField]:
        return [
            ccsdspy.PacketField(
                name=f"CATLISTAID{num}", bit_length=32, data_type="int"
            ),
            ccsdspy.PacketField(
                name=f"CATLISTPROC{num}", bit_length=1, data_type="int"
            ),
            ccsdspy.PacketField(
                name=f"CATLSTBLKCNT{num}", bit_length=15, data_type="int"
            ),
            ccsdspy.PacketField(
                name=f"CATLISTEVTCNT{num}", bit_length=16, data_type="int"
            ),
            ccsdspy.PacketField(
                name=f"CATLSTBLKSTRT{num}", bit_length=16, data_type="int"
            ),
            ccsdspy.PacketField(
                name=f"CATLSTBLKEND{num}", bit_length=16, data_type="int"
            ),
            ccsdspy.PacketField(
                name=f"CATLISTSTRTTM{num}", bit_length=32, data_type="int"
            ),
        ]

    def _add_middle_fields(self, min, max):
        for i in range(min, max):
            self._fields.extend(self._middle_fields(i))

    def _add_ending_fields(self):
        self._fields.extend(
            [
                ccsdspy.PacketField(
                    name="SYNCCATLISTPKT", bit_length=16, data_type="int"
                ),
                ccsdspy.PacketField(
                    name="CRCCATLISTPKT", bit_length=16, data_type="int"
                ),
            ]
        )


catalog_list = SudaCatalogListStructure()

hs_suda = ccsdspy.VariableLength(
    [
        ccsdspy.PacketField(name="MSCLK Seconds", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="MSCLK Subseconds", bit_length=16, data_type="uint"),
        # operational status
        ccsdspy.PacketField(
            name="Subseconds Pre-zero", bit_length=16, data_type="uint"
        ),
        ccsdspy.PacketField(name="IF Type", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(name="Selected Interface", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(name="Busy", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(name="Panic", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(name="Instrument Mode", bit_length=3, data_type="uint"),
        ccsdspy.PacketField(
            name="Operational Status Spare", bit_length=1, data_type="uint"
        ),
        # command status
        ccsdspy.PacketField(
            name="Command Accepted Cnt", bit_length=8, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="Command Executed Cnt", bit_length=8, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="Command Rejected Count", bit_length=8, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="Most Recent Command's Sequence Count", bit_length=5, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="Most Recent Command's Status", bit_length=3, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="Most Recent Command's Opcode", bit_length=16, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="2nd Most Recent Command's  Sequence Count",
            bit_length=5,
            data_type="uint",
        ),
        ccsdspy.PacketField(
            name="2nd Most Recent Command's Status", bit_length=3, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="2nd Most Recent Command's Opcode", bit_length=16, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="3rd Most Recent Command's  Sequence Count",
            bit_length=5,
            data_type="uint",
        ),
        ccsdspy.PacketField(
            name="3rd Most Recent Command's Status", bit_length=3, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="3rd Most Recent Command's Opcode", bit_length=16, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="4th Most Recent Command's  Sequence Count",
            bit_length=5,
            data_type="uint",
        ),
        ccsdspy.PacketField(
            name="4th Most Recent Command's Status", bit_length=3, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="4th Most Recent Command's Opcode", bit_length=16, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="5th Most Recent Command's  Sequence Count",
            bit_length=5,
            data_type="uint",
        ),
        ccsdspy.PacketField(
            name="5th Most Recent Command's Status", bit_length=3, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="5th Most Recent Command's Opcode", bit_length=16, data_type="uint"
        ),
        # uart status
        ccsdspy.PacketField(name="Error Count", bit_length=8, data_type="uint"),
        ccsdspy.PacketField(name="UART Spare", bit_length=14, data_type="uint"),
        # error bits (guides SC fault response)
        ccsdspy.PacketField(
            name="Req_SC_Power_Off (Requests instrument shutdown)",
            bit_length=1,
            data_type="uint",
        ),
        ccsdspy.PacketField(
            name="Req_SC_Power_Cycle (OK to attempt instrument restart)",
            bit_length=1,
            data_type="uint",
        ),
        # source data, derived parameters
        ccsdspy.PacketField(
            name="Source Data Derived Parameters SPARE", bit_length=24, data_type="uint"
        ),
        ccsdspy.PacketField(name="CLOCKS_LAST_1PPS", bit_length=24, data_type="uint"),
        ccsdspy.PacketField(name="FG1_HTR_AVG", bit_length=24, data_type="uint"),
        ccsdspy.PacketField(name="FG2_HTR_AVG", bit_length=24, data_type="uint"),
        ccsdspy.PacketField(name="FG3_HTR_AVG", bit_length=24, data_type="uint"),
        ccsdspy.PacketField(name="FG1_DRIVE_PHASE", bit_length=8, data_type="uint"),
        ccsdspy.PacketField(name="FG2_DRIVE_PHASE", bit_length=8, data_type="uint"),
        ccsdspy.PacketField(name="FG3_DRIVE_PHASE", bit_length=8, data_type="uint"),
        ccsdspy.PacketField(name="SPARE", bit_length=2, data_type="uint"),
        ccsdspy.PacketField(name="I_TP_IN1", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(name="I_TP_IN2", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(name="I_FPGA_ID0", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(name="I_FPGA_ID1", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(name="I_FPGA_ID2", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(name="I_FPGA_ID3", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(
            name="FG_GENERAL_REGISTERS", bit_length=16, data_type="uint"
        ),
        ccsdspy.PacketField(name="VERSION", bit_length=24, data_type="uint"),
    ]
)
hs_suda.name = "hs_suda"

adp_metadata_suda = ccsdspy.VariableLength(
    [
        # secondary header
        ccsdspy.PacketField(name="MSCLK Seconds", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(
            name="Subseconds Pre-zero", bit_length=16, data_type="uint"
        ),
        ccsdspy.PacketField(name="AID", bit_length=32, data_type="uint"),
        # ADP Metadata
        ccsdspy.PacketField(name="CTRL = START | END", bit_length=5, data_type="uint"),
        ccsdspy.PacketField(name="ADP Major APID", bit_length=5, data_type="uint"),
        ccsdspy.PacketField(name="ADP Minor APID", bit_length=6, data_type="uint"),
        ccsdspy.PacketField(name="SCLK", bit_length=48, data_type="uint"),
        ccsdspy.PacketField(
            name="Source Sequence Count", bit_length=14, data_type="uint"
        ),
        ccsdspy.PacketField(name="Spare", bit_length=2, data_type="uint"),
        ccsdspy.PacketField(
            name="CTRL==END ? Count : Spare", bit_length=32, data_type="uint"
        ),
        # PEC
        ccsdspy.PacketField(name="PEC (CRC-16-CCITT)", bit_length=16, data_type="uint"),
    ]
)
adp_metadata_suda.name = "adp_metadata_suda"

event_log_pkt = ccsdspy.VariableLength(
    [
        ccsdspy.PacketField(name="Source Data", bit_length=0, data_type="uint"),
        ccsdspy.PacketField(name="PEC (CRC-16-CCITT)", bit_length=16, data_type="uint"),
    ]
)
event_log_pkt.name = "event_log_pkt"

postmortem_log_pkt = ccsdspy.VariableLength(
    [
        ccsdspy.PacketField(name="Source Data", bit_length=0, data_type="uint"),
        ccsdspy.PacketField(name="PEC (CRC-16-CCITT)", bit_length=16, data_type="uint"),
    ]
)
postmortem_log_pkt.name = "postmortem_log_pkt"

command_log_pkt = ccsdspy.VariableLength(
    [
        ccsdspy.PacketField(name="Source Data", bit_length=0, data_type="uint"),
        ccsdspy.PacketField(name="PEC (CRC-16-CCITT)", bit_length=16, data_type="uint"),
    ]
)
command_log_pkt.name = "command_log_pkt"

hardware_centric_pkt = ccsdspy.VariableLength(
    [
        ccsdspy.PacketArray(
            name="Source Data", data_type="uint", bit_length=8, array_shape="expand"
        ),
        ccsdspy.PacketField(name="PEC (CRC-16-CCITT)", bit_length=16, data_type="uint"),
    ]
)
hardware_centric_pkt.name = "hardware_centric_pkt"

software_centric_pkt = ccsdspy.VariableLength(
    [
        ccsdspy.PacketArray(
            name="Source Data", data_type="uint", bit_length=8, array_shape="expand"
        ),
        ccsdspy.PacketField(name="PEC (CRC-16-CCITT)", bit_length=16, data_type="uint"),
    ]
)
software_centric_pkt.name = "software_centric_pkt"

mem_dump_pkt = ccsdspy.VariableLength(
    [
        ccsdspy.PacketField(name="Source Data", bit_length=0, data_type="uint"),
        ccsdspy.PacketField(name="PEC (CRC-16-CCITT)", bit_length=16, data_type="uint"),
    ]
)
mem_dump_pkt.name = "mem_dump_pkt"

flash_table_dump_pkt = ccsdspy.VariableLength(
    [
        ccsdspy.PacketField(name="Source Data", bit_length=0, data_type="uint"),
        ccsdspy.PacketField(name="PEC (CRC-16-CCITT)", bit_length=16, data_type="uint"),
    ]
)
flash_table_dump_pkt.name = "flash_table_dump_pkt"

dwell_pkt = ccsdspy.VariableLength(
    [
        ccsdspy.PacketField(name="Source Data", bit_length=0, data_type="uint"),
        ccsdspy.PacketField(name="PEC (CRC-16-CCITT)", bit_length=16, data_type="uint"),
    ]
)
dwell_pkt.name = "dwell_pkt"

catalog_list_pkt = ccsdspy.VariableLength(
    [
        ccsdspy.PacketField(name="Source Data", bit_length=0, data_type="uint"),
        ccsdspy.PacketField(name="PEC (CRC-16-CCITT)", bit_length=16, data_type="uint"),
    ]
)
catalog_list_pkt.name = "catalog_list_pkt"

adc_register_pkt = ccsdspy.VariableLength(
    [
        ccsdspy.PacketField(name="Source Data", bit_length=0, data_type="uint"),
        ccsdspy.PacketField(name="PEC (CRC-16-CCITT)", bit_length=16, data_type="uint"),
    ]
)
adc_register_pkt.name = "adc_register_pkt"

event_message_pkt = ccsdspy.VariableLength(
    [
        ccsdspy.PacketField(name="SHCOARSE", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="SHFINE", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(name="ELSEC_EVTPKT", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="ELSSEC_EVTPKT", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(name="ELSLICE_EVTPKT", bit_length=8, data_type="uint"),
        ccsdspy.PacketField(
            name="ELID_EVTPKT", bit_length=8, data_type="uint"
        ),  # bin_str
        ccsdspy.PacketField(name="EL1PAR_EVTPKT", bit_length=8, data_type="uint"),
        ccsdspy.PacketField(name="EL2PAR_EVTPKT", bit_length=8, data_type="uint"),
        ccsdspy.PacketField(name="EL3PAR_EVTPKT", bit_length=8, data_type="uint"),
        ccsdspy.PacketField(name="EL4PAR_EVTPKT", bit_length=8, data_type="uint"),
        ccsdspy.PacketField(name="SYNCEVT", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(name="CRCEVTPKT", bit_length=16, data_type="uint"),
    ]
)

event_message_pkt.add_converted_field(
    "ELID_EVTPKT", "ELID_EVTPKT_BIN", StringifyBytesConverter(format="bin")
)
event_message_pkt.name = "event_message_pkt"

METADATA_FIELDS = [
    ccsdspy.PacketField(name="SCIDATALENGTH", bit_length=32, data_type="uint"),
    # ccsdspy.PacketField(name='TIMESTAMP1_PAD', 16, data_type.PADDING),
    ccsdspy.PacketField(name="TIMESTAMP1", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="TIMESTAMP2_SECONDS", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(
        name="TIMESTAMP2_SUBSECONDS", bit_length=16, data_type="uint"
    ),  # 20usec per DN
    # ccsdspy.PacketField(name='EVENTNUMBER_PAD1', 1, data_type.PADDING),
    ccsdspy.PacketField(
        name="EVENTNUMBER_TRIGGER_OFFSET", bit_length=3, data_type="uint"
    ),
    # ccsdspy.PacketField(name='EVENTNUMBER_PAD2', 2, data_type.PADDING),
    ccsdspy.PacketField(
        name="EVENTNUMBER_TRIGGER_ORIGIN", bit_length=10, data_type="uint"
    ),
    ccsdspy.PacketField(
        name="EVENTNUMBER_REMAINDER", bit_length=16, data_type="uint"
    ),  # rolling over from 0xFFFF to 0
    # NBLOCKS_structure,
    # *[pf for sensor in Sensors for pf in _metadata_trigger_levels(sensor)],
    # ccsdspy.PacketField(name='LSADC_PAD', 8, data_type.PADDING),
    ccsdspy.PacketField(name="LSADC_COINCIDENCE", bit_length=3, data_type="uint"),
    ccsdspy.PacketField(name="LSADC_TRIGGER_POLARITY", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="LSADC_TRIGGER_LEVEL", bit_length=12, data_type="uint"),
    ccsdspy.PacketField(name="LSADC_TRIGGER_NMIN", bit_length=8, data_type="uint"),
    ccsdspy.PacketField(
        name="TRIGGERMODE_HVPS_POLARITY", bit_length=1, data_type="uint"
    ),
    # ccsdspy.PacketField(name='TRIGGERMODE_PAD', 22, data_type.PADDING),
    ccsdspy.PacketField(
        name="TRIGGERMODE_EXTERNAL_TRIGGER_POLARITY", bit_length=1, data_type="uint"
    ),
    ccsdspy.PacketField(
        name="TRIGGERMODE_LSADC_COINCIDENCE_MODE", bit_length=1, data_type="uint"
    ),
    ccsdspy.PacketField(
        name="TRIGGERMODE_LSADC_TRIGGER_ENABLE", bit_length=1, data_type="uint"
    ),
    ccsdspy.PacketField(name="TRIGGERMODE_ADC1Q", bit_length=2, data_type="uint"),
    ccsdspy.PacketField(name="TRIGGERMODE_ADC0Q", bit_length=2, data_type="uint"),
    ccsdspy.PacketField(name="TRIGGERMODE_ADC0I", bit_length=2, data_type="uint"),
    # *[PacketField(f'MD_SPARE{n}', 32, data_type = 'uint') for n in range(4)],
    # *[pf for min_or_max in TOFMinMax for pf in _metadata_tofminmax(min_or_max)],
    # *[pf for i in range(3) for pf in _metadata_lsadc_minmax(i)],
    # *[pf for param in TOFParams for pf in _metadata_tof_params(param)],
    # *_metadata_chan(ChanPrefix.PROCHKADC, ChanNum.n01, '1VPOLCUR', '1.9VPOLCUR'),
    # *_metadata_chan(ChanPrefix.PROCHKADC, ChanNum.n23, 'PROCBDTEMP1', 'PROCBDTEMP2'),
    # *_metadata_chan(ChanPrefix.PROCHKADC, ChanNum.n45, '1VOLTAGE', 'FPGATEMP'),
    # *_metadata_chan(ChanPrefix.PROCHKADC, ChanNum.n67, '1.9VOLTAGE', '3.3VOLTAGE'),
    # *_metadata_chan(ChanPrefix.HVPSHKADC, ChanNum.n01, 'DETECTORVOLTAGE', 'SENSORVOLTAGE'),
    # *_metadata_chan(ChanPrefix.HVPSHKADC, ChanNum.n23, 'TARGETVOLTAGE', 'REFLECTRONVOLTAGE'),
    # *_metadata_chan(ChanPrefix.HVPSHKADC, ChanNum.n45, 'REJECTIONVOLTAGE', 'DETECTORCURRENT'),
    # *_metadata_chan(ChanPrefix.HVPSHKADC, ChanNum.n67, 'SENSORIP', 'SENSORIN'),
    # *_metadata_chan(ChanPrefix.LVPSHKADC0, ChanNum.n01, 'P3.3VREF_HK', 'P3.3VREF_OP'),
    # *_metadata_chan(ChanPrefix.LVPSHKADC0, ChanNum.n23, 'N6V', 'P6V'),
    # *_metadata_chan(ChanPrefix.LVPSHKADC0, ChanNum.n45, 'P16V', 'P3.3V'),
    # *_metadata_chan(ChanPrefix.LVPSHKADC0, ChanNum.n67, 'N5V', 'P5V'),
    # *_metadata_chan(ChanPrefix.LVPSHKADC1, ChanNum.n01, 'P3.3_IMON', 'P16V_IMON'),
    # *_metadata_chan(ChanPrefix.LVPSHKADC1, ChanNum.n23, 'P6V_IMON', 'N6V_IMON'),
    # *_metadata_chan(ChanPrefix.LVPSHKADC1, ChanNum.n45, 'P5V_IMON', 'N5V_IMON'),
    # *_metadata_chan(ChanPrefix.LVPSHKADC1, ChanNum.n67, 'P2.5V_IMON', 'N2.5V_IMON'),
    # *_metadata_chan(ChanPrefix.LVPSHKADC2, ChanNum.n01, 'THERM_CSA0', 'THERM_CSA1'),
    # *_metadata_chan(ChanPrefix.LVPSHKADC2, ChanNum.n23, 'THERM_BUFF', 'THERM_LVPS'),
    # *_metadata_chan(ChanPrefix.LVPSHKADC2, ChanNum.n45, 'THERM_HVPS', 'P2.5V'),
    # *_metadata_chan(ChanPrefix.LVPSHKADC2, ChanNum.n67, 'N2.5V', 'SPARE'),
    # *[PacketField(f'MD_SPARE{n}', 32, data_type = 'uint') for n in range(4, 6)],
    # *[PacketField(f'FSWHDR{i:02d}', 32, data_type = 'uint') for i in range(16)],
    ccsdspy.PacketField(name="FPGAVER", bit_length=32, data_type="uint"),
]

fields_before_data = [
    ccsdspy.PacketField(name="SHCOARSE", bit_length=32, data_type="uint"),
    ccsdspy.PacketField(name="SHFINE", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="SCI0AID", bit_length=32, data_type="uint"),
    ccsdspy.PacketField(name="SCI0TYPE", bit_length=8, data_type="uint"),
    ccsdspy.PacketField(name="SCI0CONT", bit_length=8, data_type="uint"),
    ccsdspy.PacketField(name="SCI0SPARE1", bit_length=13, data_type="uint"),
    ccsdspy.PacketField(name="SCI0PACK", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="SCI0FRAG", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="SCI0COMP", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(
        name="SCI0EVTNUM", bit_length=16, data_type="uint"
    ),  # event number
    ccsdspy.PacketField(name="SCI0CAT", bit_length=8, data_type="uint"),
    ccsdspy.PacketField(name="SCI0QUAL", bit_length=8, data_type="uint"),
    ccsdspy.PacketField(name="SCI0FRAGOFF", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="SCI0VER", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="SCI0TIMECOARSE", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="SCI0TIMEFINE", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="SCI0SPARE2", bit_length=32, data_type="uint"),
    ccsdspy.PacketField(name="SCI0SPARE3", bit_length=32, data_type="uint"),
    ccsdspy.PacketField(name="SCI0SPARE4", bit_length=32, data_type="uint"),
]

metadata_fields = METADATA_FIELDS

fields_after_data = [
    ccsdspy.PacketField(name="SYNCSCI0PKT", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="CRCSCI0PKT", bit_length=16, data_type="uint"),
]

event_wf_transmit = ccsdspy.VariableLength(
    [
        ccsdspy.PacketField(name="SHCOARSE", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="SHFINE", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(name="SCI0AID", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="SCI0TYPE", bit_length=8, data_type="uint"),
        ccsdspy.PacketField(name="SCI0CONT", bit_length=8, data_type="uint"),
        ccsdspy.PacketField(name="SCI0SPARE1", bit_length=13, data_type="uint"),
        ccsdspy.PacketField(name="SCI0PACK", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(name="SCI0FRAG", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(name="SCI0COMP", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(
            name="SCI0EVTNUM", bit_length=16, data_type="uint"
        ),  # event number
        ccsdspy.PacketField(name="SCI0CAT", bit_length=8, data_type="uint"),
        ccsdspy.PacketField(name="SCI0QUAL", bit_length=8, data_type="uint"),
        ccsdspy.PacketField(name="SCI0FRAGOFF", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(name="SCI0VER", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(name="SCI0TIMECOARSE", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(name="SCI0TIMEFINE", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(name="SCI0SPARE2", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="SCI0SPARE3", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="SCI0SPARE4", bit_length=32, data_type="uint"),
        ccsdspy.PacketArray(
            name="data", data_type="uint", bit_length=8, array_shape="expand"
        ),
        ccsdspy.PacketField(name="SYNCSCI0PKT", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(name="CRCSCI0PKT", bit_length=16, data_type="uint"),
    ]
)
event_wf_transmit.name = "event_wf_transmit"

event_wf_fetch = ccsdspy.VariableLength(
    [
        ccsdspy.PacketField(name="SHCOARSE", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="SHFINE", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(name="SCI0AID", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="SCI0TYPE", bit_length=8, data_type="uint"),
        ccsdspy.PacketField(name="SCI0CONT", bit_length=8, data_type="uint"),
        ccsdspy.PacketField(name="SCI0SPARE1", bit_length=13, data_type="uint"),
        ccsdspy.PacketField(name="SCI0PACK", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(name="SCI0FRAG", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(name="SCI0COMP", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(
            name="SCI0EVTNUM", bit_length=16, data_type="uint"
        ),  # event number
        ccsdspy.PacketField(name="SCI0CAT", bit_length=8, data_type="uint"),
        ccsdspy.PacketField(name="SCI0QUAL", bit_length=8, data_type="uint"),
        ccsdspy.PacketField(name="SCI0FRAGOFF", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(name="SCI0VER", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(name="SCI0TIMECOARSE", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(name="SCI0TIMEFINE", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(name="SCI0SPARE2", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="SCI0SPARE3", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="SCI0SPARE4", bit_length=32, data_type="uint"),
        ccsdspy.PacketArray(
            name="data", data_type="uint", bit_length=8, array_shape="expand"
        ),
        ccsdspy.PacketField(name="SYNCSCI0PKT", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(name="CRCSCI0PKT", bit_length=16, data_type="uint"),
    ]
)
event_wf_fetch.name = "event_wf_fetch"

event_wf_transmit_with_md = ccsdspy.VariableLength(
    [
        ccsdspy.PacketField(name="SHCOARSE", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="SHFINE", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(name="SCI0AID", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="SCI0TYPE", bit_length=8, data_type="uint"),
        ccsdspy.PacketField(name="SCI0CONT", bit_length=8, data_type="uint"),
        ccsdspy.PacketField(name="SCI0SPARE1", bit_length=13, data_type="uint"),
        ccsdspy.PacketField(name="SCI0PACK", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(name="SCI0FRAG", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(name="SCI0COMP", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(
            name="SCI0EVTNUM", bit_length=16, data_type="uint"
        ),  # event number
        ccsdspy.PacketField(name="SCI0CAT", bit_length=8, data_type="uint"),
        ccsdspy.PacketField(name="SCI0QUAL", bit_length=8, data_type="uint"),
        ccsdspy.PacketField(name="SCI0FRAGOFF", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(name="SCI0VER", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(name="SCI0TIMECOARSE", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(name="SCI0TIMEFINE", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(name="SCI0SPARE2", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="SCI0SPARE3", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="SCI0SPARE4", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="SCIDATALENGTH", bit_length=32, data_type="uint"),
        # ccsdspy.PacketField(name='TIMESTAMP1_PAD', 16, data_type.PADDING),
        ccsdspy.PacketField(name="TIMESTAMP1", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(name="TIMESTAMP2_SECONDS", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(
            name="TIMESTAMP2_SUBSECONDS", bit_length=16, data_type="uint"
        ),  # 20usec per DN
        # ccsdspy.PacketField(name='EVENTNUMBER_PAD1', 1, data_type.PADDING),
        ccsdspy.PacketField(
            name="EVENTNUMBER_TRIGGER_OFFSET", bit_length=3, data_type="uint"
        ),
        # ccsdspy.PacketField(name='EVENTNUMBER_PAD2', 2, data_type.PADDING),
        ccsdspy.PacketField(
            name="EVENTNUMBER_TRIGGER_ORIGIN", bit_length=10, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="EVENTNUMBER_REMAINDER", bit_length=16, data_type="uint"
        ),  # rolling over from 0xFFFF to 0
        # NBLOCKS_structure,
        # *[pf for sensor in Sensors for pf in _metadata_trigger_levels(sensor)],
        # ccsdspy.PacketField(name='LSADC_PAD', 8, data_type.PADDING),
        ccsdspy.PacketField(name="LSADC_COINCIDENCE", bit_length=3, data_type="uint"),
        ccsdspy.PacketField(
            name="LSADC_TRIGGER_POLARITY", bit_length=1, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="LSADC_TRIGGER_LEVEL", bit_length=12, data_type="uint"
        ),
        ccsdspy.PacketField(name="LSADC_TRIGGER_NMIN", bit_length=8, data_type="uint"),
        ccsdspy.PacketField(
            name="TRIGGERMODE_HVPS_POLARITY", bit_length=1, data_type="uint"
        ),
        # ccsdspy.PacketField(name='TRIGGERMODE_PAD', 22, data_type.PADDING),
        ccsdspy.PacketField(
            name="TRIGGERMODE_EXTERNAL_TRIGGER_POLARITY", bit_length=1, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="TRIGGERMODE_LSADC_COINCIDENCE_MODE", bit_length=1, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="TRIGGERMODE_LSADC_TRIGGER_ENABLE", bit_length=1, data_type="uint"
        ),
        ccsdspy.PacketField(name="TRIGGERMODE_ADC1Q", bit_length=2, data_type="uint"),
        ccsdspy.PacketField(name="TRIGGERMODE_ADC0Q", bit_length=2, data_type="uint"),
        ccsdspy.PacketField(name="TRIGGERMODE_ADC0I", bit_length=2, data_type="uint"),
        # *[PacketField(f'MD_SPARE{n}', 32, data_type = 'uint') for n in range(4)],
        # *[pf for min_or_max in TOFMinMax for pf in _metadata_tofminmax(min_or_max)],
        # *[pf for i in range(3) for pf in _metadata_lsadc_minmax(i)],
        # *[pf for param in TOFParams for pf in _metadata_tof_params(param)],
        # *_metadata_chan(ChanPrefix.PROCHKADC, ChanNum.n01, '1VPOLCUR', '1.9VPOLCUR'),
        # *_metadata_chan(ChanPrefix.PROCHKADC, ChanNum.n23, 'PROCBDTEMP1', 'PROCBDTEMP2'),
        # *_metadata_chan(ChanPrefix.PROCHKADC, ChanNum.n45, '1VOLTAGE', 'FPGATEMP'),
        # *_metadata_chan(ChanPrefix.PROCHKADC, ChanNum.n67, '1.9VOLTAGE', '3.3VOLTAGE'),
        # *_metadata_chan(ChanPrefix.HVPSHKADC, ChanNum.n01, 'DETECTORVOLTAGE', 'SENSORVOLTAGE'),
        # *_metadata_chan(ChanPrefix.HVPSHKADC, ChanNum.n23, 'TARGETVOLTAGE', 'REFLECTRONVOLTAGE'),
        # *_metadata_chan(ChanPrefix.HVPSHKADC, ChanNum.n45, 'REJECTIONVOLTAGE', 'DETECTORCURRENT'),
        # *_metadata_chan(ChanPrefix.HVPSHKADC, ChanNum.n67, 'SENSORIP', 'SENSORIN'),
        # *_metadata_chan(ChanPrefix.LVPSHKADC0, ChanNum.n01, 'P3.3VREF_HK', 'P3.3VREF_OP'),
        # *_metadata_chan(ChanPrefix.LVPSHKADC0, ChanNum.n23, 'N6V', 'P6V'),
        # *_metadata_chan(ChanPrefix.LVPSHKADC0, ChanNum.n45, 'P16V', 'P3.3V'),
        # *_metadata_chan(ChanPrefix.LVPSHKADC0, ChanNum.n67, 'N5V', 'P5V'),
        # *_metadata_chan(ChanPrefix.LVPSHKADC1, ChanNum.n01, 'P3.3_IMON', 'P16V_IMON'),
        # *_metadata_chan(ChanPrefix.LVPSHKADC1, ChanNum.n23, 'P6V_IMON', 'N6V_IMON'),
        # *_metadata_chan(ChanPrefix.LVPSHKADC1, ChanNum.n45, 'P5V_IMON', 'N5V_IMON'),
        # *_metadata_chan(ChanPrefix.LVPSHKADC1, ChanNum.n67, 'P2.5V_IMON', 'N2.5V_IMON'),
        # *_metadata_chan(ChanPrefix.LVPSHKADC2, ChanNum.n01, 'THERM_CSA0', 'THERM_CSA1'),
        # *_metadata_chan(ChanPrefix.LVPSHKADC2, ChanNum.n23, 'THERM_BUFF', 'THERM_LVPS'),
        # *_metadata_chan(ChanPrefix.LVPSHKADC2, ChanNum.n45, 'THERM_HVPS', 'P2.5V'),
        # *_metadata_chan(ChanPrefix.LVPSHKADC2, ChanNum.n67, 'N2.5V', 'SPARE'),
        # *[PacketField(f'MD_SPARE{n}', 32, data_type = 'uint') for n in range(4, 6)],
        # *[PacketField(f'FSWHDR{i:02d}', 32, data_type = 'uint') for i in range(16)],
        ccsdspy.PacketField(name="FPGAVER", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="SYNCSCI0PKT", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(name="CRCSCI0PKT", bit_length=16, data_type="uint"),
    ]
)
event_wf_transmit_with_md.name = "event_wf_transmit_with_md"
