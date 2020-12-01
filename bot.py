import discord
from discord.ext import commands

@client.event
async def on_ready():
    print("Bot is Ready")
