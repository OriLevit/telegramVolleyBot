from urllib.request import urlopen
import Constants
import soup_manager
import helper


def get_games():
    league_table = Constants.LEAGUE_TABLE

    all_leagues_links = soup_manager.get_leagues(league_table)
    all_teams = []
    all_games = []
    counter = 1
    for link in all_leagues_links:
        print(f"{counter}/{len(all_leagues_links)}")
        counter +=1
        league_title = soup_manager.get_title(urlopen(link))
        soup_manager.get_teams(urlopen(link), all_teams)
        helper.get_games(link, league_title, all_games)

    return all_games


def get_teams():
    league_table = Constants.LEAGUE_TABLE

    all_leagues_links = soup_manager.get_leagues(league_table)
    all_teams = []
    all_games = []

    for link in all_leagues_links:
        league_title = soup_manager.get_title(urlopen(link))
        soup_manager.get_teams(urlopen(link), all_teams)
        helper.get_games(link, league_title, all_games)

    return all_teams
