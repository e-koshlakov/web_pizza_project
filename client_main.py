from Pizza.pizza_creator import PizzaCreator, CreateMenuPizza, CreateOwnPizza
from Pasta.pasta_creator import PastaCreator, CreateMenuPasta, CreateOwnPasta


def client_code_pizza(creator: PizzaCreator, order: str):
    creator.add_additional_ingredient()
    print(creator.make_pizza(order))
    print(creator.bake_pizza(order))
    print(creator.save_order_to_json(order))


def client_code_pasta(creator: PastaCreator, order: str):
    creator.add_additional_ingredient()
    print(creator.make_pasta(order))
    print(creator.bake_pasta(order))
    print(creator.save_order_to_json(order))


if __name__ == "__main__":
    dish_type = input("Вы хотите заказать пиццу или пасту? (пицца/паста): ").strip().lower()
    if dish_type == "пицца":

        menu = ["Гавайская", "Грибная", "Сырный цыпленок", "Пепперони", "Тунец - тысяча островов"]
        user_order = input("Введите ваш заказ: ")
        if user_order in menu:
            client_code_pizza(CreateMenuPizza(), user_order)
        else:
            client_code_pizza(CreateOwnPizza(), user_order)

    elif dish_type == "паста":
        menu = ["Гавайская паста", "Грибная паста", "Сырный цыпленок паста", "Пепперони паста",
                "Тунец - тысяча островов паста"]
        user_order = input("Введите ваш заказ: ")
        if user_order in menu:
            client_code_pasta(CreateMenuPasta(), user_order)
        else:
            client_code_pasta(CreateOwnPasta(), user_order)

    else:
        print("Неверный выбор. Пожалуйста, выберите 'пицца' или 'паста'.")
