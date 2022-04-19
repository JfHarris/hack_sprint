#!/usr/bin/python3
"""
Scrapes urls from target web page
"""
import requests
from bs4 import BeautifulSoup

urls = 'https://www.newson6.com/events'
grab = requests.get(urls)
soup = BeautifulSoup(grab.text, 'html.parser')


f = open("web.txt", "w")
for link in soup.find_all("a"):
    data = link.get('href')
    f.write(data)
    f.write("\n")

f.close()