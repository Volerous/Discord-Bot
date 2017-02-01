import discord
import asyncio
import Commands

class Utilities:
    def __init__(self):
        pass
async def one_liner(message: discord.message, Client: discord.client):
    try:
        command = message.content.split(' ')[0]
    except IndexError:
        return False
    if command == '.yak':
        return True
    if command == '.weeaboo':
        await Client.send_message(message.channel, 'https://www.youtube.com/watch?v=TBfWKmRFTjM')
        return True
    if command == '.hello':
        await Client.send_message(message.channel, 'https://www.youtube.com/watch?v=zdQ0J85ABX8')
        return True
    if command == '.rikka_dance':
        await Client.send_message(message.channel, Commands.ONE_LINERS_LINKS['.rikka_dance'])
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
