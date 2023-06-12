import csv

file = '../items.csv'

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price:float, quantity: int):
        self.__name = name
        self.price = price
        self.quantity = quantity
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    file = "../items.csv"
    @classmethod
    def instantiate_from_csv(cls, file):
        try:
            with open (file, newline='') as csvfile :
                reader = csv.DictReader (csvfile)
                for row in reader:
                    row_list = list(row.values())
                    item = Item(row_list[0], row_list[1], row_list[2])
                    all.append(item)
                return all
        except FileNotFoundError:
            print("FileNotFoundError: Отсутствует файл item.csv")

        except:
            if len(row.keys()) < 3:
                raise InstantiateCSVError
            elif row.keys() is None:
                raise InstantiateCSVError


    @staticmethod
    def string_to_number(number):
        if number == str(float(number)):
            return int(float(number))
        elif number == str (int (number)):
            return int (number)

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        elif len(name) > 10:
            print("Количество символов в наименовании товаров превышает 10")


    def calculate_total_price(self):
        return self.price*self.quantity

    def apply_discount(self):
        self.price = self.price*self.pay_rate
        return self.price

    @classmethod
    def __compare_quant(cls, other) :
        if issubclass (Item, (int, Item)) :
            return other if isinstance (other, int) else int (other.quantity)

        raise TypeError ("Операнд справа должен быть числом или объектом класса")

    def __add__(self, other) :
        quan = self.__compare_quant (other)
        return int (self.quantity) + int (quan)

class InstantiateCSVError(Exception):
    """Класс исключения при повреждении файла"""

    def __init__(self, *args, **kwargs) :
        self.message = args[0] if args else 'InstantiateCSVError: Файл item.csv поврежден'

    def __str__(self):
        return self.message


all = Item.all

#item = Item("Помидоры", 50.5, 100)
#print(item.name)
#item.name = "телефон"
#print(item.name)
#item.name = "супертелефон"
#print(item.name)


#print(Item.instantiate_from_csv(file))
#print(len(Item.all))
#print(Item.all[0])
#item1 = Item.all[0]
#print(item1.name)
#print(item.__repr__())
#print(item.quantity)


