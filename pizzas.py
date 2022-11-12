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
