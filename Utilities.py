import discord
import asyncio
import Commands
from random import randint
import linecache
class Utilities:
    def __init__(self):
        pass
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
        await Client.send_message(message.channel, 'http://i.imgur.com/xkE9IbA.png')
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
        await Client.send_message(message.channel, 'https://youtu.be/m1HHQ8fn_w0?t=55s')
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
    if command == '.':
        return True
    if command == '.':
        return True
    if command == '.':
        return True
    if command == '.':
        return True
    if command == '.':
        return True
    if command == '.':
        return True
    if command == '.':
        return True
    if command == '.':
        return True
    if command == '.':
        return True
    return False
async def multiLineCommands(message: discord.Message, Client: discord.Client):
    command = message.content.split(' ')
    if command[0] == '.add' and message.channel.name == 'ideas_for_discord_bot':
        print(len(command))
        if len(command) >= 3:
            MSG = "```\n Name:.{}\n\ Use:{}```".format(command[1],' '.join(command[2:]))
            await Client.send_message(message.channel, 'Add Function:'+MSG)
            return True
        else:
            MSG = '```\n'
            await Client.send_message(message.channel, 'add help')
            return True
    if command[0] == '.' and message.channel.name == 'ideas_for_discord_bot':
        
        return True
    if command[0] == '.':
        
        return True
    if command[0] == '.':
        
        return True
    if command[0] == '.':
        
        return True
    if command[0] == '.':
        
        return True
    if command[0] == '.':
        
        return True
    if command[0] == '.':
        
        return True
    if command[0] == '.':
        
        return True
    if command[0] == '.':
        
        return True
    if command[0] == '.':
        
        return True
    if command[0] == '.':
        
        return True
    if command[0] == '.':
        
        return True
    if command[0] == '.':
        
        return True
    if command[0] == '.':
        
        return True
    return False
    