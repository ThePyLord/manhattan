import discord
import os
# from discord import client
from discord.ext import commands
from discord.ext.commands import cog
from discord.ext.commands.core import command
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
		
		await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='your commands'))
		
		print(
			f'{self.client.user.name} is connected to the following guild:\t'
			f'{guild.name}(id: {guild.id})'
			"\nListening for commands..."
		)

	@commands.Cog.listener()
	async def on_command_error(self, ctx, err):
		print(f"{ctx.command.name} was invoked incorrectly.\n{err}")


def setup(client):
	client.add_cog(Commands(client))