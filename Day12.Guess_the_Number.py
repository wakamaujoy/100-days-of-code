logo ="""
   ____     _   _ U _____ u ____    ____          _____    _   _  U _____ u      _   _       _   _   __  __     ____  U _____ u   ____
U /"___|uU |"|u| |\| ___"|// __"| u/ __"| u      |_ " _|  |'| |'| \| ___"|/     | \ |"|   U |"|u| |U|' \/ '|uU | __")u\| ___"|/U |  _"\ u
\| |  _ / \| |\| | |  _|" <\___ \/<\___ \/         | |   /| |_| |\ |  _|"      <|  \| |>   \| |\| |\| |\/| |/ \|  _ \/ |  _|"   \| |_) |/
 | |_| |   | |_| | | |___  u___) | u___) |        /| |\  U|  _  |u | |___      U| |\  |u    | |_| | | |  | |   | |_) | | |___    |  _ <
  \____|  <<\___/  |_____| |____/>>|____/>>      u |_|U   |_| |_|  |_____|      |_| \_|    <<\___/  |_|  |_|   |____/  |_____|   |_| \_\
  _)(|_  (__) )(   <<   >>  )(  (__))(  (__)     _// \\_  //   \\  <<   >>      ||   \\,-.(__) )(  <<,-,,-.   _|| \\_  <<   >>   //   \\_
 (__)__)     (__) (__) (__)(__)    (__)         (__) (__)(_") ("_)(__) (__)     (_")  (_/     (__)  (./  \.) (__) (__)(__) (__) (__)  (__)
"""
import random
print(logo)
print("Welcome to the Dancing Game!")
print("i'm thinking of a number between 1 and 100")


random_number = random.randint(1,100)
print(f"pssst, the chosen number is {random_number}")
level = input("Choose a difficulty Type easy-10 attempts or hard-5 attempts :").lower()

def easy_level():
    turns = 10
    should_continue = True
    while should_continue ==True:
        guess = int(input("Enter a number between 1 and 100"))
        compare(guess)
        continues = input("Guess Again, type y or n").lower()
        if continues =="y":
            turns -=1
            if turns ==0:
                should_continue = False
                print("Game Over!")
            else:
                print(f"You have {turns} attempts remaining")
        elif continues =="n":
            should_continue = False
            print("Game Over")
        else:
            print("invalid entry")

def hard_level():
    turns = 5
    should_continue = True
    while should_continue == True:
        guess = int(input("Enter a number between 1 and 100"))
        compare(guess)
        continues = input("Guess Again, type y or n").lower()
        if continues == "y":
            turns -= 1
            if turns == 0:
                should_continue = False
                print("Game Over!")
            else:
                print(f"You have {turns} attempts remaining")
        elif continues == "n":
            should_continue = False
            print("Game Over")
def compare(guess):
    if guess > random_number:
        print("Too High")
    elif guess < random_number:
        print("Too Low")
    elif guess == random_number:
        print("You got it right, You Win!")



def game():
    if level =="easy":
        easy_level()

    elif level =="hard":
        hard_level()
    else:
        print("Invalid entry")

game()
