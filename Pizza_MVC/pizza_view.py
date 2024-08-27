class PizzaView:
    @staticmethod
    def show_all_data(data):
        print(f"Название: {data['name']}")
        print(f"Состав: {data['ingredients']}")
        print(f"Цена: {data['price']}")
        print(f"Вес: {data['weight']}")

    @staticmethod
    def show_ingredients_and_weight(data):
        print(f"Состав: {data['ingredients']}")
        print(f"Вес: {data['weight']}")

    @staticmethod
    def show_price(data):
        print(f"Цена: {data['price']}")