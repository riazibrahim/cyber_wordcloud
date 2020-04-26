from app import logger
import requests
import random
from config import Config
from threading import current_thread
from app.globalvars import urls_file


def fetch_url(url):
    logger.debug('Entered fetch_url')
    # logger.debug('Current thread {}'.format(current_thread().name))
    session = requests.Session()
    ip = session.get("http://icanhazip.com").text
    logger.debug('Thread name: {} obtained tor ip {}\n'.format(current_thread().name, ip))
    try:
        user_agent = random.choice(Config.USER_AGENT_LIST)
        headers = {'User-Agent': user_agent}
        response = session.get(url=url, headers=headers)
        logger.debug('request header {}'.format(response.request.headers))
        logger.debug('User agent used is {}\n'.format(user_agent))
        return url, response.content, None, ip
    except Exception as e:
        return url, None, e, ip


def create_url_list():
    url_list = []
    if urls_file is not None:
        logger.debug('Input file detected')
        with open(urls_file, 'r') as file:
            logger.debug('Opened input file {}'.format(urls_file))
            i = 1
            for item in file.readlines():
                site = item.rstrip()
                url_list.append(site)
                i += 1
    logger.info("Number of urls to be processed: {}".format(len(url_list)))
    return url_list
