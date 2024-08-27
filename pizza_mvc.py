from Pizza_MVC.pizza_model import PizzaModel
from Pizza_MVC.pizza_view import PizzaView
from Pizza_MVC.pizza_controller import PizzaController


if __name__ == "__main__":
    # Создаем модель
    pizza = PizzaModel("Маргарита", ["томатный соус", "сыр моцарелла", "базилик"], 500, 300)

    # Создаем контроллер
    controller = PizzaController(pizza)

    # Обновляем данные через контроллер
    controller.update_ingredients(["томатный соус", "сыр моцарелла", "базилик", "оливки"])
    controller.update_price(550)
    controller.update_weight(320)

    # Получаем данные через контроллер
    all_data = controller.get_all_data()
    ingredients_and_weight = controller.get_ingredients_and_weight()
    price = controller.get_price()

    # Показываем данные через View
    PizzaView.show_all_data(all_data)
    PizzaView.show_ingredients_and_weight(ingredients_and_weight)
    PizzaView.show_price(price)