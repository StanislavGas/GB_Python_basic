"""
Задание 3.
Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.
Класс-исключение должен контролировать типы данных элементов списка.
"""


class MyError(Exception):
    @staticmethod
    def func_check(num):
        if not num.isdigit():
            print(f"Ошибка! Присутствует элемент типа данных: {type(num)}")
        else:
            return int(num)


my_list = []
while True:
    print('Для выхода введите Q/q')
    user_in = input('Введите число: ')
    if user_in == 'q' or user_in == 'Q':
        break
    elif MyError.func_check(user_in):
        my_list.append(user_in)
    else:
        continue
print(f'Итоговый список {my_list}')
