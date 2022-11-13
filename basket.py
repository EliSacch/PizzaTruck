# BASKET AND CHECKOUT RELATED FUNCTIONS
from tabulate import tabulate
from run import clear_terminal
from run import type_write
from run import show_main_menu
from run import current_order
from display_options import *
from order import show_order_options


def show_basket_menu():
    """
    Displays the options available in the basket section
    """
    menu_options = ["Edit Order", "Place order", "Main menu"]
    action = menu_options[display_options(menu_options)-1]
    if action == "Edit Order":
        clear_terminal()
        show_order_options()
    if action == "Place order":
        clear_terminal()
        display_receipt(retrieve_current_order())
        exit()
    if action == "Main menu":
        clear_terminal()
        show_main_menu()


def retrieve_current_order():
    """
    This function displays the items currently added to the order.
    """
    items_count = []
    types = []

    for item in current_order:
        if item not in types:
            types.append(item)

    for type in types:
        num = current_order.count(type)
        if (type["name"] == "make your own"):
            ingredients = f"{type['dough'].capitalize()}, "
            ingredients += f"{type['sauce'].capitalize()}"

            selection = list(dict.fromkeys(type['toppings']))
            for i in selection:
                rep = type['toppings'].count(i)
                if rep == 1:
                    ingredients += f", {i.capitalize()}"
                else:
                    ingredients += f", {rep}x{i.capitalize()}"
            items_count.append(
                {
                    "name": type['name'],
                    "count": num,
                    "ingredients": f"({ingredients})",
                    "price": type['price']
                }
            )
        else:
            items_count.append(
                {
                    "name": type['name'],
                    "count": num,
                    "ingredients": "",
                    "price": type['price']
                }
            )
    return items_count


def display_current_order(items_count):
    """
    This functions uses retrieve_current_order to get the pizzas in order
     and displays them.
    """
    total_price = 0
    recap_order = []

    print("\nCurrent order:\n")

    for item in items_count:
        row = []
        row.append(f"{item['count']} X")
        if item["ingredients"] != "":
            row.append(f"""{
                item['count']} X {
                item['name']} {
                item['ingredients']}""")
        else:
            row.append(f"{item['count']} X {item['name'].capitalize()}")
        price = (int(item['count']) * int(item['price']))
        total_price += price
        row.append(f"€{price}")
        recap_order.append(row)

    print(tabulate(recap_order, headers=["", "Item", "Price"]))
    print(f"Total: €{total_price}")


def display_receipt(items_count):
    """
    This functions shows the items price and total order.
    It is called at the end of the flow, then the user places the order.
    """
    total_price = 0
    recap_order = []

    for item in items_count:
        row = []
        row.append(f"{item['count']} X")
        row.append(item['name'].capitalize())
        row.append(f"{item['count']} X {item['price']}")
        total_price += (int(item['count']) * int(item['price']))
        recap_order.append(row)

    recap_order.append(["---", "----------", "----------"])
    recap_order.append(["", "", f"Total: €{total_price}"])

    type_write(
        tabulate(recap_order, headers=["", "Name", "Price/€"]),
        0.000000001)

    print("\n\nThank you for your order")
