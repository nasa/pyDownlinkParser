from new_ppp.src.pydownlinkparser.europa_clipper import remove_headers


def strip_non_ccsds_headers(filename: str, is_bdsem: bool, has_header: bool):
    if is_bdsem:
        if has_header:
            return remove_headers.parse_bdsem_with_headers(filename)
        else:
            return remove_headers.parse_bdsem_without_headers(filename)
    else:
        if has_header:
            return remove_headers.parse_raw_with_headers(filename)
        else:
            return filename
