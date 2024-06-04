"""Catalog header packet definition."""
import ccsdspy
from ccsds.packets.europa_clipper.common.ccsds_header_footer import CRC_FOOTER
from ccsds.packets.europa_clipper.common.ccsds_header_footer import SECONDARY_HEADER


catalog = ccsdspy.VariableLength(SECONDARY_HEADER)
catalog.name = "catalog"
catalog.apid = 1426

current_aid = None


def is_new_header(aid):
    """Identify if the packet is a catalog header or entries for APID 1426."""
    global current_aid
    if current_aid is None or current_aid != aid:
        current_aid = aid
        return True
    else:
        return False


catalog.decision_field = "Accountability ID"
catalog.decision_fun = is_new_header


catalog_header = ccsdspy.VariableLength(
    [
        *SECONDARY_HEADER,
        ccsdspy.PacketField(name="CADHDROFFSET", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="CATHDRTOTLEN", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="CATHDRVLDCNT", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="CATHDRBLOCK", bit_length=26, data_type="uint"),
        ccsdspy.PacketField(name="CATHDRPAGE", bit_length=6, data_type="uint"),
        ccsdspy.PacketField(name="CATHDRENTRYTOTAL", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="CATHDRENTRYCNT", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="CATHDRENTRYSTART", bit_length=32, data_type="uint"),
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
        ccsdspy.PacketField(name="HS0PINCTRL", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="HS0PWRCTRL", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="HS1PINCTRL", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="HS1PWRCTRL", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="FPGATESTPATTERN", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="DCLKALIGN", bit_length=32, data_type="uint"),
        ccsdspy.PacketArray(
            name="EYEPATTERN", bit_length=32, data_type="uint", array_shape=(24,)
        ),
        ccsdspy.PacketField(name="EDACSTAT", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="ERRSTAT", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="MIRRORENA", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="STARTBLOCK", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="CURRENTWR", bit_length=32, data_type="uint"),
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
        ccsdspy.PacketField(name="OVREVT", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="OVRSEC", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="OVRSUB", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="O00EVT", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="O00SEC", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="O00SUB", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="PAGECNT", bit_length=32, data_type="uint"),
        # It does not always work !
        # ccsdspy.PacketField(
        #    name="PADDING2", bit_length=697 * 32, data_type="fill"
        # ),  # 645 in white paper
        # Make it more flexible
        ccsdspy.PacketArray(
            name="PADDING2",
            bit_length=8,
            data_type="uint",
            array_shape="expand",
        ),  #
        ccsdspy.PacketField(name="SYNCCATHDR", bit_length=16, data_type="uint"),
        CRC_FOOTER,
    ]
)

catalog_header.name = "catalog_header"
catalog_header.apid = 1426
catalog_header.sub_apid = True
