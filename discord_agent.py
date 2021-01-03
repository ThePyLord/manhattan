WEBHOOK = "YOUR WEBHOOK HERE" #insert your own channel's webhook
import discord, os

from dotenv import load_dotenv
import main

load_dotenv()
TOKEN = os.getenv('TOKEN')  # load the token
GUILD_ID = os.getenv('DISCORD_GUILD')


client = discord.Client()

"""
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
 """

@client.event
async def on_ready():
    print(f"Hot n' ready, My name is {client.user}")

@client.event
async def on_message(message):
    if "!btc price usd" in message.content.lower():
        await message.channel.send(main.btc_value_text)
        await client.close()        

client.run(TOKEN)