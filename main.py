import discord
import requests
import json
from replit import db


def update_encouragements(encouraging_message):
    if "encouragements" in db.key():
        encouragements = dc["encouragements"]
        encouragements.append(encouraging_message)
        db["encouragements"] = encouragements
    else:
        db["encouragements"] = [encouraging_message]


#  def delete_encouragment(index):
#    encouragements = dc["encouragements"]


client = discord.Client()


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

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)


client.run('ODk5MzU3NTQ4NjIzMzA2Nzcy.YWxl_A.Like2_70ct7fm9dD46tUOkYcYWA')