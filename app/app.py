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
#
# logger.debug("{} stop words used are: {}".format(len(stop_words), stop_words))
# url_response_dict = {}
# url_list = create_url_list()
# threads_count = int(len(url_list) / 2) if int(
#         len(url_list) / 2) < Config.MAX_THREAD_COUNT else Config.MAX_THREAD_COUNT
# chunk_size = int(len(url_list) / threads_count)
#
# results = ThreadPool(Config.THREADS_COUNT).imap(fetch_url, url_list, chunksize=chunk_size)
# for url, html, error, ip in results:
#     if error is None:
#         logger.debug("%r fetched -- ip used: %s" % (url, ip))
#         # id = hashlib.md5(url.encode()).hexdigest()
#         id = url
#         url_response_dict.update({id: html})
#     else:
#         logger.info("Error fetching %r: %s : ip used %s" % (url, error, ip))
# logger.debug('Number of dictionary items {}'.format(len(url_response_dict)))
# logger.debug('The urls are \n{}'.format(url_response_dict.keys()))
#
# comment_words = ''
#
# logger.info("Extracting words from the html responses ...")
#
# for key in url_response_dict:
#     val = BeautifulSoup(url_response_dict[key], "lxml").text
#     tokens = val.split()
#     for i in range(len(tokens)):
#         tokens[i] = tokens[i].lower().strip('./,!;"\':)(“”&${}?')
#     comment_words += " ".join(tokens)
#
# sorted_tokens = [item for items, c in Counter(tokens).most_common()
#                                       for item in [items] * c]
# logger.debug('Words to be made into word cloud {} - contains stopwords'.format(sorted_tokens))
sorted_tokens = ['the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'at', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', '2020', 'march', 'march', 'march', 'march', 'march', 'march', 'march', 'march', 'march', 'march', 'march', 'march', 'march', 'march', 'march', 'march', 'march', 'march', 'march', 'march', 'march', 'march', 'march', 'march', 'march', 'march', 'march', 'march', 'march', 'march', 'march', 'march', 'march', 'march', 'march', 'march', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'that', 'is', 'is', 'is', 'is', 'is', 'is', 'is', 'is', 'is', 'is', 'is', 'is', 'is', 'is', 'is', 'is', 'is', 'is', 'is', 'is', 'is', 'is', 'is', 'is', 'is', 'is', 'is', 'is', 'is', 'is', 'is', 'is', 'is', 'is', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'shadowserver', 'shadowserver', 'shadowserver', 'shadowserver', 'shadowserver', 'shadowserver', 'shadowserver', 'shadowserver', 'shadowserver', 'shadowserver', 'shadowserver', 'shadowserver', 'shadowserver', 'shadowserver', 'shadowserver', 'shadowserver', 'shadowserver', 'shadowserver', 'shadowserver', 'shadowserver', 'shadowserver', 'shadowserver', 'shadowserver', 'shadowserver', 'shadowserver', 'shadowserver', 'shadowserver', 'shadowserver', 'shadowserver', 'shadowserver', 'on', 'on', 'on', 'on', 'on', 'on', 'on', 'on', 'on', 'on', 'on', 'on', 'on', 'on', 'on', 'on', 'on', 'on', 'on', 'on', 'on', 'on', 'on', 'on', 'on', 'on', 'on', 'on', 'on', 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'am', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', '16', 'this', 'this', 'this', 'this', 'this', 'this', 'this', 'this', 'this', 'this', 'this', 'this', 'this', 'this', 'this', 'this', 'this', 'this', 'this', 'this', 'this', 'this', 'you', 'you', 'you', 'you', 'you', 'you', 'you', 'you', 'you', 'you', 'you', 'you', 'you', 'you', 'you', 'you', 'you', 'you', 'you', 'you', 'it', 'it', 'it', 'it', 'it', 'it', 'it', 'it', 'it', 'it', 'it', 'it', 'it', 'it', 'it', 'it', 'it', 'it', 'it', 'have', 'have', 'have', 'have', 'have', 'have', 'have', 'have', 'have', 'have', 'have', 'have', 'have', 'have', 'have', 'have', 'have', 'have', 'but', 'but', 'but', 'but', 'but', 'but', 'but', 'but', 'but', 'but', 'but', 'but', 'but', 'but', 'but', 'but', 'but', 'but', 'be', 'be', 'be', 'be', 'be', 'be', 'be', 'be', 'be', 'be', 'be', 'be', 'be', 'be', 'be', 'be', 'from', 'from', 'from', 'from', 'from', 'from', 'from', 'from', 'from', 'from', 'from', 'from', 'from', 'from', 'from', 'from', 'they', 'they', 'they', 'they', 'they', 'they', 'they', 'they', 'they', 'they', 'they', 'they', 'they', 'they', 'they', 'pm', 'pm', 'pm', 'pm', 'pm', 'pm', 'pm', 'pm', 'pm', 'pm', 'pm', 'pm', 'pm', 'pm', 'pm', 'as', 'as', 'as', 'as', 'as', 'as', 'as', 'as', 'as', 'as', 'as', 'as', 'as', 'as', 'cisco', 'cisco', 'cisco', 'cisco', 'cisco', 'cisco', 'cisco', 'cisco', 'cisco', 'cisco', 'cisco', 'cisco', 'cisco', 'cisco', 'we', 'we', 'we', 'we', 'we', 'we', 'we', 'we', 'we', 'we', 'we', 'we', 'we', 'we', 'about', 'about', 'about', 'about', 'about', 'about', 'about', 'about', 'about', 'about', 'about', 'about', 'about', 'are', 'are', 'are', 'are', 'are', 'are', 'are', 'are', 'are', 'are', 'are', 'are', 'are', 'so', 'so', 'so', 'so', 'so', 'so', 'so', 'so', 'so', 'so', 'so', 'so', 'so', 'your', 'your', 'your', 'your', 'your', 'your', 'your', 'your', 'your', 'your', 'your', 'your', 'help', 'help', 'help', 'help', 'help', 'help', 'help', 'help', 'help', 'help', 'help', 'help', 'with', 'with', 'with', 'with', 'with', 'with', 'with', 'with', 'with', 'with', 'with', 'with', 'will', 'will', 'will', 'will', 'will', 'will', 'will', 'will', 'will', 'will', 'will', 'will', 'security', 'security', 'security', 'security', 'security', 'security', 'security', 'security', 'security', 'security', 'security', 'has', 'has', 'has', 'has', 'has', 'has', 'has', 'has', 'has', 'has', 'has', 'funding', 'funding', 'funding', 'funding', 'funding', 'funding', 'funding', 'funding', 'funding', 'funding', 'funding', 'or', 'or', 'or', 'or', 'or', 'or', 'or', 'or', 'or', 'or', 'or', 'can', 'can', 'can', 'can', 'can', 'can', 'can', 'can', 'can', 'can', 'can', 'by', 'by', 'by', 'by', 'by', 'by', 'by', 'by', 'by', 'by', 'by', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'their', 'their', 'their', 'their', 'their', 'their', 'their', 'their', 'their', 'their', 'their', 'our', 'our', 'our', 'our', 'our', 'our', 'our', 'our', 'our', 'our', 'our', 'not', 'not', 'not', 'not', 'not', 'not', 'not', 'not', 'not', 'not', 'not', 'organization', 'organization', 'organization', 'organization', 'organization', 'organization', 'organization', 'organization', 'organization', 'organization', 'been', 'been', 'been', 'been', 'been', 'been', 'been', 'been', 'been', 'been', 'was', 'was', 'was', 'was', 'was', 'was', 'was', 'was', 'was', 'was', 'when', 'when', 'when', 'when', 'when', 'when', 'when', 'when', 'when', 'when', 'data', 'data', 'data', 'data', 'data', 'data', 'data', 'data', 'data', 'data', 'would', 'would', 'would', 'would', 'would', 'would', 'would', 'would', 'would', 'would', 'out', 'out', 'out', 'out', 'out', 'out', 'out', 'out', 'out', 'out', 'if', 'if', 'if', 'if', 'if', 'if', 'if', 'if', 'if', 'if', 'malware', 'malware', 'malware', 'malware', 'malware', 'malware', 'malware', 'malware', 'malware', 'more', 'more', 'more', 'more', 'more', 'more', 'more', 'more', 'more', 'just', 'just', 'just', 'just', 'just', 'just', 'just', 'just', 'just', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'than', 'than', 'than', 'than', 'than', 'than', 'than', 'than', 'some', 'some', 'some', 'some', 'some', 'some', 'some', 'some', 'like', 'like', 'like', 'like', 'like', 'like', 'like', 'like', 'how', 'how', 'how', 'how', 'how', 'how', 'how', 'years', 'years', 'years', 'years', 'years', 'years', 'years', 'know', 'know', 'know', 'know', 'know', 'know', 'know', 'an', 'an', 'an', 'an', 'an', 'an', 'its', 'its', 'its', 'its', 'its', 'its', 'free', 'free', 'free', 'free', 'free', 'free', 'being', 'being', 'being', 'being', 'being', 'being', 'control', 'control', 'control', 'control', 'control', 'control', 'over', 'over', 'over', 'over', 'over', 'over', 'many', 'many', 'many', 'many', 'many', 'many', 'them', 'them', 'them', 'them', 'them', 'them', 'money', 'money', 'money', 'money', 'money', 'money', 'do', 'do', 'do', 'do', 'do', 'do', 'he', 'he', 'he', 'he', 'he', 'he', 'brian', 'brian', 'brian', 'brian', 'brian', 'brian', 'could', 'could', 'could', 'could', 'could', 'could', 'needs', 'needs', 'needs', 'needs', 'needs', 'internet', 'internet', 'internet', 'internet', 'internet', 'infected', 'infected', 'infected', 'infected', 'infected', 'computer', 'computer', 'computer', 'computer', 'computer', 'countries', 'countries', 'countries', 'countries', 'countries', 'network', 'network', 'network', 'network', 'network', 'here', 'here', 'here', 'here', 'here', 'time', 'time', 'time', 'time', 'time', 'hard', 'hard', 'hard', 'hard', 'hard', 'very', 'very', 'very', 'very', 'very', 'which', 'which', 'which', 'which', 'which', 'support', 'support', 'support', 'support', 'support', 'why', 'why', 'why', 'why', 'why', 'said', 'said', 'said', 'said', 'said', 'all', 'all', 'all', 'all', 'all', 'don’t', 'don’t', 'don’t', 'don’t', 'don’t', 'there', 'there', 'there', 'there', 'there', 'should', 'should', 'should', 'should', 'should', 'what', 'what', 'what', 'what', 'what', 'hacked', 'hacked', 'hacked', 'hacked', 'hacked', 'shame', 'shame', 'shame', 'shame', 'shame', 'tax', 'tax', 'tax', 'tax', 'tax', 'me', 'me', 'me', 'me', 'where', 'where', 'where', 'where', 'government', 'government', 'government', 'government', 'new', 'new', 'new', 'new', 'now', 'now', 'now', 'now', 'isps', 'isps', 'isps', 'isps', 'systems', 'systems', 'systems', 'systems', 'national', 'national', 'national', 'national', 'certs', 'certs', 'certs', 'certs', 'federal', 'federal', 'federal', 'federal', 'law', 'law', 'law', 'law', 'enforcement', 'enforcement', 'enforcement', 'enforcement', 'operations', 'operations', 'operations', 'operations', 'botnet', 'botnet', 'botnet', 'botnet', 'one', 'one', 'one', 'one', 'any', 'any', 'any', 'any', 'long', 'long', 'long', 'long', 'alliance', 'alliance', 'alliance', 'alliance', 'make', 'make', 'make', 'make', 'may', 'may', 'may', 'may', 'world', 'world', 'world', 'world', '–', '–', '–', '–', 'work', 'work', 'work', 'work', 'blog', 'blog', 'blog', 'blog', 'reports', 'reports', 'reports', 'reports', 'perlotto', 'perlotto', 'perlotto', 'perlotto', 'bill', 'bill', 'bill', 'bill', 'it’s', 'it’s', 'it’s', 'it’s', 'does', 'does', 'does', 'does', 'cyber', 'cyber', 'cyber', 'cyber', 'into', 'into', 'into', 'into', 'under', 'under', 'under', 'under', 'everyone', 'everyone', 'everyone', 'everyone', 'thanks', 'thanks', 'thanks', 'thanks', 'cybersecurity', 'cybersecurity', 'cybersecurity', 'cybersecurity', 'my', 'my', 'my', 'my', 'doing', 'doing', 'doing', 'doing', 'public', 'public', 'public', 'public', 'had', 'had', 'had', 'had', 'please', 'please', 'please', 'please', 'get', 'get', 'get', 'get', 'sources', 'sources', 'sources', 'sources', 'his', 'his', 'his', 'his', 'without', 'without', 'without', 'without', '17', '17', '17', '17', 'rich', 'rich', 'rich', 'rich', 'pc', 'pc', 'pc', 'pc', 'bot', 'bot', 'bot', 'containment', 'containment', 'containment', 'unit', 'unit', 'unit', 'krebs', 'krebs', 'krebs', 'anyone', 'anyone', 'anyone', 'service', 'service', 'service', 'image', 'image', 'image', 'daily', 'daily', 'daily', 'emergency', 'emergency', 'emergency', 'sinkholing', 'sinkholing', 'sinkholing', 'domain', 'domain', 'domain', 'way', 'way', 'way', 'these', 'these', 'these', 'spam', 'spam', 'spam', 'domains', 'domains', 'domains', 'while', 'while', 'while', 'those', 'those', 'those', 'themselves', 'themselves', 'themselves', 'others', 'others', 'others', 'online', 'online', 'online', 'needed', 'needed', 'needed', 'people', 'people', 'people', 'company', 'company', 'company', 'supporting', 'supporting', 'supporting', 'effort', 'effort', 'effort', 'industry', 'industry', 'industry', 'organizations', 'organizations', 'organizations', 'important', 'important', 'important', 'center', 'center', 'center', 'millions', 'millions', 'millions', 'who', 'who', 'who', 'currently', 'currently', 'currently', 'foundation', 'foundation', 'foundation', 'day', 'day', 'day', 'model', 'model', 'model', 'most', 'most', 'most', 'never', 'never', 'never', 'problem', 'problem', 'problem', 'need', 'need', 'need', 'shadowserver’s', 'shadowserver’s', 'shadowserver’s', 'ago', 'ago', 'ago', 'believe', 'believe', 'believe', 'services', 'services', 'services', 'servers', 'servers', 'servers', 'cisco’s', 'cisco’s', 'cisco’s', 'comments', 'comments', 'comments', 'cause', 'cause', 'cause', 'donated', 'donated', 'donated', 'style', 'style', 'style', 'such', 'such', 'such', 'were', 'were', 'were', 'maybe', 'maybe', 'maybe', 'google', 'google', 'google', 'step', 'step', 'step', 'situation', 'situation', 'situation', 'benefit', 'benefit', 'benefit', 'posts', 'posts', 'posts', 'much', 'much', 'much', 'won’t', 'won’t', 'won’t', 'off', 'off', 'off', 'able', 'able', 'able', 'i’m', 'i’m', 'i’m', 'even', 'even', 'even', 'better', 'better', 'better', 'few', 'few', 'few', 'you’re', 'you’re', 'you’re', 'gates', 'gates', 'gates', 'investment', 'investment', 'investment', 'planet', 'planet', 'planet', 'income', 'income', 'income', 'site', 'site', 'site', 'uses', 'uses', 'uses', 'fraud', 'fraud', 'fraud', 'web’s', 'web’s', 'advertisement', 'advertisement', 'subscribe', 'subscribe', 'rss', 'rss', 'follow', 'follow', 'news', 'news', 'who’s', 'who’s', 'hit', 'hit', 'ghostbusters', 'ghostbusters', 'likely', 'likely', 'menace', 'menace', 'york', 'york', 'something', 'something', 'danger', 'danger', 'happening', 'happening', 'cyberspace', 'cyberspace', 'shadowserver.org', 'shadowserver.org', 'providers', 'providers', 'botnets', 'botnets', 'source', 'source', 'either', 'either', '4,600', '4,600', '107', '107', 'response', 'response', 'teams', 'teams', '136', '136', 'fbi', 'fbi', 'other', 'other', 'officials', 'officials', 'used', 'used', 'sinkhole', 'sinkhole', 'redirecting', 'redirecting', 'traffic', 'traffic', 'experts', 'experts', 'set', 'set', 'kind', 'kind', 'legal', 'legal', 'resources', 'resources', 'attack', 'attack', 'microsoft', 'microsoft', 'researchers', 'researchers', 'good', 'good', 'guys', 'guys', 'sinkholed', 'sinkholed', 'again', 'again', 'someone', 'someone', 'manage', 'manage', 'side', 'side', 'things', 'things', 'primarily', 'primarily', 'funded', 'funded', '15', '15', 'stop', 'stop', 'say', 'say', 'exploring', 'exploring', 'forward', 'forward', 'cost', 'cost', '400,000', '400,000', 'protection', 'protection', 'businesses', 'businesses', 'corporate', 'corporate', 'staff', 'staff', 'own', 'own', 'devices', 'devices', 'risk', 'risk', 'post', 'post', 'today', 'today', 'financial', 'financial', 'constituents', 'constituents', 'every', 'every', 'richard', 'richard', 'multiple', 'multiple', 'entities', 'entities', 'because', 'because', 'paid', 'paid', 'pretty', 'pretty', 'quietly', 'quietly', 'extremely', 'extremely', 'sell', 'sell', 'victim', 'victim', 'huge', 'huge', 'product', 'product', 'find', 'find', 'cybercrime', 'cybercrime', 'immediately', 'immediately', 'end', 'end', 'migration', 'migration', 'california', 'california', 'interested', 'interested', 'update', 'update', 'comment', 'comment', 'entry', 'entry', '2.0', '2.0', '36', '36', 'hope', 'hope', 'fully', 'fully', 'start', 'start', 'sure', 'sure', 'team', 'team', 'phil', 'phil', 'thought', 'thought', 'dhs', 'dhs', 'ought', 'ought', 'fund', 'fund', 'wouldn’t', 'wouldn’t', 'management', 'management', 'infrastructure', 'infrastructure', 'always', 'always', 'infosec', 'infosec', 'pro', 'pro', '23', '23', 'knew', 'knew', 'well', 'well', 'accepting', 'accepting', 'true', 'true', 'lot', 'lot', 'effective', 'effective', 'before', 'before', 'hey', 'hey', 'date', 'date', 'until', 'until', 'centre', 'centre', 'roel', 'roel', 'philippeth', 'philippeth', 'understand', 'understand', 'same', 'same', 'container', 'container', 'prometheus', 'prometheus', 'program', 'program', 'uk', 'uk', 'think', 'think', 'try', 'try', 'certainly', 'certainly', 'funds', 'funds', 'cisco…..well', 'cisco…..well', 'bailing', 'bailing', 'them…', 'them…', 'thinking', 'thinking', 'continue', 'continue', 'mission', 'mission', 'simply', 'simply', 'made', 'made', 'see', 'see', 'actually', 'actually', 'etc', 'etc', 'remember', 'remember', 'started', 'started', 'volunteers', 'volunteers', 'current', 'current', 'cash', 'cash', 'far', 'far', 'suddenly', 'suddenly', 'hopefully', 'hopefully', 'too', 'too', 'course', 'course', 'instead', 'instead', 'bit', 'bit', 'helps', 'helps', 'anything', 'anything', 'there’s', 'there’s', 'ask', 'ask', 'jon', 'jon', 'behave', 'behave', 'responsibly', 'responsibly', 'following', 'following', 'strategic', 'strategic', 'philanthropy', 'philanthropy', 'monies', 'monies', 'charity', 'charity', '18', '18', 'system', 'system', 'higher', 'higher', 'percentage', 'percentage', 'run', 'run', '-is', '-is', 'entire', 'entire', 'cheap', 'cheap', 'sob’s', 'sob’s', 'pandemic', 'pandemic', 'coronavirus', 'coronavirus', 'badguy', 'badguy', 'tools', 'tools', 'safer', 'safer', 'email', 'email', 'ebanking', 'ebanking', 'best', 'best', 'practices', 'practices', 'target', 'target', 'breach', 'breach', 'stolen', 'stolen', 'underground', 'underground', 'ashley', 'ashley', 'madison', 'madison', 'carding', 'carding', '—', 'twitter', 'join', 'facebook', 'in-depth', 'investigation', 'author', 'advertising/speaking', '16mar', '20', 'seen', '1984', 'movie', 'recalls', 'pivotal', 'scene', 'bureaucrat', 'orders', 'shutdown', 'ghost', 'effectively', 'unleashing', 'pent-up', 'phantom', 'city', 'similar', 'all-volunteer', 'nonprofit', 'works', 'identify', 'quarantine', 'infections', 'lost', 'longtime', 'primary', 'provides', 'live', 'feeds', 'information', 'addition', 'aided', 'nations’', 'names', 'far-flung', 'empires', 'lexicon', 'basically', 'malicious', 'captured', 'analyzed', 'and/or', 'typically', 'tandem', 'action', 'designed', 'wrest', 'key', 'powering', 'interventions', 'involving', 'documented', 'including', 'avalanche', 'takedown', 'rustock', 'takeover', 'gameover', 'seizure', 'nitol', 'sneak', 'last', 'week', 'instrumental', 'helping', 'kneecap', 'necurs', 'world’s', 'largest', 'allows', 'assume', 'network’s', 'flowing', 'server', 'none', 'computers', 'receive', 'instructions', 'harm', 'trusted', 'partner', 'agencies', 'technical', 'guns', 'badges', 'seized', 'drives', 'affected', 'hosting', 'recently', 'got', 'networking', 'giant', 'inc', 'opted', 'providing', 'declined', 'respond', 'questions', 'withdrew', 'did', 'idea', 'part', 'broader', 'technology', 'going', 'supports', 'evolution', 'enabling', 'contribute', 'grow', 'capabilities', 'written', 'statement', 'proud', 'history', 'supporter', 'explore', 'future', 'involvement', 'takes', 'shape', 'matters', 'worse', 'told', 'migrate', 'location', 'chore', 'reckons', 'somewhere', 'neighborhood', 'victims', 'protected', 'cybercriminal', '\u200bby', 'lose', 'critical', 'governments', 'forced', 'unexpectedly', 'stretch', 'perimeters', 'allow', 'home', 'potentially', 'unmanaged', 'another', 'major', 'windows', 'worm', 'increased', 'wrote', 'published', 'plight', 'serves', 'vetted', 'owners', '90%', 'giving', 'notify', '\u200babout', 'misconfigured', 'compromised', 'abusable', 'remediation', 'explained', 'group', 'several', 'options', 'self-funding', 'director', 'says', 'depend', 'tiered', 'provide', 'getting', 'charged', 'accomplishments', 'frequently', 'operate', 'different', 'story', 'valuable', 'took', 'stance', 'mean', 'anti-commercial', 'sector', 'activities', 'definitely', 'opportunities', 'innovation', 'development', 'seek', 'compete', 'commercial', 'vendors', 'disrupt', 'business', 'models', 'fundamentally', 'no-one', 'pay', 'raise', 'approximately', 'month', '1,300+', 'facility', 'directly', 'contact', 'page', '10:46', 'a.m', 'et', 'added', 'tags', 'posted', 'monday', '16th', '8:55', 'filed', 'coming', 'storm', 'through', 'feed', 'both', 'pings', 'closed', 'lindy', '9:13', 'brian’s', 'readers/fans', 'mention', 'sent', '-d', 'shout-out', 'worthy', 'laurie', '9:59', 'agree', 'sunshine', 'state', '9:17', 'gofundme', 'campaign', 'bart', '9:28', 'perhaps', 'white', 'house', 'knows', 'surely', 'connections', 'couple', '11:25', '1st', 'running', 'can’t', '2nd', 'probly', 'care', 'in-house', 'classified', 'essential', 'assumed', 'done', 'us', 'command', '11:09', 'crew', 'eight', 'ten', 'fed', 'suspect', 'thing', 'inevitable', 'consequence', 'framework', 'authorizing', 'realistic', 'expect', 'entity', 'take', 'role', 'ian', '9:40', 'lawyer', '9:41', 'i’ll', 'hearing', 'explanation', 'responds', 'unblinking', '10:14', 'desk', 'chuck', 'robbins', 'signatures', 'anuj', 'kapur', 'gerri', 'elliott', 'two', 'adults', 'required', 'implementing', 'theoretical', 'cost-saving', 'measures', 'ray', '10:19', 'extended', 'typo', '26th', '10:31', 'hi', 'trashed', 'angry', 'although', 'sort', 'self', 'healing', 'capability', 'discovered', 'installed', 'cellphone', 'use', 'means', 'fake', 'licenses', 'case', 'london', 'twice', 'kansas', 'ripencc', 'holland', 'amsterdam', 'that’s', 'probably', 'attacked', 'pick', 'hallways', 'constantly', 'yet', 'obtain', 'ip', 'adress', 'signal', 'appears', 'doesn’t', 'greets', 'jay', '10:40', 'giants', 'walmart', 'amazon', 'apple', 'wall', 'street', 'big', 'pitch', 'cover', 'expenses', 'derec', 'avery', '12:38', 'relying', 'single', 'funding/facilities', 'diversified', 'facilities', 'prevent', 'occurrence', 'nope', 'handle', 'thus', 'they’re', 'stuck', 'between', 'rock', 'place', 'scrambling', '7:29', 'generous', 'sponsors', 'eternally', 'grateful', 'valued', 'highly', 'unfortunate', 'longer', 'position', 'level', 'read', 'announcement', 'website', 'references', 'moving', 'neutral', 'governance', '2020+', 'share', 'obviously', 'perfect', 'already', 'diverse', 'failover', 'centers', 'build', 'everything', 'scratch', 'ourselves', 'scale', 'usual', 'budgets', 'levels', 'buffers', 'keeping', 'data/server', 'growth', 'drive', 'failure', 'rates', 'ensuring', 'around', 'gets', 'difficult', 'task', 'plus', 'strategy', 'keep', 'heads', 'down', 'serve', 'le', 'pr', 'focus', 'successfully', 'fighting', 'hence', 'urgent', 'challenge', 'changed', 'community’s', 'come', 'temporary', 'bump', 'road', 'exactly', 'suggesting', 'thank', 'interest', 'solve', 'together', 'dave', 'horsfall', '8:20', 'funny', 'happy', 'criticise', 'lift', 'finger', 'requires', 'actual', 'mouthing', 'asb', '10:36', 'excellent', 'you’ll', 'transition', 'difficulty', 'matthew', 'brown', '11:56', 'efforts', 'chipped', 'monthly', 'amount', 'andy_c', '21', '3:29', 'shadowservers', 'based', 'engineer', 'knowing', 'move', 'project', 'warm', 'body', 'pond', 'rack', 'stack', 'equipment', 'let', 'justnetguy', '11:05', 'glad', 'bob', '11:07', 'cert', 'customers', 'silly', 'vet', '4:22', '…yes', 'no…the', 'main', 'customer', 'spare', 'this…a', 'small', 'registration', 'icann', 'go…', 'mark', '11:17', 'somebody', 'fortinet', 'show', 'competitor', 'little', 'bondy', '11:40', 'deciding', 'kinda', 'sorta', 'cannot', 'comprehend', 'short', 'drop-dead', 'give', 'six', 'months', 'year', 'solution', 'point', 'intend', 'avoid', 'products', 'compassionately', 'ron', '12:12', 'ciscos', 'plan', 'they’ve', 'begun', 'massively', 'push', 'umbrella', 'market', 'ken', 'sims', '5:34', 'hobbyist', '500.00', 'professionals', 'donate', 'bucks', 'niteprowl2', '5:52', 'seems', 'interpol', 'lay', 'persons', 'opinion', 'mr', 'morningstar', '6:42', 'buy', 'dairy', 'farm', 'drinking', 'milk', '11:06', 'indiscriminately', 'often', 'attach', 'strings', 'soon', 'priorities', 'theirs', 'yours', 'creeps', 'satisfying', 'desires', 'battleground', 'decision', 'interests', 'emasculating', 'offense', 'having', 'defense', 'clifton', '8:48', 'since', 'complicit', 'pushing', 'defenseless', 'personal', 'rules', 'death', 'match', 'retired', 'm', 'devote', 'full', 'mattyj', '6:15', 'return', 'profit', 'maintain', 'status', 'richest', '1', '2', 'men', 'donating', 'briankrebs', '7:50', 'gist', 'saying', 'among', 'biggest', 'giver-awayer', 'he’s', 'billion', 'wife', 'billionaires', 'followed', 'suit', 'undoubtedly', 'tom', '4:13', 'm|b)illionnaires', 'mote', 'spend', 'democratic', 'fashion', 'beat', 'willing', '1%', 'diss', 'ideally', 'exist', 'jim', 'quinn', '22', '9:14', 'amen', 'taxed', 'supposed', 'progressive', 'i’ve', 'total', 'moderate', 'joint', 'politician', '30', 'million', 'warren', 'buffet', 'secretary', 'pays', 'go', '2017(i', 'cut', 'favorable', 'mike', '9:57', 'i’d', 'volunteer', 'assist', 'large', 'org', 'ie', 'hands', 'exp', 'organizational', 'skills', 'thx', '-m', 'blue', 'critter', '24', '4:42', 'details', 'listed', 'navigator', '501(c)(3', '-if', 'send', 'check', 'bushman', 'april', '8', '3:10', 'remind', 'supplies', 'hand', 'lots', 'intelligent', 'happen', 'planet’s', 'collapses', 'planned', 'massive', 'then', 'realize', 'really', 'gotten', 'mailing', 'list', 'recent', 'unproven', 'therapy', 'proves', 'cow', 'shadow', 'pharmacies', 'doubt', 'hang', 'look', '', 'call', 'back', 'behind', 'reopen', 'surge', 'sipping', 'firehose', 'covid-19', 'united', 'unity', 'survive', 'skimmers', 'click', 'skimmer', 'series', 'nation', 'times', 'bestseller', 'value', 'pharma', 'wars', 'spammers', 'duke', 'account', 'worth', 'imagine', 'popular', 'sextortion', 'scam', "recipient's", 'passwords', '1076', 'cheating', 'ashleymadison', '798', 'investigating', '620', 'cards', 'flood', 'markets', '445', 'liberty', 'reserve', 'founder', 'arrested', 'shuttered', '416', 'database', 'leaked', '376', 'goodbye', 'using', 'truecrypt', 'secure', '363', '361', 'epassporte', 'edition', '353', 'u.s', 'seizes', 'libertyreserve.com', '315', 'category', 'web', 'innovations', 'id', 'examined', 'antivirus', 'dead', 'reasons', 'decline', 'growing', 'file', 'em', 'bad', 'inside', 'shop', 'crash', 'beware', 'social', 'sign', 'signed', 'card', 'finding', 'easy', 'krebs’s', '3', 'rules…', 'safety', '©', 'powered', 'wordpress', 'privacy', 'policy']
unique_tokens = list(set(sorted_tokens)-stop_words)
logger.debug('Unique words to be made into word cloud {}'.format(list(set(unique_tokens))))
logger.info("Generating the word cloud...")
comment_words = " ".join(unique_tokens) #TODO delete this line

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
