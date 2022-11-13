from tabulate import tabulate
import sys
import time
import os
import copy
from validation import *
from display_option import *
from pizzas import *


# VARIABLES

current_order = []


# GENERAL FUNCTIONS


def clear_terminal():
    """
    This functions clears the terminal.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def type_write(message, speed):
    """
    This function takes a message as input and prints it one char at a time.
    It also takes the speed input to customize the typing speed.
    """
# The following code is from Learn Learn Scratch Tutorials
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
# End of code from Learn Learn Scratch Tutorials


def show_main_menu():
    """
    Displays the main menu
    """
    menu_options = ["Menu and Order", "Exit program"]
    if len(current_order) != 0:
        menu_options.insert(-1, "View current order")

    action = menu_options[display_options(menu_options)-1]
    if action == "Menu and Order":
        clear_terminal()
        show_order_options()
    if action == "View current order":
        clear_terminal()
        display_current_order(retrieve_current_order())
        show_main_menu()
    if action == "Exit program":
        clear_terminal()
        print("\nThank you for visiting Pizza Truck\n")
        exit()


def main_menu():
    """
    Calls the display options function to displays the main menu options.
    Validates the input to check if it's a valid action.
    Runs a sifferent function based on the returned action.
    """
    file = open("intro.txt")
    INTRO_MESSAGE = file.read()
    file.close()

    # type_write(INTRO_MESSAGE, 0.05)
    show_main_menu()


# ORDER RELATED FUNCTIONS

def show_order_options():
    """
    This functions displays order options
    """
    global current_order

    menu_options = [
        "Show menu",
        "Add pizza",
        "Remove pizza",
        "Main options"
    ]

    if len(current_order) != 0:
        menu_options.insert(-1, "View current order")

    action = menu_options[display_options(menu_options)-1]
    if action == "Show menu":
        clear_terminal()
        show_menu()
    elif action == "Add pizza":
        clear_terminal()
        current_order.extend(add_pizza(pizza_menu))
        show_order_options()
    elif action == "Remove pizza":
        remove_pizza()
        show_order_options()
    elif action == "View current order":
        clear_terminal()
        display_current_order(retrieve_current_order())
        show_main_menu()
    elif action == "Main options":
        clear_terminal()
        show_main_menu()
    else:
        print("Action not recognized. Try again")


def show_menu():
    """
    This function shows the available pizzas, with ingredients and price
    """

    print("\nMenu:\n")

    menu = []

    for pizza in pizza_menu:
        row = []
        number = pizza_menu.index(pizza) + 1
        row.append(number)
        row.append(pizza.name.capitalize())
        row.append(pizza.ingredients())
        row.append(pizza.price)
        menu.append(row)

    type_write(
        tabulate(menu, headers=["#", "Name", "Ingredients", "Price/€"]),
        0.000000001)

    print("\n* + €1.5 per topping\n")

    show_order_options()


def show_menu_short():
    """
    This function shows the available pizzas only
    """

    print("\nMenu:\n")

    for pizza in pizza_menu:
        number = pizza_menu.index(pizza) + 1
        menu = f"{number}- {pizza.name.capitalize()}\n"
        type_write(menu, 0.001)


def add_pizza(pizza_menu):
    """
    This function takes one integer as input from the user.
    The integer needs to correspond to the pizza they want to order.
    It adds the pizza to the crrent_order array.
    """
    add_to_order = []

    show_menu_short()

    print("\nEnter the number corresponding to the pizza")
    print("Enter 0 (zero) to exit")

    while True:
        choosen_pizza = input("\nAdd pizza: ")
        if choosen_pizza == "0":
            clear_terminal()
            print(f"\n{len(add_to_order)} pizzas added to your order")
            break
        elif validate_action(choosen_pizza, pizza_menu):
            if (int(choosen_pizza) == len(pizza_menu)):
                custom = make_custom_pizza()
                add_to_order.append(custom)
            else:
                add_to_order.append(pizza_menu[int(choosen_pizza)-1])

    order = []
    for pizza in add_to_order:
        item = {
            "name": pizza.name,
            "dough": pizza.dough,
            "sauce": pizza.sauce,
            "toppings": pizza.toppings,
            "price": pizza.price
        }
        order.append(item)

    return order


def make_custom_pizza():
    """
    This function creates a new instance of the class pizza.
    """
    new_custom = copy.copy(custom)

    dough = choose_dough()
    sauce = choose_sauce()
    toppings = choose_toppings()
    # price = update_price(toppings)

    new_custom.dough = dough
    new_custom.sauce = sauce
    new_custom.toppings = toppings
    # new_custom.price = price

    return new_custom


def remove_pizza():
    """
    This functions removes selected item from current order
    """

    print("\nSelect the number corresponding to the pizza you want to remove")
    print("\nEnter 0 to exit")
    """
    while True:
        items = retrieve_current_order()
        for item in items:
            ind = (items.index(item)) + 1
            if item["ingredients"] != "":
                print(f""{ind}- {item['name']}
                 {item['ingredients']} (X{item['count']})"")
            else:
                print(f"{ind}- {item['name']} (X{item['count']})")

        choosen_pizza = input("\nRemove pizza: ")
        if choosen_pizza == "0":
            break
        elif validate_action(choosen_pizza, current_order):
            to_be_removed = items[int(choosen_pizza)-1]
            current_order.remove(to_be_removed)
    """
    while True:
        items = retrieve_current_order()
        for item in items:
            ind = (items.index(item)) + 1
            if item["ingredients"] != "":
                print(f"""{ind}- {item['name']}
                 {item['ingredients']} (X{item['count']})""")
            else:
                print(f"{ind}- {item['name']} (X{item['count']})")

        choosen_pizza = input("\nRemove pizza: ")

        if choosen_pizza == "0":
            break
        elif validate_action(choosen_pizza, current_order):
            to_be_removed = (items[int(choosen_pizza)-1])['name']
            for item in current_order:
                if item['name'] == to_be_removed:
                    current_order.remove(item)
                    break


# BASKET AND CHECKOUT RELATED FUNCTIONS


def retrieve_current_order():
    """
    This function displays the items currently added to the order.
    """
    print("\nCurrent order:\n***************")

    items_count = []
    types = []

    for item in current_order:
        if item not in types:
            types.append(item)

    for type in types:
        num = current_order.count(type)
        if (type["name"] == "make your own"):
            ingredients = f"{type['dough'].capitalize()}, "
            ingredients += f"{type['sauce'].capitalize()}"

            selection = list(dict.fromkeys(type['toppings']))
            for i in selection:
                rep = type['toppings'].count(i)
                if rep == 1:
                    ingredients += f", {i.capitalize()}"
                else:
                    ingredients += f", {rep}x{i.capitalize()}"
            items_count.append(
                {
                    "name": type['name'],
                    "count": num,
                    "ingredients": f"({ingredients})"
                }
            )
        else:
            items_count.append(
                {
                    "name": type['name'],
                    "count": num,
                    "ingredients": ""
                }
            )
    return items_count


def display_current_order(items_count):
    """
    This functions uses retrieve_current_order to get the pizzas in order
     and displays them.
    """
    for item in items_count:
        if item["ingredients"] != "":
            print(f"{item['count']} X {item['name']} {item['ingredients']}")
        else:
            print(f"{item['count']} X {item['name'].capitalize()}")


# MAIN

def main():
    """
    This function runs the progam.
    """
    clear_terminal()

    file = open("logo.txt")
    logo = file.read()
    file.close()

    # type_write(logo, 0.0000000000001)

    main_menu()


main()
