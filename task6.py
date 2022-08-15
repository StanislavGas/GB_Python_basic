"""6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с
прописной первой буквой. Например, print(int_func(‘text’)) -> Text."""

in_str = input("Введите слова: ")


def int_func1(word):
    print(word.title())


int_func1(in_str)
