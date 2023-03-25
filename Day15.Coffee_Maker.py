from data import MENU, resources

def choice_made(choice):
    if choice == "espresso":
       return MENU["espresso"]["cost"]
    elif choice == "latte":
        return MENU["latte"]["cost"]
    elif choice == "cappuccino":
        return MENU["cappuccino"]["cost"]

def money(quarters,dimes,nickels,pennies):
    money_put = round((quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01), 2)
    return money_put


def manage_resources():

def order_coffee():
    game_over = False
    while not game_over:
        choice = input("What would you like?(espresso/latte/cappuccino):").lower()
        if choice == "report":
            game_over = True
            manage_resources()

        else:
            choice_made(choice)
        price = choice_made(choice)
        print(f"placed order is $: {price}")
        print("Please insert coins.")
        quarters = int(input("How many quarters?:"))
        dimes = int(input("How many dimes?:"))
        nickels = int(input("How many nickels?:"))
        pennies = int(input("How many pennies"))
        money(quarters,dimes,nickels,pennies)
        money_submitted = money(quarters,dimes,nickels,pennies)
        print(f"money submited is {money_submitted}")
        change = round(money_submitted - price,2)
        print(f"your balance is {change}")
        if change < 0:
            print("Sorry that's not enough money. Money refunded.")
            game_over = True
        else:
            print(f"Here is {change} in change, enjoy your {choice}☕️!")


order_coffee()