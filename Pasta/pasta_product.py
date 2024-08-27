from abc import ABC, abstractmethod


class PastaProduct(ABC):

    @abstractmethod
    def make_pasta(self, order):
        pass

    @abstractmethod
    def add_additional_ingredient(self):
        pass

    @abstractmethod
    def bake_pasta(self, order):
        pass


class MenuPasta(PastaProduct):
    menu = {
        "Гавайская паста": [100, 150, ["сливочный соус", "ветчина", "филе цыпленка", "ананасы", "сыр пармезан", "базилик"]],
        "Грибная паста": [80, 120, ["чесночный соус", "ветчина", "свежие шампиньоны", "сыр пармезан", "базилик"]],
        "Сырный цыпленок паста": [110, 155, ["сливочный соус", "филе цыпленка", "свежие томаты", "сыр пармезан", "базилик"]],
        "Пепперони паста": [120, 170, ["сливочный соус", "пепперони", "сыр пармезан", "базилик"]],
        "Тунец - тысяча островов паста": [200, 300, ["соус тысяча островов", "тунец", "маслины", "сыр пармезан", "лимон", "базилик"]],
    }
    additional_ingredients = []

    def make_pasta(self, order):
        if order in self.menu.keys() and self.additional_ingredients:
            return f"Формируем пасту {order} с составом:\n{', '.join(self.menu[order][2])}\nДополнительно: {', '.join(self.additional_ingredients)}"
        elif order in self.menu.keys():
            return f"Формируем пасту {order} со стандартным составом:\n{', '.join(self.menu[order][2])}\n"

    def add_additional_ingredient(self):
        ingredient = input("Выберете дополнительный ингредиент или нажмите стоп: ")
        while ingredient not in ['stop', 'end', 'стоп', 'конец', 'нет']:
            self.additional_ingredients.append(ingredient)
            ingredient = input("Выберете дополнительный ингредиент или нажмите стоп: ")

    def bake_pasta(self, order):
        if not self.additional_ingredients:
            return f"Выпекаем пасту {order} со стандартным составом:\n{', '.join(self.menu[order][2])}\n"
        else:
            return f"Выпекаем пасту {order} со дополнительными ингредиентами:\n{', '.join(self.additional_ingredients)}\n"


class OwnPasta(PastaProduct):
    ingredients = []

    def make_pasta(self, order):
        ingredient = input("Выберете желаемый ингредиент или нажмите стоп: ")
        while ingredient not in ['stop', 'end', 'стоп', 'конец', 'нет']:
            self.ingredients.append(ingredient)
            ingredient = input("Выберете желаемый ингредиент или нажмите стоп: ")
        print()
        return f"Формируем пасту {order} с желаемыми ингредиентами:\n{', '.join(self.ingredients)}"

    def add_additional_ingredient(self):
        pass

    def bake_pasta(self, order):
        own_pasta = {order: [150, 200, self.ingredients]}
        return f"Выпекаем пасту {order} с желаемыми ингредиентами:\n{', '.join(self.ingredients)}\n", own_pasta
