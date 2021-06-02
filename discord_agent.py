#todo: clean up the whole program, load and unload the cog

WEBHOOK = "YOUR WEBHOOK HERE" #insert your own channel's webhook
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

# from module import search

load_dotenv()
TOKEN = os.getenv('TOKEN')  # load the token
GUILD_ID = os.getenv('DISCORD_GUILD')
EMBED_COLOUR = 0xff9416


client = commands.Bot(command_prefix='$')

@client.command()
async def load(ctx, extension):
	client.load_extension(f"cogs.{extension}")
	print("Cogs loaded")

@client.command()
async def unload(ctx, extension):
	client.unload_extension(f"cogs.{extension}")

for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f"cogs.{filename[:-3]}")



@client.command()
async def help_docs(ctx):
	embed = discord.Embed(
		title = 'Title', 
		description = 'Help for the Manhattan bot',
		colour = discord.Colour(EMBED_COLOUR)
	)
	#The link for the image to be used in the embed(shortened for readability)
	img = "https://bit.ly/3slHEvS"

	embed.set_footer(text='Manhattan Bot')
	embed.set_image(url=img)
	embed.set_thumbnail(url=img)
	embed.set_author(
		name='ThePyLord x Danquilius', 
		icon_url=img
	)
	embed.add_field(name='Field Name', value='Field Value1', inline=True)
	embed.add_field(name='Field Name', value='Field Value2', inline=True)
	embed.add_field(name='Field Name', value='Field Value3', inline=True)

	await ctx.send(embed=embed)


# client.run(TOKEN)
if __name__ == '__main__':
	try:
		client.run(TOKEN)
	except RuntimeError as e:
		print('Event Loop Error')