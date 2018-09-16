#please run this script only with Python3

import discord #pip install discord.py / pip3 install discord.py
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import requests
import os
from os import getenv
import asyncio #pip install asyncio / pip3 install asyncio
import ctx
from weather import Weather, Unit #pip install weather-api / pip3 install weather-api
import time #pip install time / pip3 install time
from datetime import datetime
import pytz
import random
import site
import sys #pip install sys / pip3 install sys
# hide config.py
sys.path.insert(0, '/home/dietpi/discord')

client = discord.Client()

@client.event
async def on_member_join(member):
    print("Recognised that a member called " + member.name + " joined")
    await client.send_message(member, 'Welcome to this server, ' + member.mention + '! I\'m Archie, the official CADevelopers discord bot, nice to meet you! Please, read our #rules and #about in our discord server https://discord.gg/TS583KK to be updated. To see the list of commands type !help. Have fun and RESPECT!! :grinning: :desktop:')
    # await client.send_message(message.channel, 'Welcome to this server, @' + member.name + '! I\'m Archie, the official CADevelopers discord bot, nice to meet you! Please, read our #rules and #about in our discord server https://discord.gg/TS583KK to be updated. To see the list of commands type !help. Have fun and RESPECT!! :grinning: :desktop:')
    print("Message sent to " + member.name)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="CAD Developers | !help"))
    await client.send_message(discord.Object(id='481951758722138113'), 'Archie is now online! Type !help for more info. Enjoy!')

if __name__ == '__main__':
    import config
    client.run(config.token)
