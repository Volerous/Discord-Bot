import discord
import asyncio
from Commands import *
from random import randint
import linecache
import youtube_dl


async def getRandImage(file, message, Client):
    file = open('links/' + file, 'r')
    urls = file.readlines()
    await Client.send_message(message.channel, urls[randint(0, len(urls) - 1)])
    file.close()


async def writeHelp(Client, message):
    helpstr = ""
    helpstr += "```\n"
    for i in SFW_COMMANDS:
        helpstr += i
        helpstr += "\n"
    helpstr += "```"
    print(helpstr)
    await Client.send_message(message.channel, helpstr)


async def one_liner(message: discord.Message, Client: discord.Client):
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
        await getRandImage('surr20.txt', message, Client)
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
    # bem
    if command == '.bem':
        await Client.send_message(message.channel,
                                  'https://youtu.be/m1HHQ8fn_w0?t=56s')
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
            message.channel, 'http://giphy.com/gifs/chang-senor-gciMbZy9jADa8')
        return True
    # anime
    if command == '.anime':
        await getRandImage('anime.txt', message, Client)
        return True
    # yak
    if command == '.yak':
        await getRandImage('yak.txt', message, Client)
        return True
    # abugin
    if command == '.abugin':
        await getRandImage('abugin.txt', message, Client)
        return True
    # dattebayo
    if command == '.dattebayo':
        await getRandImage('dattebayo.txt', message, Client)
        return True
    # eggplant
    if command == '.eggplant':
        await getRandImage('eggplant.txt', message, Client)
        return True
    # smash
    if command == '.smash':
        await Client.send_message(
            message.channel, 'https://www.youtube.com/watch?v=-TcLxlkc2pA')
        return True
    # freak_out
    if command == '.freak_out':
        await getRandImage('freak_out.txt', message, Client)
        return True
    # konosuba_dance
    if command == '.konosuba_dance':
        await getRandImage('konosuba_dance.txt', message, Client)
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
            'http://i2.kym-cdn.com/photos/images/newsfeed/001/093/836/b89.png')
        return True
    # feels
    if command == '.feels':
        await getRandImage('feels.txt', message, Client)
        return True
    # mugi
    if command == '.mugi':
        await getRandImage('mugi.txt', message, Client)
        return True
    # blackbaby
    if command == '.blackbaby':
        await Client.send_message(
            message.channel, ':eggplant: :sweat_drops: :baby::skin-tone-4:')
        return True
    # arabruski
    if command == '.arabruski':
        await Client.send_message(
            message.channel, 'https://www.youtube.com/watch?v=Cn5S79ZFRcY')
        return True
    return False


async def multiLineCommands(message: discord.Message, Client: discord.Client):
    command = message.content.split(' ')
    if command[
            0] == '.add' and message.channel.name == 'ideas_for_discord_bot':
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
    if command[
            0] == '.remove' and message.channel.name == 'ideas_for_discord_bot':
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
    return False
