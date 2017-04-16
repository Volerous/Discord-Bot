import discord
import asyncio
import Commands
from random import randint
import linecache
import youtube_dl
from imagescrapper import scrapePage

async def getRandImage(file, message, Client):
    file = open('links/' + file, 'r')
    urls = file.readlines()
    await Client.send_message(message.channel, urls[randint(0, len(urls) - 1)])
    file.close()


async def one_liner(message: discord.Message, Client: discord.Client):
    try:
        command = message.content.split(' ')[0]
    except IndexError:
        return False
    if command == '.weeaboo':
        await Client.send_message(
            message.channel, 'https://www.youtube.com/watch?v=TBfWKmRFTjM')
        return True
    if command == '.hello':
        await Client.send_message(
            message.channel, 'https://www.youtube.com/watch?v=zdQ0J85ABX8')
        return True
    if command == '.rikka_dance':
        await Client.send_message(message.channel,
                                  'http://i.imgur.com/eFoCtqk.gifv')
        return True
    if command == '.surr20':
        await getRandImage('surr20.txt', message, Client)
        return True
    if command == '.saltbae':
        await Client.send_message(message.channel,
                                  'http://i.imgur.com/8hCCQVo.jpg')
        return True
    if command == '.lewd':
        await Client.send_message(message.channel,
                                  'https://i.stack.imgur.com/yICNQm.png')
        return True
    if command == '.nobeard':
        await Client.send_message(message.channel,
                                  'http://i.imgur.com/puUW8ax.jpg')
        return True
    if command == '.bem':
        await Client.send_message(message.channel,
                                  'https://youtu.be/m1HHQ8fn_w0?t=56s')
        return True
    if command == '.butthurt':
        await Client.send_message(message.channel,
                                  'http://i.imgur.com/Lk7bIwl.jpg')
        return True
    if command == '.hesright':
        await Client.send_message(message.channel,
                                  'https://i.imgur.com/8NgkZwD.jpg')
        return True
    if command == '.john_cena':
        await Client.send_message(
            message.channel, 'https://www.youtube.com/watch?v=RZIhpba83hY')
        return True
    if command == '.gay':
        await Client.send_message(
            message.channel, 'http://giphy.com/gifs/chang-senor-gciMbZy9jADa8')
        return True
    if command == '.anime':
        await getRandImage('anime.txt', message, Client)
        return True
    if command == '.yak':
        await getRandImage('yak.txt', message, Client)
        return True
    if command == '.abugin':
        await getRandImage('abugin.txt', message, Client)
        return True
    if command == '.dattebayo':
        await getRandImage('dattebayo.txt', message, Client)
        return True
    if command == '.eggplant':
        await getRandImage('eggplant.txt', message, Client)
        return True
    if command == '.smash':
        await Client.send_message(
            message.channel, 'https://www.youtube.com/watch?v=-TcLxlkc2pA')
        return True
    if command == '.freak_out':
        await getRandImage('freak_out.txt', message, Client)
        return True
    if command == '.konosuba_dance':
        await getRandImage('konosuba_dance.txt', message, Client)
        return True
    if command == '.fucku':
        await Client.send_message(message.channel,
                                  'http://i.imgur.com/I08DYpC.gifv')
        return True
    if command == '.explosion':
        await Client.send_message(
            message.channel,
            'http://giphy.com/gifs/explosion-gif-Dnb7EUzpgfiPS')
        return True
    if command == '.dennis':
        await Client.send_message(message.channel,
                                  'http://i.imgur.com/i81hHDw.png')
        return True
    if command == '.tilt':
        await Client.send_message(message.channel,
                                  'http://i.imgur.com/wDnoH6R.png')
        return True
    if command == '.okay':
        await Client.send_message(message.channel, 'https://www.youtube.com/watch?v=SOIDVB7wROw')
        return True
    if command == '.huh':
        await Client.send_message(message.channel, 'https://www.youtube.com/watch?v=X_ckHY38M0U')
        return True
    if command == '.help_me':
        await Client.send_message(message.channel, 'https://www.youtube.com/watch?v=-K1vGcH3gSY')
        return True
    return False


async def multiLineCommands(message: discord.Message, Client: discord.Client):
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
    if command[0] == '.':
        await writeHelp()
        return True
    if command[0] == '.add_link':
        if command[1] in Commands.SFW_COMMANDS:
            command[1] = command[1].strip('.')
            newUrl = scrapePage(command[2])
            with open(command[1]+'.txt', 'w') as file:
                urls = file.readlines()
                urls.append(newUrl)
            await Client.send_message(message.channel, command[1])
        else:
            await Client.send_message(message.channel, 'The given command does not exist.')
    return False


async def writeHelp():
    pass
