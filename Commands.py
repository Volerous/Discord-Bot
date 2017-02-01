import discord
import asyncio

SFW_COMMANDS = [
    '.yak',
    '.test',
    '.sleep',
    '.chaika',
    '.anime',
    '.konosuba',
    '.konosuba_dance',
    '.lewd',
    '.butthurt',
    '.eggplant',
    '.abugin',
    '.freak_out',
    '.k',
    '.hello',
    '.meme',
    '.hesright',
    '.rikka_dance',
    '.john_cena',
    '.gay',
    '.explosion',
    '.saltbae',
    '.salt',
    '.surr20',
    '.dattebayo',
    '.bem',
    '.add',
    '.remove',
    '.nobeard'
]

NSFW_COMMANDS = [
    '.r34'
]

ONE_LINERS_LINKS = {
    '.hello' : 'https://www.youtube.com/watch?v=zdQ0J85ABX8',
    '.lewd' : 'https://i.stack.imgur.com/yICNQm.png',
    '.butthurt' : 'https://s-media-cache-ak0.pinimg.com/736x/60/b5/0c/60b50c0aeaf5b8e56dd183a8b28e5027.jpg',
    '.hesright' : 'https://i.imgur.com/8NgkZwD.jpg',
    '.rikka_dance' : 'https://31.media.tumblr.com/3b54975f9491e32b5a7d7d0f779c588b/tumblr_n5y3trN4QK1s706yxo1_500.gif',
    '.surr20' : 'http://imgur.com/a/TAYnv',
    '.saltbae' : 'http://imgur.com/a/l22go',
}
def buildFiles():
    for i in SFW_COMMANDS:
        with open('links/'+i.strip('.')+'.txt', 'w'):
            write = ''
