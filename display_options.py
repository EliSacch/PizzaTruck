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
    while (count < limit):
        print(f"\n{count} of {limit} toppings added.")
        choosen_option = input(f"\nChoose {category}:\n")
        if (int(choosen_option) == 0):
            break
        elif validate_action(choosen_option, options):
            toppings_choice.append(options[int(choosen_option)-1])
            count += 1

    print("\nYou choose the following toppings: ")

    selection = list(dict.fromkeys(toppings_choice))
    for i in selection:
        num = toppings_choice.count(i)
        print(f"{num} X {i}")

    return toppings_choice
