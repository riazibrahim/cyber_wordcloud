import argparse
import logging
from logging.handlers import RotatingFileHandler
import os
from config import Config
import sys
import signal
from wordcloud import STOPWORDS

# Setup arguments
parser = argparse.ArgumentParser(allow_abbrev=False, description="A tool to create word clouds from a bunch of URLs")
url_or_list = parser.add_mutually_exclusive_group(required=True)
url_or_list.add_argument('-u', '--url',
                    dest='url',
                    type=str,
                    help='Give URL to obtain word cloud')
url_or_list.add_argument('-f', '--file',
                    dest='file',
                    type=str,
                    help='Give URLs in a file')

parser.add_argument('-o', '--output',
                    dest='output',
                    type=str,
                    help='Give output file name',
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
file_handler.setFormatter(file_formatter)
console_handler.setFormatter(console_formatter)
# add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.debug('Cyber Cloud app has started')


# Obtain stopwords
filename = 'stopwords.lst'
stopwords_from_file = []
try:
    with open(filename) as f:
        stopwords_from_file = f.read().splitlines()
        logger.debug('Stop words loaded from file {}\n'.format(stopwords_from_file))
except Exception as e:
    logger.warning('stopwords.lst could not be loaded {}. Continuing with default'.format(e))

if stopwords_from_file is not None:
    stopwords = set(STOPWORDS)
    for item in stopwords_from_file:
        stopwords.add(item)
else:
    stopwords = STOPWORDS


# Signal handler To exit on Ctrl+C
def signal_handler(sig, frame):
    print('\n\nYou pressed Ctrl+C! .. exiting..')
    sys.exit('Bye!')


signal.signal(signal.SIGINT, signal_handler)