logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
from data import data
import random



def presentation1(item1):
    name = item1["name"]
    descr = item1["description"]
    country = item1["country"]
    print(f"Compare A: {name},a {descr},from {country}")

def presentation2(item2):
    name = item2["name"]
    descr = item2["description"]
    country = item2["country"]
    print(f"Against B: {name},a {descr},from {country}")

def compare(selection,item1,item2):
    num = item1["follower_count"]
    dig = item2["follower_count"]
    proper_selection = max(num,dig)

    if selection == "a" and num < proper_selection:
        return "You Lose"
    elif selection == "a" and num == proper_selection:
        return "You Win"

    if selection == "b" and dig < proper_selection:
        return "You Lose"
    elif selection == "b" and dig == proper_selection:
        return "You Win"


def play_game():
    print(logo)
    item1 = random.choice(data)
    game_over = False
    while not game_over:
        item2 = random.choice(data)

        presentation1(item1)
        print(vs)
        presentation2(item2)
        selection = input("Who has more followers? Type 'A' or 'B'").lower()
        compare(selection, item1, item2)
        ans = compare(selection, item1, item2)
        print(ans)
        if ans == "You Win":
            game_over = False
            selection = item1
        else:
            game_over = True

play_game()
