import os
import pickle

import pandas as pd
from pydownlinkparser import parse_ccsds_file
from pydownlinkparser import strip_non_ccsds_headers


def compare(
    local_dir: str,
    is_bdsem: bool,
    has_pkt_header: bool,
    has_json_header: bool,
    create_output: bool = False,
):

    input_file = os.path.join(local_dir, "in.bin")

    with open(input_file, "rb") as f:
        ccsds_file = strip_non_ccsds_headers(
            f, is_bdsem, has_pkt_header, has_json_header
        )
        dfs = parse_ccsds_file(ccsds_file)

    output_file = os.path.join(local_dir, "out.pickle")

    # save the result as needed
    if create_output:
        with open(output_file, "wb") as f:
            f.write(pickle.dumps(dfs))

    with open(output_file, "rb") as f:
        dfs_expected = pickle.load(f)

    recursive_compare(dfs, dfs_expected)


def recursive_compare(dfs, dfs_expected):
    """
    Compare embedded dictionnary of dictionnaries of panda dataframes. Compare the keys and the actual dataframes.
    None should be missing or
    @param dfs: dictionnary of dictionbaries of dataframe
    @param dfs_expected: expected dictionnary of dictionnaries
    @return: True is the pandas dataframe are identical at the same location as in the
    """
    for k, df in dfs.items():
        assert k in dfs_expected.keys()
        if isinstance(dfs_expected[k], dict):
            recursive_compare(df, dfs_expected[k])
        else:
            pd.testing.assert_frame_equal(df, dfs_expected[k])
        del dfs_expected[k]

    assert len(dfs_expected) == 0
