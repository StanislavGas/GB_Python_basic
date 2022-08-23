"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

count_lines = 0
count_words = 0
with open(r"test.txt", "r", encoding='utf-8') as file:
    for line in file:
        count_lines += 1
        for el in line.split():
            count_words += 1
        print(f"В строке №{count_lines} количество слов - {count_words}")
        count_words = 0
print(f"Общее количество строк - {count_lines}")
