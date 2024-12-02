from menu import Menu, MenuItem
from coffeeMaker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

is_on = True
user = input("What would you like? (espresso/latte/cappuccino):\n")
while is_on:
    if user == "off":
        is_on = False
    elif user == "report":
        coffeeMaker.report()
        moneyMachine.report()
        user = input("What would you like? (espresso/latte/cappuccino):\n")
    elif user in menu.get_items():
        drink = menu.find_drink(user)
        if coffeeMaker.is_resource_sufficient(drink):
            print(f"Your bill is ${menu.find_drink(user).cost}")
            if moneyMachine.make_payment(menu.find_drink(user).cost):
                coffeeMaker.make_coffee(drink)
                user = input(
                    "What would you like? (espresso/latte/cappuccino):\n")
        else:
            user = input("What would you like? (espresso/latte/cappuccino):\n")

    else:
        user = input("What would you like? (espresso/latte/cappuccino):\n")
