from urllib.request import urlopen

import scrape_main

API_KEY = "5942002978:AAEbSswU9yB_GxkLI7Z3rQjICfD4eV2PaPs"
LEAGUE_TABLE = urlopen('https://www.iva.org.il/boards.asp')
ALL_GAMES = scrape_main.get_games()
#ALL_TEAMS = scrape_main.get_teams()

