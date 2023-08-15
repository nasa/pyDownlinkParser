# pyDownLinkParser
This library parses binary files containing CCSDS packets of various structures (APID) and distribute them in pandas dataframes.


## Developers

Clone the repository

Install the package

    pip install -e '.[dev]'

Run an example:

    python src/pydownlinkparser/main.py
    
Steps to run: 
1) Clone the repo
2) In Runtime > Edit Config enter the Filename, Mode and Header Status (Like --file data/ecm_0406193095-0283151.DAT --mode BDSEM --header Y)
3) Available Modes - BDSEM, RAW; Headers - Y/N
4) For ECM, mode - BDSEM, header - Y, For Suda, mode - BDSEM, header - N, for MISE, mode - RAW, header - Y
