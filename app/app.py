from wordcloud import WordCloud
import matplotlib.pyplot as plt
from app.globalvars import *
from multiprocessing.pool import ThreadPool
from config import Config
from app.utils import *
from app import stopwords
import sys
import re
from bs4 import BeautifulSoup
from collections import Counter

url_response_dict = {}
url_list = create_url_list()
threads_count = 1
chunk_size = 1

if len(url_list) > 1:
    threads_count = int(len(url_list) / 2) if int(
        len(url_list) / 2) < Config.MAX_THREAD_COUNT else Config.MAX_THREAD_COUNT
    chunk_size = int(len(url_list) / threads_count)

#TODO: Use tor for parallel execution
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
    content = BeautifulSoup(url_response_dict[key], "lxml").text
    content_list = content.split()
    words = []
    for item in content_list:
        sanitized_item = str(item).lower().strip('./,!;"\':)(“”&${}?')
        if not re.match('^[.0-9%-]+$', sanitized_item):
            words.append(sanitized_item)
        else:
            logger.debug('Junk number detected "{} ", moving on ...'.format(sanitized_item))
    logger.debug('Number of words sanitized is {}.. stopword needs to be applied'.format(len(words)))
    comment_words += " ".join(words)

logger.info("Generating the word cloud...")

word_cloud = WordCloud(width=800, height=800,
                       background_color='white',
                       stopwords=stopwords,
                       min_font_size=10).generate(comment_words)

plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(word_cloud)
plt.axis('off')
plt.tight_layout(pad=0)

logger.info("Saving the word cloud image to outputs folder...")
plt.savefig('outputs/{}.png'.format(op_filename))
