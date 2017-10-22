import discord
import asyncio
from discord.ext import commands
from git import *
import os
desc = """
This is a Discord Bot
"""
git=Git(os.getcwd())
help_attrs = dict(hidden=True)
bot_prefix = ["."]
bot = commands.Bot(
    command_prefix=bot_prefix,
    description=desc,
    pm_help=None,
    help_attrs=help_attrs)
init_extensions = [
    'cogs.Misc',
    'cogs.Rand',
    'cogs.Extra',
    'cogs.Warframe'
]



@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-------')
    bot.say("bot running")


@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    await bot.process_commands(message)


@bot.command(hidden=True)
async def close():
    await bot.close()

@bot.command(hidden=True)
async def update():
    for i in init_extensions:
        bot.unload_extension(i)
    ret = git.pull()
    for i in init_extensions:
        bot.load_extension(i)
    print(ret)

@bot.command(name="load", hidden=True)
async def load_ext(*, module: str):
    bot.load_extension("cogs." + module)


@bot.command(name="unload", hidden=True)
async def unload_ext(*, module: str):
    bot.unload_extension("cogs." + module)


@bot.command(name="reload", hidden=True)
async def reload_ext(*, module: str):
    bot.unload_extension("cogs." + module)
    bot.load_extension("cogs." + module)


for item in init_extensions:
    bot.load_extension(item)

bot.run('Mjc2MTEzNTQ4NDQ5NDE1MTcx.C3KeSg.Xt1ztH1_goNYIiRU27YYcJVbGk4')
