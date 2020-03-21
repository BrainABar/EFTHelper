import discord
from discord.ext import commands, tasks
from itertools import cycle
from config import Config


client = commands.Bot(command_prefix="!")
status = cycle(['test status 1', 'status test 2'])

users = {}

# Events
@client.event
async def on_ready():
    set_status.start()
    print("On ready")


@client.event
async def command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command does not exist")


@client.event
async def on_member_join(member):
    print(f'(member) joined')


# Commands
@client.command(aliases=['ping', 'pings'])
async def _ping(ctx):
    await ctx.send(f"Ping {round(client.latency *1000)}ms")


@client.command(aliases=['setmap', 'mymap', 'smap'], pass_context=True)
async def _setmap(ctx, *args):
    if len(args) > 0:
        if args[0] in ['customs']:
            await ctx.send(str(ctx.message.author))
    else:
        await ctx.send("Missing an argument: !<command> <map name>")


@client.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount+1)


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Send in all command requirements")


# Update function @ intervals
@tasks.loop(minutes=30)
async def set_status():
    await client.change_presence(activity=discord.Game(next(status)))


client.run(Config.BOT_TOKEN)
