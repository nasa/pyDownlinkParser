import argparse
import os.path
import pandas as pd
from pydownlinkparser.remove_non_ccsds_headers import strip_non_ccsds_headers
from pydownlinkparser.parse_ccsds_downlink import parse_ccsds_file


def get_parser():
    parser = argparse.ArgumentParser(description="Parse Files")
    parser.add_argument("--file", type=str, required=True, help="Input File")
    parser.add_argument("--bdsem", action="store_true", help="Mode BDSEM")
    parser.add_argument("--header", action="store_true", help="Header Status")
    return parser


def export_dfs_to_xlsx(dfs, filename1):
    with pd.ExcelWriter(filename1) as writer:
        for name, df in dfs.items():
            df.to_excel(writer, sheet_name=name, index=True)


def export_ccsds_to_excel(ccsds_file, output_filename):
    dfs = parse_ccsds_file(ccsds_file)
    export_dfs_to_xlsx(dfs, output_filename)


def main():
    parser = get_parser()
    args = parser.parse_args()

    ccsds_file = strip_non_ccsds_headers(args.file, args.bdsem, args.header)

    file_base, _ = os.path.splitext(args.file)
    xlsx_filename = file_base + ".xlsx"
    export_ccsds_to_excel(ccsds_file, xlsx_filename)


main()
