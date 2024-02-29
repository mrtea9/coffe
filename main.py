from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffe_machine = True

machine = CoffeeMaker()
money = MoneyMachine()
menu = Menu()


while coffe_machine:

    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
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
    if machine.is_resource_sufficient(drink):
        if money.make_payment(drink.cost):
            machine.make_coffee(drink)

    machine.report()
    money.report()

