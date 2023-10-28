# Задание 3.
# Написать программу, реализующую сортировку списка
# методом усовершенствованной сортировки пузырьковым
# методом. Усовершенствование состоит в том, чтобы анализировать количество перестановок на каждом шагу, если
# это количество равно нулю, то продолжать сортировку нет смысла — список отсортирован.

from random import randint


def bubble_sort_mod(array: list) -> list:
    """Функция усовершенствованная пузырьковая сортировка"""
    for i in range(len(array) - 1):
        counter = 0
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j + 1], array[j] = array[j], array[j + 1]
                counter += 1
        if counter == 0:
            return array
    return array


# формируем несортированный список, вызываем фукнцию сортировки
myOriginList = [(randint(-100, 100)) for i in range(12)]
mySortedList = bubble_sort_mod(myOriginList)

# вывод элементов сортированного списка
print('Сортированный список: ')
for el in mySortedList:
    print(el, end=' ')
