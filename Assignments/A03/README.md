This assignment scrapes data from nfl.com/schedules and nfl.com/liveupdate/game-center to ultimately find stats on football

### scrape_game_id.py
This file finds gameids of every NFL game from 2009 to 2019 using the html behind nfl.com/schedules. It does this by leveraging the url formatting used (nfl.com/schedules/year/seasontypeWeekNumber e.g. nfl.com/schedules/2018/REG16) and searching the html for the div schedules-list-content to find the gameids.

It then writes those ids to the local file '/json_data/nfl_gameids.json'

### scrape_game_data.py
This file reads nfl_gameids.json and loops through each gameid therein. It then uses urllib.request to scrape the json file of each game from http://www.nfl.com/liveupdate/game-center/ because the url uses the pattern http://www.nfl.com/liveupdate/game-center/gameid/gameid_gtd.json

This data is saved locally under json_data/live_update_data/gameid.json where gameid is the actual, unique gameid used for each game.
