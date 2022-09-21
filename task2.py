"""
Задание 2.
Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyException(Exception):
    def __init__(self, result):
        self.result = result


while True:
    a = int(input("Введите делимое число: "))
    b = int(input("Введите делитель число: "))

    try:
        if b == 0:
            raise MyException("На ноль делить нельзя!")
        else:
            print(f"Результат деления = {a / b}")
    except MyException as err:
        print(err)
    except ValueError:
        print("Ошибка ввода! Введите число")
    q = input("q/Q - выход / Enter - Продолжить: ")
    if q == 'q' or q == 'Q':
        break
    else:
        continue
