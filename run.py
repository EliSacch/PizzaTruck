from general import *


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
