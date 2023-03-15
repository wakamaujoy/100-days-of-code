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
   # bidding_dictionary[name]
    prize = max(bidding_dictionary[name])
    print(prize)
    print(f"The winner of the bid is {name} with {bid}")

end_of_bid = False
while end_of_bid == False:
    name = input("Write your name?\n")
    bid = input("Enter your bid price\n")
    bidding_dictionary[name] = bid

    addition = input("Is there another bidder in the house? type Yes or No\n").lower()
    if addition == "no":
        end_of_bid = True
        winner()
