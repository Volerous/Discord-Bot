import discord
import asyncio
import youtube_dl

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