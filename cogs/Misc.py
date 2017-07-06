import discord
import asyncio
from random import randint
import linecache
import youtube_dl
import pickle
import sqlite3
from discord.ext import commands


class Utilities:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def weeaboo(self):
        await self.bot.say('https://www.youtube.com/watch?v=TBfWKmRFTjM')

    @commands.command()
    async def hello(self):
        await self.bot.say('https://www.youtube.com/watch?v=zdQ0J85ABX8')

    @commands.command()
    async def rikka_dance(self):
        await self.bot.say('http://i.imgur.com/eFoCtqk.gifv')

    @commands.command()
    async def saltbae(self):
        await self.bot.say('http://i.imgur.com/8hCCQVo.jpg')

    @commands.command()
    async def lewd(self):
        await self.bot.say('https://i.stack.imgur.com/yICNQm.png')

    @commands.command()
    async def nobeard(self):
        await self.bot.say('http://i.imgur.com/puUW8ax.jpg')

    @commands.command()
    async def butthurt(self):
        await self.bot.say('http://i.imgur.com/Lk7bIwl.jpg')

    @commands.command()
    async def hesright(self):
        await self.bot.say('https://i.imgur.com/8NgkZwD.jpg')

    @commands.command()
    async def john_cena(self):
        await self.bot.say('https://www.youtube.com/watch?v=RZIhpba83hY')

    @commands.command()
    async def gay(self):
        await self.bot.say('http://giphy.com/gifs/chang-senor-gciMbZy9jADa8')

    @commands.command()
    async def smash(self):
        await self.bot.say('https://www.youtube.com/watch?v=-TcLxlkc2pA')

    @commands.command()
    async def fucku(self):
        await self.bot.say('http://i.imgur.com/I08DYpC.gifv')

    @commands.command()
    async def explosion(self):
        await self.bot.say('http://giphy.com/gifs/explosion-gif-Dnb7EUzpgfiPS')

    @commands.command()
    async def dennis(self):
        await self.bot.say('http://i.imgur.com/i81hHDw.png')

    @commands.command()
    async def tilt(self):
        await self.bot.say('http://i.imgur.com/wDnoH6R.png')

    @commands.command()
    async def okay(self):
        await self.bot.say('https://www.youtube.com/watch?v=SOIDVB7wROw')

    @commands.command()
    async def huh(self):
        await self.bot.say('https://www.youtube.com/watch?v=X_ckHY38M0U')

    @commands.command()
    async def helpme(self):
        await self.bot.say('https://www.youtube.com/watch?v=-K1vGcH3gSY')

    @commands.command()
    async def plot(self):
        await self.bot.say(
            'https://media.giphy.com/media/12E3VSS7k41JjW/giphy.gif')

    @commands.command()
    async def martin(self):
        await self.bot.say('https://www.youtube.com/watch?v=4TMwO73S5w4')

    @commands.command()
    async def kys(self):
        await self.bot.say(
            'http://i2.kym-cdn.com/photos/images/newsfeed/001/093/836/b89.png')

    @commands.command()
    async def blackbaby(self):
        await self.bot.say(':eggplant: :sweat_drops: :baby: :skin-tone-4:')

    @commands.command()
    async def arabruski(self):
        await self.bot.say('https://www.youtube.com/watch?v=Cn5S79ZFRcY')

    @commands.command()
    async def showmethecode():
        await self.bot.say("https://github.com/Volerous/Discord-Bot")

    async def multiLineCommands(self,
                                message: discord.Message,
                                Client: discord.Client):
        command = message.content.split(' ')
        if command[0] == '.add' and message.channel.name == 'ideas_for_discord_bot':
            if len(command) >= 3:
                MSG = "```\n Add Function:\n Name:.{}\n Use: {}```".format(
                    command[1], ' '.join(command[2:]))
                newMes = await Client.send_message(message.channel, MSG)
                await Client.pin_message(newMes)
                return True
            else:
                MSG = '```\n'
                await Client.send_message(message.channel, 'add help')
                return True
        if command[0] == '.remove' and message.channel.name == 'ideas_for_discord_bot':
            if len(command) >= 3:
                MSG = "```\n Remove Function:\n Name:.{}\n Use: {}```".format(
                    command[1], ' '.join(command[2:]))
                newMes = await Client.send_message(message.channel, MSG)
                await Client.pin_message(newMes)
                return True
            else:
                MSG = '```\n'
                await Client.send_message(message.channel, 'remove help')
                return True
            return True
        if command[0] == '.help':
            await writeHelp(Client, message)
            return True
        if command[0] == '.add_link':
            if command[1] in SFW_COMMANDS:
                command[1] = command[1].strip('.')
                newUrl = scrapePage(command[2])
                with open("links/" + command[1] + '.txt', 'r+') as file:
                    urls = file.readlines()
                    if not newUrl in urls:
                        urls.append(newUrl)
                    for url in urls:
                        file.write(url)
                await Client.send_message(message.channel,
                                          'img put in to list')
            else:
                await Client.send_message(message.channel,
                                          'The given command does not exist.')
            return True
        # arg for site
        # arg for type
        # arg for search
        if command[0] == ".lmgtfy":
            return True
        if command[0] == ".embed":
            embed = discord.Embed(title="Test Wishlist")
            embed.add_field(name="Item", value="Ember")
            embed.add_field(name="Elements", value="Blueprints, Systems")
            await Client.send_message(message.channel, embed=embed)
            return True

        return False

    def save_wishlist(self, wlist):
        with open("wishlist.pkl", "w") as w_list_file:
            pickle.dump(self.wishlists, w_list_file, pickle.HIGHEST_PROTOCOL)

    def load_wishlist(self, wlist):
        with open("wishlist.pkl", "r") as w_list_file:
            self.wishlists = pickle.load(w_list_file)


def setup(bot):
    bot.add_cog(Utilities(bot))