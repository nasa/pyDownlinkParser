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


#### Deploy the project, for developers

Clone the repository

Install the package

    pip install -e '.[dev]'
    pre-commit install && pre-commit install -t pre-push

Run an example:

    python src/pydownlinkparser/downlink_to_excel.py

or

    parse-downlink --help

or

    parse-downlink --file ./data/ecm_mag_testcase6_cmds_split_out.log --bdsem --header
