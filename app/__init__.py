import argparse
import logging
from logging.handlers import RotatingFileHandler
import os
from config import Config

parser = argparse.ArgumentParser(allow_abbrev=False, description="A tool to create word clouds from a bunch of URLs")
parser.add_argument('-u', '--url',
                    dest='url',
                    type=str,
                    help='Give URL to obtain word cloud',
                    required=True)
args = parser.parse_args()

# Configure Logging

if not os.path.exists('logs'):
    os.mkdir('logs')

if not os.path.exists('outputs'):
    os.mkdir('outputs')

# create logger with 'spam_application'
logger = logging.getLogger('cyber_cloud')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
file_handler = logging.FileHandler('logs/{}'.format(Config.LOG_FILENAME))
file_handler.setLevel(Config.FILE_LOGGING_LEVEL)
# create console handler with a higher log level
console_handler = logging.StreamHandler()
console_handler.setLevel(Config.CONSOLE_LOGGING_LEVEL)
# create formatter and add it to the handlers
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
console_formatter = logging.Formatter('%(levelname)s: %(message)s')
# console_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
console_handler.setFormatter(console_formatter)
# add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.debug('Cyber Cloud app has started')
logger.info('Cyber Cloud app has started')
