# Задание 2.
# Написать программу «книги». Создать два списка годы выпуска. Реализовать меню для пользователя:
# ■ Отсортировать по названию книг;
# ■ Отсортировать по годам выпуска;
# ■ Вывести список книг с названиями и годами выпуска;
# ■ Выход;


def printing_lists(array1: list, array2: list) -> None:
    for i in range(len(array1)):
        print(f"{array1[i]} : {array2[i]}")


# список книг и список дат издания этих книг
listBooks = ['Старик и море', 'Прощай оружие!', 'Тошнота', 'Чума', 'Конец режима', 'Физика невозможного']
listPublishing = [1952, 1929, 1938, 1947, 2023, 2008]

printing_lists(array1=listBooks, array2=listPublishing)

# выбор пользователя по какому списку проводить сортировку
while True:
    _typeOfSorting = input('Выберите вид сортировки: 0 - по названиям книг, 1 - по датам издания: ')
    if _typeOfSorting == '1' or _typeOfSorting == '0':
        break
    print('Ввести надо ноль или единицу.')

match _typeOfSorting:
    case '0':
        for i in range(len(listBooks) - 1):
            for j in range(len(listBooks) - i - 1):
                if listBooks[j] > listBooks[j + 1]:
                    listBooks[j], listBooks[j + 1] = listBooks[j + 1], listBooks[j]
                    listPublishing[j], listPublishing[j + 1] = listPublishing[j + 1], listPublishing[j]
        printing_lists(array1=listBooks, array2=listPublishing)
    case '1':
        for i in range(len(listPublishing) - 1):
            for j in range(len(listPublishing) - i - 1):
                if listPublishing[j] > listPublishing[j + 1]:
                    listPublishing[j], listPublishing[j + 1] = listPublishing[j + 1], listPublishing[j]
                    listBooks[j], listBooks[j + 1] = listBooks[j + 1], listBooks[j]
        printing_lists(array1=listBooks, array2=listPublishing)
    case _:
        pass
