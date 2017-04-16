from bs4 import BeautifulSoup
import urllib
import requests
import os
import sys


def scrapePage(url):
    siteSoup = BeautifulSoup(requests.get(url).text, 'html.parser')
    return(siteSoup.find('img')['src'])

def scrapeFile(file):
    openfile = open(file, 'r')
    urls = openfile.readlines()
    openfile.close()
    for i in range(len(urls)):
        if '.gif' not in urls[i] and '.jpg' not in urls[i] and 'png' not in urls[i]:
            urls[i] = scrapePage(urls[i])
            print(urls[i])
    openfile = open(file, 'w')
    for url in urls:
        if '\n' not in url:
            url = url + '\n'
        openfile.write(url)
    openfile.close()

'''
for paths,subdirs,files in os.walk('D:\Documents\GitHub\Discord Bot\links'):
    for file in files:
        print(file)
        scrapeFile(file)'''
#scrapeFile('D:\Documents\GitHub\Discord Bot\links\mugi.txt')