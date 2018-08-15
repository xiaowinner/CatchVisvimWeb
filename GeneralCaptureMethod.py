import requests
import codecs
import datetime
from pymongo import MongoClient

Virtual_UserAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'

default_headers = {
    'User-Agent': Virtual_UserAgent,
}

def get_page(url, headers):
    if headers is not None:
        default_headers = headers
        data = requests.get(url, headers = default_headers).content
    return data

def post_page(url, parameters, headers):
    if headers is not None:
        default_headers = headers
    data = requests.post(url, headers = default_headers, data = parameters).content
    return data