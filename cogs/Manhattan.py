import asyncio
import discord, random
import requests
from aiohttp import ClientSession
from typing import List
from discord.ext import commands
# using relative import to import a module from a parent directory
from module.portfolio import Portfolio

from pymongo import MongoClient


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

	
	@commands.has_role('Oligarchs')
	@manhattan.command(name='delete')
	async def del_cmd(self, ctx, num_msg: int, sender):
		for i in range(0, num_msg+1):
			if ctx.message == sender:
				ctx.message.delete()

	#TODO: Add flags for the crypto to show more/less detail about it
	@manhattan.command(name='price')
	async def price(self, ctx, ticker):
		async with ClientSession() as session:
			async with session.get('http://localhost:5000/api/prices/'+ticker) as res:
				d = await res.json()
				# Show that the bot is "typing"
				async with ctx.typing():
					await asyncio.sleep(random.uniform(0.5, 2))
			await ctx.message.reply(f"The price of {d['data']['name'].capitalize()} is currently: {d['data']['price']} USD", mention_author=False)

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


		# Post the new asset group to the database
		self.pft = Portfolio()
		self.pft.holder = ctx.message.author
		self.pft.update_portfolio(ticker, entry, target=arg)
		r = requests.post('http://localhost:5000/api/portfolios', json=self.pft.to_json())
		print(r.status_code)



		embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")
		embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
		embed.add_field(name="Ticker", value=self.pft.portfolio["tick_name"], inline=True)
		embed.add_field(name="Entry", value=self.pft.portfolio["entry"], inline=True)
		embed.add_field(name="Target/Exit", value=self.pft.portfolio["target"], inline=True)
		# if arg[1]:
		# 	embed.add_field(name="Quantity", value=self.pft.portfolio["quantity"], inline=True)
		embed.set_footer(text="Bitcoin's Eye. Powered by ThePyLord.")
		async with ctx.typing():
			await asyncio.sleep(random.uniform(1, 3))
		
		await ctx.send(embed=embed)
		return self.pft

	@manhattan.command()
	async def ping(self, ctx, invoke_without_command=True):
		async with ctx.typing():
			await asyncio.sleep(random.uniform(0.5, 1.5))
		await ctx.send(f"Pong {round(self.client.latency, 3)} 🎾")

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
