#!/usr/bin/python3
"""
Scrapes urls from target web page
"""

import requests
from bs4 import BeautifulSoup

 
text = "Tulsa events"
url = 'https://google.com/search?q=' + text
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
 
urls = []
for link in soup.find_all('a'):
    print(link.get('href'))


f = open("web.txt", "w")
for link in soup.find_all("a"):
    data = link.get('href')
    f.write(data)
    f.write("\n")

f.close()
