# Задание 2.
# Написать программу «успеваемость». Пользователь вводит 10 оценок студента. Оценки от 1 до 12. Реализовать
# меню для пользователя:
# Вывод оценок (вывод содержимого списка);
# Пересдача экзамена (пользователь вводит номер элемента списка и новую оценку);
# Выходит ли стипендия (стипендия выходит, если средний бал не ниже 10.7);
# Вывод отсортированного списка оценок: по возрастанию или убыванию.

def print_grades():
    """Функция вывода оценок студента"""
    print('\n' * 100)
    print('*' * 48)
    for j in range(len(grade_pool)):
        print(f'Оценка номер {j + 1} = {grade_pool[j]}')
    print('*' * 48)


def bubble_sort(array: list) -> list:
    """Функция сортировки массива оценок"""
    for i in range(len(array)):
        for j in range(len(array) - 1, 0, -1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
    return array


grade_pool = []     # формируем список оценок студента
counter = 1         # счётчик оценок студента

# блок ввода данных об оценках студента
while True:
    try:
        while len(grade_pool) < 10:
            _grade = int(input(f'Введите оценку номер {counter} студента от 1 до 12: '))
            if 0 < _grade <= 12:
                grade_pool.append(_grade)
                counter += 1  # счётчик оценок
            else:
                print("Введенные данные должны быть число от 1 до 12.")
        break
    except ValueError:
        print("Введенные данные должны быть число от 1 до 12.")

print_grades()

# блок изменения оценок
_choiceOfRetake = input('Нужно ли менять какую-либо оценку?(yes/no): ')
if 'y' in _choiceOfRetake:
    while True:
        try:
            _indexOfGrade = int(input('Введите порядковый номер оценки для пересдачи: '))
            _gradeValue = int(input('Введите новую оценку после пересдачи: '))
            if 1 <= _indexOfGrade <= 10 and 1 <= _gradeValue <= 12:
                break
            else:
                print('Кол-во оценок всего 10.')
        except ValueError:
            print('Номер оценки должен быть числом.')

    grade_pool[_indexOfGrade - 1] = _gradeValue
    print_grades()




# выходит ли стипендия, стипендия выходит, если средний бал не ниже 10.7
_avgGrades = round((sum(grade_pool) / len(grade_pool)), 1)
if _avgGrades >= 10.7:
    print(f'Средняя оценка студента {_avgGrades}')
    print('Данному студенту можно платить стипендию.')
else:
    print(f'Средняя оценка студента {_avgGrades}')
    print('Данный студент стипендии недостоин.')

# вызываем функцию сортировки списка
sorted_grade_pool = bubble_sort(grade_pool)

# выводим оценки данного студента в порядке возрастания или убывания
while True:
    _typePrintGradePools = input('Для отображения оценок в порядке возрастания выберите 1, в порядке убывания 0: ')
    match _typePrintGradePools:
        case "1":
            print('Оценки данного студента в порядке возрастания:  ')
            for el in sorted_grade_pool:
                print(el, end=', ')
            break
        case "0":
            print('Оценки данного студента в порядке убывания: ')
            for el in sorted_grade_pool[::-1]:
                print(el, end=', ')
            break
        case _:
            print('Выбрать надо 1 или 0.')
