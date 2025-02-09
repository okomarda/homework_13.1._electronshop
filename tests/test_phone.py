"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.phone import Phone
from src.item import Item

phone1 = Phone("iPhone 14", 120000, 5, 2)
item1 = Item ("Смартфон", 10000, 20)

def test_str():
    assert phone1.__str__() == "iPhone 14"

def test_repr():
    assert phone1.__repr__() == "Phone('iPhone 14', 120000, 5, 2)"

def test_number_of_sim():
    assert phone1.number_of_sim == 2

def test_error_number_of_sim():
    if phone1.number_of_sim <= 0:
        assert phone1.number_of_sim == "ValueError: Количество физических SIM-карт должно быть целым числом больше нуля."

def test_add():
    assert phone1 + item1 == 25
    assert phone1 + phone1 == 10
    assert phone1 + 10 == 15
    assert item1 + phone1 == 25







