# python trakt.tv documentation 
# https://github.com/fuzeman/trakt.py
import requests
import json
import os
import logging

from bs4 import *
import pandas as pd 
import urllib.request
import sys
import pathlib
from trakt import Trakt # pip install trakt.py
from trakt.objects import *


logging.basicConfig(level=logging.DEBUG)
#api credentials
traktID = os.environ.get('TRAKT_TV_CLIENT_ID')
traktSecret = os.environ.get('TRAKT_TV_CLIENT_SECRET')
usr_agent = {
    # 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    # 'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    # 'Accept-Encoding': 'none',
    # 'Accept-Language': 'en-US,en;q=0.8',
    # 'Connection': 'keep-alive',

    'Content-type': 'application/json',
    'trakt-api-key': traktID,
    'trakt-api-version':'2',

}

trakt = Trakt.configuration.defaults.client(
    id = traktID,
    secret = traktSecret
)





response = requests.get("https://api.trakt.tv", headers=usr_agent)

print(response)



