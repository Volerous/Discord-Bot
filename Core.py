import discord
import asyncio
import Logger
import Commands
import Utilities
Client = discord.Client()


#Utilities = Utilities.Utilities()
@Client.event
async def on_ready():
    print('Logged in as')
    print(Client.user.name)
    print(Client.user.id)
    print('-------')
    print(Client)


@Client.event
async def on_message(message: discord.Message):
    if message.content.startswith('.test'):
        counter = 0
        tmp = await Client.send_message(message.channel, 'calc message')
        async for log in Client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await Client.edit_message(tmp, 'you have {} messages'.format(counter))
    elif message.content.startswith('.sleep'):
        await asyncio.sleep(5)
        await Client.send_message(message.channel, 'Done sleeping')
    elif await Utilities.one_liner(message, Client):
        return
    elif await Utilities.multiLineCommands(message, Client):
        return
    elif message.content.startswith(
            '.close') and message.author.permissions_in(
                message.channel).administrator:
        await Client.close()


Client.run('Mjc2MTEzNTQ4NDQ5NDE1MTcx.C3KeSg.Xt1ztH1_goNYIiRU27YYcJVbGk4')
