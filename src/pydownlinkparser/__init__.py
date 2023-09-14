"""Generic code to parse a downlink binary file encoded using CCSDS."""
import os
from logging.config import fileConfig

conf_file_dir = os.path.dirname(os.path.abspath(__file__))
fileConfig(os.path.join(conf_file_dir, "logger.conf"))
