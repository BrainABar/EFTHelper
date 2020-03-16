import discord
from discord.ext import commands
from config import Config

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print("On ready")


@client.event
async def on_member_join(member):
    print(f'(member) joined')


@client.command(aliases=['ping', 'pings'])
async def _ping(ctx):
    await ctx.send(f"Ping {round(client.latency *1000)}ms")

client.run(Config.BOT_TOKEN)
