from data import resources
from data import MENU


def check_resources_sufficient(drink, drink["ingredients"]):
    for item in drink["ingredients"]:
        ingredients[item] >= resources[item]
        print(f"sorry, there is not enough {item}")
        return False
    return True
def process_coins(quarters, dimes, nickles, pennies):
    money_in = round((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01), 2)


profit =0
should_continue = True
while should_continue:
    choice = input("What would you like, Espresso, latte or cappuccino: ")
    if choice == "off":
        should_continue = False
    elif choice == "report":
        all_water = resources["water"]
        all_milk = resources["milk"]
        all_coffee = resources["coffee"]
        print(f"water = {all_water}ml")
        print(f"milk = {all_milk}ml")
        print(f"coffee = {all_coffee}g")
        print(f"money = ${profit}")


    else:
        drink = MENU[choice]
        check_resources_sufficient(drink["ingredients"])
        if check_resources_sufficient(drink["ingredients"]):
            quarters = input("add quarters")
            dimes = input("add dimes")
            nickles = input("add nickles")
            pennies = input("add pennies")
            process_coins()

        print(drink)