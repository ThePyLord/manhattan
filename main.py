#main file for the project

import requests, discord
import json
from bs4 import BeautifulSoup


URL = "https://www.google.com/search?q=btc+usd&oq=BTC+usd&aqs=chrome.0.69i59j0i67i131i433j0i131i433j0l2j69i60l3.2445j0j7&sourceid=chrome&ie=UTF-8"
site = requests.get(URL)

soup = BeautifulSoup(site.content, 'html.parser')

with open("priceinfo.txt", "w") as f:
    f.write(soup.text)
    f.close()