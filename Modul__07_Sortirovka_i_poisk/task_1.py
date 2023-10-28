# Задание 1.
# Необходимо отсортировать первые две трети списка
# в порядке возрастания, если среднее арифметическое
# всех элементов больше нуля; иначе — лишь первую треть.
# Остальную часть списка не сортировать, а расположить
# в обратном порядке.


from random import randint

# формируем исходный список и перемешиваем значения
myList = [randint(-10,10) for i in range(12)]

# находим среднеарифметическое элементов списка
_avgOfmyList = sum(myList) / len(myList)
print(f'myList: {myList}')
print(f'Среднеарифметическое списка {_avgOfmyList}')

if _avgOfmyList > 0:            # случай когда если среднее арифметическое всех элементов больше нуля
    print('1й случай')
    lenTargetList = (len(myList) // 3) * 2  # вырезаем 2/3 списка
    for i in range(lenTargetList):          # производим пузырьковую сортировку
        for j in range(lenTargetList-1, 0, -1):
            if myList[j-1] > myList[j]:
                myList[j-1], myList[j] = myList[j], myList[j-1]
    reverseList = list(reversed(myList[lenTargetList:len(myList)]))     # делаем reverse для остальной 1/3 списка
    print(myList[0:lenTargetList] + reverseList)                        # соединяем все части списка
else:                           # случай когда если среднее арифметическое всех элементов меньше нуля
    print('2й случай')
    lenTargetList = (len(myList) // 3)      # вырезаем 1/3 списка
    for i in range(lenTargetList):          # производим пузырьковую сортировку
        for j in range(lenTargetList-1, 0, -1):
            if myList[j-1] > myList[j]:
                myList[j-1], myList[j] = myList[j], myList[j-1]
    reverseList = list(reversed(myList[lenTargetList:len(myList)]))     # делаем reverse для остальных 2/3 списка
    print(myList[0:lenTargetList] + reverseList)                        # соединяем все части списка
