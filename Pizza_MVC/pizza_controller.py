class PizzaController:
    def __init__(self, model):
        self.model = model

    def update_ingredients(self, ingredients):
        self.model.set_ingredients(ingredients)

    def update_price(self, price):
        self.model.set_price(price)

    def update_weight(self, weight):
        self.model.set_weight(weight)

    def get_all_data(self):
        return {
            "name": self.model.name,
            "ingredients": self.model.ingredients,
            "price": self.model.price,
            "weight": self.model.weight
        }

    def get_ingredients_and_weight(self):
        return {
            "ingredients": self.model.ingredients,
            "weight": self.model.weight
        }

    def get_price(self):
        return {
            "price": self.model.price
        }