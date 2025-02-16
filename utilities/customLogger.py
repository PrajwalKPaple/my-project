import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        log_folder = "logs"
        log_file = os.path.join(log_folder, "automation.log")

        # Ensure the logs directory exists
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)
        logging.basicConfig(filename='.\\logs\\automation.log',
                        format='%(asctime)s: %(levelname)s: %(message)s', datefmt = '%m/%d/%Y %I:%M:%S %p'
                        )
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

