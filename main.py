import discord
import requests
import json
import time
import random
import asyncio
from replit import db

TOKEN = "ODk5MzU3NTQ4NjIzMzA2Nzcy.YWxl_A.yk02UEHqTtZorUYcTvg_6PbooJc"
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

client.run(TOKEN)
