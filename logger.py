import logging
import sys

# get logger: returns a logger instance
logger = logging.getLogger()

# formatter: add options to the formatting, ie which fields, etc ...
formatter = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s - %(message)s"
)

# create hanlders: specifies the output of the logger
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)

# add handler(s) to the logger
logger.handlers = [stream_handler]

# set the level of the logger: INFO, DEBUG, WARN, ERROR, CRITICAL
logger.setLevel(logging.INFO)