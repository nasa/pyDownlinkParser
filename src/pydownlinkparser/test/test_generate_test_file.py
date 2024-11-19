import tempfile

import pytest
from ccsds.packets.europa_clipper.common.ec_packet import ec_regular_packet
from pydownlinkparser import generate_test_file


class TestGenerateTestFileCase:
    def test_generate_file(self):

        output_file = tempfile.TemporaryFile()

        generate_test_file(ec_regular_packet, output_file, 12345678, 1024, 48)
