from discord.ext import commands
import os
from mimetypes import guess_extension
import urllib

class Extra:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add_to_bot(self, funcname: str=None, use: str=None):
        MSG = "```\n Add Function:\n Name:.{}\n Use: {}```".format(
            funcname, use)
        msgpin = await self.bot.say(MSG)
        await self.bot.pin_message(msgpin)
    
    @commands.command()
    async def remove_from_bot(self, funcname:str=None):
        MSG = "```\n Remove Function:\n Name:.{}\n```".format(funcname)
        msgpin = await self.bot.say(MSG)
        await self.bot.pin_message(msgpin)

    @commands.command(name="add_link")
    async def add_link(self, target:str=None, link:str=None):
        if target == None or link==None:
            await self.bot.say("Link or command missing")
            return
        if not os.path.exists("links/{}.txt".format(target)):
            await self.bot.say("{} is not a valid command.".format(target))
            return
        else:
            if link[:-3] not in ["jpg", "png", "gif"] and not link.startswith("http"):
                await self.bot.say("The link: {} is not valid".format(link))
            else:
                with open("links/{}.txt".format(target), "r+") as f:
                    urls = f.readlines()
                    if link in urls:
                        await self.bot.say("The link is already in the list")
                        return
                    else:
                        urls.append(link)
                        f.writelines(urls)
                await self.bot.say("{} added to {}".format(link, target))
                
def setup(bot):
    bot.add_cog(Extra(bot))