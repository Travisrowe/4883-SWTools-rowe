import os,sys
import json
from pprint import pprint

"""
In this file, we will create and call functions which will calculate 
specific statistics based on our JSON files
"""

##############################################################
# calculateMostTeamsPlayed()
# This function calculates which players played on the most
# teams in their career
# 
# Params: 
#    none
#           
# Returns: 
#    playerDict - a dictionary of playerIds with a set of 
#                   team abbreviations as values
def CalculateMostTeamsPlayed():
    playerDict = {}
    with open('json_data/nfl_gameids.json', 'r') as readFP:
        data = json.load(readFP)
        for year, weeks_dict in data.items():
            print(year)
            for week, gameids in weeks_dict.items():
                for game in gameids:
                    #now that we have gameids, we loop through our live_update_data
                    with open('json_data/live_update_data/%s.json' % (game), 'r') as gameJsonFP:
                        gameData = json.load(gameJsonFP)
                        #pprint(gameData)
                        teamLabels = ["home", "away"]
                        for tLabel in teamLabels:
                            # print(tLabel)
                            # pprint(gameData[game][tLabel])

                            #here we can grab the team abbreviation of the current team
                            teamAbbrev = gameData[game][tLabel]['abbr']
                            #and loop through playerIds, adding teamAbbrev to their key's values in playerDict
                            for statType, statDict in gameData[game][tLabel]['stats'].items():
                                # print(statType)
                                # pprint(statDict)
                                if statType != "team":
                                    for playerId in statDict:
                                        #print(playerId)
                                        if not playerId in playerDict.keys():
                                            playerDict[playerId] = set()
                                        playerDict[playerId].add(teamAbbrev)
                                        # numTeamsDict = {}
                                        # if not playerId in numTeamsDict:
                                        #     numTeamsDict[playerId] = 0
                                        # for tAbbrev in playerDict[playerId]:
                                        #     numTeamsDict[playerId] += 1
                                        # pprint(numTeamsDict)
                                        # sorted(playerDict, key=playerDict.__getitem__)
                                        # pprint(playerDict)
    numTeamsDict = {}                                    
    for playerId, tAbbrev in playerDict.items():
        numTeamsDict[playerId] = len(tAbbrev)
    # pprint(numTeamsDict)
    #sorted(numTeamsDict, key = numTeamsDict.__getitem__)
    newList = []
    for key,value in sorted(numTeamsDict.items(), key=lambda kv: kv[1], reverse=True):
        newList.append((key,value))
        #print(key,value)
    pprint(newList)
    print("======================================================================================================================================================================")
    sorted(playerDict, key=newList[1])
    return(playerDict)

##############################################################
# calculateMostTeamsPlayed()
# This function calculates which players played on the most
# teams in their career
# 
# Params: 
#    none
#           
# Returns: 
#    playerDict - a dictionary of playerIds with a set of 
#                   team abbreviations as values
def CalculateNumTeamsPlayedInOneYear():
    playerDict = {}
    with open('json_data/nfl_gameids.json', 'r') as readFP:
        data = json.load(readFP)
        for year, weeks_dict in data.items():
            print(year)
            for week, gameids in weeks_dict.items():
                for game in gameids:
                    #now that we have gameids, we loop through our live_update_data
                    with open('json_data/live_update_data/%s.json' % (game), 'r') as gameJsonFP:
                        gameData = json.load(gameJsonFP)
                        #pprint(gameData)
                        teamLabels = ["home", "away"]
                        for tLabel in teamLabels:

                            #here we can grab the team abbreviation of the current team
                            teamAbbrev = gameData[game][tLabel]['abbr']
                            #and loop through playerIds, adding teamAbbrev to their key's values in playerDict
                            for statType, statDict in gameData[game][tLabel]['stats'].items():
                                if statType != "team":
                                    for playerId in statDict:
                                        #print(playerId)
                                        if not playerId in playerDict.keys():
                                            playerDict[playerId] = {}
                                            playerDict[playerId]["playerName"] = statDict[playerId]['name']
                                        if not year in playerDict[playerId].keys():
                                            playerDict[playerId][year] = set()
                                        playerDict[playerId][year].add(teamAbbrev)
    
    return(playerDict)

