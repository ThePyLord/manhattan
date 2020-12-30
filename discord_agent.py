WEBHOOK = "" #insert your own channel's webhook
import discord

client = discord.Client()

@client.event
async def on_ready():
    print("Hot n' ready")

@client.event
async def on_message(message):
    if "!btc price":
        await message.channel.send()