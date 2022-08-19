"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
Реализуйте вариант без и с генераторным выражением
"""

start_list = [1, 10, 25, 32, 5, 4, 86, 4]
final_list = []
for el in range(1, len(start_list)):
    if start_list[el] > start_list[el - 1]:
        final_list.append(start_list[el])
print(final_list)

gen_list = [start_list[el] for el in range(1, len(start_list)) if start_list[el] > start_list[el - 1]]
print(gen_list)
