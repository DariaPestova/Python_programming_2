# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Bouquet:
    def __init__(self, number_of_flowers: int, cost_of_flowers: float):
        """
        Создание и подготовка к работе объекта "Букет"

        :param number_of_flowers: Количество цветов в шт.
        :param cost_of_flowers: Стоимость цветка в руб.

        Примеры:
        >>> bouquet = Bouquet(7, 2750)  # инициализация экземпляра класса
        """
        if not isinstance(number_of_flowers, int):
            raise TypeError("Количество цветов должно быть типа int")
        if number_of_flowers < 0:
            raise ValueError("Количество цветов не может быть отрицательным числом")
        if number_of_flowers % 2 == 0:
            raise ValueError("Количество цветов не должно быть четным числом")
        self.number_of_flowers = number_of_flowers

        if not isinstance(cost_of_flowers, (int, float)):
            raise TypeError("Стоимость цветка должна быть int или float")
        if cost_of_flowers < 0:
            raise ValueError("Стоимость цветка не может быть отрицательным числом")
        self.cost_of_flowers = cost_of_flowers

    def cost_of_bouquet(self) -> float:
        """
        Функция которая рассчитывает стоимость букета

        :return: Стоимость букета

        Примеры:
        >>> bouquet = Bouquet(7, 2750)
        >>> bouquet.cost_of_bouquet()
        """
        ...

    def add_decor(self, decor: bool) -> None:
        """
        Добавление обертки к букету.
        :param decor: Наличие обертки у букета


        Примеры:
        >>> bouquet = Bouquet(7, 2750)
        >>> bouquet.add_decor(True)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации


class TVseries:
    def __init__(self, name: str, number_of_episodes: int, genre_: str):
        """
        Создание и подготовка к работе объекта "Сериал"

        :param name: Название
        :param number_of_episodes: Количество серий
        :param genre_: Жанр


        Примеры:
        >>> tv_series = TVseries("Кухня", 120, "Комедия")  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название сериала должно быть указана типом string")
        self.name = name

        if not isinstance(number_of_episodes, int):
            raise TypeError("Количество серий должно быть типа int")
        if number_of_episodes < 0:
            raise ValueError("Количество серий не может быть отрицательным числом")
        self.number_of_episodes = number_of_episodes

        if not isinstance(genre_, str):
            raise TypeError("Жанр должен быть указан типом string")
        self.genre_ = genre_

    def recommendation(self, want_length: int, want_genre: str) -> bool:
        """
        Функция которая отвечает запросу стоит ли рекомендовать данный сериал по заданному запросу

        :param want_length: Желаемая длина сериала
        :param want_genre: Желаемый жанр

        :return: Стоит ли рекомендовать этот сериал

        Примеры:
        >>> tv_series = TVseries("Кухня", 120, "Комедия")
        >>> tv_series.recommendation(16,"Драма")
        """
        ...

    def add_reviews(self, reviews: str) -> None:
        """
        Добавление отзыва к карточке сериала.
        :param reviews: Отзыв к сериалу


        Примеры:
        >>> tv_series = TVseries("Кухня", 120, "Комедия")
        >>> tv_series.add_reviews("Сейчас папочка всех накормит!")
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации


class SweetBox:
    def __init__(self, type_of_sweets: str, number_of_sweets: int):
        """
        Создание и подготовка к работе объекта "Сладкий подарок"

        :param type_of_sweets: Вид конфет
        :param number_of_sweets: Количество конфет


        Примеры:
        >>> sweet_box = SweetBox("Мишка на севере", 150)  # инициализация экземпляра класса
        """
        if not isinstance(type_of_sweets, str):
            raise TypeError("Вид конфет должен быть указан типом string")
        self.type_of_sweets = type_of_sweets

        if not isinstance(number_of_sweets, int):
            raise TypeError("Количество конфет должно быть типа int")
        if number_of_sweets < 0:
            raise ValueError("Количество конфет не может быть отрицательным числом")
        self.number_of_sweets = number_of_sweets

    def weight(self, weight_of_one: int) -> float:
        """
        Функция которая вычисляет итоговый вес в кг "Сладкого подарка"

        :param weight_of_one: Вес одной конфетки в гр

        :return Вес сладкого подарка в кг

        Примеры:
        >>> sweet_box = SweetBox("Мишка на севере", 150)
        >>> sweet_box.weight(13)
        """
        ...

    def cost(self, price: float) -> float:
        """
        Функция которая вычисляет итоговую стоимость "Сладкого подарка" в руб
        :param price: Стоимость конфет

        :return Стоимость сладкого подарка


        Примеры:
        >>> sweet_box = SweetBox("Мишка на севере", 150)
        >>> sweet_box.cost(800)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
