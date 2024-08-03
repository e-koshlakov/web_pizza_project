from pizza_creator import PizzaCreator, CreateMenuPizza, CreateOwnPizza


def client_code(creator: PizzaCreator, order: str):
    creator.add_additional_ingredient()
    print(creator.make_pizza(order))
    print(creator.bake_pizza(order))
    print(creator.save_order_to_json(order))


if __name__ == "__main__":
    menu = ["Гавайская", "Грибная", "Сырный цыпленок", "Пепперони", "Тунец - тысяча островов"]
    user_order = input("Введите ваш заказ: ")
    if user_order in menu:
        client_code(CreateMenuPizza(), user_order)
    else:
        client_code(CreateOwnPizza(), user_order)
