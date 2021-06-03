#TODO: Scrape the cryptonator website
from os import sep
import pprint
from colorama import Fore
import colorama
from colorama.initialise import init
import requests
import json
from bs4 import BeautifulSoup

init()

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

crypto_lst = []
#TODO: Parameterize the data and return the info for a specific crypto
def get_price_data():
	site = requests.get('https://coinmarketcap.com/')
	soup = BeautifulSoup(site.content, 'html.parser')
	keys = ('rank', 
			'name',
			'price', 
			'24h Change', 
			'7d Change', 
			'market cap', 
			'volume(24h)', 
			'circulating supply',
			'sparkline'
	)
	info = {}
	for rowIdx, rows in enumerate(soup.find_all('tr')[1:]):
		keyIdx = 0
		counter = 0
		if rowIdx < 10:
			for child in rows.children:
				child_text = child.text
	
				# print(child.prettify())
				#Get the name of the crypto without the ticker
				if keyIdx == 1 or keyIdx == 6:
					child_text = ''.join([i.text for i in child.select("p:nth-of-type(1)")[:1]])

				#Get the market cap in USD(long version)
				#----There's two tags with matching values, 
				#---- one in a shorter version of the value interpretation
				if keyIdx == 5:
					for sub_child in child.children:
						child_text = ''.join([i for i in sub_child.select("span:nth-of-type(2)")[-1]])

				# Add the data for the specific crypto into the dictionary
				if child_text:
					info[keys[keyIdx]] = child_text
					keyIdx += 1

				for img in child.find_all('img'):
					if img.get('alt'):
						info[keys[keyIdx]] = img['src']
						# print(img['src'])

		else: break
		counter += 1
		crypto_lst.append(info)

		pprint.pprint(crypto_lst[rowIdx])

	print(crypto_lst)
	return info

get_price_data()