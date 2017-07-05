import discord
import asyncio
import Logger
import Commands
from Utilities import *
from discord.ext import commands
desc = """
This is a Discord Bot
"""
help_attrs = dict(hidden=True)
bot_prefix = ["."]
bot = commands.Bot(
    command_prefix=bot_prefix,
    description=desc,
    pm_help=None,
    help_attrs=help_attrs)



@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-------')


@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    await bot.process_commands(message)



@bot.command()
async def close():
    await bot.close()


@bot.command()
async def showmethecode():
    await bot.say("https://github.com/Volerous/Discord-Bot")

bot.load_extension("Utilities")
bot.run('Mjc2MTEzNTQ4NDQ5NDE1MTcx.C3KeSg.Xt1ztH1_goNYIiRU27YYcJVbGk4')

