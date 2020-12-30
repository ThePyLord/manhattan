WEBHOOK = "https://discord.com/api/webhooks/793726582060875786/elSlN6AF_qZNyR4rsfsooYjIjbZi7GCvpmHnBFB7y-QqivMxM5WCU6sBcc0kDHf91NSl" #insert your own channel's webhook
import discord


client = discord.Client()

@client.event
async def on_ready():
    print("Hot n' ready")

@client.event
async def on_message(message):
    if "!btc price usd":
        await message.channel.send()