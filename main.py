import credentials
from replit import db

import discord

client = discord.Client()

@client.event
async def on_ready():
    print("Pomyslnie wlaczono bota")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('ping'):
        await message.channel.send("pong")
    if message.content.startswith('pong'):
        await message.channel.send("ping")

client.run(credentials.TOKEN) #credentials.py for saver usage
