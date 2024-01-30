"""CCSDS parser for binary file with multiple APIDs."""
from __future__ import annotations

import copy
import io
import logging

import ccsdspy
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
            # copy the input stream because the load function alters it
            stream1 = copy.deepcopy(streams)
            pkt = apid_packets.get(apid, default_pkt)
            parsed_apids = pkt.load(streams, include_primary_header=True)
            name = get_tab_name(apid, pkt, dfs.keys())
            if apid in apid_multi_pkt:
                dfs[name] = ParsedDFs()
                keys = get_sub_packet_keys(parsed_apids, apid_multi_pkt[apid])
                buffer = distribute_packets(keys, stream1)
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
                        buffer[key], include_primary_header=True
                    )
                    inner_name = get_tab_name(apid, minor_pkt, dfs.keys())
                    parsed_sub_apid = cast_to_list(parsed_sub_apid)
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
