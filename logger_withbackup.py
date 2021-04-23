import os
import sys
import logging
from logging.handlers import TimedRotatingFileHandler
from time import sleep


PATH = "logs/log"
LOG_FORMAT = '%(asctime)s %(levelname)s [MODULE] %(module)s [FUNCTION] %(funcName)s - %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

# The log handler will first store the most recent logs in PATH. 
# After 30 seconds, it will create a new log file appended with given suffix
# and move the log lines that are currently stored in PATH to the new file.
# It will repeat the process, and at the same time, keeping track on 
# number of log files created. If it exceeds the backupCount, it will
# periodically delete the oldest files and keep the most recent 3 files.
#
# Note: using "namer" or "suffix" attribute seems to change the behavior of "backupCount"
#       i.e. "backupCount" is somehow ignored if either "namer" or "suffix" is used.
#       As the result, old logs will not be deleted
#
# In this example, the file naming is left as default to prevent unexpected behavior

log_handler = TimedRotatingFileHandler(PATH, when="M", interval=1, backupCount=3)
log_handler.setFormatter(logging.Formatter(LOG_FORMAT,datefmt=DATE_FORMAT))

logger = logging.getLogger()
logger.addHandler(log_handler)
logger.setLevel(logging.INFO)


if __name__ == "__main__":
    
    counter = 0
    # Keep logging every 10 seconds
    while True:
        try:
            logger.info(f"Logging count {counter}")
            counter += 1
            sleep(10)

        except KeyboardInterrupt:
            sys.exit(1)