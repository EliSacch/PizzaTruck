import sys
import time
from time import sleep
import os
import copy
from tabulate import tabulate
from validation import *
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

    action = menu_options[int(display_options(menu_options, "option"))-1]
    if action == "Menu and Order":
        clear_terminal()
        show_order_options()
    if action == "View current order":
        clear_terminal()
        display_current_order(retrieve_current_order())
        show_basket_menu()
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
    print("\n")
    type_write(INTRO_MESSAGE, 0.05)
    show_main_menu()


def display_options(options, category):
    """
    This function displays the options for the related section.
    It also takes the category input to display
    the relevant ingredient category.
    """
    while True:
        print(f"\nChoice of {category}: \n")
        for option in options:
            prefix = options.index(option) + 1
            print(f"{prefix}. {option}")
        choosen_option = input(f"\nChoose {category}:\n")
        if validate_action(choosen_option, options):
            break

    return choosen_option


def display_toppings_options(options, category):
    """
    This function displays the options for the related section.
    Because it accepts more than one input,
    it has been changed to display the options just once.
    """
    print(f"\nChoice of {category}: \n")
    print("\n0. No more toppings")
    for option in options:
        prefix = options.index(option) + 1
        print(f"{prefix}. {option}")

    toppings_choice = []
    limit = 4
    count = 0
    while True:
        print(f"\n{count} of {limit} toppings added.")
        choosen_option = input(f"\nChoose {category}:\n")
        if (choosen_option == "0"):
            break
        elif validate_action(choosen_option, options):
            index = choosen_option
            toppings_choice.append(options[int(index)-1])
            count += 1

        if (count >= limit):
            break

    print("\nYou choose the following toppings: ")

    selection = list(dict.fromkeys(toppings_choice))
    for i in selection:
        num = toppings_choice.count(i)
        print(f"{num} X {i}")

    return toppings_choice


# ORDER RELATED FUNCTIONS

def show_order_options():
    """
    This functions displays order options
    """
    global current_order

    menu_options = [
        "Show menu",
        "Add pizza",
        "Main options"
    ]

    if len(current_order) != 0:
        menu_options.insert(-1, "Remove pizza")
        menu_options.insert(-1, "View current order")

    action = menu_options[int(display_options(menu_options, "option"))-1]
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
        show_basket_menu()
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

    for pizza in pizza_menu:
        item = f"""
        {pizza.name.upper()}
        {pizza.ingredients()}
        €{pizza.price}\n"""

        type_write(item, 0.000000001)
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
        choosen_pizza = input("\nAdd pizza:\n")
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


def remove_pizza():
    """
    This functions removes selected item from current order
    """
    while True:
        print("\nSelect the number of the pizza you want to remove")
        print("\nEnter 0 to exit")
        items = retrieve_current_order()

        if len(items) == 0:
            clear_terminal()
            print("\n There are no items in the order")
            break

        for item in items:
            ind = (items.index(item)) + 1
            if item["ingredients"] != "":
                print(f"""{ind}- {
                    item['name']}{
                    item['ingredients']} (X{item['count']})""")
            else:
                print(f"{ind}- {item['name']} (X{item['count']})")

        choosen_pizza = input("\nRemove pizza:\n")

        if choosen_pizza == "0":
            break
        elif validate_action(choosen_pizza, current_order):
            to_be_removed = (items[int(choosen_pizza)-1])['name']
            for item in current_order:
                if item['name'] == to_be_removed:
                    current_order.remove(item)
                    clear_terminal()
                    break


# CUSTOM PIZZA FUNCTIONS

def make_custom_pizza():
    """
    This function creates a new instance of the class pizza.
    """
    new_custom = copy.copy(custom)

    dough = choose_dough()
    sauce = choose_sauce()
    toppings = choose_toppings()
    price = update_price(toppings)

    new_custom.dough = dough
    new_custom.sauce = sauce
    new_custom.toppings = toppings
    new_custom.price = price

    return new_custom


