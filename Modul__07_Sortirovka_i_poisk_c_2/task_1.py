# Задание 1.
# Написать программу «справочник». Создать два списка целых. Один
# список хранит идентификационные коды, второй — телефонные номера.
# Реализовать меню для пользователя:
# ■ Отсортировать по идентификационным кодам;
# ■ Отсортировать по номерам телефона;
# ■ Вывести список пользователей с кодами и телефонами;
# ■ Выход.

import random


codes = [i for i in range(1, 21)]      # список кодов
random.shuffle(codes)               # перемешиваем список кодов

# формируем список номеров телефонов
phone_numbers = []
operators_prefixes = [911, 912, 917, 919, 981, 982, 987, 988, 989, 904, 921, 922, 927, 929, 931, 932, 937, 939, 999,
                      900, 901, 902, 904, 908, 950, 951, 952, 953, 991, 992]
for i in range(20):
    _first_part_phone_num = str(random.choice(operators_prefixes))
    _second_part_phone_num = str(random.randint(1000000, 9999999))
    _telephone_number = _first_part_phone_num + _second_part_phone_num      # объединяем префикс оператора и номер
    phone_numbers.append(int(_telephone_number))        # добавляем в массив конвертировав в число

print(f'Codes: {codes}')
print(f'Numbers: {phone_numbers}')

# выбор пользователя по какому списку проводить сортировку
while True:
    _typeOfSorting = input('Выберите вид сортировки: 0 - по идентификационным кодам, 1 - по номерам телефона: ')
    if _typeOfSorting == '1' or _typeOfSorting == '0':
        break
    print('Ввести надо ноль или единицу.')

# блок сортировки списков
match _typeOfSorting:
    case '0':
        for i in range(len(codes)):
            for j in range(0, 20-i-1):
                if codes[j] > codes[j + 1]:
                    codes[j], codes[j + 1] = codes[j + 1], codes[j]
                    phone_numbers[j], phone_numbers[j+1] = phone_numbers[j + 1], phone_numbers[j]
        print('Выполнена сортировка по кодам.')
        print(f'Codes: {codes}')
        print(f'Numbers: {phone_numbers}')
    case '1':
        for i in range(len(phone_numbers)):
            for j in range(0, 20 - i - 1):
                if phone_numbers[j] > phone_numbers[j + 1]:
                    phone_numbers[j], phone_numbers[j + 1] = phone_numbers[j + 1], phone_numbers[j]
                    codes[j], codes[j + 1] = codes[j + 1], codes[j]
        print('Выполнена сортировка по номерам телефона.')
        print(f'Codes: {codes}')
        print(f'Numbers: {phone_numbers}')
    case _:
        pass