##############################################################
# MostYardsByRushesForLoss(gameids, playerDict)
# This function calculates which players lost the most yards
# by rushes for a loss in their career. It uses the NFL statId of 10
# to find which plays were considered a "rush"
# 
# Params: 
#    gameids [list] : a list of gameids to iterate
#    playerDict [dictionary] : a reference parameter, 
#
# Returns: 
#    playerDict - a dictionary of playerIds with the
#           total number of yards lost from rushing
def MostYardsByRushesForLoss():
    playerDict = {}
    with open('json_data/nfl_gameids.json', 'r') as readFP:
        data = json.load(readFP)
        for year, weeks_dict in data.items():
            print(year)
            for week, gameids in weeks_dict.items():
                for game in gameids:
                    #now that we have gameids, we loop through our live_update_data
                    with open('json_data/live_update_data/%s.json' % (game), 'r') as gameJsonFP:
                        gameData = json.load(gameJsonFP)
                        for driveId, driveData in gameData[game]['drives'].items():
                            if driveId != "crntdrv":
                                #pprint(driveData)
                                for playId, playData in driveData['plays'].items():
                                    for playerId, playerData in playData['players'].items():
                                        if playerId != '0':
                                            if playerData[0]['statId'] == 10:
                                                if type(playerData[0]['yards']) is int:
                                                    if playerData[0]['yards'] < 0:
                                                        #check if the player is already in the dictionary
                                                        if not playerId in playerDict:
                                                            playerDict[playerId] = {}
                                                            playerDict[playerId]["name"] = playerData[0]['playerName']
                                                            playerDict[playerId]["yardsLost"] = 0
                                                        playerDict[playerId]["yardsLost"] += playerData[0]['yards']
                                                        #sorted(playerDict.values()["yardsLost"])
    #sorted(playerDict.values()["yardsLost"])
    pprint(playerDict)

##############################################################
# MostRushesForLoss(gameids, playerDict)
# This function calculates which players had the most rushes
# for a loss in their career. It uses the NFL statId of 10
# to find which plays were considered a "rush"
# 
# Params: 
#    gameids [list] : a list of gameids to iterate
#    playerDict [dictionary] : a reference parameter, 
#
# Returns: 
#    playerDict - a dictionary of playerIds with the
#           total number of yards lost from rushing
def MostRushesForLoss():
    playerDict = {}
    with open('json_data/nfl_gameids.json', 'r') as readFP:
        data = json.load(readFP)
        
        for year, weeks_dict in data.items():
            print(year)
            for week, gameids in weeks_dict.items():
                for game in gameids:
                    #now that we have gameids, we loop through our live_update_data
                    with open('json_data/live_update_data/%s.json' % (game), 'r') as gameJsonFP:
                        gameData = json.load(gameJsonFP)
                        for driveId, driveData in gameData[game]['drives'].items():
                            if driveId != "crntdrv":
                                #pprint(driveData)
                                for playId, playData in driveData['plays'].items():
                                    for playerId, playerData in playData['players'].items():
                                        if playerId != '0':
                                            if playerData[0]['statId'] == 10:
                                                if type(playerData[0]['yards']) is int:
                                                    if playerData[0]['yards'] < 0:
                                                        #check if the player is already in the dictionary
                                                        if not playerId in playerDict:
                                                            playerDict[playerId] = {}
                                                            playerDict[playerId]["name"] = playerData[0]['playerName']
                                                            playerDict[playerId]["numRushes"] = 0
                                                        playerDict[playerId]["numRushes"] += 1
                                                        #sorted(playerDict.values()["yardsLost"])
    #sorted(playerDict.values()["yardsLost"])
    pprint(playerDict)

##############################################################
# MostRushesForLoss()
# This function calculates which players had the most rushes
# for a loss in their career. It uses the NFL statId of 15
# to find which plays were considered a "rush"
# 
# Params: 
#    none
#
# Returns: 
#    playerDict - a dictionary of playerIds with the
#           total number of yards lost from rushing
def MostPassesForLoss():
    playerDict = {}
    with open('json_data/nfl_gameids.json', 'r') as readFP:
        data = json.load(readFP)
        for year, weeks_dict in data.items():
            print(year)
            for week, gameids in weeks_dict.items():
                for game in gameids:
                    #now that we have gameids, we loop through our live_update_data
                    with open('json_data/live_update_data/%s.json' % (game), 'r') as gameJsonFP:
                        gameData = json.load(gameJsonFP)
                        for driveId, driveData in gameData[game]['drives'].items():
                            if driveId != "crntdrv":
                                #pprint(driveData)
                                for playId, playData in driveData['plays'].items():
                                    for playerId, playerData in playData['players'].items():
                                        if playerId != '0':
                                            if playerData[0]['statId'] == 15:
                                                if type(playerData[0]['yards']) is int:
                                                    if playerData[0]['yards'] < 0:
                                                        #check if the player is already in the dictionary
                                                        if not playerId in playerDict:
                                                            playerDict[playerId] = {}
                                                            playerDict[playerId]["name"] = playerData[0]['playerName']
                                                            playerDict[playerId]["numPasses"] = 0
                                                        playerDict[playerId]["numPasses"] += 1
                                                        #sorted(playerDict.values()["yardsLost"])
    #sorted(playerDict.values()["yardsLost"])
    pprint(playerDict)
    return playerDict

