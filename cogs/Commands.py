import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
GUILD_ID = os.getenv('DISCORD_GUILD')


class Commands(commands.Cog):
	"""


	"""

	def __init__(self, client):
		"""

		"""
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		for guild in self.client.guilds:
			if guild.name == GUILD_ID:
				break

		print(
			f'{self.client.user} is connected to the following guild:\t'
			f'{guild.name}(id: {guild.id})'
		)

	

def setup(client):
	client.add_cog(Commands(client))