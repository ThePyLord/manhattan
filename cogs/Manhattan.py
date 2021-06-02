import aiohttp
import discord
import requests
from aiohttp import ClientSession
from typing import List
from discord.ext import commands
# using relative import to import a module from a parent directory
# from module import search, PortfolioSchema
from portfolio import Portfolio
from pymongo import MongoClient

# mySchema = PortfolioSchema

try:
	client = MongoClient(
		host='localhost',
		port=27017,
		serverSelectionTimeoutMS=1000
	)
	# Trigger exception if connection fails
	client.server_info()
	manhattan_db = client.manhattan
	portfolio_col = manhattan_db['portfolios']
except:
	print('Failed to Connect to the database')


EMBED_COLOUR = 0xff9416



class Manhattan(commands.Cog):
	"""
	Manhattan bot
	-------------

	The main object for all subcommands of the Manhattan bot
	 a.k.a "Bitcoin's Eye"
	....

	Attributes:
	-----------
	manhattan
		Used as "$manhattan".
		Does not provide a response to the user

	price
		Used as "$manhattan price `<ticker>`". 
		Responds with the price of the asset given

	pft: Portfolio
		Used as "$manhattan pft <ticker> <entry> <target(optional)>".
		Creates a portfolio for the user
	"""
	def __init__(self, client):
		self.client = client

	@commands.group(name='manhattan', aliases=['m'],  invoke_without_command=False)
	async def manhattan(self, ctx):
		# await ctx.channel.send("Base group for the Manhattan bot")
		pass



	#TODO: Add flags for the crypto to show more/less detail about it
	@manhattan.command(name='price')
	async def price(self, ctx):
		await ctx.channel.send(search.refresh_data())

	@manhattan.command(name='pft')
	async def pft(self, ctx, ticker: str, entry: float, *, arg):
		
		"""
		Shows the portfolio only

		Parameters
		----------
		ticker: str
			The ticker symbol
		
		entry: int
			The entry price of the asset specified

		target/exit:  int
			The price of the asset you want to exit at
		"""
		embed = discord.Embed(
			title = f"{ctx.message.author.name}'s portfolio",
			description = "This is what your portfolio looks like",
			colour = discord.Colour(EMBED_COLOUR),
			icon_url = ctx.message.author.avatar_url
			)



		self.pft = Portfolio()
		self.pft.holder = ctx.message.author
		self.pft.update_portfolio(ticker, entry, target=arg[0])
		requests.post('http://localhost:5000/api/portfolios', self.pft.to_json())
		print(self.pft.portfolio)



		embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")
		embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
		embed.add_field(name="Ticker", value=self.pft.portfolio["tick_name"], inline=True)
		embed.add_field(name="Entry", value=self.pft.portfolio["entry"], inline=True)
		embed.add_field(name="Target/Exit", value=self.pft.portfolio["target"], inline=True)
		# if arg[1]:
		# 	embed.add_field(name="Quantity", value=self.pft.portfolio["quantity"], inline=True)
		embed.set_footer(text="Bitcoin's Eye. Powered by ThePyLord.")
		await ctx.send(embed=embed)
		return self.pft

	@manhattan.command()
	async def ping(self, ctx, invoke_without_command=True):
		await ctx.send(f"Pong {round(self.client.latency, 3)}")

	@manhattan.command()
	async def my_pft(self, ctx):
		# self.user_portfolio = portfolio_col.find_one({"_id": self.doc_id})
		await ctx.send(self.user_portfolio)
		requests.get('http://localhost:5000/api/portfolios')
	
	@manhattan.command()
	async def delete_pft(self, ctx):
		# Asynchronously call the API endpoint 
		async with ClientSession() as session:
			async with session.delete('http://localhost:5000/portfolios/') as res:
				await res.json()
	


def setup(client):
	client.add_cog(Manhattan(client))
