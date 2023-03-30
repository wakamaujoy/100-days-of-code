from data import resources, MENU


def check_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry, there is not enough {item}")
            return False
    return True


def process_coins():
    print("Please insert coins")
    quarters = int(input("add quarters"))
    dimes = int(input("add dimes"))
    nickles = int(input("add nickles"))
    pennies = int(input("add pennies"))
    money_in = round((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01), 2)
    return money_in
def check_transaction_successful(paid, cost):
    if paid < cost:
        print('Sorry, the amount is not sufficient')
        return False
    elif paid >= cost:
        return True


profit = 0
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
        if check_resources_sufficient(drink["ingredients"]):
            paid = process_coins()
            if check_transaction_successful(paid, drink["cost"]):
                balance = paid - drink["cost"]
                profit += drink["cost"]
                for item in resources:
                    resources[item] -= drink["ingredients"][item]


            print(f"Here is your balance {balance}, enjoy your {choice}")

