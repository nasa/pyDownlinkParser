"""CCSDS parser for binary file with multiple APIDs."""
from __future__ import annotations

import io
import logging

import ccsdspy
import crccheck
import numpy as np
import pandas as pd
from pydownlinkparser.europa_clipper.apid_packet_structures import apid_multi_pkt
from pydownlinkparser.europa_clipper.apid_packet_structures import apid_packets
from pydownlinkparser.util import default_pkt

logger = logging.getLogger(__name__)


class ParsedDFs(dict):
    """Dictionary of parsed dataframes. The dictionary has a structure so that values can be dictionaries."""

    def add_as_leaf(self, name: str, df: ParsedDFs | pd.DataFrame):
        """Add the dictionary as the deepest value for the given name."""
        if name in self.keys():
            self[name].add_as_leaf(name, df)
        else:
            self[name] = df


class CCSDSParsingException(Exception):
    """CCSDS packet parsing Exception."""

    pass


class CalculatedChecksum(ccsdspy.converters.Converter):
    """Converter which calculates a CRC checksum from a parsed packet and compare it with the one found in the packet."""

    CRC = crccheck.crc.Crc16CcittFalse
    JUMBO_CRC = crccheck.crc.Crc32Mpeg2
    JUMBO_TLM_PKT_LEN_BYTES = 4089  # not including the CCSDS header

    def __init__(self):
        """Initialization."""
        pass

    @classmethod
    def calculate_crc(
        cls,
        ccsds_version_number,
        ccsds_packet_type,
        ccsds_secondary_flag,
        ccsds_apid,
        ccsds_sequence_flag,
        ccsds_sequence_count,
        ccsds_packet_length,
        body,
    ):
        """Calculate one CRC from the parsed fields of one packet.

        Parsed fields must be the CCSDS header and one body excluding the CRC at the end of the packet.
        """
        pkt_header_bit_string = ""
        # TODO re-use header field length in ccsdspy packet_types.py
        pkt_header_bit_string += "{0:03b}".format(ccsds_version_number)
        pkt_header_bit_string += "{0:01b}".format(ccsds_packet_type)
        pkt_header_bit_string += "{0:01b}".format(ccsds_secondary_flag)
        pkt_header_bit_string += "{0:011b}".format(ccsds_apid)
        pkt_header_bit_string += "{0:02b}".format(ccsds_sequence_flag)
        pkt_header_bit_string += "{0:014b}".format(ccsds_sequence_count)
        pkt_header_bit_string += "{0:016b}".format(ccsds_packet_length)
        pkt_bytearray = [
            int(pkt_header_bit_string[i : i + 8], 2)
            for i in range(0, len(pkt_header_bit_string), 8)
        ]
        pkt_bytearray += body.tolist()

        crc = (
            cls.JUMBO_CRC
            if ccsds_packet_length > cls.JUMBO_TLM_PKT_LEN_BYTES
            else cls.CRC
        )
        return crc.calc(pkt_bytearray)

    def convert(
        self,
        ccsds_version_number_array,
        ccsds_packet_type_array,
        ccsds_secondary_flag_array,
        ccsds_apid_array,
        ccsds_sequence_flag_array,
        ccsds_sequence_count_array,
        ccsds_packet_length_array,
        body_array,
    ):
        """Converter to add a calculated CRC to the parsed packets.

        @param ccsds_version_number_array: from the CCSDS header
        @param ccsds_packet_type_array: from the CCSDS header
        @param ccsds_secondary_flag_array: from the CCSDS header
        @param ccsds_apid_array: from the CCSDS header
        @param ccsds_sequence_flag_array: from the CCSDS header
        @param ccsds_sequence_count_array: from the CCSDS header
        @param ccsds_packet_length_array: from the CCSDS header
        @param body_array: body of the packet, without the trailing CRC.
        @return: the array of calculated CRCs.
        """
        calculated_crc_array = []

        for (
            ccsds_version_number,
            ccsds_packet_type,
            ccsds_secondary_flag,
            ccsds_apid,
            ccsds_sequence_flag,
            ccsds_sequence_count,
            ccsds_packet_length,
            body,
        ) in zip(
            ccsds_version_number_array,
            ccsds_packet_type_array,
            ccsds_secondary_flag_array,
            ccsds_apid_array,
            ccsds_sequence_flag_array,
            ccsds_sequence_count_array,
            ccsds_packet_length_array,
            body_array,
        ):
            crc = self.calculate_crc(
                ccsds_version_number,
                ccsds_packet_type,
                ccsds_secondary_flag,
                ccsds_apid,
                ccsds_sequence_flag,
                ccsds_sequence_count,
                ccsds_packet_length,
                body,
            )
            calculated_crc_array.append(crc)

        return calculated_crc_array


def calculate_crc(f, crc_size_bytes=2):
    """Calculate a CRC for each packet so to compare it with the CRC sent at the end of the packets."""
    pkt = ccsdspy.VariableLength(
        [
            ccsdspy.PacketArray(
                name="body",
                data_type="uint",
                bit_length=8,
                array_shape="expand",  # makes the body field expand
            ),
            ccsdspy.PacketField(
                name="checksum_real", data_type="uint", bit_length=8 * crc_size_bytes
            ),
        ]
    )

    input_fields = [
        "CCSDS_VERSION_NUMBER",
        "CCSDS_PACKET_TYPE",
        "CCSDS_SECONDARY_FLAG",
        "CCSDS_APID",
        "CCSDS_SEQUENCE_FLAG",
        "CCSDS_SEQUENCE_COUNT",
        "CCSDS_PACKET_LENGTH",
        "body",
    ]
    pkt.add_converted_field(
        input_fields,
        "checksum_calculated",
        CalculatedChecksum(),
    )

    parsed_result = pkt.load(f, include_primary_header=True, reset_file_obj=True)

    # check that the calculated checksum and the one found in the packet are the same
    if np.all(parsed_result["checksum_real"] == parsed_result["checksum_calculated"]):
        # return the found checksum for further comparisons
        return parsed_result["checksum_real"]
    else:
        raise CCSDSParsingException(
            "The CRC calculated does not match the CRC read in the packet "
        )


