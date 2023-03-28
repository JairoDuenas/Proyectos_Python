
# TODO $ pip3 install bs4
# TODO $ pip3 install requests

import requests
from bs4 import BeautifulSoup

url = "https://www.google.com"
r = requests.get(url)
print(r)

soup = BeautifulSoup(r.content, 'lxml')
title = soup.find_all('h2', {'class':'post-title'})