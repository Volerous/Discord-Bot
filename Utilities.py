import discord
import asyncio
from Commands import *
from random import randint
import linecache
import youtube_dl
import pickle
import sqlite3


class Utilities(object):
    def __init__(self):
        pass

    async def getRandImage(self, file, message, Client):
        file = open('links/' + file, 'r')
        urls = file.readlines()
        await Client.send_message(message.channel,
                                  urls[randint(0, len(urls) - 1)])
        file.close()

    async def writeHelp(self, Client, message):
        helpstr = ""
        helpstr += "```\n"
        for i in SFW_COMMANDS:
            helpstr += i
            helpstr += "\n"
        helpstr += "```"
        await Client.send_message(message.author, helpstr)

    async def findArg():
        pass

    async def one_liner(self, message: discord.Message,
                        Client: discord.Client):
        try:
            command = message.content.split(' ')[0]
        except IndexError:
            return False
        #weeaboo
        if command == '.weeaboo':
            await Client.send_message(
                message.channel, 'https://www.youtube.com/watch?v=TBfWKmRFTjM')
            return True
        #hello
        if command == '.hello':
            await Client.send_message(
                message.channel, 'https://www.youtube.com/watch?v=zdQ0J85ABX8')
            return True
        # rikka_dance
        if command == '.rikka_dance':
            await Client.send_message(message.channel,
                                      'http://i.imgur.com/eFoCtqk.gifv')
            return True
        # surr20
        if command == '.surr20':
            await self.getRandImage('surr20.txt', message, Client)
            return True
        # saltbae
        if command == '.saltbae':
            await Client.send_message(message.channel,
                                      'http://i.imgur.com/8hCCQVo.jpg')
            return True
        # lewd
        if command == '.lewd':
            await Client.send_message(message.channel,
                                      'https://i.stack.imgur.com/yICNQm.png')
            return True
        # nobeard
        if command == '.nobeard':
            await Client.send_message(message.channel,
                                      'http://i.imgur.com/puUW8ax.jpg')
            return True
        # butthurt
        if command == '.butthurt':
            await Client.send_message(message.channel,
                                      'http://i.imgur.com/Lk7bIwl.jpg')
            return True
        # hesright
        if command == '.hesright':
            await Client.send_message(message.channel,
                                      'https://i.imgur.com/8NgkZwD.jpg')
            return True
        # john_cena
        if command == '.john_cena':
            await Client.send_message(
                message.channel, 'https://www.youtube.com/watch?v=RZIhpba83hY')
            return True
        # gay
        if command == '.gay':
            await Client.send_message(
                message.channel,
                'http://giphy.com/gifs/chang-senor-gciMbZy9jADa8')
            return True
        # anime
        if command == '.anime':
            await self.getRandImage('anime.txt', message, Client)
            return True
        # yak
        if command == '.yak':
            await self.getRandImage('yak.txt', message, Client)
            return True
        # abugin
        if command == '.abugin':
            await self.getRandImage('abugin.txt', message, Client)
            return True
        # dattebayo
        if command == '.dattebayo':
            await self.getRandImage('dattebayo.txt', message, Client)
            return True
        # eggplant
        if command == '.eggplant':
            await self.getRandImage('eggplant.txt', message, Client)
            return True
        # smash
        if command == '.smash':
            await Client.send_message(
                message.channel, 'https://www.youtube.com/watch?v=-TcLxlkc2pA')
            return True
        # freak_out
        if command == '.freak_out':
            await self.getRandImage('freak_out.txt', message, Client)
            return True
        # konosuba_dance
        if command == '.konosuba_dance':
            await self.getRandImage('konosuba_dance.txt', message, Client)
            return True
        # fucku
        if command == '.fucku':
            await Client.send_message(message.channel,
                                      'http://i.imgur.com/I08DYpC.gifv')
            return True
        # explosion
        if command == '.explosion':
            await Client.send_message(
                message.channel,
                'http://giphy.com/gifs/explosion-gif-Dnb7EUzpgfiPS')
            return True
        # dennis
        if command == '.dennis':
            await Client.send_message(message.channel,
                                      'http://i.imgur.com/i81hHDw.png')
            return True
        # tilt
        if command == '.tilt':
            await Client.send_message(message.channel,
                                      'http://i.imgur.com/wDnoH6R.png')
            return True
        # okay
        if command == '.okay':
            await Client.send_message(
                message.channel, 'https://www.youtube.com/watch?v=SOIDVB7wROw')
            return True
        # huh
        if command == '.huh':
            await Client.send_message(
                message.channel, 'https://www.youtube.com/watch?v=X_ckHY38M0U')
            return True
        # helpme
        if command == '.helpme':
            await Client.send_message(
                message.channel, 'https://www.youtube.com/watch?v=-K1vGcH3gSY')
            return True
        # plot
        if command == '.plot':
            await Client.send_message(
                message.channel,
                'https://media.giphy.com/media/12E3VSS7k41JjW/giphy.gif')
            return True
        # martin
        if command == '.martin':
            await Client.send_message(
                message.channel, 'https://www.youtube.com/watch?v=4TMwO73S5w4')
            return True
        # kys
        if command == '.kys':
            await Client.send_message(
                message.channel,
                'http://i2.kym-cdn.com/photos/images/newsfeed/001/093/836/b89.png'
            )
            return True
        # feels
        if command == '.feels':
            await self.getRandImage('feels.txt', message, Client)
            return True
        # mugi
        if command == '.mugi':
            await self.getRandImage('mugi.txt', message, Client)
            return True
        # blackbaby
        if command == '.blackbaby':
            await Client.send_message(
                message.channel,
                ':eggplant: :sweat_drops: :baby::skin-tone-4:')
            return True
        # arabruski
        if command == '.arabruski':
            await Client.send_message(
                message.channel, 'https://www.youtube.com/watch?v=Cn5S79ZFRcY')
            return True
        return False

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
        if command[0] == '.warframe':
            if command[1] == 'show':
                target = message.mentions[0]
                conn = sqlite3.connect("discord.db")
                args = (target.id, )
                msgembed = discord.Embed(
                    name="{} Missing Items".format(target.id))
                msgembed.description = "Missing Items for {}".format(
                    target.name)
                msgembed.color = target.color
                cur = conn.cursor()
                cur.execute(
                    "SELECT item, components FROM Wishlists WHERE ID=?", args)
                queryret = cur.fetchall()
                prev = None
                gather = {}
                for row in queryret:
                    if prev != row[0]:
                        gather[row[0]] = []
                        prev = row[0]
                    gather[row[0]].append(row[1])
                for item in gather.keys():
                    msgembed.add_field(
                        name="{}".format(item), value=", ".join(gather[item]),inline=False)
                conn.close()
                await Client.send_message(
                    message.channel,
                    "showing missing items for",
                    embed=msgembed)
            #await Client.send_message(message.channel, command)
            elif command[1] == "add":
                target = message.mentions[0]
                conn = sqlite3.connect("discord.db")
                cur = conn.cursor()
                item = command[3:-1]
                if target != message.author:
                    await Client.send_message()
                print(item)
                await Client.send_message(message.channel, command)
                # try:
                    # cur.execute("INSERT INTO Wishlists VALUES (?,?,?)", (target.id, ))
            return True
        return False

    def save_wishlist(self, wlist):
        with open("wishlist.pkl", "w") as w_list_file:
            pickle.dump(self.wishlists, w_list_file, pickle.HIGHEST_PROTOCOL)

    def load_wishlist(self, wlist):
        with open("wishlist.pkl", "r") as w_list_file:
            self.wishlists = pickle.load(w_list_file)
