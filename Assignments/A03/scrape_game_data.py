import json
from pprint import pprint
import urllib.request
from time import sleep

"""
In this file we will loop through the game ids we scraped in scrape_game_ids.py, 
which we saved in json_data/nfl_gameids.json. Then we will leverage the use of those game ids in
the url http://www.nfl.com/liveupdate/game-center/gameid/gameid_gtd.json to scrape data from each football
game since 2009 and save that data locally
"""

years = [x for x in range(2009, 2019)]
weeks = [x for x in range(1,18)]

with open('json_data/nfl_gameids.json', 'r') as readFP:
    data = json.load(readFP)

for year, weeks_dict in data.items():
    print(year)
    for week, gameids in weeks_dict.items():
        print(week)
        for game in gameids:
            print(game)
            url = 'http://www.nfl.com/liveupdate/game-center/%s/%s_gtd.json' % (game, game)

            urllib.request.urlretrieve(url, 'json_data/live_update_data/' + game + '.json')