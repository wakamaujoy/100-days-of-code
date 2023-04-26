from menu import Menu,MenuItem
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
coffee = CoffeeMaker()
money = MoneyMachine()

menu = Menu()
is_on = True
while is_on:
    choice = input(f"What would you like?{menu.get_items()}")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)


