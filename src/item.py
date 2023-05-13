import csv

file = 'items.csv'

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        self.__name = name
        self.price = price
        self.quantity = quantity


    @classmethod
    def instantiate_from_csv(cls):
        with open ("C:\lessons\homework_13.1._electronshop\src\items.csv", newline='') as csvfile :
            reader = csv.DictReader (csvfile)
            for row in reader:
                row_list = list(row.values())
                item = Item(row_list[0], row_list[1], row_list[2])
                all.append(item)
            return all

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

    def calculate_total_price(self) -> float:
        return self.price*self.quantity

    def apply_discount(self):
        self.price = self.price*self.pay_rate
        return self.price


all = Item.all

#item = Item("Помидоры", 50.5, 100)
#print(item.name)
#item.name = "телефон"
#print(item.name)
#item.name = "супертелефон"
#print(item.name)


#print(Item.instantiate_from_csv())
#print(Item.all)
#print(Item.all[0])
#item1 = Item.all[0]
#print(item1.name)


