import pandas as pd
import discord 
from discord.utils import get
from discord.ext import commands
from apikeys import *

intents =discord.Intents.all()
intents.members = True
client = commands.Bot(intents=intents,command_prefix ='!')



  

@client.command()
async def members(ctx):
    for guild in client.guilds:
        for member in guild.members:
            print(member)


@client.command()
async def autorole(ctx,sheetid):
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheetid}/export?format=csv")
    channel = ctx.channel
    #guild = client.get_guild(message.guild_id)
    for  member  in df['user']:
        member = client.get_user(member)
        for role in df['roles']:
            role = get(ctx.guild.roles,name=role)
            await member.add_roles(role)
            await channel.send(role +" added to user "+member)

                

client.run(BOTTOKEN)
