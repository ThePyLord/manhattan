#TODO: clean up the whole program, load and unload the cog

WEBHOOK = "YOUR WEBHOOK HERE" #insert your own channel's webhook
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv


from tesco import search

load_dotenv()
TOKEN = os.getenv('TOKEN')  # load the token
GUILD_ID = os.getenv('DISCORD_GUILD')



client = commands.Bot(command_prefix='$')


@client.command()
async def load(ctx, extension):
	client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')


#Send a message to the intended recipient and guild x
@client.event
async def on_message(message):
	id = client.get_guild(GUILD_ID)
	if "!btc price usd" in message.content.lower():
		# send the value of bitcoin in USD via a Google Search
		await message.channel.send(search.btc_value_text) 
		# await client.close()       

	elif "!users" in message.content.lower():
		# Find the number of users in the server
		await message.channel.send(f'There\'s {id.member_count} users in this server')

	elif "!bye" in message.content.lower():
		# End the session
		await client.close()

	elif "!clear" in message.content.lower():
		# Delete the previous message
		pass
		"""elif "$manhattan help" in message.content.lower():
		help_message = """"""
		```
		Usage: $manhattan <ticker> <entry> <target(optional)>
		MUST HAVE TICKER SYMBOL AND ENTRY!!!
		No target -> $manhattan btc 2000
		Notifications -> $manhattan btc notif !0.2, 0.4, 0.5, 0.6
		Price -> $manhattan <ticker>```
		"""
		"""" """
		
		# await message.channel.send(help_message)



@client.command()
async def help_docs():
	embed = discord.Embed(
		title = 'Title', 
		description = 'Help for the Manhattan bot',
			colour = discord.Colour.blue()
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
	embed.add_field(name='Field Name', value='Field Value1', inline=False)
	embed.add_field(name='Field Name', value='Field Value2', inline=False)
	embed.add_field(name='Field Name', value='Field Value3', inline=False)

	await client.send(embed=embed)



if __name__ == '__main__':
	client.run(TOKEN)
