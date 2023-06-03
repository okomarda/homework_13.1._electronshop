from src.item import Item

file = '../items.csv'

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv(file)
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv(file)
    # InstantiateCSVError: Файл item.csv поврежден
