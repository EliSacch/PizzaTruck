import sys,time,os

intro_message = "Hello, welcome to Pizza Truck"

def type_intro(message):
#The following code is from Learn Learn Scratch Tutorials
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
# Rnd of code from Learn Learn Scratch Tutorials  

def main():
    type_intro(intro_message)

main()