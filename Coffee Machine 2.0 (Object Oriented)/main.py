import menu
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

game = True

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

money_machine.report()

while game is True:
    menu = Menu()
    answer = input(f"What would you like? {menu.get_items()}: ")

    if answer == "off":
        game = False
        print("Goodbye!")
        break
    elif answer == "report":
        coffee_maker.report()
    else:
        order = menu.find_drink(answer)

        if coffee_maker.is_resource_sufficient(order):
            payment_accepted = money_machine.make_payment(order.cost)
            make_coffee = coffee_maker.make_coffee(order)
            continue
        else:
            break















