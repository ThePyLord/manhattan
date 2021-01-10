WEBHOOK = "YOUR WEBHOOK HERE" #insert your own channel's webhook

import discord, os

from dotenv import load_dotenv
import main


Class Manhattan:
	pass


load_dotenv()
TOKEN = os.getenv('TOKEN')  # load the token
GUILD_ID = os.getenv('DISCORD_GUILD')


client = discord.Client()

@client.event
async def on_ready():
	for guild in client.guilds:
		if guild.name == GUILD_ID:
			break

	print(
		f'{client.user} is connected to the following guild:\n'
		f'{guild.name}(id: {guild.id})'
	)


""" @client.event
async def on_ready():
	print(f"Hot n' ready, My name is {client.user}") """

#Send a message to the intended recipient and guild x
@client.event
async def on_message(message):
	id = client.get_guild(GUILD_ID)
	if "!btc price usd" in message.content.lower():
		# send the value of bitcoin in USD via a Google Search
		await message.channel.send(main.btc_value_text) 
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
	elif "$manhattan help" in message.content.lower():
		help_message = "manhattan help\n
		"usage: $manhattan <ticker> <entry> <target(optional)>\n"
		"MUST HAVE TICKER SYMBOL AND ENTRY!!!\n\n"
		"no target -> $manhattan btc 2000\n"
		"notifications -> $manhattan btc notif !0.2, 0.4, 0.5, 0.6\n"
		"price -> $manhattan <ticker>"
		
		await message.channel.send(help_message)


client.run(TOKEN)