##############################################################
# MostRushesForLoss(playerDict)
# This function calculates which players had the most rushes
# for a loss in their career. It uses the NFL statId of 15
# to find which plays were considered a "rush"
# 
# Params: 
#    none
#
# Returns: 
#    playerDict - a dictionary of playerIds with the
#           total number of yards lost from rushing
def TeamWithMostPenalties():
    teamDict = {}
    with open('json_data/nfl_gameids.json', 'r') as readFP:
        data = json.load(readFP)
        for year, weeks_dict in data.items():
            print(year)
            for week, gameids in weeks_dict.items():
                for game in gameids:
                    #now that we have gameids, we loop through our live_update_data
                    with open('json_data/live_update_data/%s.json' % (game), 'r') as gameJsonFP:
                        gameData = json.load(gameJsonFP)
                        teamLabels = ["home", "away"]
                        for tLabel in teamLabels:
                            # print(tLabel)
                            # pprint(gameData[game][tLabel])

                            #here we can grab the team abbreviation of the current team
                            teamAbbrev = gameData[game][tLabel]['abbr']

                            #Note that team stats are totalled for each game under 
                            # gameData[game][tLabel]['stats']['team']
                            #Therfore, all we have to do is access
                            # gameData[game][tLabel]['stats']['team']['pen']
                            # and add that number to our teamDict
                            if not teamAbbrev in teamDict:
                                teamDict[teamAbbrev] = 0
                            teamDict[teamAbbrev] += gameData[game][tLabel]['stats']['team']['pen']
    #sorted(playerDict.values()["yardsLost"])
    return teamDict

##############################################################
# MostRushesForLoss(playerDict)
# This function calculates which players had the most rushes
# for a loss in their career. It uses the NFL statId of 15
# to find which plays were considered a "rush"
# 
# Params: 
#    none
#
# Returns: 
#    playerDict - a dictionary of playerIds with the
#           total number of yards lost from rushing
def TeamWithMostPenaltyYards():
    teamDict = {}
    with open('json_data/nfl_gameids.json', 'r') as readFP:
        data = json.load(readFP)
        for year, weeks_dict in data.items():
            print(year)
            for week, gameids in weeks_dict.items():
                for game in gameids:
                    #now that we have gameids, we loop through our live_update_data
                    with open('json_data/live_update_data/%s.json' % (game), 'r') as gameJsonFP:
                        gameData = json.load(gameJsonFP)
                        teamLabels = ["home", "away"]
                        for tLabel in teamLabels:
                            # print(tLabel)
                            # pprint(gameData[game][tLabel])

                            #here we can grab the team abbreviation of the current team
                            teamAbbrev = gameData[game][tLabel]['abbr']

                            #Note that team stats are totalled for each game under 
                            # gameData[game][tLabel]['stats']['team']
                            #Therfore, all we have to do is access
                            # gameData[game][tLabel]['stats']['team']['penyds']
                            # and add that number to our teamDict
                            if not teamAbbrev in teamDict:
                                teamDict[teamAbbrev] = 0
                            teamDict[teamAbbrev] += gameData[game][tLabel]['stats']['team']['penyds']
    #sorted(playerDict.values()["yardsLost"])
    return teamDict

