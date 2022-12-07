from urllib.request import urlopen

import scrape_main

API_KEY = "5942002978:AAEbSswU9yB_GxkLI7Z3rQjICfD4eV2PaPs"
LEAGUE_TABLE = urlopen('https://www.iva.org.il/boards.asp')
ALL_GAMES = scrape_main.get_games()
#ALL_TEAMS = scrape_main.get_teams()
MEN = [1,2,6,7,10,11,12,13,14,46,47]
WOMEN = [3,4,5,8,9,15,16,17]
GIRLS = [21,22,23,26,27,36,37,38,39,40,41,42,43,44,45]
BOYS = [18,19,20,24,25,28,29,30,31,32,33,34,35]
