"""
Ce fichier crée un fichier journal aux fin de testes.
Toutes les actions sont consignées via ce fichier et dans
le fichier journal.
"""

import sys
import logging

class Monitor:
    def logger(self, name):
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        # create file handler to log even of module
        file_handler = logging.FileHandler(name + ".log", mode="w")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        # create console handler to log higher log level
        console_handler = logging.StreamHandler(stream=sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)

        # add the handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger

if __name__ == '__main__':
    
    monitor = Monitor()
    logger = monitor.logger(__name__)
    logger.debug("This is not monitor")