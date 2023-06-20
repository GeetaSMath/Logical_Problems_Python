# Create a class Smoothie and do the following:
#
# Create an instance attribute called ingredients.
# Create a get_cost method which calculates the total cost of the ingredients used to make the smoothie.
# Create a get_price method which returns the number from get_cost plus the number from
# get_cost multiplied by 1.5. Round to two decimal places.
# Create a get_name method which gets the ingredients and puts them in alphabetical order
# into a nice descriptive sentence. If there are multiple ingredients, add the word "Fusion" to
# the end but otherwise, add "Smoothie". Remember to change "-berries" to "-berry". See the examples below.
# Ingredient	Price
# Strawberries	$1.50
# Banana	$0.50
# Mango	$2.50
# Blueberries	$1.00
# Raspberries	$1.00
# Apple	$1.75
# Pineapple	$3.50
# Examples
# s1 = Smoothie(["Banana"])
#
# s1.ingredients ➞ ["Banana"]
#
# s1.get_cost() ➞ "$0.50"
# s1.get_price() ➞ "$1.25"
# s1.get_name() ➞ "Banana Smoothie"
# s2 = Smoothie(["Raspberries", "Strawberries", "Blueberries"])
# s2.ingredients ➞ ["Raspberries", "Strawberries", "Blueberries"]
# s2.get_cost() ➞ "$3.50"
# s2.get_price() ➞ "$8.75"
# s2.get_name() ➞ "Blueberry Raspberry Strawberry Fusion"

class Smoothie:
    ingredient_prices = {
        "Strawberries": 1.50,
        "Banana": 0.50,
        "Mango": 2.50,
        "Blueberries": 1.00,
        "Raspberries": 1.00,
        "Apple": 1.75,
        "Pineapple": 3.50
    }

    def __init__(self, ingredients):
        self.ingredients = ingredients

    def get_cost(self):
        total_cost = sum(Smoothie.ingredient_prices.get(ingredient, 0) for ingredient in self.ingredients)
        return f"${total_cost:.2f}"

    def get_price(self):
        cost = self.get_cost().replace("$", "")
        total_price = float(cost) + (float(cost) * 1.5)
        return f"${total_price:.2f}"

    def get_name(self):
        sorted_ingredients = sorted(self.ingredients)
        if len(sorted_ingredients) > 1:
            name = " ".join(ingredient[:-1] + "y" if ingredient.endswith("ies") else ingredient for ingredient in
                            sorted_ingredients)
            return f"{name} Fusion"
        else:
            return f"{sorted_ingredients[0]} Smoothie"


s1 = Smoothie(["Banana"])
print(s1.ingredients)
print(s1.get_cost())
print(s1.get_price())
print(s1.get_name())

s2 = Smoothie(["Raspberries", "Strawberries", "Blueberries"])
print(s2.ingredients)
print(s2.get_cost())
print(s2.get_price())
print(s2.get_name())
