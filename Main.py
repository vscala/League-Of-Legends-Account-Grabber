# Project Created By: Finnegan McGuire
# Status: In Progress
# Date Started: 11/16/2019 (1:20 AM, EST)

# Imports
import json
import requests
from colorama import init
from colorama import Fore, Back, Style

# Colorama init
init(autoreset=True)

summonerName = input('Summoner Name: ')
APIKey = input('API KEY: ')

print("An Error Occured")
print("=====================================================")
print(Fore.BLUE + Back.WHITE + "Connection to API Successful and Account Detected")

print('COMMANDS: ')
print(Fore.RED + 'getaccount | listmasterys | checkmatchinfo | getfreechamps | currentgameinfo')

# API LINKS
addressAccInfo = f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}?api_key={APIKey}'
addressChampRot = f'https://na1.api.riotgames.com/lol/platform/v3/champion-rotations?api_key={APIKey}'


# Parses JSON into a manipulible information from the JSON link
def parse(link):
    jsonlink = requests.get(link)
    parseinfo = jsonlink.json()
    return parseinfo

# Getting Json Info from League Of Legends API web address
AccInfo = parse(f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}?api_key={APIKey}')
encryptedId = AccInfo['id']

# Parsing all the JSON info into usable data
SpectatorGame = parse(f'https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{encryptedId}?api_key={APIKey}')
ChampionList = parse(f'http://ddragon.leagueoflegends.com/cdn/9.22.1/data/en_US/champion.json')
ChampRot = parse(f'https://na1.api.riotgames.com/lol/platform/v3/champion-rotations?api_key={APIKey}')
ChampMastery = parse(f'https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedId}?api_key={APIKey}')
ChampionListMasterys = parse(f'https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedId}?api_key={APIKey}')
Gamemodes = parse(f'http://static.developer.riotgames.com/docs/lol/gameModes.json')

appRunning = True
FREE_CHAMPION_IDS = ChampRot['freeChampionIds']

# COMMANDS / While Loop to keep shit runnin
while appRunning:
    userInput = input('> ').lower()

    if userInput == 'getaccount':
        print('-----------------')
        for items in AccInfo:
            print(items.title() + ': ' + Fore.LIGHTYELLOW_EX + str(AccInfo[items]))

    # Lists Masteries and changes champion id's to champion names for a more readible experience for user.
    if userInput == 'listmasterys':
        for items in ChampionListMasterys:
            print('------------------')

            # Convert Champion Id's into Champ Name
            for x in items:
                if x.lower() == 'championid':
                    for y in ChampionList['data']:
                        if items[x] == int(ChampionList['data'][y]['key']):
                            items[x] = ChampionList['data'][y]['name']

                print(x.title() + ': ' + str(items[x]))

    # Idetifies specific match (Match Id Needed) & Displays Info
    if userInput == 'checkmatchinfo':
        matchID = input('Match ID: ')
        addressMatch = f'https://na1.api.riotgames.com/lol/match/v4/matches/{matchID}?api_key={APIKey}'
        MatchInfo = parse(addressMatch)

        print('------------------------')
        print('Season: ' + str(MatchInfo['seasonId']))
        print('Map: ' + str(MatchInfo['mapId']).replace('11', 'Summoners Rift'))
        print(MatchInfo['teams']['teamId'])

    # Displays Free Champion Data (Shows Id's and not names of champs so can be changed for easier readable info for user)
    if userInput == 'getfreechamps':
        print(ChampRot['freeChampionIds'])

    # Work In Progress
    if userInput == 'currentgameinfo':

        print(" ")
        print(Back.RED + Fore.WHITE + "-------- GAME INFO --------")
        for items in SpectatorGame:
            print(items.title() + ': ' + Fore.YELLOW + str(SpectatorGame[items]))

    if userInput == '':
        break
