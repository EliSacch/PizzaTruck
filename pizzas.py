from validation import *
from display_option import *


class Pizza:
    """
    Creates an instance of pizza
    """
    def __init__(self, name, dough, sauce, toppings, price):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings
        self.price = price

    def description(self):
        name = self.name.capitalize()
        ingredients = ""
        if self.dough != "":
            ingredients += f"{self.dough.capitalize()} dough"
        if self.sauce != "":
            ingredients += f", {self.sauce.capitalize()} sauce"
        if len(self.toppings) != 0:
            for item in self.toppings:
                ingredients += f", {item.capitalize()}"
        if ingredients != "":
            ingredients = f"({ingredients})"

        return f"{name} {ingredients}"


margherita = Pizza(
    "margerita",
    "white",
    "tomato",
    ["mozzarella", "basil"],
    8.00)


vegan = Pizza(
    "vegan",
    "wholegrain",
    "tomato",
    ["vegan cheese", "mushrooms", "jackfruit"],
    10.00)


spicy = Pizza(
    "spicy",
    "white",
    "bbq",
    ["mozzarella", "pepperoni"],
    10.00)


truffle = Pizza(
    "truffle",
    "white",
    "tomato",
    ["scamorza", "mushrooms", "black truffle"],
    12.00)


custom = Pizza(
    "make your own",
    "",
    "",
    [],
    8.00)


pizza_menu = [margherita, vegan, spicy, truffle, custom]


def choose_dough():
    """
    This function updates the dough attrobute of custom pizza
    """
    options = [
        "white",
        "wholegarain",
        "gluten free"
    ]

    display_options(options)

    dough = input("\nChoice of dough: ")

    if validate_action(dough, pizza_menu):
        print(options[int(dough)-1])


def choose_sauce():
    """
    This function updates the sauce attrobute of custom pizza
    """


def choose_toppings():
    """
    This function updates the toppings attrobute of custom pizza
    """


def update_price():
    """
    This function updates the price attrobute of custom pizza
    """
