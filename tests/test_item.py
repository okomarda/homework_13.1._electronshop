"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item
import csv

file = "../items.csv"

item1 = Item ("Смартфон", 10000, 20)
item2 = Item ("Ноутбук", 20000, 5)
item1.pay_rate = 0.8
item2.pay_rate = 0.9
item2.name = "Суперсмартфон"


def test_item_repr() :
    assert item1.__repr__ ( ) == "Item('Смартфон', 10000, 20)"


def test_item_str() :
    assert item1.__str__ ( ) == 'Смартфон'


def test_calculation() :
    assert Item.calculate_total_price (item1) == 200000
    assert Item.calculate_total_price (item2) == 100000


def test_discount() :
    assert Item.apply_discount (item1) == 8000
    assert Item.apply_discount (item2) == 18000


def test_private() :
    assert item2.name == "Ноутбук"
    assert item1.name == "Смартфон"


def test_len_list() :
    assert len (Item.instantiate_from_csv (file)) == 5


def test_string_to_number() :
    assert Item.string_to_number ('5.45') == 5
    assert Item.string_to_number ('5.0') == 5
    assert Item.string_to_number ('77') == 77

def test_filenotfound():
    if file is None:
        assert Item.instantiate_from_csv(file) == "FileNotFoundError: Отсутствует файл item."

def test_file_bad():
    with open (file, newline='') as csvfile :
        reader = csv.DictReader (csvfile)
        for row in reader:
            row_list = list (row.values ( ))
            if len(row_list) < 3:
                assert Item.instantiate_from_csv(file) == "src.item.InstantiateCSVError: InstantiateCSVError: Файл item.csv поврежден"


