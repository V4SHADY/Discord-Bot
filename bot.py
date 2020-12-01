import discord
from discord.ext import commands

client = commands.Bot(command_prefix=">")

@client.event
async def on_ready():
    print("Bot is Ready")

@client.command
async def hello(ctx):
    await ctx.send("Hi!")



client.run('Your Bot Token')
