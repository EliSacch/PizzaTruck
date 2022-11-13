# ORDER RELATED FUNCTIONS
from tabulate import tabulate
from run import clear_terminal
from run import show_main_menu
from run import type_write
from display_options import *
from basket import *
from customize import *
from pizzas import *


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

        choosen_pizza = input("\nRemove pizza: ")

        if choosen_pizza == "0":
            break
        elif validate_action(choosen_pizza, current_order):
            to_be_removed = (items[int(choosen_pizza)-1])['name']
            for item in current_order:
                if item['name'] == to_be_removed:
                    current_order.remove(item)
                    clear_terminal()
                    break
