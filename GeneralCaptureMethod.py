import requests
import codecs
import datetime
from pymongo import MongoClient

Virtual_UserAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'

headers = {
    'User-Agent': Virtual_UserAgent,
    'Content-Type': 'application/x-www-form-urlencoded',
    'Postman-Token': '418e8d14-f6e8-42da-a367-b23096206668',
    'cookie': 'VISVIM_FRONT_PAGE_SESSION=0ra12aik83dmf29gsl8sjvniv1',
    'cache-control': 'no-cache'

}

def get_page(url):
    data = requests.get(url, headers = headers).content
    return data

def post_page(url, parameters):
    data = requests.post(url, headers = headers, data = parameters).content
    return data