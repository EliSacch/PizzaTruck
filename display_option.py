from validation import *


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
