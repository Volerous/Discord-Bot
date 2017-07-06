from discord.ext import commands
from random import randint

class Rand:
    def __init__(self, bot):
        self.bot = bot

    async def getRandImage(self, file):
        file = open('links/' + file, 'r')
        urls = file.readlines()
        await self.bot.say(urls[randint(0, len(urls) - 1)])
        file.close()

    @commands.command()
    async def feels(self):
        await self.getRandImage('feels.txt')

    @commands.command()
    async def mugi(self):
        await self.getRandImage('mugi.txt')

    @commands.command()
    async def freak_out(self):
        await self.getRandImage('freak_out.txt')

    @commands.command()
    async def konosuba_dance(self):
        await self.getRandImage('konosuba_dance.txt')

    @commands.command()
    async def surr20(self):
        await self.getRandImage('surr20.txt')

    @commands.command()
    async def anime(self):
        await self.getRandImage('anime.txt')

    @commands.command()
    async def yak(self):
        await self.getRandImage('yak.txt')

    @commands.command()
    async def abugin(self):
        await self.getRandImage('abugin.txt')

    @commands.command()
    async def dattebayo(self):
        await self.getRandImage('dattebayo.txt')

    @commands.command()
    async def eggplant(self):
        await self.getRandImage('eggplant.txt')


def setup(bot):
    bot.add_cog(Rand(bot))
