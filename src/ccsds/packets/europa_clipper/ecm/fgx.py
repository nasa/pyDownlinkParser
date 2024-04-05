"""ECM FGX packet structures."""
import ccsdspy
from ccsdspy.converters import Converter


class BytesTo24BitInts(Converter):
    """Convert from array of bytes to arrays of 24bits (3 bytes) integer."""

    def __init__(self):
        """Does nothing."""
        pass

    def convert(self, field_array):
        """Convert list of arrays of bytes to list of arrays of int, each from 3 bytes."""
        fgx_channels_24bits_list = []
        for fgx_channels in field_array:
            fgx_channels_24bits = []
            for i in range(0, len(fgx_channels), 3):
                meas_3bytes = bytes(fgx_channels[i : i + 3])
                meas_int = int.from_bytes(meas_3bytes, "big", signed=True)
                fgx_channels_24bits.append(meas_int)
            fgx_channels_24bits_list.append(fgx_channels_24bits)
        return fgx_channels_24bits_list


class FGXPacketStructure(ccsdspy.VariableLength):
    """Flux Gate Packet Structure."""

    def __init__(self, sensor, frequency, apid):
        """Constructor.

        @param sensor: sensor is 1, 2 or 3
        @param frequency: is "low" or "high", low is for both high and max rates
        """
        super().__init__(
            [
                ccsdspy.PacketField(
                    name="Instrument SCLK Time second", bit_length=32, data_type="uint"
                ),
                ccsdspy.PacketField(
                    name="Instrument SCLK Time subsec", bit_length=16, data_type="uint"
                ),
                ccsdspy.PacketField(
                    name="Accountability ID", bit_length=32, data_type="uint"
                ),
                # shape is 3 bytes * 3 channels * number of samples
                # 255, 237, 147]
                ccsdspy.PacketArray(
                    name="FGX_CHANNELS_8bits",
                    data_type="uint",
                    bit_length=8,
                    array_shape="expand",
                ),
                ccsdspy.PacketField(name="FGx_-4.7VHK", bit_length=24, data_type="int"),
                ccsdspy.PacketField(name="FGx_+4.7VHK", bit_length=24, data_type="int"),
                ccsdspy.PacketField(name="FGx_2VREF", bit_length=24, data_type="int"),
                ccsdspy.PacketField(name="FGx_1VREF", bit_length=24, data_type="int"),
                ccsdspy.PacketField(name="FGx_DRV_SNS", bit_length=24, data_type="int"),
                ccsdspy.PacketField(name="FGx_OP_PRTA", bit_length=24, data_type="int"),
                ccsdspy.PacketField(name="FGx_FBX", bit_length=24, data_type="int"),
                ccsdspy.PacketField(name="FGx_FBY", bit_length=24, data_type="int"),
                ccsdspy.PacketField(name="FGx_FBZ", bit_length=24, data_type="int"),
                ccsdspy.PacketField(name="FGx_BPFX", bit_length=24, data_type="int"),
                ccsdspy.PacketField(name="FGx_BPFY", bit_length=24, data_type="int"),
                ccsdspy.PacketField(name="FGx_BPFZ", bit_length=24, data_type="int"),
                ccsdspy.PacketField(name="FGx_+4.7_I", bit_length=24, data_type="int"),
                ccsdspy.PacketField(name="FGx_-4.7_I", bit_length=24, data_type="int"),
                ccsdspy.PacketField(name="FGx_HK_CH14", bit_length=24, data_type="int"),
                ccsdspy.PacketField(name="FGx_HK_CH15", bit_length=24, data_type="int"),
                ccsdspy.PacketField(
                    name="Register 80", bit_length=16, data_type="uint"
                ),
                ccsdspy.PacketField(
                    name="PEC (CRC-16-CCITT)", bit_length=16, data_type="uint"
                ),
            ]
        )
        self.name = f"fg{sensor}_{frequency}"
        self.add_converted_field(
            "FGX_CHANNELS_8bits", "FGX_CHANNELS_24bits", BytesTo24BitInts()
        )
        self.apid = apid


fg1_low = FGXPacketStructure(1, "low", 1218)
fg1_high = FGXPacketStructure(1, "high", 1219)
fg2_low = FGXPacketStructure(2, "low", 1222)
fg2_high = FGXPacketStructure(2, "high", 1223)
fg3_low = FGXPacketStructure(3, "low", 1226)
fg3_high = FGXPacketStructure(3, "high", 1227)
