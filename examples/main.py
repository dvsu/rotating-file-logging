import os
import sys
import logging
from logging.handlers import TimedRotatingFileHandler
from time import sleep
from firstmodule import FirstClass
from secondmodule import SecondClass


PATH = "logs/log"
LOG_FORMAT = '%(asctime)s.%(msecs)03d %(levelname)s [MODULE] %(module)s [FUNCTION] %(funcName)s - %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


def filename_renamer(filename):
    # get the full path of logs directory
    dir_path = os.path.dirname(filename)

    # get the original file name
    file_name = os.path.basename(filename)
    
    # the file does not have any format at the beginning. Append ".log" to convert it into log file
    # Next, join the full path of logs directory with the renamed file
    renamed = os.path.join(dir_path, f"{file_name.split('.')[-1]}.log")

    return renamed


# The log handler will first store the most recent logs in PATH. 
# It will then create a new log file appended with given suffix
# and move the log lines that are currently stored in PATH to the new file periodically.
log_handler = TimedRotatingFileHandler(PATH, when="M", interval=1)
log_handler.setFormatter(logging.Formatter(LOG_FORMAT,datefmt=DATE_FORMAT))
log_handler.suffix = "%Y-%m-%dT%H-%M-%SZ"
log_handler.namer = filename_renamer

# Make the logger available globally by giving it a name
logger = logging.getLogger("main_logger")
logger.addHandler(log_handler)
logger.setLevel(logging.INFO)


if __name__ == "__main__":
    
    fc = FirstClass()
    sc = SecondClass()

    fc.run()
    sc.run()

    # Both threads will run and log continuously in the background.
    # The while loop below is added to ensure the program does not end, i.e.
    # keeping the threads alive.
    while True:
        try:
            sleep(10)

        except KeyboardInterrupt:
            sys.exit(1)