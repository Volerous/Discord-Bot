import discord
import asyncio

SFW_COMMANDS = [
    '.yak',
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
    '.nobeard',
    '.smash'
]

NSFW_COMMANDS = [
    '.r34'
]


def buildFiles():
    for i in SFW_COMMANDS:
        with open('links/'+i.strip('.')+'.txt', 'w'):
            write = ''
