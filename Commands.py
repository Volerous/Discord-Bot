import discord
import asyncio
import youtube_dl

SFW_COMMANDS = [
    '.weeaboo',
    '.hello',
    '.rikka_dance',
    '.surr20',
    '.saltbae',
    '.lewd',
    '.nobeard',
    '.butthurt',
    '.hesright',
    '.john_cena',
    '.gay',
    '.anime',
    '.yak',
    '.abugin',
    '.dattebayo',
    '.eggplant',
    '.smash',
    '.freak_out',
    '.konosuba_dance',
    '.fucku',
    '.explosion',
    '.dennis',
    '.tilt',
    '.okay',
    '.huh',
    '.helpme',
    '.plot',
    '.martin',
    '.kys',
    '.feels',
    '.mugi',
    '.blackbaby',
    '.arabruski'
]
FUNC_COMMANDS = [
    '.add',
    '.help',
    '.remove',
    '.add_link'
]

NSFW_COMMANDS = [
    '.r34'
]


def buildFiles():
    for i in SFW_COMMANDS:
        with open('links/' + i.strip('.') + '.txt', 'w'):
            write = ''
'''
ytdlopts = {
    'get_id': True
}
with youtube_dl.YoutubeDL(ytdlopts) as ytdl:
    ie = youtube_dl.extractor.YoutubeChannelIE()
    video_list = ytdl.extract_info(
        'https://www.youtube.com/channel/UCI7HWYaijk2ChE9Ce5YCgAQ', download=False)
for i in video_list:
    print(video_list)
'''