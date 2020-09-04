import typing
import requests
import bs4
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import json
import re
import lxml.html
import time
from time import gmtime, strftime
import random
from random import randint
import logging
import collections

import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

import re
from tabulate import tabulate
import os

links: List[str] = []
count = 1
# loop over the web pages of Immoweb to scrap links of houses and apartment for sale in belgium
for index in range(1,50):

    # url of the web page to scrap
    url = "https://www.immoweb.be/en/search/house/for-sale?countries=BE&page={}&orderBy=relevance".format(index)
    driver = webdriver.Firefox()
    # http request to identify the url
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, features="lxml")
    driver.close()

    # get the url link for each house or apartment listed in the web page
    for a in soup.find_all('a', attrs={'class': 'card__title-link'}):
        links.append(a.get('href'))

df = pd.DataFrame({'Links': links})
df.to_csv('/home/redkaton/Desktop/becode_projects/house_link.csv', index=False)
