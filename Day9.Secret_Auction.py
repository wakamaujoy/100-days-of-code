logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
bidding_dictionary = {}

def winner():
    #print(bidding_dictionary)
    highest_bid = 0
    winner =""

    for most in bidding_dictionary:
        prize = bidding_dictionary[most]
        if prize > highest_bid:
            highest_bid = prize
            winner = most
    print(f"The winner of the bid is {winner} with {highest_bid}")

end_of_bid = False
while end_of_bid == False:
    name = input("Write your name?\n")
    bid = int(input("Enter your bid price\n"))
    bidding_dictionary[name] = (bid)

    addition = input("Is there another bidder in the house? type Yes or No\n").lower()
    if addition == "no":
        end_of_bid = True
        winner()
