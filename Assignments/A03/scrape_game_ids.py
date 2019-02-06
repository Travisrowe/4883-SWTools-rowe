print("prog start")

import os,sys
import json
import pprint as pp
from time import sleep
from beautifulscraper import BeautifulScraper

scraper = BeautifulScraper()

years = [x for x in range(2009, 2019)]
weeks = [x for x in range(1, 18)]

gameids = {}

stype = "REG"

"""
Loop through years and weeks to get to each nfl.com/schedules page.
Then find all data-gameids inside of schedules-list-content divs
"""
for year in years:
    gameids[year] = {} #dict
    for week in weeks:
        gameids[year][week] = [] #list
        url = "http://www.nfl.com/schedules/%d/%s%s" % (year, stype, str(week))
        page = scraper.go(url)
        

        divs = page.find_all('div',{"class":"schedules-list-content"})

        for div in divs:
            print(div['data-gameid'])
            gameids[year][week].append(div['data-gameid'])
        sleep(.02) #keeps server from rejecting our requests
print("gameids dictionary...")
pp.pprint(gameids)

#save gameids to a local file and query that instead of server
with open('json_data/nfl_gameids.json', 'w') as fp:
    json.dump(gameids, fp, sort_keys=True, indent=4)