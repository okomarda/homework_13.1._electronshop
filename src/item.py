class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []


    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
        all.append(self)


    def calculate_total_price(self) -> float:
        return self.price*self.quantity

    def apply_discount(self):
        self.price = self.price*self.pay_rate
        return self.price


all = Item.all

#item_1 = Item("Помидоры", 50.5, 100)
#item_2 = Item("Огурцы", 30.5, 200)

#print(item_1.name)
#print(item_1.calculate_total_price())

#Item.pay_rate = 0.8
#print(item_1.apply_discount())
#print(Item.all)