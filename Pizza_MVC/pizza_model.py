class PizzaModel:
    def __init__(self, name, ingredients, price, weight):
        self.name = name
        self.ingredients = ingredients
        self.price = price
        self.weight = weight

    def set_ingredients(self, ingredients):
        self.ingredients = ingredients

    def set_price(self, price):
        self.price = price

    def set_weight(self, weight):
        self.weight = weight