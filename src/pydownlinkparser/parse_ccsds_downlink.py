"""CCSDS parser for binary file with multiple APIDs."""
from __future__ import annotations

import gc
import io
import logging

import ccsdspy
import crccheck
import numpy as np
import pandas as pd
from pydownlinkparser.util import default_pkt

logger = logging.getLogger(__name__)


class CCSDSParsingException(Exception):
    """CCSDS packet parsing Exception."""

    pass


class CRCNotCalculatedError(Exception):
    """CRC Calculation exception."""

    pass


class CalculatedChecksum(ccsdspy.converters.Converter):
    """Converter which calculates a CRC checksum from a parsed packet and compare it with the one found in the packet.

    TODO: make something better, by supporting any packets as input...
    """

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

    try:
        parsed_result = pkt.load(f, include_primary_header=True, reset_file_obj=True)

        # check that the calculated checksum and the one found in the packet are the same
        if np.all(
            parsed_result["checksum_real"] == parsed_result["checksum_calculated"]
        ):
            # return the found checksum for further comparisons
            return parsed_result["checksum_real"]
        else:
            raise CCSDSParsingException(
                "The CRC calculated does not match the CRC read in the packet "
            )
    except IndexError:
        logger.warning("Unable to parse packet to calculate CRC")
        raise CRCNotCalculatedError("Unable to parse packet to calculate CRC")


def import_ccsds_packet_packages():
    """Import of the subpackages of ccsds.packets which are meant to contain the CCSDSpy packet definitions.

    Stolen from https://packaging.python.org/en/latest/guides/creating-and-discovering-plugins/#using-namespace-packages

    @return: the set of the imported packages
    """
    import importlib
    import pkgutil

    # TODO: use a constant for ccsds.packets
    import ccsds.packets  # noqa

    def iter_namespace(ns_pkg):
        return pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + ".")

    return {
        name: importlib.import_module(name)
        for finder, name, ispkg in iter_namespace(ccsds.packets)
    }


def get_packet_definitions():
    """Select packet definitions which will be parsed in the first round or second round, as a refinement for some APIDs.

    First round parsing: object instances of _BasePackets which have an `apid` but no `sub_apid`
    Second round parsing: object instances of _BasePackets which have an `apid` and a `sub_apid`
    """
    # TODO use the clasees defined in Packets.py to simply the handling of packets
    first_round_parsers = {}
    second_round_parsers = {}

    import_ccsds_packet_packages()

    for object in gc.get_objects():
        if isinstance(object, ccsdspy.packet_types._BasePacket) and hasattr(
            object, "apid"
        ):
            if hasattr(object, "sub_apid"):
                if object.apid not in second_round_parsers:
                    second_round_parsers[object.apid] = {}
                if "pkts" not in second_round_parsers[object.apid]:
                    second_round_parsers[object.apid]["pkts"] = {}
                second_round_parsers[object.apid]["pkts"][object.sub_apid] = object
            else:
                first_round_parsers[object.apid] = object
                if hasattr(object, "decision_fun"):
                    if object.apid not in second_round_parsers:
                        second_round_parsers[object.apid] = {}
                    second_round_parsers[object.apid]["pre_parser"] = object

    return first_round_parsers, second_round_parsers


def get_sub_packet_keys(parsed_apids, sub_apid: dict):
    """Identify sub-packet keys when single APId does not have consistent packet structures."""
    decision_fun = sub_apid["pre_parser"].decision_fun
    if hasattr(sub_apid["pre_parser"], "decision_field"):
        decision_field = sub_apid["pre_parser"].decision_field
        return [
            decision_fun(decision_value)
            for decision_value in list(parsed_apids[decision_field])
        ]
    else:
        # all the elements of the parsed_aids dictionary have
        # the same length which is the number of packet parsed.
        # we pick the first one to iterate on our packets.
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


def parse_ccsds_file(ccsds_file: str, do_calculate_crc: bool = False):
    """Parse a pure CCSDS binary file (only CCSDS packets)."""
    apid_packets, apid_multi_pkt = get_packet_definitions()
    logger.info("Split input file per APIDs")
    stream_by_apid = ccsdspy.utils.split_by_apid(ccsds_file)
    dfs = dict()
    for apid, streams in stream_by_apid.items():
        logger.info("Parse APID %s", apid)
        try:
            pkt = apid_packets.get(apid, default_pkt)
            parsed_apids = pkt.load(
                streams, include_primary_header=True, reset_file_obj=True
            )
            if do_calculate_crc:
                try:
                    parsed_apids["calculated_crc"] = calculate_crc(streams)
                except CRCNotCalculatedError as e:
                    logger.warning(str(e))
            name = get_tab_name(apid, pkt, dfs.keys())
            if apid in apid_multi_pkt:
                dfs[name] = dict()
                keys = get_sub_packet_keys(parsed_apids, apid_multi_pkt[apid])
                buffer = distribute_packets(keys, streams)
                for key, minor_pkt in apid_multi_pkt[apid]["pkts"].items():
                    logger.info(
                        "Parse sub-APID %s %s",
                        apid_multi_pkt[apid]["pre_parser"].decision_fun,
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
                    if do_calculate_crc:
                        try:
                            parsed_sub_apid["calculated_crc"] = calculate_crc(streams)
                        except CRCNotCalculatedError as e:
                            logger.warning(str(e))
                    dfs[name][inner_name] = pd.DataFrame.from_dict(parsed_sub_apid)
                    logger.info(
                        "%s/%s, found %i records.",
                        name,
                        inner_name,
                        dfs[name][inner_name].size,
                    )
            else:
                try:
                    parsed_apids = cast_to_list(parsed_apids)
                    current_df = pd.DataFrame.from_dict(parsed_apids)
                    dfs[name] = current_df
                    logger.info("%s, found %i records.", name, len(current_df))
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
