import os, sys

current_dir = os.path.dirname(os.path.realpath((__file__)))
root_dir = os.path.dirname(current_dir)
sys.path.append(root_dir)

import discord
from discord.ext import commands
#using relative import to import a module from a parent directory
from tesco import search


class Manhattan(commands.Cog):
	"""Lmaoo its a bot that tells you bitcoin prices"""
	def __init__(self, client):
		self.client = client

	@commands.group(name='manhattan', invoke_without_command=False)
	async def manhattan(self, ctx):
		await ctx.channel.send("Base group for the Manhattan bot")

	@manhattan.command(name='price')
	async def price(self, ctx):
		await ctx.channel.send(search.btc_value_text)

	@manhattan.command(name='pft')
	async def pft(self, ctx):
		pass






def setup(client):
	client.add_cog(Manhattan(client))