from discord.ext import commands
from random import randint
from urllib.request import urlopen
from bs4 import BeautifulSoup
from apiclient.discovery import build


class Rand:

    def __init__(self, bot):
        self.bot = bot
        self.api_key = 'AIzaSyBVAP4DI7oxQYyyHJMxB94qWjFjsIHph_o'
        API_SERVICE_NAME = "youtube"
        API_VERSION = "v3"
        self.service = build(
            'youtube', 'v3', developerKey='AIzaSyBVAP4DI7oxQYyyHJMxB94qWjFjsIHph_o')

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

    @commands.cooldown(rate=5, per=10)
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

    @commands.command()
    async def gigis(self):
        results = self.service.search().list(part='id', maxResults=50,
                                             channelId="UCI7HWYaijk2ChE9Ce5YCgAQ").execute()
        result = results["items"][randint(
            0, len(results["items"]))]["id"]["videoId"]
        await self.bot.say("https://www.youtube.com/watch?v=" + result)


def setup(bot):
    bot.add_cog(Rand(bot))