def choose_dough():
    """
    This function updates the dough attrobute of custom pizza
    """
    options = [
        "White",
        "Wholegarain",
        "Gluten free"
    ]

    dough = display_options(options, "dough")

    if validate_action(dough, options):
        choice = options[int(dough)-1]
        print(f"You choose the following dough: {choice}")
        return choice


def choose_sauce():
    """
    This function updates the sauce attrobute of custom pizza
    """
    options = [
        "Tomato sauce",
        "BBQ sauce",
        "No sauce"
    ]

    sauce = display_options(options, "sauce")

    if validate_action(sauce, options):
        choice = options[int(sauce)-1]
        print(f"You choose the following sauce: {choice}")
        return choice


def choose_toppings():
    """
    This function updates the toppings attrobute of custom pizza
    """
    options = [
        "Mozzarella",
        "Scamorza",
        "Vegan cheese",
        "Mushrooms",
        "Jackfruit",
        "pepperoni",
        "Black Truffle",
        "Cherry tomatoes",
        "Peppers"
    ]

    toppings = display_toppings_options(options, "toppings")

    return toppings


def update_price(toppings):
    """
    This function updates the price attribute of custom pizza
    """
    count = len(toppings)
    price = 8 + (1.5 * count)

    return price


# BASKET AND CHECKOUT RELATED FUNCTIONS

def show_basket_menu():
    """
    Displays the options available in the basket section
    """
    menu_options = ["Edit Order", "Place order", "Main menu"]
    action = menu_options[int(display_options(menu_options, "option"))-1]
    if action == "Edit Order":
        clear_terminal()
        show_order_options()
    if action == "Place order":
        clear_terminal()
        display_receipt(retrieve_current_order())
        terminate_program()
    if action == "Main menu":
        clear_terminal()
        show_main_menu()


def retrieve_current_order():
    """
    This function retrieves the items currently added to the order.
    It returns the relevant information the be used the display ord functions.
    It also return the count for each item.
    """
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
                    "ingredients": f"({ingredients})",
                    "price": type['price']
                }
            )
        else:
            items_count.append(
                {
                    "name": type['name'],
                    "count": num,
                    "ingredients": "",
                    "price": type['price']
                }
            )
    return items_count


def display_current_order(items_count):
    """
    This functions uses retrieve_current_order to get the pizzas in order
    and displays them.
    """
    total_price = 0
    recap_order = []

    print("\nCurrent order:\n")

    for item in items_count:
        row = []
        row.append(f"{item['count']} X")
        row.append(f"{item['name'].capitalize()}")
        price = (float(item['count']) * float(item['price']))
        total_price += price
        row.append(f"€{price}")
        recap_order.append(row)
        if item["ingredients"] != "":
            recap_order.append(["", f"{item['ingredients']}", ""])

    header = ["", "Item", "Price"]
    width = [None, 50, None]
    print(tabulate(recap_order, headers=header, maxcolwidths=width))
    print(f"Total: €{total_price}")


def display_receipt(items_count):
    """
    This functions shows the final order and total price.
    It is called at the end of the flow, when the order is placed.
    """
    total_price = 0
    recap_order = []

    for item in items_count:
        row = []
        row.append(f"{item['count']} X")
        row.append(item['name'].capitalize())
        row.append(f"{item['count']} X {item['price']}")
        total_price += (float(item['count']) * float(item['price']))
        recap_order.append(row)

    recap_order.append(["---", "----------", "----------"])
    recap_order.append(["", "", f"Total: €{total_price}"])

    type_write(
        tabulate(recap_order, headers=["", "Name", "Price/€"]),
        0.000000001)


# TERMINATE

def terminate_program():
    """
    This function is called only at the end of the program.
    It prints a goodbye message and then exits the progra.
    """
    input("\nPress any key to exit:\n")

    thanks = "Thank you for your order!"

    type_write(thanks, 0.0000000000001)
    sleep(5)
    exit()


# MAIN

def main():
    """
    This function runs the progam.
    """
    clear_terminal()

    file = open("logo.txt")
    logo = file.read()
    file.close()
    type_write(logo, 0.0000000000001)

    main_menu()


main()
