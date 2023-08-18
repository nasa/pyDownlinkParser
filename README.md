# pyDownLinkParser
This library parses binary files containing CCSDS packets of various structures (APID) and distribute them in pandas dataframes.


## Developers

### Requirements

#### Python 3.9

#### Create a virtual environment

For example in command line:

    python3 -m venv venv
    source venv/bin/activate


#### Install the latest version of CCSDSPY.

    git clone https://github.com/CCSDSPy/ccsdspy.git
    cd ccsdspy
    pip install .


#### Deploy the project

Clone the repository

Install the package

    pip install -e '.[dev]'
    pre-commit install && pre-commit install -t pre-push

Run an example:

    python src/pydownlinkparser/main.py

Steps to run:
1) Clone the repo
2) In Runtime > Edit Config enter the Filename, Mode and Header Status (Like --file data/ecm_0406193095-0283151.DAT --mode BDSEM --header Y)
3) Available Modes - BDSEM, RAW; Headers - Y/N
4) For ECM, mode - BDSEM, header - Y, For Suda, mode - BDSEM, header - N, for MISE, mode - RAW, header - Y

For example:

   python src/