##############################################################
# MostRushesForLoss()
# This function calculates which players had the most rushes
# for a loss in their career. It uses the NFL statId of 15
# to find which plays were considered a "rush"
# 
# Params: 
#    none
#
# Returns: 
#    playerDict - a dictionary of playerIds with the
#           total number of yards lost from rushing
def CalculateAverageNumPlaysInAGame():
    gameCount = 0
    playCount = 0
    with open('json_data/nfl_gameids.json', 'r') as readFP:
        data = json.load(readFP)
        for year, weeks_dict in data.items():
            print(year)
            for week, gameids in weeks_dict.items():
                for game in gameids:
                    #add 1 to number of games
                    gameCount += 1
                    
                    #now that we have gameids, we loop through our live_update_data
                    with open('json_data/live_update_data/%s.json' % (game), 'r') as gameJsonFP:
                        gameData = json.load(gameJsonFP)
                        for driveId, driveData in gameData[game]['drives'].items():
                            if driveId != "crntdrv":
                                #pprint(driveData)
                                for playId, playData in driveData['plays'].items():
                                    # add 1 to number of plays
                                    playCount += 1
    return playCount / gameCount

##############################################################
# MostRushesForLoss()
# This function calculates which players had the most rushes
# for a loss in their career. It uses the NFL statId of 70
# to find which plays were considered a "field goal"
# 
# Params: 
#    none
#
# Returns: 
#    playerDict - a dictionary of playerIds with the
#           total number of yards lost from rushing
def CalculateLongestFieldGoal():
    fieldGoalDict = {}
    fieldGoalDict["longestFieldGoal"] = 0
    fieldGoalDict["kickerName"] = "N/A"
    with open('json_data/nfl_gameids.json', 'r') as readFP:
        data = json.load(readFP)
        for year, weeks_dict in data.items():
            print(year)
            for week, gameids in weeks_dict.items():
                for game in gameids:
                    #now that we have gameids, we loop through our live_update_data
                    with open('json_data/live_update_data/%s.json' % (game), 'r') as gameJsonFP:
                        gameData = json.load(gameJsonFP)
                        for driveId, driveData in gameData[game]['drives'].items():
                            if driveId != "crntdrv":
                                #pprint(driveData)
                                for playId, playData in driveData['plays'].items():
                                    for playerId, playerData in playData['players'].items():
                                        if playerId != '0':
                                            if playerData[0]['statId'] == 70:
                                                if type(playerData[0]['yards']) is int:
                                                    if playerData[0]['yards'] > fieldGoalDict["longestFieldGoal"]:
                                                        fieldGoalDict["longestFieldGoal"] = playerData[0]['yards']
                                                        fieldGoalDict["kickerName"] = playerData[0]['playerName']
                                                        
    #sorted(playerDict.values()["yardsLost"])
    return fieldGoalDict

##############################################################
# MostRushesForLoss()
# This function calculates which players had the most rushes
# for a loss in their career. It uses the NFL statId of 70
# to find which plays were considered a "field goal"
# 
# Params: 
#    none
#
# Returns: 
#    playerDict - a dictionary of playerIds with the
#           total number of yards lost from rushing
def MostFieldGoals():
    fieldGoalDict = {}
    with open('json_data/nfl_gameids.json', 'r') as readFP:
        data = json.load(readFP)
        for year, weeks_dict in data.items():
            print(year)
            for week, gameids in weeks_dict.items():
                for game in gameids:
                    #now that we have gameids, we loop through our live_update_data
                    with open('json_data/live_update_data/%s.json' % (game), 'r') as gameJsonFP:
                        gameData = json.load(gameJsonFP)
                        for driveId, driveData in gameData[game]['drives'].items():
                            if driveId != "crntdrv":
                                #pprint(driveData)
                                for playId, playData in driveData['plays'].items():
                                    for playerId, playerData in playData['players'].items():
                                        if playerId != '0':
                                            if playerData[0]['statId'] == 70:
                                                if not playerId in fieldGoalDict:
                                                    fieldGoalDict[playerId] = {}
                                                    fieldGoalDict[playerId]["numFieldGoals"] = 0
                                                    fieldGoalDict[playerId]["kickerName"] = playerData[0]['playerName']
                                                fieldGoalDict[playerId]["numFieldGoals"] += 1
                                                        
    #sorted(playerDict.values()["yardsLost"])
    return fieldGoalDict

