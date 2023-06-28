from setuptools import find_namespace_packages
from setuptools import setup

setup(
    name="pydownlinkparser",
    description="Parsing the packets using CCSDSPy",
    url="https://github-fn.jpl.nasa.gov/loubrieu/new_ppp",
    install_requires=[
        "ccsdspy~=1.1.1",
    ],
    extras_require={

    },
    package_data={

    },
    include_package_data=True,
    # All bin scripts should be named with snake_case convention and located in
    # the subpackage bin/ directory. Upon installation scripts will be
    # accessible via hyphenated names. E.g., "foo_bar.py" becomes "foo-bar"
    entry_points={},
)