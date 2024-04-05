"""Packet structure for the SuDa events."""
from copy import copy
from enum import Enum

import ccsdspy

from .event_wf_metadata import METADATA_FIELDS
from .rice_decompressor_converter import RICEDecompressor

wf_subpacket_types = Enum("wf_subpacket_types", ["DATA", "METADATA"])

CONVERTER_INPUT_FIELDS = ("SCI0TYPE", "SCI0FRAG", "data")
CONVERTER_OUTPUT_FIELD = "decompressed_data"


class SudaEventWFPacketStructure(ccsdspy.VariableLength):
    """SUDA event waveform packet definition."""

    start_fields = [
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
        ccsdspy.PacketField(name="SCI0TIMEFINE", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(name="SCI0TIMECOARSE", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(name="SCI0SPARE2", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="SCI0SPARE3", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(name="SCI0SPARE4", bit_length=32, data_type="uint"),
    ]

    end_fields = [
        ccsdspy.PacketField(name="SYNCSCI0PKT", bit_length=16, data_type="uint"),
        ccsdspy.PacketField(name="CRCSCI0PKT", bit_length=16, data_type="uint"),
    ]

    def __init__(self, type: wf_subpacket_types = None):
        """Constructor."""
        if type == wf_subpacket_types.METADATA:
            middle_fields = METADATA_FIELDS
        else:
            middle_fields = [
                ccsdspy.PacketArray(
                    name="data", data_type="uint", bit_length=8, array_shape="expand"
                )
            ]

        fields = copy(self.start_fields)
        fields.extend(middle_fields)
        fields.extend(self.end_fields)

        super().__init__(fields)

        if type == wf_subpacket_types.DATA:
            self.add_converted_field(
                CONVERTER_INPUT_FIELDS, CONVERTER_OUTPUT_FIELD, RICEDecompressor()
            )

    def set_alt_inputs(self, df_dict: dict):
        """Add additional inputs needed by the converters."""
        if "1424.event_wf_transmit_metadata" in df_dict:
            self._converters[CONVERTER_INPUT_FIELDS][1].set_pre_post(
                df_dict["1424.event_wf_transmit_metadata"]
            )


event_wf_transmit = SudaEventWFPacketStructure()
event_wf_transmit.name = "event_wf_transmit"
event_wf_transmit.apid = 1424


def is_metadata(decision_value):
    """Identify which packet APID 1424 is an event header (metadata)."""
    return decision_value == 0x1


event_wf_transmit.decision_field = "SCI0TYPE"
event_wf_transmit.decision_fun = is_metadata


event_wf_transmit_metadata = SudaEventWFPacketStructure(
    type=wf_subpacket_types.METADATA
)
event_wf_transmit_metadata.name = "event_wf_transmit_metadata"
event_wf_transmit_metadata.apid = 1424
event_wf_transmit_metadata.sub_apid = True

event_wf_transmit_data = SudaEventWFPacketStructure(type=wf_subpacket_types.DATA)
event_wf_transmit_data.name = "event_wf_transmit_data"
event_wf_transmit_data.apid = 1424
event_wf_transmit_data.sub_apid = False

# NOT USED
# TODO: need to check what APID it is associated with
# event_wf_fetch = SudaEventWFPacketStructure()
# event_wf_fetch.name = "event_wf_fetch"
# event_wf_fetch.apid = 1424
# event_wf_fetch.sub_apid = True
