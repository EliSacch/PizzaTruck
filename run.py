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


def display_main_options():
    """
    This function displays the main navigation options.
    """

    options = ["Menu and Order", "View current order"]
    print("\n\nOptions:\n")
    for option in options:
        prefix = options.index(option) + 1
        print(f"{prefix}. {option}")
    
    choosen_option = input("\nEnter the number corresponding to the desired action: ")
    
    print(choosen_option)



def main():
    """
    This function runs the progam.
    """
    file = open("logo.txt")
    logo = file.read()
    file.close()

    intro_message = "\n\nWelcome to Pizza Truck!\nCheck our menu and place your order."

    #type_intro(logo, 0.0000000000001)
    #type_intro(intro_message, 0.1)

    display_main_options()

main()