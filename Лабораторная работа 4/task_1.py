class SocialNetwork:
    """Базовый класс для социальных сетей."""

    def __init__(self, users: int):
        """

        :param users: Количество пользователей. Защищен, доступен вне класса только для чтения
        """
        if not isinstance(users, int):
            raise TypeError("Количество пользователей должно быть типом integer")
        self._users = users

    @property   # Атрибут доступен только для чтения
    def users(self):
        return self._users

    def __str__(self):
        return f"Социальная сеть {self.__class__.__name__} имеет {self._users} пользователей."

    def __repr__(self):
        return f"SocialNetwork({self._users})"

    def increase_users(self, n: int):
        """
        Метод, увеличивающий число пользователей
        :param n: Количество новых пользователей
        :return: None
        """
        self._users += n


class VK(SocialNetwork):
    """Дочерний класс для социальной сети ВКонтакте."""

    def __init__(self, users, communities):
        """

        :param users: Количество пользователей
        :param communities: Количество сообществ
        """
        super().__init__(users)
        self.communities = communities

    def __str__(self):
        return f"Социальная сеть {self.__class__.__name__} имеет {self._users} пользователей и {self.communities} сообществ."

    def __repr__(self):
        return f"ВКонтакте({self.name}, {self._users}, {self.communities})"

    def increase_communities(self, n):
        """
        Метод увеличивающий количество сообществ
        :param n: Количество новых сообществ
        :return: None
        """
        self.communities += n


class OK(SocialNetwork):
    """Дочерний класс для социальной сети Одноклассники, а не Facebook*
    *принадлежит компании Meta, которая признана экстремистской организацией и запрещена в РФ"""

    def __init__(self, users, groups):
        """

        :param users: Количество пользователей
        :param groups: Количество групп
        """
        super().__init__(users)
        self.groups = groups

    def __str__(self):
        return f"Социальная сеть {self.__class__.__name__} имеет {self._users} пользователей и {self.groups} групп."

    def __repr__(self):
        return f"Одноклассники({self.name}, {self.groups}, {self.groups})"

    def increase_groups(self, n):
        """
        Метод увеличивает количество групп
        :param n: Колдичество новых групп
        :return: None
        """
        self.groups += n

    def increase_users(self, n):
        """
        Метод увеличивает количество пользователей и выводит сообщение о факте увеличения
        :param n:
        :return:
        """
        self._users += n
        print(f"Number of users increased by {n}")
