"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

while True:
    line = input("Введите строку или нажмите Enter для завершения: ")
    if line != '':
        with open('data.txt', 'a', encoding='utf-8') as file:
            file.write('%s\n' % line)
    else:
        break

"""В целом написанная часть выше соответсвует тз. Текстовый файл создается и информация добавляется поcтрочно с каждой
итерацией. Далее написал часть кода, которая дополнительно выведет содержание файла
в терминал после завершения ввода"""
with open('data.txt', 'r', encoding='utf-8') as file:
    print(file.read())

"""Второй вариант решения задания через список"""
words_list = []
while True:
    word = input("Введите строку, для завершения ввода нажмите Enter: ")
    if word != '':
        words_list.append(word)
    else:
        break
with open('data2.txt', 'a', encoding='utf-8') as new_file:
    for el in words_list:
        new_file.write('%s\n' % el)
with open('data2.txt', 'r', encoding='utf-8') as new_file:
    print(new_file.read())
