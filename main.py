from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffe_machine = True

machine = CoffeeMaker()
money = MoneyMachine()
menu = Menu()


while coffe_machine:

    while True:
        options = menu.get_items()
        choice = input(f"What would you like? {options}: ")
        if choice.lower() == "off":
            exit()
        elif choice.lower() == "report":
            machine.report()
            money.report()
        elif choice.lower() not in ["espresso", "latte", "cappuccino"]:
            print(f"Please select from espresso/latte/cappuccino. Try again.")
        else:
            break

    drink = menu.find_drink(choice)
    if machine.is_resource_sufficient(drink) and money.make_payment(drink.cost):
        machine.make_coffee(drink)



