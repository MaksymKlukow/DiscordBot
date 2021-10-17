import discord
import requests
import json
from replit import db
import credentials
import random
import asyncio
from discord.ext.commands import Bot


client = discord.Client()
WORDS = ("python", "jumble", "easy", "difficult", "answer", "fuck u", "xylophone")


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return (quote)


@client.event
async def on_ready():
    print("Pomyslnie wlaczono bota")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(message.author)

    if message.author.name == "niczow":
        await message.channel.send("WYPIERDALAJ")

    if message.content.startswith('ping'):
        await message.channel.send("pong")
    if message.content.startswith('pong'):
        await message.channel.send("ping")
    if message.content.startswith('Ping'):
        await message.channel.send("Pong")
    if message.content.startswith('Pong'):
        await message.channel.send("Ping")

    if message.content.startswith('ruletka'):
        await message.channel.send(random.choice(WORDS))

client.run(credentials.token)
