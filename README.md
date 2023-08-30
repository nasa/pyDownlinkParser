# pyDownLinkParser
This library parses binary files containing CCSDS packets of various structures (APID) and distribute them in pandas dataframes.


## Developers

### Requirements

#### Python 3.9

#### Create a virtual environment

For example in command line:

    python3 -m venv venv
    source venv/bin/activate

#### Install CCSDSPy

To install the latest version of CCSDSPy:
    
    pip install git+https://github.com/CCSDSPy/ccsdspy.git


#### Deploy the project

Clone the repository

Install the package

    pip install -e '.[dev]'
    pre-commit install && pre-commit install -t pre-push


Steps to run:
1) Clone the repo
2) In Runtime > Edit Config enter the Filename, Mode and Header Status (Like --file data/ecm_0406193095-0283151.DAT --bdsem --header)
4) For each mode, enter the filename using --file path_to_file, followed by --bdsem and --header depending on the mode
5) For ECM --bdsem --header, for RAW --bdsem, for MISE --header
6) Run the file downlink_to_excel.py to generate the Excel file with data for the respective file

Run an example:

    python src/pydownlinkparser/downlink_to_excel.py
