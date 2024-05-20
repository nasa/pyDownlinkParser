"""Catalog entries sub-packet converter."""
import logging

import ccsdspy
from bitstring import ConstBitStream
from bitstring import ReadError

logger = logging.getLogger(__name__)


class SudaCatalogEntries(ccsdspy.VariableLength):
    """Catalog packet structure definition."""

    def __init__(self):
        """Initialization."""
        fields = [
            # SUDA Science Packet White Paper, 3.2, first table
            # per word (32bits), the order of the fields are reversed because of the FPGA specification
            # which handle word bits from 32 to 1
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
            ccsdspy.PacketField(name="CATHDRBLOCK", bit_length=26, data_type="uint"),
            ccsdspy.PacketField(name="CATHDRPAGE", bit_length=6, data_type="uint"),
            ccsdspy.PacketField(name="CATHDRRSVD1", bit_length=32, data_type="uint"),
            ccsdspy.PacketField(name="CATHDRRSVD2", bit_length=32, data_type="uint"),
            ccsdspy.PacketField(name="CATHDRRSVD3", bit_length=32, data_type="uint"),
            ccsdspy.PacketField(name="CATNOISECNT", bit_length=16, data_type="uint"),
            ccsdspy.PacketField(name="CATPROCCNT", bit_length=16, data_type="uint"),
            ccsdspy.PacketField(name="CATLASTEVT", bit_length=16, data_type="uint"),
            ccsdspy.PacketField(name="CATFIRSTEVT", bit_length=16, data_type="uint"),
            ccsdspy.PacketField(name="NOISECATEGORY", bit_length=5, data_type="uint"),
            ccsdspy.PacketField(name="OVRFLOW", bit_length=1, data_type="uint"),
            ccsdspy.PacketField(name="CATSPARE0", bit_length=10, data_type="uint"),
            ccsdspy.PacketField(name="SCICSCVER", bit_length=16, data_type="uint"),
            ccsdspy.PacketField(name="CATSPARE1", bit_length=32, data_type="uint"),
            # SUDA Science Packet White Paper, 3.2, second table, individual entries
            ccsdspy.PacketArray(name="INDENTRIES", bit_length=8, array_shape="expand"),
            # SUDA Science Packet White Paper, 3.2, first table
            ccsdspy.PacketField(name="SYNCCATENTRIES", bit_length=16, data_type="uint"),
            ccsdspy.PacketField(name="CRCCATENTRIES", bit_length=16, data_type="uint"),
        ]
        super().__init__(fields)
        self.name = "catalog_entries"
        self.apid = 1426
        self.sub_apid = False
        self.add_converted_field(
            ["NOISECATEGORY", "INDENTRIES"], "DECODEDENTRIES", InEntriesDecoder()
        )


class InEntriesDecoder(ccsdspy.converters.Converter):
    """Converter used to parse the entries in a single packet."""

    def __init__(self):
        """Initialization, default."""
        pass

    @staticmethod
    def __parse_entry(noise_category, entries_stream: ConstBitStream):
        """Parse a single entry.

        @param noise_category: noise category below which an entry is considered noise.
        @param entries_stream: ConstBitStream containing the entries to be parsed.
        @return: the entry parsed, as a dictionary field:value.
        """
        decoded_entry = {}

        category = entries_stream.read(5).uint
        decoded_entry["CATEGORY"] = category
        decoded_entry["EVENTTIME"] = entries_stream.read(16).uint

        # TODO 0 is noise, above 0 is not noise.
        if category <= noise_category:
            # noise entry, see white paper, section 3.2 third table
            # 5+16+6+5 = 32bits for noise category
            decoded_entry["QTAMAX"] = entries_stream.read(6).uint
            decoded_entry["QIAMAX"] = entries_stream.read(5).uint

        else:
            # size of an event non noise entry
            # 16+5+4+7+4*16+5+11+8+16+11*8 = 224bits
            # regular entry, see white paper, section 3.2 second table
            decoded_entry["TOFPEAKCOUNT"] = entries_stream.read(4).uint
            decoded_entry["TOFAPEAK1"] = entries_stream.read(7).uint
            decoded_entry["TOFTPEAK1"] = entries_stream.read(11).uint
            decoded_entry["TOFAPEAK2"] = entries_stream.read(5).uint
            decoded_entry["TOFTPEAK2"] = entries_stream.read(11).uint
            decoded_entry["TOFAPEAK3"] = entries_stream.read(5).uint
            decoded_entry["TOFTPEAK3"] = entries_stream.read(11).uint
            decoded_entry["TOFAPEAK4"] = entries_stream.read(5).uint
            decoded_entry["TOFTPEAK4"] = entries_stream.read(11).uint
            decoded_entry["TOFAPEAK5"] = entries_stream.read(5).uint
            decoded_entry["Spare"] = entries_stream.read(1).uint
            decoded_entry["TOFCLIP"] = entries_stream.read(1).uint
            decoded_entry["QVCLIP"] = entries_stream.read(1).uint
            decoded_entry["QTCLIP"] = entries_stream.read(1).uint
            decoded_entry["QICLIP"] = entries_stream.read(1).uint
            # TODO: check if TOFTPEAK5 properly located
            decoded_entry["TOFTPEAK5"] = entries_stream.read(11).uint
            decoded_entry["TOFMEAN"] = entries_stream.read(8).uint
            decoded_entry["TOFSNR"] = entries_stream.read(4).uint
            decoded_entry["QVSNR"] = entries_stream.read(4).uint
            decoded_entry["QTSNR"] = entries_stream.read(4).uint
            decoded_entry["QISNR"] = entries_stream.read(4).uint
            decoded_entry["QVMEAN"] = entries_stream.read(8).uint
            decoded_entry["QVAMAX"] = entries_stream.read(8).uint
            decoded_entry["QVTMAX"] = entries_stream.read(8).uint
            decoded_entry["QTMEAN"] = entries_stream.read(8).uint
            decoded_entry["QTAMAX"] = entries_stream.read(8).uint
            decoded_entry["QTTMAX"] = entries_stream.read(8).uint
            decoded_entry["QTTIMPACT"] = entries_stream.read(8).uint
            decoded_entry["QIMEAN"] = entries_stream.read(8).uint
            decoded_entry["QIAMAX"] = entries_stream.read(8).uint
            decoded_entry["QITMAX"] = entries_stream.read(8).uint
            decoded_entry["QITIMPACT"] = entries_stream.read(8).uint

        return decoded_entry

    def convert(self, noise_categories, entry_list):
        """Parses the entries.

        @param noise_categories: values of the noise categories for all packets
        @param entry_list: entries bytes for all packets.
        @return:
        """
        all_decoded_entries = []

        for noise_category, entries in zip(noise_categories, entry_list):
            decoded_entries = []
            entries_stream = ConstBitStream(bytes=bytearray(entries))
            while True:
                try:
                    decoded_entry = self.__parse_entry(noise_category, entries_stream)
                    decoded_entries.append(decoded_entry)
                except ReadError:
                    break

            all_decoded_entries.append(decoded_entries)

        return all_decoded_entries


catalog_entries = SudaCatalogEntries()
