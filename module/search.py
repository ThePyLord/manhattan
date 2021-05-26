#TODO: Scrape the cryptonator website
import requests
import json
from bs4 import BeautifulSoup

URL = "https://www.google.com/search?q=btc+usd&oq=BTC+usd&aqs=chrome.0.69i59j0i67i131i433j0i131i433j0l2j69i60l3.2445j0j7&sourceid=chrome&ie=UTF-8"
url_c = "https://www.cryptonator.com/rates/BTC-USD"
# print(type(site), site, sep="\n")

def refresh_data():
	site = requests.get(URL)
	soup = BeautifulSoup(site.content, 'html.parser')
	btc_value = soup.find(class_="BNeawe iBp4i AP7Wnd")
	btc_value_text = btc_value.text + 's'

	return btc_value_text
	
def refresh_data_c():
	site = requests.get(url_c)
	soup = BeautifulSoup(site.content, 'html.parser')
	btc_val = soup.find('strong')
	print(btc_val)
	return btc_val

#TODO: Parameterize the data and return the info for a specific crypto
def get_price_data():
	site = requests.get('https://coinmarketcap.com/')
	soup = BeautifulSoup(site.content, 'html.parser')
	info, keys = {}, []
	num = 0
	for rowIdx, rows in enumerate(soup.find_all('tr')[1:]):
		if rowIdx < 20:
			for child in rows.children:
				# print(child.html)
				num += rowIdx
		else: break
	print(f'There are {rowIdx} rows on the page')
	 
get_price_data()