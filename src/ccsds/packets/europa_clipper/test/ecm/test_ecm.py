import os
import unittest

from pydownlinkparser import compare


class TestECMCase:
    def test_parse(self):
        local_dir = os.path.dirname(__file__)
        compare(local_dir, True, True, False, create_output=False)


if __name__ == "__main__":
    unittest.main()
