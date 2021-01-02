WEBHOOK = "https://discord.com/api/webhooks/793726582060875786/elSlN6AF_qZNyR4rsfsooYjIjbZi7GCvpmHnBFB7y-QqivMxM5WCU6sBcc0kDHf91NSl" #insert your own channel's webhook
import discord, os

from dotenv import load_dotenv
import main

load_dotenv()
TOKEN = os.getenv('TOKEN')
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
    print("Hot n' ready")

@client.event
async def on_message(message):
    if "!btc price usd":
        await message.channel.send()
        