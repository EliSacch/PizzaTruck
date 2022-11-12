import sys
import time
from pizzas import *

# GENERAL FUNCTIONS

current_order = []


def type_intro(message, speed):
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
        show_order_options()
    if action == "View current order":
        display_current_order()
        show_main_menu()
    if action == "Exit program":
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

    # type_intro(INTRO_MESSAGE, 0.05)
    show_main_menu()


def display_options(options):
    """
    This function displays the options for the related section.
    """
    while True:
        print("\nOptions:\n")
        for option in options:
            prefix = options.index(option) + 1
            print(f"{prefix}. {option}")
        choosen_action = input("\nChoose an action(enter the action number): ")
        if validate_action(choosen_action, options):
            break

    return int(choosen_action)


def validate_action(value, choices):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if it is outside of the range of choices.
    """
    try:
        if value.isnumeric() is False:
            raise ValueError('Please, enter a whole number')
        action = int(value)-1
        is_valid_choice = action >= 0 and action < len(choices)
        if is_valid_choice is False:
            raise IndexError("No option corresponding to this number")
    except (ValueError, IndexError) as e:
        print(f"\nInvalid data: {e}. Please try again.")
        return False

    return True


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
        show_menu()
    elif action == "Add pizza":
        current_order.extend(add_pizza(pizza_menu))
        show_order_options()
    elif action == "Remove pizza":
        remove_pizza()
        show_order_options()
    elif action == "View current order":
        display_current_order()
        show_main_menu()
    elif action == "Main options":
        show_main_menu()
    else:
        print("Action not recognized. Try again")


def show_menu():
    """
    This function shows the available pizzas
    """

    print("\nMenu:\n")

    for pizza in pizza_menu:
        number = pizza_menu.index(pizza) + 1
        menu = f"{number}- {pizza.description()}\n"
        type_intro(menu, 0.001)

    show_order_options()


def add_pizza(pizza_menu):
    """
    This function takes one integer as input from the user.
    The integer needs to correspond to the pizza they want to order.
    It adds the pizza to the crrent_order array.
    """
    add_to_order = []

    print("\nEnter the number corresponding to the pizza")
    print("Enter 0 (zero) to exit")

    while True:
        choosen_pizza = input("\nAdd pizza: ")
        if choosen_pizza == "0":
            print(f"\n{len(add_to_order)} pizzas added to your order")
            break
        elif validate_action(choosen_pizza, pizza_menu):
            if (int(choosen_pizza) == len(pizza_menu) - 1):
                add_to_order.append(make_custom_pizza())
            else:
                add_to_order.append(pizza_menu[int(choosen_pizza)-1])

    return add_to_order


def make_custom_pizza():
    """
    This function creates a new instance of the class pizza
    """
    new_custom = Pizza(
        "make your own",
        "test",
        "test",
        [],
        8.00)

    return new_custom


def remove_pizza():
    """
    This functions removes selected item from current order
    """

    print("\nSelect the number corresponding to the pizza you want to remove")
    print("\nEnter 0 to exit")

    while True:
        order_items = []
        items_count = []
        print("\nCurrent order:\n***************")
        for type in pizza_menu:
            num = current_order.count(type)
            if num == 0:
                pass
            else:
                order_items.append(type.name)
                items_count.append(num)

        for item, count in zip(order_items, items_count):
            ind = (order_items.index(item)) + 1
            print(f"{ind}- {item} (X{count})")

        choosen_pizza = input("\nRemove pizza: ")
        if choosen_pizza == "0":
            break
        elif validate_action(choosen_pizza, current_order):
            to_be_removed = order_items[int(choosen_pizza)-1]
            for item in current_order:
                if item.name == to_be_removed:
                    current_order.remove(item)
                    break


# BASKET AND CHECKOUT RELATED FUNCTIONS

def display_current_order():
    """
    This function displays the items currently added to the order.
    """
    print("\nCurrent order:\n***************")
    for type in pizza_menu:
        num = current_order.count(type)
        if num == 0:
            pass
        else:
            print(f"{num} X {type.name}")


# MAIN

def main():
    """
    This function runs the progam.
    """
    file = open("logo.txt")
    logo = file.read()
    file.close()

    # type_intro(logo, 0.0000000000001)

    main_menu()


main()
