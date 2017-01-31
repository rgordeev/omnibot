# coding: utf-8
import logging
import random
import time
import copy
from datetime import datetime

import requests

from omnibot.client import Client
from omnibot.message import Message

import multiprocessing
from multiprocessing import Pool

import certifi
import urllib3

__title__ = 'omnibot'
__version__ = '0.1'
__author__ = 'Roman Gordeev'
__license__ = 'MIT'


http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where()
)

lock = multiprocessing.Lock()

HOST = ''
USER_AGENT = 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:32.0) Gecko/20100101 Firefox/32.0'


def push_message(message):
    delay = random.randint(2, 7)
    time.sleep(delay)

    url = HOST + 'msg_api?sec=pushMessage'

    message = copy.copy(message)

    headers = {
        'User-Agent': USER_AGENT,
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'Keep-Alive',
        'Content-Length': '500',
        'Content-Type': 'application/json',
    }

    body = {
        'external_dialog_id': message.client.login,
        'client_login': message.client.login,
        'login': message.client.login,
        'client_name': message.client.name,
        'date': str(datetime.now()),
        'messenger_type': message.message_type,
        'external_message_id': random.randint(1, 100000),
        'text': message.text,
        'notification': 1,
        'media_type': 1,
        'project_id': 1,
    }
    try:
        logging.info("SEND REQUEST TO SERVER")
        logging.info(url)
        logging.info(headers)
        logging.info(body)

        r = requests.post(url, headers=headers, json=body, timeout=60)

        if r.status_code == 200:
            data = r.json()
            if data is not None and 'errors' in data:
                errors = data['errors']
                if 'external_dialog_id' in errors:
                    message.error = errors['external_dialog_id']
            logging.info("REQUEST WAS SUCCESSFULLY SEND. status=%s, text=%s" % (r.status_code, r.text))
        else:
            logging.error("CAN NOT SEND REQUEST: status=%s, text=%s" % (r.status_code, r.text))
            message.error = r.status_code
    except:
        logging.exception("CAN NOT SEND REQUEST: unknown exception")
        message.error = 'unknown exception'
    return message


def save_client(message):
    delay = random.randint(2, 7)
    time.sleep(delay)

    url = HOST + 'msg_api?sec=saveClient'

    message = copy.copy(message)
    headers = {
        'User-Agent': USER_AGENT,
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'Keep-Alive',
        'Content-Length': '500',
        'Content-Type': 'application/json',
    }

    body = {
        'login': message.client.login,
        'messenger_type': message.message_type,
        'name': message.client.name,
        'photo': ''
    }

    try:
        logging.info("SEND REQUEST TO SERVER")
        logging.info(url)
        logging.info(headers)
        logging.info(body)

        r = requests.post(url, headers=headers, json=body, timeout=60)

        if r.status_code == 200:
            message.error = None
            logging.info("REQUEST WAS SUCCESSFULLY SEND. status=%s, text=%s" % (r.status_code, r.text))
        else:
            logging.error("CAN NOT SEND REQUEST: status=%s, text=%s" % (r.status_code, r.text))
            message.error = r.status_code
    except:
        logging.exception("CAN NOT SEND REQUEST: unknown exception")
        message.error = 'unknown exception'
    return message


def publish():
    print("Start publishing!")

    start_time = time.time()

    REQUESTS_LIMIT = random.randint(5, 10)
    clients = Client.clients(REQUESTS_LIMIT)
    messages = [Message.message(client) for client in clients]
    for msg in messages:
        print(str(msg))

    pool = Pool(4)
    messages = pool.map(push_message, messages)
    pool.close()
    pool.join()

    messages = [message for message in messages if message.error is not None]

    pool = Pool(4)
    messages = pool.map(save_client, messages)
    pool.close()
    pool.join()

    messages = [message for message in messages if message.error is None]

    pool = Pool(4)
    pool.map(push_message, messages)
    pool.close()
    pool.join()

    print('Done! Time taken: {}'.format(time.time() - start_time))
