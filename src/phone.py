import csv
from src.item import Item

class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    # def _is_valid_number(self, number_of_sim):
    #     if number_of_sim <= 0:
    #         raise ValueError ("Количество физических SIM-карт должно быть целым числом больше нуля.")
    #     else:
    #         return number_of_sim

    def _is_valid_number_of_sim(self, number_of_sim):
        return number_of_sim > 0

    def __setattr__(self, key, value):

        if key == 'number_of_sim' and not self._is_valid_number_of_sim(value):
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        super().__setattr__(key, value)



    @classmethod
    def __compare_quant(cls, other):
        if issubclass(Phone, (int, Item)):
            return other if isinstance (other, int) else int (other.quantity)
        elif issubclass(Phone, (str, float)):
            raise AttributeError("Операнд справа должен быть целым числом")

        #raise TypeError("Операнд справа должен быть числом или объектом класса")


    def __add__(self, other):
        quan = self.__compare_quant(other)
        return int(self.quantity) + int(quan)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    # def check_number_of_sim(self):
    #     if self.number_of_sim is not int:
    #         raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")
    #     elif self.number_of_sim <= 0:
    #         raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")
    #     else:
    #         return self.number_of_sim

# item = Item("Молотки", 100, 250)
# phone = Phone("Xiaomi", 1000, 50, 100)
# phone1 = Phone("iPhone 14", 120000, 5, 2)
# item1 = Item ("Смартфон", 10000, 20)
# print(phone + item)
# print(str(phone1))
# print(repr(phone1))
# print(phone1 + 56)
# print(phone1 + 40)
# phone1.number_of_sim = 2
# print(phone1.number_of_sim)
# print(phone1.__dict__)
# print(item1 + 10)
# print(phone1 + 30)
# print(phone1 + 10)


