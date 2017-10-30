from bs4 import BeautifulSoup
import urllib
import requests
import os
import sys


def scrapeFile(file):
    openfile = open(file, 'r')
    urls = openfile.readlines()
    openfile.close()
    for i in range(len(urls)):   
        urls[i] = requests.get(urls[i]).url
        print(urls[i])
    openfile = open(file, 'w')
    for url in urls:
        if '\n' not in url:
            url = url + '\n'
        openfile.write(url)
    openfile.close()

"""
for paths,subdirs,files in os.walk('D:\Documents\GitHub\Discord Bot\links'):
    for file in files:
        print(paths+ "\\" + file)
        scrapeFile(paths+ "\\" + file)
# scrapeFile('D:\Documents\GitHub\Discord Bot\links\\anime.txt')
# scrapePage("http://s19.postimg.org/oc3w471uq/No_Game_No_Life.jpg")
"""