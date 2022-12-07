from datetime import datetime
import Constants
import helper
from tabulate import tabulate
import scrape_main


# Generate the table using the tabulate function
def sample_responses(update,input_text):
    #print(helper.print_games(Constants.ALL_GAMES[0]["games"][0]))
    user_message = str(input_text).lower()

    #games = Constants.ALL_GAMES[league_number]["games"]
    #text = helper.print_games(games)
    if user_message in ("hello", "hi", "sup", "hey", "heyy", "yo", "היי", "הי", "שלום", "יו"):
        return "Hey Ori! How's it going?"
    if user_message in ("who", "who are you?","ליגה"):
        return helper.print_all_leagues(Constants.ALL_GAMES)
    else:
        return "I dont know what you said"
