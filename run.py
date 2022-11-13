import sys
import time
import os
from validation import *
from display_options import *
from pizzas import *
from order import *
from basket import *


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
    type_write(INTRO_MESSAGE, 0.05)
    show_main_menu()


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
