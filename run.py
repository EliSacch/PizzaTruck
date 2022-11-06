import sys,time,os

def type_intro(message, speed):
    """
    This function takes a message as input and prints it one char at a time.
    It also takes the speed input to customize the typing speed.
    """
#The following code is from Learn Learn Scratch Tutorials
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
# Rnd of code from Learn Learn Scratch Tutorials 


def main_menu():
    """ 
    Calls the display options function to displays the main menu options.
    Validates the input to check if it's a valid action.
    Runs a sifferent function based on the returned action.
    """
    intro_message = "\n\nWelcome to Pizza Truck!\nCheck our menu and place your order.\n"
    type_intro(intro_message, 0.05)

    menu_options = ["Menu and Order", "View current order"]
    action = display_options(menu_options)
    if action == 1:
        show_order_options()
    if action == 2:
        display_current_order()


def display_options(options):
    """
    This function displays the options for the related section.
    """
    while True:
        print("\nOptions:\n")
        
        for option in options:
            prefix = options.index(option) + 1
            print(f"{prefix}. {option}")
        
        choosen_action = input("\nEnter the number corresponding to the desired action: ")
        
        if validate_action(choosen_action, options):
            break

    return int(choosen_action) 

    

def validate_action(action, choices):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if it is outside of the range of choices.
    """
    try:
        is_integer = int(action)
        is_valid_choice = ((is_integer-1)) >= 0 and ((is_integer-1) < len(choices))

        if (is_integer == False) or (is_valid_choice == False) :
            raise ValueError("Please, enter the number corrisponding to the desired action (Example: 1)"
            )
    except ValueError as e:
        print(f"\nInvalid data: {e}. Please try again.")
        return False
        
    return True

def display_menu():
    """
    This function shows the available pizzas
    """
    pizzas = [
        "Margherita(White dough, tomato sauce, mozzarella chese, basil)", 
        "Vegan(Wholegrain dough, tomato sauce, vegan cheese, mushrooms",
        "Spicy{White dough, bbq sauce, mozzarella cheese, pepperoni",
        "Truffle(White dough, mozzarella cheese, mushrooms, black truffle",
        "Make your own"]

    print("\nMenu:\n")

    for pizza in pizzas:
        number = pizzas.index(pizza) + 1
        menu = f"{number}- {pizza}\n"
        type_intro(menu, 0.001)

    show_order_options()
    
    
    
def show_order_options():
    """
    This functions displays order options
    """
    menu_options = [
        "Show menu",
        "Add pizza",
        "Remove pizza",
        "Finish",
        "Main menu"
    ]

    action = display_options(menu_options)
    if action == 1:
        display_menu()
    if (action == 5):
        main_menu()
    else:
        print("Other action")


def display_current_order():
    """
    This function displays the items currently added to the order.
    """
    print("Here is the current order:")


def main():
    """
    This function runs the progam.
    """
    file = open("logo.txt")
    logo = file.read()
    file.close()

    #type_intro(logo, 0.0000000000001)

    main_menu()


main()