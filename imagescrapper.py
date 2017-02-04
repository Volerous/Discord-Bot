from bs4 import BeautifulSoup
import urllib
import requests
import os
import sys

def scrapePage(url):
    siteSoup = BeautifulSoup(requests.get(url).text, 'html.parser')
    print(siteSoup.find('img')['src'])

for paths,subdirs,files in os.walk('D:\Documents\GitHub\Discord Bot\links'):
    for file in files:
        with open(os.path.join(paths,file), 'r') as openfile:
            urls =  
