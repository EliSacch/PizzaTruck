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


def display_ingredients_options(options, category):
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
        choosen_option = input(f"\nChoose {category}: ")
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
    for option in options:
        prefix = options.index(option) + 1
        print(f"{prefix}. {option}")

    toppings_choice = []
    limit = 4
    for i in range(limit):
        choosen_option = input(f"\nChoose {category}: ")
        if validate_action(choosen_option, options):
            toppings_choice.append(options[int(choosen_option)-1])
        i += 1

    return toppings_choice
