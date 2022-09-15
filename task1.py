"""
Задание 1.
Реализовать класс «Дата», на уровне класса определить атрибут day_month_year,
присвоить ему значение
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц,
год, преобразовывать их тип к типу «Число» и делать атрибутами класса.
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    day_month_year = ''

    @classmethod
    def date_extract(cls, day_month_year):
        extract = []
        for i in day_month_year.split():
            extract.append(int(i))
        cls.day = extract[0]
        cls.month = extract[1]
        cls.year = extract[2]
        return extract

    @staticmethod
    def date_validation(day_month_year):

        if 0 < day_month_year[0] <= 31 and 0 < day_month_year[1] <= 12 and 1900 < day_month_year[2] <= 2999:
            return f'Дата корректна {day_month_year[0]}.{day_month_year[1]}.{day_month_year[2]}'
        else:
            return f'{day_month_year[0]}.{day_month_year[1]}.{day_month_year[2]} - Введенная дата не корректна'


time1 = Date()
time2 = Date()
print(time1.date_extract('13 09 2022'))
print(f'День - {time1.day}, Месяц - {time1.month}, Год - {time1.year}')
print(time1.date_validation(time1.date_extract('13 09 2022')))
print(time2.date_validation(time2.date_extract('45 82 12')))
