# CUSTOM PIZZA FUNCTIONS
import copy
from pizzas import custom
from validation import *
from display_options import *


def make_custom_pizza():
    """
    This function creates a new instance of the class pizza.
    """
    new_custom = copy.copy(custom)

    dough = choose_dough()
    sauce = choose_sauce()
    toppings = choose_toppings()
    price = update_price(toppings)

    new_custom.dough = dough
    new_custom.sauce = sauce
    new_custom.toppings = toppings
    new_custom.price = price

    return new_custom


def choose_dough():
    """
    This function updates the dough attrobute of custom pizza
    """
    options = [
        "White",
        "Wholegarain",
        "Gluten free"
    ]

    dough = display_ingredients_options(options, "dough")

    if validate_action(dough, options):
        return options[int(dough)-1]


def choose_sauce():
    """
    This function updates the sauce attrobute of custom pizza
    """
    options = [
        "Tomato sauce",
        "BBQ sauce",
        "No sauce"
    ]

    sauce = display_ingredients_options(options, "sauce")

    if validate_action(sauce, options):
        return options[int(sauce)-1]


def choose_toppings():
    """
    This function updates the toppings attrobute of custom pizza
    """
    options = [
        "Mozzarella",
        "Scamorza",
        "Vegan cheese",
        "Mushrooms",
        "Jackfruit",
        "pepperoni",
        "Black Truffle",
        "Cherry tomatoes",
        "Peppers"
    ]

    toppings = display_toppings_options(options, "toppings")

    return toppings


def update_price(toppings):
    """
    This function updates the price attrobute of custom pizza
    """
    count = len(toppings)
    price = 8 + (1.5 * count)

    return price