##############################################################
# MostRushesForLoss()
# This function calculates which players had the most rushes
# for a loss in their career. It uses the NFL statId of 69
# to find which plays were considered a "field goal"
# 
# Params: 
#    none
#
# Returns: 
#    playerDict - a dictionary of playerIds with the
#           total number of yards lost from rushing
def MostMissedFieldGoals():
    fieldGoalDict = {}
    with open('json_data/nfl_gameids.json', 'r') as readFP:
        data = json.load(readFP)
        for year, weeks_dict in data.items():
            print(year)
            for week, gameids in weeks_dict.items():
                for game in gameids:
                    #now that we have gameids, we loop through our live_update_data
                    with open('json_data/live_update_data/%s.json' % (game), 'r') as gameJsonFP:
                        gameData = json.load(gameJsonFP)
                        for driveId, driveData in gameData[game]['drives'].items():
                            if driveId != "crntdrv":
                                #pprint(driveData)
                                for playId, playData in driveData['plays'].items():
                                    for playerId, playerData in playData['players'].items():
                                        if playerId != '0':
                                            if playerData[0]['statId'] == 69:
                                                if not playerId in fieldGoalDict:
                                                    fieldGoalDict[playerId] = {}
                                                    fieldGoalDict[playerId]["numFieldGoals"] = 0
                                                    fieldGoalDict[playerId]["kickerName"] = playerData[0]['playerName']
                                                fieldGoalDict[playerId]["numFieldGoals"] += 1
                                                        
    #sorted(playerDict.values()["yardsLost"])
    return fieldGoalDict

# gameData[gameId][‘drives’][‘plays’][playId]    
#     If “dropped” in [‘desc’] AND “pass” in [‘desc’]:
#         If [‘players’][playerId][‘statId’] = 115
#             Add 1 to playerDict[playerId]

##############################################################
# MostRushesForLoss()
# This function calculates which players had the most rushes
# for a loss in their career. It uses the NFL statId of 115
# to find which plays were considered a "field goal"
# 
# Params: 
#    none
#
# Returns: 
#    playerDict - a dictionary of playerIds with the
#           total number of yards lost from rushing
def MostDroppedPasses():
    playerDict = {}
    with open('json_data/nfl_gameids.json', 'r') as readFP:
        data = json.load(readFP)
        for year, weeks_dict in data.items():
            print(year)
            for week, gameids in weeks_dict.items():
                for game in gameids:
                    #now that we have gameids, we loop through our live_update_data
                    with open('json_data/live_update_data/%s.json' % (game), 'r') as gameJsonFP:
                        gameData = json.load(gameJsonFP)
                        for driveId, driveData in gameData[game]['drives'].items():
                            #crntdrv (current drive) generally points to the last drive of the game
                            #unless the game is ongoing. It should be ignored
                            if driveId != "crntdrv":
                                for playId, playData in driveData['plays'].items():
                                    #look for plays that have the words "dropped" and 
                                    # "pass" in their description
                                    if 'dropped' in playData['desc'] and "pass" in playData['desc']:
                                        for playerId, playerData in playData['players'].items():
                                            #the player who dropped the pass will have statId of 115
                                            if playerData[0]['statId'] == 115:
                                                if not playerId in playerDict:
                                                    playerDict[playerId] = {}
                                                    playerDict[playerId]["playerName"] = playerData[0]['playerName']
                                                    playerDict[playerId]["numDroppedPasses"] = 0
                                                playerDict[playerId]["numDroppedPasses"] += 1
                                                        
    #sorted(playerDict.values()["yardsLost"])
    return playerDict

######################################################
# Main function
# with open('json_data/nfl_gameids.json', 'r') as readFP:
#     data = json.load(readFP)
playerDict = {}
teamDict = {}
fieldGoalDict = {}
# for year, weeks_dict in data.items():
#     #print(year)
#     for week, gameids in weeks_dict.items():
#         #call functions here
playerDict = CalculateMostTeamsPlayed()


# ==================================================================================
# 1. Find the player(s) that played for the most teams.

# Answer:

# Player 1 played for X teams.
# Player 2 played for X teams.

# playerDict = CalculateNumTeamsPlayedInOneYear()
# MostYardsByRushesForLoss(playerDict)
# MostRushesForLoss(playerDict)
# playerDict = MostPassesForLoss()
# teamDict = TeamWithMostPenalties()
# teamDict = TeamWithMostPenaltyYards()
# avgNumPlays = CalculateAverageNumPlaysInAGame()
# fieldGoalDict = CalculateLongestFieldGoal()
# fieldGoalDict = MostFieldGoals()
# fieldGoalDict = MostMissedFieldGoals()
# playerDict = MostDroppedPasses()
pprint(playerDict)
#print(avgNumPlays)

        


# sorted(len(playerDict.values()))
# pprint(playerDict)
