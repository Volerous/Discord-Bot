from discord.ext import commands


class Extra:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add_to_bot(self, funcname: str=None, use: str=None):
        MSG = "```\n Add Function:\n Name:.{}\n Use: {}```".format(
            funcname, use)
        await msgpin = self.bot.say(MSG)
        await self.bot.pin_message(msgpin)
    
    @commands.command()
    async def remove_from_bot(self, funcname:str=None):
        MSG = "```\n Remove Function:\n Name:.{}\n```".format(funcname)
        await msgpin = self.bot.say(MSG)
        await self.bot.pin_message(msgpin)

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
            await Client.send_message(message.channel, 'img put in to list')
        else:
            await Client.send_message(message.channel,
                                      'The given command does not exist.')
        return True
