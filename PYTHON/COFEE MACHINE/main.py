from menu import Menu, MenuItem
from coffeeMaker import CoffeeMaker
from money_machine import MoneyMachine
my_money = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True
while is_on == True:
    options = menu.get_items()
    user_choice = input(f"What would you like to have {options}?\n")
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        coffee_maker.report()
        my_money.report()
    elif user_choice != "latte" and user_choice != "espresso" and user_choice != "cappuccino":
        print("Wrong input please try again.")
    else:
        drink = menu.find_drink(user_choice)
        print(drink)
        if coffee_maker.is_resource_sufficient(drink) == True:
            if my_money.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
            else:
                0
        else:
            0
