"""
Задание 1.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init()__),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода __str()__ для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add()__ для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
Пример:
1 2 3
4 5 6
7 8 9
1 2 3
4 5 6
7 8 9
Сумма матриц:
2 4 6
8 10 12
14 16 18
"""


class Matrix:
    def __init__(self, *args):
        self.matrix_list = list(*args)

    def __str__(self):
        result = '\n'.join(map(str, self.matrix_list))
        result = result.replace(',', '').replace('[', '').replace(']', '')
        return result

    def __add__(self, other):
        matrix_sum = []
        for i in range(len(self.matrix_list)):
            line_sum = []
            for j in range(len(self.matrix_list[i])):
                line_sum.append(self.matrix_list[i][j] + other.matrix_list[i][j])
            matrix_sum.append(line_sum)
        matrix_result = '\n'.join(map(str, matrix_sum))
        matrix_result = matrix_result.replace(',', '').replace('[', '').replace(']', '')
        return matrix_result


matrix = Matrix([[2, 5, 3], [1, 2, 7], [1, 4, 3]])
matrix_2 = Matrix([[1, 2, 3], [9, 6, 3], [1, 2, 8]])
print(f'Матрица 1:\n{matrix}')
print(f'Матица 2:\n{matrix_2}')
print(f'Сумма матриц:\n{matrix + matrix_2}')
