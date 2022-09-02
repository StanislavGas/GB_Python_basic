"""
Задание 4.
Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).
А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
from time import *


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} начала движение.")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn(self, direction):
        print(f"Автомобиль {self.name} повернул {direction}")

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"{self.name}!Превышение скорости!Вы оштрафованы\nПопробуйте еще раз")

    def __str__(self):
        return f'{self.name} цвета {self.color}'


class SportCar(Car):

    def speed_up(self, speed):
        self.speed += 20
        print(f'Текущая скорость {speed}')

    def __str__(self):
        return f'{self.name} цвета {self.color}'

    def speed_break(self, speed):
        self.speed -= 20
        print(f'Снижение скорости {speed}')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости!")

    @staticmethod
    def drop():
        print('Разгрузка')
        for i in range(10):
            print('.', end='')
            sleep(1)
        print('Процесс разгрузки завершен')

    def __str__(self):
        return f'{self.name} цвета {self.color}'


class PoliceCar(Car):
    @staticmethod
    def criminal(target, obj):
        if target > 60 and type(obj).__name__ == 'TownCar':
            print(f'Внимание! Зафиксировано превышение скорости {target} км/ч, водитель остановитесь!')
        elif target > 40 and type(obj).__name__ == 'WorkCar':
            print(f'Внимание! Зафиксировано превышение скорости {target} км/ч, водитель остановитесь!')
        else:
            print('Нарушений не обнаружено')

    @staticmethod
    def radar(obj_car):
        print(f'Обнаружено транспортное средство {obj_car}. Сканирую скорость')
        for i in range(3):
            print('.', end='')
            sleep(1)


def test_drive():
    change = input("Добро пожаловать в автосалон! \nПожалуйста выберите автомобиль из предложенных:\n1-Honda Fit"
                   "\n2-UAZ-Police"
                   "\n3-KAMAZ"
                   "\n4-Ferrari\n")
    if change == '1':
        honda = TownCar(20, 'grey', 'Honda Fit', False)
        input(f'{honda}\nНажмите Enter для начала движения')
        honda.go()
        honda.speed = int(input(f'Ваша текущая скорость {honda.speed}\nВведите значение желаемой скорости: '))
        if honda.speed > 60:
            honda.show_speed()
        else:
            direct = ['налево', 'направо']
            intersection = int(
                input('Через 50 метров перекресток. Укажите направление движения\n1-Налево\n2-Направо\n '))
            honda.turn(direct[intersection - 1])
        breach = input('Вы встречаете нарушителя! Будете преследовать его?\n1-Да\n2-Нет\n')
        if breach == '1' and honda.is_police:
            print('Вы поймали нарушителя!')
        elif breach == '1' and not honda.is_police:
            print('Ваш автомобиль не относится к полицейскому транспорту')
        else:
            print('Нарушитель скрылся')
        print(f'{honda.name} прибыл к месту назначения')
        honda.stop()
    if change == '2':
        uaz = PoliceCar(100, 'white', 'UAZ-Police', True)
        volvo = TownCar(20, 'black', 'Volvo', False)
        tractor = WorkCar(80, 'red', 'Tractor', False)
        lada = TownCar(160, 'green', 'Lada2109', False)
        print("Сводка патрульной машины:")
        uaz.go()
        uaz.turn('направо')
        uaz.turn('налево')
        uaz.stop()
        sleep(3)
        print('Запись рации:')
        uaz.radar(volvo)
        uaz.criminal(volvo.speed, volvo)
        sleep(2)
        uaz.radar(tractor)
        uaz.criminal(tractor.speed, tractor)
        sleep(2)
        uaz.radar(lada)
        uaz.criminal(lada.speed, lada)
    if change == '3':
        kamaz = WorkCar(30, 'yellow', 'KAMAZ', False)
        reno = TownCar(70, 'grey', 'Reno', False)
        print(f'{kamaz} двигался со скоростью {kamaz.speed}\nВ какой-то момент его обогнал автомобиль {reno}\nВодитель'
              f'решил прибавить скорость до {kamaz.speed + 30}. Но тут же получил предупреждение')
        kamaz.speed += 30
        sleep(5)
        kamaz.show_speed()
        sleep(4)
        print(f'Скинув скорость до допустимого значения {kamaz.speed - 20}. Водитель добрался до точки назначения.')
        kamaz.speed -= 20
        kamaz.stop()
        sleep(3)
        print('Водитель приступил к разгрузке.')
        kamaz.drop()
        print('На этом рабочий день подошел к концу! :)')
    if change == '4':
        ferrari = SportCar(0, 'red', 'Ferrari', False)
        print(f'Вы оказались за рулем спорткара {ferrari}. Клавиша Enter - газ')
        start_race = ['Три', 'Два', 'Один', 'Поехали!']
        for i in start_race:
            sleep(1)
            print(i)
        while True:
            input()
            if ferrari.speed == 100:
                print('Внимание! Поверните "направо" (< = налево|аправо = >). У вас 3 секунды!')
                for i in range(3):
                    print('>', end='')
                    sleep(0.5)
                t1 = time()
                direction_race = input()
                t2 = time()
                t_result = t2 - t1
                if direction_race == '>' and t_result <= 3:
                    ferrari.turn('направо')
                    while ferrari.speed != 0:
                        ferrari.speed_break(ferrari.speed)
                        sleep(0.5)
                    ferrari.stop()
                    print('Поздравляем! Вы победили!')
                    break
                else:
                    print('Упс! Вы не успели( \nПопробуйте еще раз')
                    break
            else:
                ferrari.speed_up(ferrari.speed)


while True:
    test_drive()
    restart = input('Желаете поменять автомобиль? yes/no: ')
    if restart == 'yes' or restart == 'y':
        continue
    else:
        print('Спасибо за участие! Всего хорошего')
        break
"""К творческой части подошёл с энтузиазмом :) Каждый выбор имеет уникальный сюжет, поэтому если найдется минутка
попробуйте пожалуйста :) я старался :) код думаю можно оптимизировать, но я и так затянул со сдачей работы"""
