import discord
from discord.ext import commands
from config import Config

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print("On ready")

client.run(Config.BOT_TOKEN)
