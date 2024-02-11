MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 12.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 10.0,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 13.0,
    }
}

profit = 0
resources = {
    "water": 1000,
    "milk": 1000,
    "coffee": 500,
}


def is_resource_sufficient(order_ingredients):
    """Return True if order is successful or False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}!")
            return False
    return True


def process_coins():
    """Returns the total calculated coins."""
    print("Please insert coins.")
    total = int(input("How many 5 Rs. Coins: ")) * 5
    total += int(input("How many 10 Rs. Coins: ")) * 10
    total += int(input("How many 2 Rs. Coins: ")) * 2
    total += int(input("How many 1 Rs. Coins: ")) * 1
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True if payment successful and False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your Rs. {change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money Refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ")


is_on = True
while is_on:
    choice = input("What would you like to have: Espresso?, Latte?, Cappuccino: ")
    if choice == "off":
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: Rs. {profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
