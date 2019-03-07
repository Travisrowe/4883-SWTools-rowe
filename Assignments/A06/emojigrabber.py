import os,sys
import json
import pprint as pp
from time import sleep
from beautifulscraper import BeautifulScraper
import urllib.request

"""
In this file, we use beautifulscraper to get all emojis
from a website: webfx.com. It saves all these emojis in
the ./emojis/ folder
"""

scraper = BeautifulScraper()

url = 'https://www.webfx.com/tools/emoji-cheat-sheet/'
page = scraper.go(url)

for emoji in page.find_all("span",{"class":"emoji"}):
    image_path = emoji['data-src']

    #grab name of emoji. It will be the last in the list
    web_fp = image_path.split('/')
    #print(web_fp[-1])

    # save the image using requests library
    urllib.request.urlretrieve(url, 'emojis/' + web_fp[-1])