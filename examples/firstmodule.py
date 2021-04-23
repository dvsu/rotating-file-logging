import threading
import logging
from time import sleep


class FirstClass:

    def __init__(self):
        self.counter = 0
        self.logger = logging.getLogger("main_logger")

    def logging_text(self):
        while True:
            self.logger.info(f"Logging text from first module. Counter: {self.counter+1}")
            self.counter += 1
            sleep(5)

    def run(self):
        first_thread = threading.Thread(target=self.logging_text, daemon=True).start()
