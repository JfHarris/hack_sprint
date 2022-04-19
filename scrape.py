#!/usr/bin/python3
"""
Scrapes urls from target web page
"""

from bs4 import BeautifulSoup
import requests

url = 'https://www.newson6.com/events'
req = requests.get(url)
result = BeautifulSoup(req.text, 'html.parser')

urls = []
for link in result.find_all('a'):
    print(link.get('href'))
