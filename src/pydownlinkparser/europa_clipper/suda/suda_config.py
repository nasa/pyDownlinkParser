"""Packet definitions for SUDA instrument."""
from enum import Enum

import ccsdspy
from ccsdspy.converters import StringifyBytesConverter

Major_APID = 0x16


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
        ccsdspy.PacketField(name="TIMESTAMP1_PAD", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(name="TIMESTAMP1", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(name="TIMESTAMP2_SECONDS", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(
            name="TIMESTAMP2_SUBSECONDS", bit_length=16, data_type="uint"
        ),  # 20usec per DN
        ccsdspy.PacketField(name="EVENTNUMBER_PAD1", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(
            name="EVENTNUMBER_TRIGGER_OFFSET", bit_length=3, data_type="uint"
        ),
        ccsdspy.PacketField(name="EVENTNUMBER_PAD2", bitlength=2, data_type="uint"),
        ccsdspy.PacketField(
            name="EVENTNUMBER_TRIGGER_ORIGIN", bit_length=10, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="EVENTNUMBER_REMAINDER", bit_length=16, data_type="uint"
        ),  # rolling over from 0xFFFF to 0
        # NBLOCKS_structure,
        *[pf for sensor in Sensors for pf in _metadata_trigger_levels(sensor)],
        ccsdspy.PacketField(name="LSADC_PAD", bit_length=8, data_type="uint"),
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
        *[
            ccsdspy.PacketField(name=f"MD_SPARE{n}", bit_length=32, data_type="uint")
            for n in range(4)
        ],
        *[pf for min_or_max in TOFMinMax for pf in _metadata_tofminmax(min_or_max)],
        *[pf for i in range(3) for pf in _metadata_lsadc_minmax(i)],
        *[pf for param in TOFParams for pf in _metadata_tof_params(param)],
        *_metadata_chan(ChanPrefix.PROCHKADC, ChanNum.n01, "1VPOLCUR", "1.9VPOLCUR"),
        *_metadata_chan(
            ChanPrefix.PROCHKADC, ChanNum.n23, "PROCBDTEMP1", "PROCBDTEMP2"
        ),
        *_metadata_chan(ChanPrefix.PROCHKADC, ChanNum.n45, "1VOLTAGE", "FPGATEMP"),
        *_metadata_chan(ChanPrefix.PROCHKADC, ChanNum.n67, "1.9VOLTAGE", "3.3VOLTAGE"),
        *_metadata_chan(
            ChanPrefix.HVPSHKADC, ChanNum.n01, "DETECTORVOLTAGE", "SENSORVOLTAGE"
        ),
        *_metadata_chan(
            ChanPrefix.HVPSHKADC, ChanNum.n23, "TARGETVOLTAGE", "REFLECTRONVOLTAGE"
        ),
        *_metadata_chan(
            ChanPrefix.HVPSHKADC, ChanNum.n45, "REJECTIONVOLTAGE", "DETECTORCURRENT"
        ),
        *_metadata_chan(ChanPrefix.HVPSHKADC, ChanNum.n67, "SENSORIP", "SENSORIN"),
        *_metadata_chan(
            ChanPrefix.LVPSHKADC0, ChanNum.n01, "P3.3VREF_HK", "P3.3VREF_OP"
        ),
        *_metadata_chan(ChanPrefix.LVPSHKADC0, ChanNum.n23, "N6V", "P6V"),
        *_metadata_chan(ChanPrefix.LVPSHKADC0, ChanNum.n45, "P16V", "P3.3V"),
        *_metadata_chan(ChanPrefix.LVPSHKADC0, ChanNum.n67, "N5V", "P5V"),
        *_metadata_chan(ChanPrefix.LVPSHKADC1, ChanNum.n01, "P3.3_IMON", "P16V_IMON"),
        *_metadata_chan(ChanPrefix.LVPSHKADC1, ChanNum.n23, "P6V_IMON", "N6V_IMON"),
        *_metadata_chan(ChanPrefix.LVPSHKADC1, ChanNum.n45, "P5V_IMON", "N5V_IMON"),
        *_metadata_chan(ChanPrefix.LVPSHKADC1, ChanNum.n67, "P2.5V_IMON", "N2.5V_IMON"),
        *_metadata_chan(ChanPrefix.LVPSHKADC2, ChanNum.n01, "THERM_CSA0", "THERM_CSA1"),
        *_metadata_chan(ChanPrefix.LVPSHKADC2, ChanNum.n23, "THERM_BUFF", "THERM_LVPS"),
        *_metadata_chan(ChanPrefix.LVPSHKADC2, ChanNum.n45, "THERM_HVPS", "P2.5V"),
        *_metadata_chan(ChanPrefix.LVPSHKADC2, ChanNum.n67, "N2.5V", "SPARE"),
        *[
            ccsdspy.PacketField(name=f"MD_SPARE{n}", bit_length=32, data_type="uint")
            for n in range(4, 6)
        ],
        *[
            ccsdspy.PacketField(name=f"FSWHDR{i:02d}", bit_length=32, data_type="uint")
            for i in range(16)
        ],
        ccsdspy.PacketField(name="FPGAVER", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="SYNCSCI0PKT", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(name="CRCSCI0PKT", bit_length=16, data_type="uint"),
    ]
)
event_wf_transmit_with_md.name = "event_wf_transmit_with_md"
