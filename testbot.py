import discord
import os
from dotenv import load_dotenv
from greetings import GREETINGS
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
#bot = commands.Bot(case_insensitive=False, command_prefix='/')

@client.event
async def on_ready():
    print("We are in as {0.user}".format(client))



@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.channel.id ==898270716263268372:
        if message.content.lower() in GREETINGS:
            await message.channel.send(f'Hello {message.author.display_name}')








client.run(TOKEN)
