import operator
from urllib.request import urlopen
from prettytable import PrettyTable
import soup_manager


def print_all_games(all_games: list):
    for _ in range(len(all_games)):
        print_games(all_games[_]["games"], all_games[_]["title"])


def get_games(link, league_title, all_games):
    league_games = []
    soup_manager.get_upcoming_games(urlopen(link), league_games)
    league_games.sort(key=operator.itemgetter('date'))
    league = {
        "games": league_games,
        "title": league_title
    }
    all_games.append(league)


def print_teams(teams_list: list):
    teams_list.sort(key=operator.itemgetter('score'), reverse=True)
    t = PrettyTable(["קבוצה", "ניקוד"])
    for team in teams_list:
        t.add_row([team["name"], team["score"]])
    return (t)


def print_games(games_list: list):
    final_msg = ""
    counter = 1
    for game in games_list:
        final_msg += "------------------------------------------------------------------------"
        final_msg += f"\nמשחק #{counter}\n"
        final_msg += f"\nמתי?"
        final_msg += f"\nבתאריך {game['date']} בשעה {game['time']}"
        final_msg += f"\nמי?"
        final_msg += f"\n{game['first_team']}  *נגד*  {game['second_team']}" + "\n"
        final_msg += f"\nאיפה?"
        final_msg += f"\n{game['venue']}" + "\n"

        counter += 1
    final_msg += "------------------------------------------------------------------------"
    return final_msg


def get_teams_sorted(league_table):
    all_leagues_links = soup_manager.get_leagues(league_table)
    all_teams = []

    for link in all_leagues_links:
        soup_manager.get_teams(link, all_teams)
        return all_teams


def print_all_leagues(game_list):
    leagues = ""
    counter = 1
    for league in game_list:
        leagues += f"\n{counter}. {league['title']}"
        counter+=1
    return leagues+"\n"
