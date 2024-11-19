"""Generate simulated datasets from CCSDS packet definition."""
from datetime import datetime
from typing import Union

import ccsdspy


def generate_test_file(
    packet_def: Union[ccsdspy.VariableLength, ccsdspy.FixedLength],
    output_file: str,
    aid: int,
    apid: int,
    packet_size_bytes: Union[int, list],  # constant value or range
    packet_count: int = 10,
    start_time: datetime = datetime(2010, 1, 1, 0, 0, 0),
    end_time: datetime = datetime(2010, 1, 1, 1, 0, 0),
    initial_packet_seq: int = 0,
    delta_time_seconds: int = 1.0,
    packet_version: int = 0,  # between in [0, 99]
):
    """Generate simulated dataset from a CCSDSpy packet definition.

    @param packet_def: packet definition as CCSDSpy object
    @param output_file: output file where the test data is going to be saved
    @param aid: AID for the data.
    @param apid: APID for the data. Warning will be raised if it does not match the APID of the packet definition.
    @param packet_size_bytes: size of the generated packet in bytes.
    @param packet_count: number of packets generated.
    @param start_time: datetime of the first generated packet
    @param end_time: datetime of the last generated packet
    @param initial_packet_seq: sequence count of the first generated packet
    @param delta_time_seconds: time in seconds between the generated packets
    @param packet_version: packet version used in the CCSDS packet header.
    @return:
    """
    fields = packet_def._fields

    data = {}

    packet_def.to_file(
        output_file,
        0,  # only support telemetry packets for now
        apid,
        1,  # always secondary header for now
        3,  # always 3 for now
        data,
    )
