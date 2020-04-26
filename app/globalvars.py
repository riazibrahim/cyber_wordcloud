from app import parser, args
from datetime import datetime
from wordcloud import STOPWORDS
from config import Config

# Define or initiate all global variables here
filename_prepend = datetime.now().strftime("%Y%m%d-%H%M%S")
url = args.url
urls_file = args.file
op_filename = args.output
stop_words = set(STOPWORDS)
if Config.ADDITIONAL_STOPWORDS is not None:
    for item in Config.ADDITIONAL_STOPWORDS:
        stop_words.add(item)
