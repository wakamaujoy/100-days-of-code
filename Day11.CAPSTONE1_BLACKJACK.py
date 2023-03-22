import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    selected_card = random.choice(cards)
    return selected_card


def calculate_score(user_cards, computer_cards):
    if sum(user_cards) == 21 or sum(computer_cards) == 21 and range(2):
        no = 0
        return no

    if 11 in user_cards and sum(user_cards) > 21:
        user_cards.remove(11)
        user_cards.append(1)
        user_sum = sum(user_cards)
        return user_sum

    if 11 in computer_cards and sum(computer_cards) > 21:
        computer_cards.remove(11)
        computer_cards.append(1)
        computer_sum = sum(computer_cards)
        return computer_sum


def play_game():
    deal_card()
    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        # print(user_cards)
        # print(computer_cards)
    game_over = False
    while not game_over:
        calculate_score(user_cards, computer_cards)
        print(f"Player cards:{user_cards}")
        print(f"Computer cards:{computer_cards}")
        # Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then
        #     # use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
        #
        if sum(user_cards)== 0 or sum(user_cards)>21:
            print("Game Over, You Lose!")
            game_over = True
        else:
            if_continues = input("Do you want to draw another card? type y or n")
            if if_continues == "n":
                game_over = True
                print("Game Over!")

            else:
                user_cards.append(deal_card())
                print(user_cards)
                print(computer_cards)
                calculate_score(user_cards, computer_cards)

play_game()

# #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
#
# #Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
#
# #Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
#
