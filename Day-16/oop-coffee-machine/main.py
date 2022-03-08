from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

switch = True

while switch:
    options = menu.get_items()
    user_input = input(f"What would you like to have? ({options})")

    if user_input == 'report':
        coffee_maker.report()
        money_machine.report()
    elif user_input == 'off':
        switch = False
    else:
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
                print(f"Here is your drink {drink.name}")
