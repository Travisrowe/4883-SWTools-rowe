This assignment scrapes data from nfl.com/schedules and nfl.com/liveupdate/game-center to ultimately find stats on football

## Note on running the program
To properly execute this code, you must run scrape_game_id.py BEFORE you run scrape_game_data.py
Afterward, you can run calculate_stats.py to learn about some pre-programmed NFL stats!

### scrape_game_id.py
This file finds gameids of every NFL game from 2009 to 2019 using the html behind nfl.com/schedules. It does this by leveraging the url formatting used (nfl.com/schedules/year/seasontypeWeekNumber e.g. nfl.com/schedules/2018/REG16) and searching the html for the div schedules-list-content to find the gameids.

It then writes those ids to the local file '/json_data/nfl_gameids.json'

### scrape_game_data.py
This file reads nfl_gameids.json and loops through each gameid therein. It then uses urllib.request to scrape the json file of each game from http://www.nfl.com/liveupdate/game-center/ because the url uses the pattern http://www.nfl.com/liveupdate/game-center/gameid/gameid_gtd.json

This data is saved locally under json_data/live_update_data/gameid.json where gameid is the actual, unique gameid used for each game.

### calculate_stats.py
This file uses the scraped game data, written by scrape_game_data.py, to calculate and print out some pre-programmed NFL stats.
Those stats, in order, are:

    1. Find the player(s) that played for the most teams.
    2. Find the player(s) that played for multiple teams in one year.
    3. Find the player(s) that had the most yards rushed for a loss.
    4. Find the player(s) that had the most rushes for a loss.
    5. Find the player(s) with the most number of passes for a loss.
    6. Find the team with the most penalties.
    7. Find the team with the most yards in penalties.
    8. Find the correlation between most penalized teams and games won / lost.
    9. Average number of plays in a game.
    10. Longest field goal.
    11. Most field goals.
    12. Most missed field goals.
    13. Most dropped passes (Search for "pass" and "dropped" in play description, and stat-id 115).

