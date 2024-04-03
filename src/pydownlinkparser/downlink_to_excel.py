"""Utility to convert a downlink CCSDS binary file to excel."""
import argparse
import os.path

import pandas as pd
from pydownlinkparser.parse_ccsds_downlink import parse_ccsds_file
from pydownlinkparser.remove_non_ccsds_headers import strip_non_ccsds_headers


def get_parser():
    """Parser for the command line utility."""
    parser = argparse.ArgumentParser(description="Parse Files")
    parser.add_argument("--file", type=str, required=True, help="Input File")
    parser.add_argument(
        "--bdsem",
        action="store_true",
        help="Mode BDSEM, with specific, non-CCSDS, packet wrappers, "
        "if not present, RAW mode is assumed, "
        "with other specific non CCSDS markers in betwwen packets",
    )

    parser.add_argument(
        "--pkt-header",
        action="store_true",
        help="When additional non CCSDS header are added between packets",
    )

    parser.add_argument(
        "--json-header",
        action="store_true",
        help="When a JSON ASCII header starts the file",
    )

    parser.add_argument(
        "--calculate-crc",
        action="store_true",
        help="Check if CRC in packet matches with the one calculateed, "
        "return the calculated CRC in the spreadsheet next to the one of the packet.",
    )

    return parser


def add_tab_to_xlsx(dfs, writer, name=""):
    """Add tab to excel writer from a dictionary, recursively.

    Only use the name in the leaf of the dictionary tree.

    @param dfs: dictionary (of dictionary) of pandas dataframes or single pandas dataframe
    @param writer: pandas.ExcelWriter
    @param name: name of the tab to be used, optional when
    @return: Nothing
    """
    if isinstance(dfs, dict):
        for name, df in dfs.items():
            add_tab_to_xlsx(df, writer, name=name)
    else:
        dfs.to_excel(writer, sheet_name=name, index=True)


def export_dfs_to_xlsx(dfs, filename1):
    """Export a dictionnary of pandas dataframes to an Excel file."""
    with pd.ExcelWriter(filename1) as writer:
        add_tab_to_xlsx(dfs, writer)


def export_ccsds_to_excel(ccsds_file, output_filename, do_calculate_crc):
    """Export a binary file of CCSDS packets into an Excel file."""
    dfs = parse_ccsds_file(ccsds_file, do_calculate_crc)
    export_dfs_to_xlsx(dfs, output_filename)


def main():
    """Command line interface to parse downlink binary file and export to Excel file."""
    parser = get_parser()
    args = parser.parse_args()

    with open(args.file, "rb") as f:

        ccsds_file = strip_non_ccsds_headers(
            f, args.bdsem, args.pkt_header, args.json_header
        )

        # to write the content of the file without non CCSDS code
        # with open("ecm_test.bin", "wb") as f:
        #    f.write(ccsds_file.read())

        file_base, _ = os.path.splitext(args.file)
        xlsx_filename = file_base + ".xlsx"
        export_ccsds_to_excel(ccsds_file, xlsx_filename, args.calculate_crc)


if __name__ == "__main__":
    main()
