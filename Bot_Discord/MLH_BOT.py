import discord
from discord.ext import commands
import asyncio

from apikeys import *

intents =discord.Intents.all()
intents.members = True
client = commands.Bot(intents=intents,command_prefix ='_')

@client.event
async def on_ready():
    print('bot is ready !!!!!!!!!!!!!')
    print('--------------------------')

@client.command()
async def hello(ctx):
    await ctx.send('Hello , MLH Bot is here')

@client.event
async def on_member_join(member):
    channel = client.get_channel()
    await channel.send('Welcome to MLH server '+ member)

@client.event
async def on_member_remove(member):
    channel = client.get_channel()
    await channel.send('Good Bye and thnx for your time Xd : '+ member)



@client.event
async def on_message(message):
    if message.content.startswith('_like'):
        channel = message.channel
        await channel.send('Send me that 👍 reaction, mate')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎')
        else:
            await channel.send('👍')

client.run(BOTTOKEN)
