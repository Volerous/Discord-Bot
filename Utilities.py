import discord
import asyncio
import Commands
from random import randint
import linecache
import youtube_dl

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
        await Client.send_message(message.channel, 'https://www.youtube.com/watch?v=TBfWKmRFTjM')
        return True
    if command == '.hello':
        await Client.send_message(message.channel, 'https://www.youtube.com/watch?v=zdQ0J85ABX8')
        return True
    if command == '.rikka_dance':
        await Client.send_message(message.channel, 'http://i.imgur.com/eFoCtqk.gifv')
        return True
    if command == '.surr20':
        await getRandImage('surr20.txt', message, Client)
        return True
    if command == '.saltbae':
        await Client.send_message(message.channel, 'http://i.imgur.com/8hCCQVo.jpg')
        return True
    if command == '.lewd':
        await Client.send_message(message.channel, 'https://i.stack.imgur.com/yICNQm.png')
        return True
    if command == '.nobeard':
        await Client.send_message(message.channel, 'http://i.imgur.com/puUW8ax.jpg')
        return True
    if command == '.bem':
        await Client.send_message(message.channel, 'https://youtu.be/m1HHQ8fn_w0?t=56s')
        return True
    if command == '.butthurt':
        await Client.send_message(message.channel, 'http://i.imgur.com/Lk7bIwl.jpg')
        return True
    if command == '.hesright':
        await Client.send_message(message.channel, 'https://i.imgur.com/8NgkZwD.jpg')
        return True
    if command == '.john_cena':
        await Client.send_message(message.channel, 'https://www.youtube.com/watch?v=RZIhpba83hY')
        return True
    if command == '.gay':
        await Client.send_message(message.channel, 'http://giphy.com/gifs/chang-senor-gciMbZy9jADa8')
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
        await Client.send_message(message.channel, 'https://www.youtube.com/watch?v=-TcLxlkc2pA')
        return True
    if command == '.freak_out':
        await getRandImage('freak_out.txt', message, Client)
        return True
    if command == '.konosuba_dance':
        await getRandImage('konosuba_dance.txt', message, Client)
        return True
    if command == '.fucku':
        await Client.send_message(message.channel, 'http://i.imgur.com/I08DYpC.gifv')
    if command == '.explosion':
        await Client.send_message(message.channel, 'http://giphy.com/gifs/explosion-gif-Dnb7EUzpgfiPS')
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
    if command[0] == '.help':

        return True
    return False

async def writeHelp():
    pass
