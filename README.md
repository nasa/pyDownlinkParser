# pyDownLinkParser

This library parses binary files containing CCSDS packets of various structures (APID) and distribute them in pandas dataframes.

It is modular and configurable for multiple missions, but is being primarily developed for Europa-Clipper.

## Usage

Install:

    pip install pydownlinkparser

Use

    parse-downlink --file {your ccsds file}

See more options with:

    parse-downlink --help


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


#### Build and publish the package

Update the version number in file `setup.cfg`

Create a tag in the repostory

Build the project:

    python3 -m pip install --upgrade build
    python3 -m build


Publish the project:

    twine upload dist/*



## Acknowledgment

This package heavily relies on `ccsdspy` library (see https://github.com/CCSDSPy/ccsdspy).
