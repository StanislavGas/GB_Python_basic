"""
Задание 5.
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    @staticmethod
    def draw():
        print('Запуск отрисовки')


Stationery.draw()


class Pen(Stationery):

    def draw(self):
        print(f'Рисуем {self.title}\n[̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅]')


class Pencill(Stationery):

    def draw(self):
        print(f'Рисуем {self.title}\n(̾●̮̮̃̾•̃̾)۶٩(̾●̮̮̃̾•̃̾)۶٩(̾●̮̮̃̾•̃̾)۶٩(̾●̮̮̃̾•̃̾)۶٩(̾●̮̮̃̾•̃̾)۶٩(̾●̮̮̃̾•̃̾)۶')


class Handle(Stationery):

    def draw(self):
        print(f'Рисуем {self.title}\n♜♞♝♚♛♝♞♜♟♟♟♟♟♟♟♟ vs. ♙♙♙♙♙♙♙♙♖♘♗♔♕♗♘♖')


pen = Pen("Pen")
pen.draw()
pencill = Pencill('Pencill')
pencill.draw()
handle = Handle('Handle')
handle.draw()
