"""Event metadata packet field list."""
from enum import Enum

import ccsdspy

Sensors = Enum("Sensor", ["ADC0I", "ADC0Q", "ADC1Q"])
TOFMinMax = Enum("TOFMinMax", ["MAX", "MIN"])
TOFParams = Enum("TOFParams", ["TRIGGERDELAY", "SAMPLEDELAY", "TRANSCOUNT"])
ChanNum = Enum(
    "ChanNum", ["n01", "n23", "n45", "n67"]
)  # Enum names cannot start with numbers
ChanPrefix = Enum(
    "ChanPrefix", ["PROCHKADC", "HVPSHKADC", "LVPSHKADC0", "LVPSHKADC1", "LVPSHKADC2"]
)


def _metadata_timestamp():
    """Timestamp fields.

    The fine grained parsing is not needed anymore.
    """
    return [
        ccsdspy.PacketField(name="TIMESTAMP1_PAD", bit_length=16, data_type="fill"),
        ccsdspy.PacketField(name="TIMESTAMP1", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(name="TIMESTAMP2", bit_length=32, data_type="uint"),
    ]


def EVENTNUMBER_structure():  # noqa: N802
    """Event number fields."""
    return [
        ccsdspy.PacketField(
            name="EVENTNUMBER_REMAINDER", bit_length=16, data_type="uint"
        ),  # rolling over from 0xFFFF to 0
        ccsdspy.PacketField(
            name="EVENTNUMBER_TRIGGER_ORIGIN", bit_length=10, data_type="uint"
        ),
        ccsdspy.PacketField(name="EVENTNUMBER_PAD2", bit_length=2, data_type="uint"),
        ccsdspy.PacketField(
            name="EVENTNUMBER_TRIGGER_OFFSET", bit_length=3, data_type="uint"
        ),
        ccsdspy.PacketField(name="EVENTNUMBER_PAD1", bit_length=1, data_type="uint"),
    ]


def NBLOCKS_structure():  # noqa: N802
    """NBLOCKS fields."""
    return [
        ccsdspy.PacketField(name="NBLOCKS_HS_ERROR", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(name="NBLOCKS_LS_ERROR", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(
            name="NBLOCKS_DEAD_BASE", bit_length=6, data_type="uint"
        ),  # 0-63
        ccsdspy.PacketField(
            name="NBLOCKS_DEAD_SHIFT", bit_length=4, data_type="uint"
        ),  # 0-15
        ccsdspy.PacketField(name="NBLOCKS_HS_PRE", bit_length=4, data_type="uint"),
        ccsdspy.PacketField(name="NBLOCKS_HS_POST", bit_length=4, data_type="uint"),
        ccsdspy.PacketField(name="NBLOCKS_LS_PRE", bit_length=6, data_type="uint"),
        ccsdspy.PacketField(name="NBLOCKS_LS_POST", bit_length=6, data_type="uint"),
    ]


def LSADC_Structure():  # noqa: N802
    """LSADC fields."""
    return [
        ccsdspy.PacketField(name="LSADC_TRIGGER_NMIN", bit_length=8, data_type="uint"),
        ccsdspy.PacketField(
            name="LSADC_TRIGGER_LEVEL", bit_length=12, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="LSADC_TRIGGER_POLARITY", bit_length=1, data_type="uint"
        ),
        ccsdspy.PacketField(name="LSADC_COINCIDENCE", bit_length=3, data_type="uint"),
        ccsdspy.PacketField(name="LSADC_PAD", bit_length=8, data_type="uint"),
    ]


def _metadata_trigger_levels(sensor: Sensors) -> list[ccsdspy.PacketField]:
    """Trigger level fields."""
    return [
        ccsdspy.PacketField(
            name=f"HS{sensor.name}HDR1_TRIGGER_NMIN12", bit_length=11, data_type="uint"
        ),
        ccsdspy.PacketField(
            name=f"HS{sensor.name}HDR1_TRIGGER_NMAX12", bit_length=11, data_type="uint"
        ),
        ccsdspy.PacketField(
            name=f"HS{sensor.name}HDR1_TRIGGER_LEVEL", bit_length=10, data_type="uint"
        ),
        ccsdspy.PacketField(
            name=f"HS{sensor.name}HDR2_TRIGGER_NMIN1", bit_length=8, data_type="uint"
        ),
        ccsdspy.PacketField(
            name=f"HS{sensor.name}HDR2_TRIGGER_NMAX1", bit_length=8, data_type="uint"
        ),
        ccsdspy.PacketField(
            name=f"HS{sensor.name}HDR2_TRIGGER_NMIN2", bit_length=8, data_type="uint"
        ),
        ccsdspy.PacketField(
            name=f"HS{sensor.name}HDR2_TRIGGER_NMAX2", bit_length=8, data_type="uint"
        ),
    ]


def TRIGGERMODE_Structure():  # noqa: N802
    """Trigger Mode fields."""
    return [
        ccsdspy.PacketField(name="TRIGGERMODE_ADC0I", bit_length=2, data_type="uint"),
        ccsdspy.PacketField(name="TRIGGERMODE_ADC0Q", bit_length=2, data_type="uint"),
        ccsdspy.PacketField(name="TRIGGERMODE_ADC1Q", bit_length=2, data_type="uint"),
        ccsdspy.PacketField(
            name="TRIGGERMODE_LSADC_TRIGGER_ENABLE", bit_length=1, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="TRIGGERMODE_LSADC_COINCIDENCE_MODE", bit_length=1, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="TRIGGERMODE_EXTERNAL_TRIGGER_POLARITY", bit_length=1, data_type="uint"
        ),
        ccsdspy.PacketField(name="TRIGGERMODE_PAD", bit_length=22, data_type="uint"),
        ccsdspy.PacketField(
            name="TRIGGERMODE_HVPS_POLARITY", bit_length=1, data_type="uint"
        ),
    ]


def _metadata_tofminmax(min_or_max: TOFMinMax) -> list[ccsdspy.PacketField]:
    """TOF min max fields."""
    return [
        ccsdspy.PacketField(
            name=f"TOF{min_or_max.name}_ADC0I", bit_length=10, data_type="uint"
        ),
        ccsdspy.PacketField(
            name=f"TOF{min_or_max.name}_ADC0Q", bit_length=10, data_type="uint"
        ),
        ccsdspy.PacketField(
            name=f"TOF{min_or_max.name}_ADC1Q", bit_length=10, data_type="uint"
        ),
        ccsdspy.PacketField(
            name=f"TOF{min_or_max.name}_PAD", bit_length=2, data_type="uint"
        ),  # TODO make a function
    ]


def _metadata_lsadc_minmax(lsadc_number: int) -> list[ccsdspy.PacketField]:
    """LSADC min/max fields."""
    return [
        ccsdspy.PacketField(
            name=f"LSADC{lsadc_number}MINMAX_MIN", bit_length=12, data_type="uint"
        ),
        ccsdspy.PacketField(
            name=f"LSADC{lsadc_number}MINMAX_MAX", bit_length=12, data_type="uint"
        ),
        ccsdspy.PacketField(
            name=f"LSADC{lsadc_number}MINMAX_PAD", bit_length=8, data_type="uint"
        ),  # TODO make a function
    ]


def _metadata_tof_params(param: TOFParams) -> list[ccsdspy.PacketField]:
    """TOF params."""
    return [
        ccsdspy.PacketField(
            name=f"TOF{param.name}_ADC0I", bit_length=10, data_type="uint"
        ),
        ccsdspy.PacketField(
            name=f"TOF{param.name}_ADC0Q", bit_length=10, data_type="uint"
        ),
        ccsdspy.PacketField(
            name=f"TOF{param.name}_ADC1Q", bit_length=10, data_type="uint"
        ),
        ccsdspy.PacketField(
            name=f"TOF{param.name}_PAD", bit_length=2, data_type="uint"
        ),
    ]


def _metadata_chan(
    prefix: ChanPrefix, numbers: ChanNum, val1: str, val2: str
) -> list[ccsdspy.PacketField]:
    """CHAN fields."""
    # "PROCHKADC", "HVPSHKADC", "LVPSHKADC0", "LVPSHKADC1", "LVPSHKADC2"
    # "n01", "n23", "n45", "n67"

    return [
        ccsdspy.PacketField(
            name=f"{prefix.name}CHAN{numbers.name[1:]}_PAD1",
            bit_length=4,
            data_type="uint",
        ),
        ccsdspy.PacketField(
            name=f"{prefix.name}CHAN{numbers.name[1:]}_{val1}",
            bit_length=12,
            data_type="uint",
        ),
        ccsdspy.PacketField(
            name=f"{prefix.name}CHAN{numbers.name[1:]}_PAD2",
            bit_length=4,
            data_type="uint",
        ),
        ccsdspy.PacketField(
            name=f"{prefix.name}CHAN{numbers.name[1:]}_{val2}",
            bit_length=12,
            data_type="uint",
        ),
    ]


METADATA_FIELDS = [
    ccsdspy.PacketField(name="SCIDATALENGTH", bit_length=32, data_type="uint"),
    *_metadata_timestamp(),
    *EVENTNUMBER_structure(),
    *NBLOCKS_structure(),
    *LSADC_Structure(),
    *[pf for sensor in Sensors for pf in _metadata_trigger_levels(sensor)],
    *TRIGGERMODE_Structure(),
    *[
        ccsdspy.PacketField(name=f"MD_SPARE{n}", bit_length=32, data_type="uint")
        for n in range(4)
    ],
    *[pf for min_or_max in TOFMinMax for pf in _metadata_tofminmax(min_or_max)],
    *[pf for i in range(3) for pf in _metadata_lsadc_minmax(i)],
    *[pf for param in TOFParams for pf in _metadata_tof_params(param)],
    *_metadata_chan(ChanPrefix.PROCHKADC, ChanNum.n01, "1VPOLCUR", "1.9VPOLCUR"),
    *_metadata_chan(ChanPrefix.PROCHKADC, ChanNum.n23, "PROCBDTEMP1", "PROCBDTEMP2"),
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
    *_metadata_chan(ChanPrefix.LVPSHKADC0, ChanNum.n01, "P3.3VREF_HK", "P3.3VREF_OP"),
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
]