def get_sub_packet_keys(parsed_apids, sub_apid: dict):
    """Identify sub-packet keys when single APId does not have consistent packet structures."""
    decision_fun = sub_apid["decision_fun"]
    if "decision_field" in sub_apid:
        decision_field = sub_apid["decision_field"]
        return [
            decision_fun(decision_value)
            for decision_value in list(parsed_apids[decision_field])
        ]
    else:
        first_key = list(parsed_apids.keys())[0]
        return [decision_fun() for _ in range(0, len(parsed_apids[first_key]))]


def distribute_packets(keyss, stream1):
    """Distribute binary stream into multiple binary stream with consistent sub-packet structures.

    Used when single APID does not have consistent packet structure.
    """
    buffers = {}
    rows = ccsdspy.utils.split_packet_bytes(stream1)
    for i in range(0, len(keyss)):
        if keyss[i] not in buffers:
            buffers[keyss[i]] = bytes()
        buffers[keyss[i]] += rows[i]
    buffers = {k: io.BytesIO(v) for k, v in buffers.items()}
    return buffers


def parse_ccsds_file(ccsds_file: str):
    """Parse a pure CCSDS binary file (only CCSDS packets)."""
    stream_by_apid = ccsdspy.utils.split_by_apid(ccsds_file)
    dfs = ParsedDFs()
    for apid, streams in stream_by_apid.items():
        logger.info("Parse APID %s", apid)
        try:
            pkt = apid_packets.get(apid, default_pkt)
            parsed_apids = pkt.load(
                streams, include_primary_header=True, reset_file_obj=True
            )
            # TODO complete that development
            parsed_apids["calculated_crc"] = calculate_crc(streams)
            name = get_tab_name(apid, pkt, dfs.keys())
            if apid in apid_multi_pkt:
                dfs[name] = ParsedDFs()
                keys = get_sub_packet_keys(parsed_apids, apid_multi_pkt[apid])
                buffer = distribute_packets(keys, streams)
                for key, minor_pkt in apid_multi_pkt[apid]["pkts"].items():
                    logger.info(
                        "Parse sub-APID %s %s",
                        apid_multi_pkt[apid]["decision_fun"],
                        key,
                    )
                    if hasattr(minor_pkt, "set_alt_inputs"):
                        minor_pkt.set_alt_inputs(
                            dfs[name]
                        )  # add reference to previously parsed pkt in the same group
                    parsed_sub_apid = minor_pkt.load(
                        buffer[key], include_primary_header=True, reset_file_obj=True
                    )
                    inner_name = get_tab_name(apid, minor_pkt, dfs.keys())
                    parsed_sub_apid = cast_to_list(parsed_sub_apid)
                    parsed_sub_apid["calculated_crc"] = calculate_crc(buffer[key])
                    dfs[name][inner_name] = pd.DataFrame.from_dict(parsed_sub_apid)

            elif hasattr(pkt, "is_ancillary_of"):
                parent_pkt = pkt.is_ancillary_of
                # move downward, to make room for the ancillary parsed packet in the same dict
                parsed_dfs = ParsedDFs()
                if parent_pkt in dfs.keys():
                    if not isinstance(dfs[parent_pkt], ParsedDFs):
                        parsed_dfs[parent_pkt] = dfs[parent_pkt]
                        dfs[parent_pkt] = parsed_dfs
                    # else do nothing
                else:
                    dfs[parent_pkt] = parsed_dfs

                dfs[parent_pkt][name] = pd.DataFrame.from_dict(parsed_apids)
            else:
                try:
                    parsed_apids = cast_to_list(parsed_apids)
                    dfs.add_as_leaf(name, pd.DataFrame.from_dict(parsed_apids))
                except ValueError as e:
                    print(str(e))
        except AssertionError:
            logger.warning(
                "APID %i was not parseable because packet length inconsistent with CCSDS header description",
                apid,
            )
        except CCSDSParsingException as e:
            logger.warning("APID %i: %s", apid, str(e))

    return dfs


def get_tab_name(apid, pkt_def, existing_names):
    """Proposes a tab name for each APID or sub-packet structure of an APID.

    The tab name can be used as keys in the dictionary of DataFrames or as tab names in the Excel spreadsheet.

    @param apid: APID
    @param pkt_def: current packet definition.
     preferably, the packet definition has a "name" property which will be used to name the tab.
     If not available the name of the class implementing the packet structure definitionn is used.
    @param existing_names: already used names, to avoid duplicates. A counter is added to duplicate names.
    @return: a unique tab name for the current APID and packet structure definition.
    """
    if hasattr(pkt_def, "name"):
        name = f"{apid}.{pkt_def.name}"
    else:
        name = f"{apid}.{pkt_def.__class__.__name__}"
    # we need that in case the name is used twice so that data is not overridden
    n = 1
    while name in existing_names:
        name = f"{name} ({n})"
    return name


def cast_to_list(d):
    """Casts any multidimensional arrays to lists."""
    for key, value in d.items():
        if hasattr(value[0].__class__, "tolist"):
            value = [v.tolist() for v in value]
            d[key] = value

    return d
