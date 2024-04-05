"""ECM Metadata packet structure."""
import ccsdspy


metadata_ecm = ccsdspy.VariableLength(
    [
        # secondary header
        ccsdspy.PacketField(name="MSCLK Seconds", bit_length=32, data_type="uint"),
        ccsdspy.PacketField(
            name="Subseconds Pre-zero", bit_length=16, data_type="uint"
        ),
        ccsdspy.PacketField(name="AID", bit_length=32, data_type="uint"),
        # ADP Metadata
        ccsdspy.PacketField(name="CTRL = START | END", bit_length=5, data_type="uint"),
        ccsdspy.PacketField(name="ADP Major APID", bit_length=5, data_type="uint"),
        ccsdspy.PacketField(name="ADP Minor APID", bit_length=6, data_type="uint"),
        ccsdspy.PacketField(name="SCLK", bit_length=48, data_type="uint"),
        ccsdspy.PacketField(
            name="Source Sequence Count", bit_length=14, data_type="uint"
        ),
        ccsdspy.PacketField(name="Spare", bit_length=2, data_type="uint"),
        ccsdspy.PacketField(
            name="CTRL==END ? Count : Spare", bit_length=32, data_type="uint"
        ),
        # PEC
        ccsdspy.PacketField(name="PEC (CRC-16-CCITT)", bit_length=16, data_type="uint"),
    ]
)
metadata_ecm.name = "adp_metadata_ecm"
metadata_ecm.apid = 1217
