"""
Задание 2.
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Единственный класс этого проекта — одежда (класс Clothes).
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5),
для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать
абстрактный класс для единственного класса проекта,
проверить на практике работу декоратора @property
Пример:
Расход ткани на пальто = 1.27
Расход ткани на костюм = 20.30
Общий расход ткани = 21.57
Два класса: абстрактный и Clothes
"""
from abc import ABC, abstractmethod


class AbstractCloth(ABC):

    def expend(self):
        return print('Затраты')

    @abstractmethod
    def coat_cloth(self):
        pass

    @abstractmethod
    def suit_cloth(self):
        pass


class Clothes(AbstractCloth):

    def __init__(self, v, h):
        self.v = v
        self.h = h
        self.coat_res = round((self.v / 6.5 + 0.2), 2)
        self.suit_res = round((2 * self.h + 0.3), 2)

    def coat_cloth(self):
        return f'Расход ткани на пальто = {self.coat_res}'

    def suit_cloth(self):
        return f'Расход ткани на костюм = {self.suit_res}'

    @property
    def expend(self):
        return f'Общий расход ткани = {self.suit_res + self.coat_res}'


c = Clothes(48, 180)
print(c.suit_cloth())
print(c.coat_cloth())
print(c.expend)

"""Пытался придумать другое решение, но в итоге все попытки привели меня только к такому"""
