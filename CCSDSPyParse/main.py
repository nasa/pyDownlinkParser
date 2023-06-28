import io

import ccsdspy
import numpy as np
import pandas as pd
from collections import defaultdict
from ccsdspy.constants import BITS_PER_BYTE, PRIMARY_HEADER_NUM_BYTES
from CCSDSPyParse.parsers.config.ecm_config import ecm_packet
from CCSDSPyParse.parsers.config.suda_config import suda_packet


with open('data/suda_0409517390-0283787_cleansplit.dat', 'rb') as mixed_file:
    # dictionary mapping integer apid to BytesIO
    stream_by_apid = ccsdspy.utils.split_by_apid(mixed_file)

header_list = []

default_pkt = ccsdspy.VariableLength(
    [
        ccsdspy.PacketArray(
            name="unused", data_type="uint", bit_length=BITS_PER_BYTE, array_shape="expand"
        )
    ]
)

d = {
    0xb: suda_packet
}

output = {}

for apid, stream in stream_by_apid.items():
    print(apid)
    pkt = d.get(apid, default_pkt)
    output[apid] = pkt.load(stream)




