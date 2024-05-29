"""Metadata fields used for all instruments."""
import ccsdspy

METADATA_FIELDS = [
    # secondary header
    ccsdspy.PacketField(name="MSCLK_Seconds", bit_length=32, data_type="uint"),
    ccsdspy.PacketField(name="Subseconds_Prezero", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="AID", bit_length=32, data_type="uint"),
    # ADP Metadata
    ccsdspy.PacketField(name="CTRL", bit_length=5, data_type="uint"),
    ccsdspy.PacketField(name="ADP_APID", bit_length=11, data_type="uint"),
    ccsdspy.PacketField(name="SCLK", bit_length=48, data_type="uint"),
    ccsdspy.PacketField(name="Source_Sequence_Count", bit_length=14, data_type="uint"),
    ccsdspy.PacketField(name="Spare", bit_length=2, data_type="uint"),
    ccsdspy.PacketField(name="Count", bit_length=32, data_type="uint"),
    # PEC
    ccsdspy.PacketField(name="PEC_CRC_16_CCITT", bit_length=16, data_type="uint"),
]
