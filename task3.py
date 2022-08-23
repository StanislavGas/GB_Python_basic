"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
# Деревянное решение :) ниже есть вариант с более гибким подходом:)
with open("numbers.txt", "r", encoding="utf-8") as file:
    for line in file:
        for el in line.split():
            if el == "One":
                with open("ru_numbers.txt", "a", encoding="utf-8") as ru_file:
                    ru_file.write(line.replace("One", "Один"))
                print(line.replace("One", "Один"))
            if el == "Two":
                with open("ru_numbers.txt", "a", encoding="utf-8") as ru_file:
                    ru_file.write(line.replace("Two", "Два"))
                print(line.replace("Two", "Два"))
            if el == "Three":
                with open("ru_numbers.txt", "a", encoding="utf-8") as ru_file:
                    ru_file.write(line.replace("Three", "Три"))
                print(line.replace("Three", "Три"))
            if el == "Four":
                with open("ru_numbers.txt", "a", encoding="utf-8") as ru_file:
                    ru_file.write(line.replace("Four", "Четыре"))
                print(line.replace("Four", "Четыре"))

# Вариант с более гибким подходом)
ru_num = {1: "Один", 2: "Два", 3: "Три", 4: "Четыре"}
count = 1
with open("numbers.txt", "r", encoding="utf-8") as file:
    for line in file:
        for el in line.split():
            with open("rus_numbers.txt", "a", encoding="utf-8") as rus:
                line.replace(el, ru_num[count])
            count += 1
            break
