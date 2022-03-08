import os
import data
import art
from time import sleep


def cls():
    os.system('cls' if os.system == 'nt' else 'clear')


def power_on():
    print(art.logo)
    global machine_power
    machine_power = True


def switch_off():
    global machine_power
    machine_power = False


def take_funds(type_coffee):
    quarters = int(input("Please Enter the Number of Quarters:"))
    dimes = int(input("Please Enter the Number of Dimes:"))
    nickels = int(input("Please Enter the Number of Nickels:"))
    pennies = int(input("Please Enter the Number of Pennies:"))

    total_income = (quarters * 0.5) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)

    if data.MENU[type_coffee]['cost'] <= total_income:
        data.resources['money'] += data.MENU[type_coffee]['cost']
        print(f"Please collect your Change amount: ${total_income - data.MENU[type_coffee]['cost']}")
        return True
    else:
        print(f"Insufficient Funds, Entire ${total_income} refunded")
        return False


def check_resources(type_coffee):
    water = data.MENU[type_coffee]["ingredients"]["water"]
    milk = data.MENU[type_coffee]["ingredients"]["milk"]
    coffee = data.MENU[type_coffee]["ingredients"]["coffee"]

    if water <= data.resources["water"] and coffee <= data.resources["coffee"] and milk <= data.resources["milk"]:
        data.resources["water"] -= water
        data.resources["coffee"] -= coffee
        data.resources["milk"] -= milk
        return True
    else:
        return False


def build_report(resources):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    return f"Water: {water} \nMilk: {milk} \nCoffee: {coffee} \nMoney: ${money}  "


machine_power = None
power_on()
while machine_power:

    user_command = input("What would you like? (espresso/latte/cappuccino):")
    if user_command == 'off':
        switch_off()
    elif user_command == 'report':
        print(build_report(data.resources))
    elif user_command in data.MENU:
        if check_resources(user_command):
            if take_funds(user_command):
                print(f"Transaction Successful Here is your {user_command}")
                sleep(2)
                cls()
                print(art.logo)
        else:
            print("Insufficient resources, Apologies!")
    else:
        print("Invalid Input Try Again!")
# TODO: 1)Prompt user by asking “What would you like? (espresso/latte/cappuccino):"
# TODO: 2)Turn off the Coffee Machine by entering "off" to the prompt.
# TODO: 3)Print report.
# TODO: 4)Check resources sufficient?
# TODO: 5)Process coins.
# TODO: 6)Check transaction successful?
# TODO: 7)Make Coffee.
