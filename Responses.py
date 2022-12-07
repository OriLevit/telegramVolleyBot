from datetime import datetime
import Constants
import helper
from tabulate import tabulate
import scrape_main


# Generate the table using the tabulate function

def sample_responses(input_text):
    #print(helper.print_games(Constants.ALL_GAMES[0]["games"][0]))
    games=Constants.ALL_GAMES[0]["games"]
    text = helper.print_games(games)
    user_message = str(input_text).lower()
    if user_message in ("hello", "hi", "sup", "hey", "heyy", "yo", "היי", "הי", "שלום", "יו"):
        return "Hey Ori! How's it going?"
    if user_message in ("who", "who are you?"):
        return text

    return "I dont know what you said"
