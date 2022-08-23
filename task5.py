"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

numbers = input("Введите набор чисел разделяя их пробелами: ")
num_list = []
sum_numbers = 0
with open('task5.txt', 'w', encoding='utf-8') as num:
    for el in numbers:
        num.write(el)
for i in numbers.split():
    num_list.append(int(i))
sum_numbers = sum(num_list)
print(f"Сумма чисел в файле равна {sum_numbers}")
