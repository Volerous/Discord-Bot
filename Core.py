import discord
import asyncio
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
init_extensions = [
    'cogs.Misc',
    'cogs.Rand',
    # 'cogs.Extra',
    'cogs.Warframe'
]


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


@bot.command(hidden=True)
async def close():
    await bot.close()


for item in init_extensions:
    bot.load_extension(item)

bot.run('Mjc2MTEzNTQ4NDQ5NDE1MTcx.C3KeSg.Xt1ztH1_goNYIiRU27YYcJVbGk4')
