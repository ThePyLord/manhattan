import os, sys

import discord
from discord.ext import commands
#using relative import to import a module from a parent directory
from tesco import search
from portfolio import Portfolio

current_dir = os.path.dirname(os.path.realpath((__file__)))
root_dir = os.path.dirname(current_dir)
sys.path.append(root_dir)

class Manhattan(commands.Cog):
	"""
	Manhattan bot
	-------------

	The main object for all subcommands of the Manhattan bot a.k.a "Bitcoin's Eye"
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

	@commands.group(name='manhattan', invoke_without_command=False)
	async def manhattan(self, ctx):
		await ctx.channel.send("Base group for the Manhattan bot")

	@manhattan.command(name='price')
	async def price(self, ctx, arg):
		await ctx.channel.send(search.btc_value_text)

	@manhattan.command(name='pft')
	async def pft(self, ctx, ticker, entry):
		"""
		Shows the portfolio only

		Parameters
		----------
		ticker:
			The ticker symbol
		
		entry:
			The entry price of the asset specified
		"""
		self.pft = Portfolio()
		self.pft.update_portfolio()






def setup(client):
	client.add_cog(Manhattan(client))