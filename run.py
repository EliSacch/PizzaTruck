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



def display_main_options():
    """
    This function displays the main navigation options.
    """
    while True:
        options = ["Menu and Order", "View current order"]
        print("\nOptions:\n")
        for option in options:
            prefix = options.index(option) + 1
            print(f"{prefix}. {option}")
        
        choosen_action = input("\nEnter the number corresponding to the desired action: ")
        
        if validate_action(choosen_action, options):
            print("Valid action")
            break




def main():
    """
    This function runs the progam.
    """
    file = open("logo.txt")
    logo = file.read()
    file.close()

    intro_message = "\n\nWelcome to Pizza Truck!\nCheck our menu and place your order.\n"

    type_intro(logo, 0.0000000000001)
    type_intro(intro_message, 0.1)

    display_main_options()

main()