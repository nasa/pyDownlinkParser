"""Utilities to test the packet parsing."""
import logging
import os
import pickle

import pandas as pd
from pydownlinkparser import parse_ccsds_file
from pydownlinkparser import strip_non_ccsds_headers

logger = logging.getLogger(__name__)


def compare(
    local_dir: str,
    is_bdsem: bool,
    has_pkt_header: bool,
    has_json_header: bool,
    create_output: bool = False,
):
    """Run paring and compare results with a reference.

    @param local_dir:
    @param is_bdsem:
    @param has_pkt_header:
    @param has_json_header:
    @param create_output:
    @return:
    """
    input_file = os.path.join(local_dir, "in.bin")

    with open(input_file, "rb") as f:
        ccsds_file = strip_non_ccsds_headers(
            f, is_bdsem, has_pkt_header, has_json_header
        )
        dfs = parse_ccsds_file(ccsds_file, do_calculate_crc=True)

    output_file = os.path.join(local_dir, "out.pickle")

    # save the result as needed
    if create_output:
        with open(output_file, "wb") as f:
            f.write(pickle.dumps(dfs))

    with open(output_file, "rb") as f:
        dfs_expected = pickle.load(f)

    recursive_compare(dfs, dfs_expected)


def recursive_compare(dfs, dfs_expected):
    """Compare embedded dictionary of dictionaries of panda dataframes. Compare the keys and the actual dataframes.

    None should be missing and all should match.
    @param dfs: dictionnary of dictionbaries of dataframe
    @param dfs_expected: expected dictionnary of dictionnaries
    @return: True is the pandas dataframe are identical at the same location as in the
    """
    for k, df in dfs.items():
        logger.info("Compare dataframe %s", k)
        assert k in dfs_expected.keys()
        if isinstance(dfs_expected[k], dict):
            recursive_compare(df, dfs_expected[k])
        else:
            pd.testing.assert_frame_equal(df, dfs_expected[k], check_dtype=False)
        del dfs_expected[k]

    assert len(dfs_expected) == 0
