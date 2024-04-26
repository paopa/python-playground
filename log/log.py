import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.setLevel(logging.DEBUG)

logging.warning("Watch out!")  # will print a message to the console
logging.info("I told you so")  # will not print anything
