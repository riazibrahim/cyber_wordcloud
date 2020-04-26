from wordcloud import WordCloud
import matplotlib.pyplot as plt
from app.globalvars import *
from multiprocessing.pool import ThreadPool
from config import Config
from app.utils import *
import sys
import re
from bs4 import BeautifulSoup

logger.debug("{} stop words used are: {}".format(len(stop_words), stop_words))
url_response_dict = {}
url_list = create_url_list()
threads_count = int(len(url_list) / 2) if int(
        len(url_list) / 2) < Config.MAX_THREAD_COUNT else Config.MAX_THREAD_COUNT
chunk_size = int(len(url_list) / threads_count)

results = ThreadPool(Config.THREADS_COUNT).imap(fetch_url, url_list, chunksize=chunk_size)
for url, html, error, ip in results:
    if error is None:
        logger.debug("%r fetched -- ip used: %s" % (url, ip))
        # id = hashlib.md5(url.encode()).hexdigest()
        id = url
        url_response_dict.update({id: html})
    else:
        logger.info("Error fetching %r: %s : ip used %s" % (url, error, ip))
logger.debug('Number of dictionary items {}'.format(len(url_response_dict)))
logger.debug('The urls are \n{}'.format(url_response_dict.keys()))

comment_words = ''

logger.info("Extracting words from the html responses ...")

for key in url_response_dict:
    val = BeautifulSoup(url_response_dict[key], "lxml").text
    tokens = val.split()
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
    comment_words += " ".join(tokens)

logger.info("Generating the word cloud...")
word_cloud = WordCloud(width=800, height=800,
                      background_color='white',
                      stopwords=stop_words,
                      min_font_size=10).generate(comment_words)

plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(word_cloud)
plt.axis('off')
plt.tight_layout(pad=0)

logger.info("Saving the word cloud image to outputs folder...")
plt.savefig('outputs/{}.png'.format(op_filename))
