"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)
item1.pay_rate = 0.8
item2.pay_rate = 0.9
item2.name = "Суперсмартфон"


def test_item():
    assert Item.calculate_total_price(item1) == 200000
    assert Item.calculate_total_price(item2) == 100000
    assert Item.apply_discount(item1) == 8000
    assert Item.apply_discount(item2) == 18000
    assert item2.name == "Ноутбук"
    assert item1.name == "Смартфон"
    assert len(Item.instantiate_from_csv()) == 5
    assert Item.string_to_number('5.45') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('77') == 77

