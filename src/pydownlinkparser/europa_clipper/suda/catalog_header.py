"""Catalog header packet definition."""
import ccsdspy


catalog = ccsdspy.VariableLength(
    [ccsdspy.PacketField(name="CATHDRAID", bit_length=32, data_type="uint")]
)
catalog.name = "catalog"


catalog_header = ccsdspy.VariableLength(
    [
        ccsdspy.PacketField(
            name="Instrument SCLK Time second", bit_length=32, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="Instrument SCLK Time subsec", bit_length=16, data_type="uint"
        ),
        ccsdspy.PacketField(name="CATHDRAID", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="CADHDROFFSET", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="CATHDRTOTLEN", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="CATHDRVLDCNT", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="CATHDRVLDCNT", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="CATHDRBLOCK", bit_length=26, data_type="uint"),
        ccsdspy.PacketField(name="CATHDRPAGE", bit_length=6, data_type="uint"),
        ccsdspy.PacketField(name="CATHDRRSVD1", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="CATHDRRSVD2", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="CATHDRRSVD3", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="CATHDRKEY", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="CATHDRCKSUM", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="CATHDRLEN", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="CATHDRMORE", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="CATHDRCONT", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="SPARE0", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="SPARE1", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="SPARE2", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="AID", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="EVTCNT", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="BLOCKCNT", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="FPGAEVTCNT", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="STARTTIME", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="ENDTIME", bit_length=32, data_type="uint"),
        ccsdspy.PacketArray(
            name="CATEGORYCOUNT", bit_length=32, data_type="uint", array_shape=(32,)
        ),
        ccsdspy.PacketField(name="PADDING", bit_length=16 * 32, data_type="fill"),
        # HS0PINCTRL
        ccsdspy.PacketField(name="HS0PINCTRL_PADDING", bit_length=26, data_type="fill"),
        ccsdspy.PacketField(
            name="HS0PINCTRL_CALRUNFLAG", bit_length=1, data_type="uint"
        ),
        ccsdspy.PacketField(name="HS0PINCTRL_CALSEQ", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(
            name="HS0PINCTRL_CALINITINPUT", bit_length=1, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="HS0PINCTRL_TESTPATMODE", bit_length=1, data_type="uint"
        ),
        ccsdspy.PacketField(name="HS0PINCTRL_FSR", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(name="HS0PINCTRL_ECEN", bit_length=1, data_type="uint"),
        # HS0PWRCTRL
        ccsdspy.PacketField(name="HS0PWRCTRL_PADDING", bit_length=28, data_type="fill"),
        ccsdspy.PacketField(name="HS0PWRCTRL_PDNQ", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(name="HS0PWRCTRL_PDQ", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(name="HS0PWRCTRL_PDNI", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(name="HS0PWRCTRL_PDI", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(name="HS1PINCTRL", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="HS1PWRCCTRL", bit_length=32, data_type="uint"),
        # FPGATESTPATTERN
        # TODO size is 40 bits which sounds weird
        ccsdspy.PacketField(
            name="FPGATESTPATTERN_PADDING1", bit_length=22, data_type="fill"
        ),
        ccsdspy.PacketField(
            name="FPGATESTPATTERN_PBL", bit_length=10, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="FPGATESTPATTERN_PADDING2", bit_length=1, data_type="fill"
        ),
        ccsdspy.PacketField(
            name="FPGATESTPATTERN_ADC0DI", bit_length=1, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="FPGATESTPATTERN_LSADC2", bit_length=1, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="FPGATESTPATTERN_LSADC1", bit_length=1, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="FPGATESTPATTERN_LSADC0", bit_length=1, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="FPGATESTPATTERN_ADC1DQ", bit_length=1, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="FPGATESTPATTERN_ADC0DQ", bit_length=1, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="FPGATESTPATTERN_ADC0DI", bit_length=1, data_type="uint"
        ),
        # DCLKALIGN
        ccsdspy.PacketField(
            name="DCLKALIGN_CLOCKALISTATUS", bit_length=1, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="DCLKALIGN_DCLKPSDONE", bit_length=1, data_type="uint"
        ),
        ccsdspy.PacketField(name="DCLKALIGN_PADDING1", bit_length=5, data_type="fill"),
        ccsdspy.PacketField(name="DCLKALIGN_EYESIZE", bit_length=9, data_type="uint"),
        ccsdspy.PacketField(name="DCLKALIGN_EYESTART", bit_length=8, data_type="uint"),
        ccsdspy.PacketField(name="DCLKALIGN_PADDING2", bit_length=1, data_type="fill"),
        ccsdspy.PacketField(name="DCLKALIGN_EYECENTER", bit_length=7, data_type="uint"),
        # EYEPATTERN
        ccsdspy.PacketArray(
            name="EYEPATTERN", bit_length=32, data_type="uint", array_shape=(24,)
        ),
        # EDACSTAT
        ccsdspy.PacketField(name="EDACSTAT_PADDING1", bit_length=12, data_type="fill"),
        ccsdspy.PacketField(name="EDACSTAT_BTMBE", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(name="EDACSTAT_BTSBE", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(name="EDACSTAT_FIFOMBE", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(name="EDACSTAT_FIFOSBE", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(name="EDACSTAT_PADDING2", bit_length=1, data_type="fill"),
        ccsdspy.PacketField(
            name="EDACSTAT_LSEDACMERR3", bit_length=1, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="EDACSTAT_LSEDACMERR2", bit_length=1, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="EDACSTAT_LSEDACMERR1", bit_length=1, data_type="uint"
        ),
        ccsdspy.PacketField(name="EDACSTAT_PADDING3", bit_length=1, data_type="fill"),
        ccsdspy.PacketField(
            name="EDACSTAT_LSEDACSERR3", bit_length=1, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="EDACSTAT_LSEDACSERR2", bit_length=1, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="EDACSTAT_LSEDACSERR1", bit_length=1, data_type="uint"
        ),
        ccsdspy.PacketField(name="EDACSTAT_PADDING4", bit_length=1, data_type="fill"),
        ccsdspy.PacketField(
            name="EDACSTAT_HSEDACMERR3", bit_length=1, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="EDACSTAT_HSEDACMERR2", bit_length=1, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="EDACSTAT_HSEDACMERR1", bit_length=1, data_type="uint"
        ),
        ccsdspy.PacketField(name="EDACSTAT_PADDING5", bit_length=1, data_type="fill"),
        ccsdspy.PacketField(
            name="EDACSTAT_HSEDACSERR3", bit_length=1, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="EDACSTAT_HSEDACSERR2", bit_length=1, data_type="uint"
        ),
        ccsdspy.PacketField(
            name="EDACSTAT_HSEDACSERR1", bit_length=1, data_type="uint"
        ),
        # ERRSTAT
        ccsdspy.PacketField(name="ERRSTAT_PADDING", bit_length=27, data_type="fill"),
        ccsdspy.PacketField(name="ERRSTAT_MBNAND", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(name="ERRSTAT_DBNAND", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(name="ERRSTAT_SBNAND", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(name="ERRSTAT_NAND", bit_length=1, data_type="uint"),
        ccsdspy.PacketField(name="ERRSTAT_FLASHOVER", bit_length=1, data_type="uint"),
        # MIRRORENA
        ccsdspy.PacketField(name="MIRRORENA_PADDING", bit_length=31, data_type="fill"),
        ccsdspy.PacketField(name="MIRRORENA_STATUS", bit_length=1, data_type="uint"),
        # STARTBLOCK
        ccsdspy.PacketField(name="STARTBLOCK_PADDING", bit_length=17, data_type="fill"),
        ccsdspy.PacketField(name="STARTBLOCK_NUMBER", bit_length=15, data_type="uint"),
        # CURRENTWR
        ccsdspy.PacketField(name="CURRENTWR_PADDING", bit_length=11, data_type="fill"),
        ccsdspy.PacketField(name="CURRENTWR_CDN", bit_length=3, data_type="uint"),
        ccsdspy.PacketField(name="CURRENTWR_CBN", bit_length=12, data_type="uint"),
        ccsdspy.PacketField(name="CURRENTWR_CPN", bit_length=6, data_type="uint"),
        ccsdspy.PacketField(name="PROCESSCNT", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="PROCESSTIMESTAMP", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="ACQDURATION", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="PARAMTABLE1", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="PARAMTABLE2", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="MEMPARAM1", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="MEMPARAM2", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="EVTSTARTMARKER", bit_length=32, data_type="uint"),
        ccsdspy.PacketArray(
            name="FIRSTEVENTHDR", bit_length=32, data_type="uint", array_shape=(64,)
        ),
        ccsdspy.PacketField(name="PROCCHANS", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="TOFPEAKWIDTH", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="TOFPEAKMIN", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="TOFPEAKSIG", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="HSSAMPLES", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="LSSAMPLES", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="HSBLKCNT", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="LSBLKCNT", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="HSCLIP", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="LSCLIP", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="HSPREMIN", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="HSPOSTMIN", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="LSPREMIN", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="LSPOSTMIN", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="HSMINDELTA", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="LSMINDELTA", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="NOISECAT", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="FIRSTEVT", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="FIRSTSEC", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="FIRSTSUB", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="LASTEVT", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="LASTSEC", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="LASTSUB", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="FIRSTEVT", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="FIRSTSEC", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="OVREVT", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="OVRSEC", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="OVRSUB", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="O00EVT", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="O00SEC", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="O00SUB", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="PAGECNT", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="PADDING2", bit_length=645 * 32, data_type="fill"),
        ccsdspy.PacketField(name="SYNCCATHDR", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(name="CRCCATHDR", bit_length=16, data_type="uint"),
    ]
)

catalog_header.name = "catalog_header"
