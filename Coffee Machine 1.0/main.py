MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

game = True

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
machine_money = 0.0


def get_change():
    print(f"Here is ${change} in change.")
    print(f"Here is your {answer} ☕. Enjoy!")


def use_resources():
    global water, milk, coffee
    if answer == "espresso":
        water -= 100
        milk -= 50
        coffee -= 24
    if answer == "latte":
        water -= 200
        milk -= 150
        coffee -= 24
    if answer == "cappuccino":
        water -= 200
        milk -= 100
        coffee -= 15


while game is True:
    cappuccino_price = MENU["cappuccino"]["cost"]
    latte_price = MENU["latte"]["cost"]
    espresso_price = MENU["espresso"]["cost"]
    resources = f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${machine_money}"

    answer = input("What would you like? (espresso/latte/cappuccino): ")

    if answer == "off":
        game = False
        print("Goodbye!")
        break
    if answer == "report":
        print(resources)
        answer = input("What would you like? (espresso/latte/cappuccino): ")

    print("Please insert coins")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))

    quarters *= 0.25
    dimes *= 0.10
    nickles *= 0.05
    pennies *= 0.01

    user_money = quarters + dimes + nickles + pennies

    if answer == "espresso":
        change = user_money - espresso_price
        change = round(change, 2)
        if user_money < espresso_price:
            print("Sorry, that's not enough money. Money refunded.")
        elif water >= 100 and milk >= 50 and coffee >= 76:
            machine_money += espresso_price
            use_resources()
            get_change()
        elif water < 100:
            print("Sorry, there is not enough water.")
        elif milk < 50:
            print("Sorry, there is not enough milk.")
        elif coffee < 24:
            print("Sorry, there is not enough coffee.")
    elif answer == "latte":
        change = user_money - latte_price
        change = round(change, 2)
        if user_money < latte_price:
            print("Sorry, that's not enough money. Money refunded.")
        elif water >= 200 and milk >= 150 and coffee >= 24:
            machine_money += latte_price
            use_resources()
            get_change()
        elif water < 200:
            print("Sorry, there is not enough water.")
        elif milk < 150:
            print("Sorry, there is not enough milk.")
        elif coffee < 24:
            print("Sorry, there is not enough coffee.")
    elif answer == "cappuccino":
        change = user_money - cappuccino_price
        change = round(change, 2)
        if user_money < cappuccino_price:
            print("Sorry, that's not enough money. Money refunded.")
        elif water >= 200 and milk >= 100 and coffee >= 15:
            machine_money += cappuccino_price
            use_resources()
            get_change()
        elif water < 200:
            print("Sorry, there is not enough water.")
        elif milk < 100:
            print("Sorry, there is not enough milk.")
        elif coffee < 15:
            print("Sorry, there is not enough coffee.")


