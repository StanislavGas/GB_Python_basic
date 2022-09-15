"""
Задание 2.
Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyException(Exception):
    @staticmethod
    def division_func(a, b):
        try:
            res = round(a / b, 2)
            print(f"{a} / {b} = {res} \n")
        except ZeroDivisionError:
            print (f"{a} / {b} -> На ноль делить нельзя!\n")


while True:
    print('Для выхода введите Q/q')
    user_in_1 = input('Введите делимое число: ')
    if user_in_1 == 'Q' or user_in_1 == 'q':
        break
    user_in_2 = input('Введите число делитель: ')
    MyException.division_func(int(user_in_1), int(user_in_2))
