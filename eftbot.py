import discord
from discord.ext import commands, tasks
from itertools import cycle
from config import Config


client = commands.Bot(command_prefix="!")
status = cycle(['test status 1', 'status test 2'])

@client.event
async def on_ready():
    set_status.start()
    print("On ready")


@client.event
async def on_member_join(member):
    print(f'(member) joined')


@client.command(aliases=['ping', 'pings'])
async def _ping(ctx):
    await ctx.send(f"Ping {round(client.latency *1000)}ms")


@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)


@tasks.loop(minutes=30)
async def set_status():
    await client.change_presence(activity=discord.Game(next(status)))


client.run(Config.BOT_TOKEN)
