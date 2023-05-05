"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item ("Смартфон", 10000, 20)
item2 = Item ("Ноутбук", 20000, 5)
item1.pay_rate = 0.8
item2.pay_rate = 0.9

def test_item():
    assert Item.calculate_total_price(item1) == 200000
    assert Item.calculate_total_price (item2) == 100000
    assert Item.apply_discount(item1) == 8000
    assert Item.apply_discount (item2) == 18000

