import doctest


# TODO Написать 3 класса с документацией и аннотацией типов
class Flat:
    def __init__(self, area: float, floor: int, number_of_residents: int):
        """
        Создание и подготовка к работе объекта "Квартира"

        :param area: Площадь квартиры
        :param floor: Этаж, на котором находится квартира
        :param number_of_residents: Количество постоянных жильцов квартиры

        Примеры:
        >>> flat = Flat(45.5, 4, 3)  # инициализация экземпляра класса
        """
        if not isinstance(area, (int, float)):
            raise TypeError("Площадь квартиры должна быть типа int или float")
        if area <= 0:
            raise ValueError("Площадь квартиры должна быть положительной")
        self.area = area

        if not isinstance(floor, int):
            raise TypeError("Этаж должен быть типа int")
        if floor <= 0:
            raise ValueError("Этаж должен быть положительным")
        self.floor = floor

        if not isinstance(number_of_residents, int):
            raise TypeError("Количество постоянных жильцов должно быть типа int")
        if number_of_residents < 0:
            raise ValueError("Количество постоянных жильцов не может быть отрицательным")
        self.number_of_residents = number_of_residents

    def is_another_resident(self, num_of_beds) -> bool:
        """
        Данный метод позволяет узнать есть ли возможность заселить в квартиру еще одного человека

        :param num_of_beds: Сколько кроватей в квартире

        :raise ValueErorr: Если количество кроватей отрицательное, то выводим ошибку

        :return: Есть ли свободная кровать в квартире

        Примеры:
        >>> flat = Flat(45.5, 4, 3)
        >>> flat.is_another_resident(4)
        """
        if not isinstance(num_of_beds, int):
            raise TypeError("Количество кроватей должно быть типа int или float")
        if num_of_beds < 0:
            raise ValueError("Количество кровей не может быть отрицательным")
        ...

    def flat_population_density(self) -> float:
        """
        Данный метод позволяет рассчитать плотность населения квартиры

        :return: Плотность населения в квартире

        Примеры:
        >>> flat = Flat(45.5, 4, 3)
        >>> flat.flat_population_density()
        """
        ...

    def lock(self):
        """
        Данный метод позволяет закрыть квартиру

        Примеры:
        >>> flat = Flat(45.5, 4, 3)
        >>> flat.lock()
        """
        ...


class Furniture:
    def __init__(self, kind_of_furniture: str, material: str, cost: int):
        """
        Создание и подготовка к работе объекта "Мебель"

        :param kind_of_furniture: Тип мебели
        :param material: Материал, из которого сделана мебель
        :param cost: Стоимость мебели в рублях

        Примеры:
        >>> furniture = Furniture("Шкаф", "ДСП", 20000)  # инициализация экземпляра класса
        """
        if not isinstance(kind_of_furniture, str):
            raise TypeError("Тип мебели должен быть типа str")
        self.kind_of_furniture = kind_of_furniture

        if not isinstance(material, str):
            raise TypeError("Материал мебели должен быть типа str")
        self.material = material

        if not isinstance(cost, (int, float)):
            raise TypeError("Стоимость мебели должна быть типа int или float")
        if cost < 0:
            raise ValueError("Стоимость не может быть отрицательной")
        self.cost = cost

    def is_it_fireresistant(self) -> bool:
        """
        Данный метод позволяет узнать огнестойкая ли мебель

        :return: Огнеупорная ли мебель

        Примеры:
        >>> furniture = Furniture("Шкаф", "ДСП", 20000)
        >>> furniture.is_it_fireresistant()
        """
        ...

    def build(self):
        """
        При помощи данного метода осуществляется сборка мебели

        Примеры:
        >>> furniture = Furniture("Шкаф", "ДСП", 20000)
        >>> furniture.build()
        """
        ...

    def which_room(self) -> str:
        """
        Данный метод осуществляет выбор подходящего помещения

        :return: Помещение, в котором будет установлена мебель

        Примеры:
        >>> furniture = Furniture("Шкаф", "ДСП", 20000)
        >>> furniture.which_room()
        """
        ...


class Code:
    def __init__(self, language: str, platform: str, number_of_strings: int):
        """
        Создание и подготовка к работе объекта "Код"

        :param language: Название языка программирования, на котором написан код
        :param platform: Платформа для которой написан код
        :param number_of_strings: Количество строк

        Примеры:
        >>> code = Code("Java", "Android", 537)  # инициализация экземпляра класса
        """
        if not isinstance(language, str):
            raise TypeError("Название языка программирования должнн быть типа str")
        self.language = language

        if not isinstance(platform, str):
            raise TypeError("Платформа должна быть типа str")
        self.platform = platform

        if not isinstance(number_of_strings, int):
            raise TypeError("Число строк должно быть типа int")
        if number_of_strings <= 0:
            raise ValueError("Число строе должно быть положительным")
        self.number_of_strings = number_of_strings

    def rewrite(self, new_language: str) -> str:
        """
        Данный метод позволяет переписать код на другом языке программирования

        :param new_language: Новый язык программирования

        :raise TypeError: Если введене несуществующий или не сопоставимый язык программирования, выводим ошибку

        :return: Переписанный код

        Примеры:
        >>> code = Code("Java", "Android", 537)
        >>> code.rewrite("C")
        """
        if not isinstance(new_language, str):
            raise TypeError("Новый язык программирования должен быть типа str")
        ...

    def run(self):
        """
        Данный метод позволяет запустить код

        Примеры:
        >>> code = Code("Java", "Android", 537)
        >>> code.run()
        """
        ...

    def count_symbols(self) -> int:
        """
        Высчитывает количество символов в коде

        :return: Количество символов в коде

        Примеры:
        >>> code = Code("Java", "Android", 537)
        >>> code.count_symbols()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
