'''
4.Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5.Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники 
на склад и передачу в определенное подразделение компании. Для хранения данных 
о наименовании и количестве единиц оргтехники, а также других данных, можно использовать 
любую подходящую структуру, например словарь.

6.Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых 
пользователем данных. Например, для указания количества принтеров, отправленных 
на склад, нельзя использовать строковый тип данных. 
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» 
максимум возможностей, изученных на уроках по ООП.
'''


class Warehouse:
    warehouse_items = {}
    item_id = 1

    def reception(self):
        item_add = Technics()
        while True:
            rec_type = input(
                'Выберите тип техники поступающей на склад\n1)Принтер\n2)Сканер\n3)Ксерокс\nВведите номер: ')
            if rec_type == '1':
                item_add.tech_type = 'Принтер'
                item_type = Printer()
                print('Выберите тип принтера:')
                add_change = item_type.printer_type
                break
            elif rec_type == '2':
                item_add.tech_type = 'Сканер'
                item_type = Scanner()
                print('Выберите тип сканера:')
                add_change = item_type.scanner_type
                break
            elif rec_type == '3':
                item_add.tech_type = 'Ксерокс'
                item_type = Xerox()
                print('Выберите тип ксерокса:')
                add_change = item_type.xerox_type
                break
            else:
                print('Такого типа не существует. Повторите выбор')
                continue
        while True:
            try:
                for el in range(len(add_change)):
                    print(f'{el + 1}){add_change[el]}')
                change = int(input())
                break
            except ValueError:
                print('Введите корректное значение')
        add_change = add_change[change - 1]
        item_add.tech_collor = input('Введите цвет: ')
        item_add.tech_model = input('Введите модель: ')
        while True:
            try:
                item_add.price = int(input('Введите цену: '))
                break
            except ValueError:
                print('Введите корректное значение')

        self.warehouse_items[self.item_id] = f'Тип: {item_add.tech_type}', f'Вид: {add_change}', \
                                             f'Модель: {item_add.tech_model}', f'Цвет: {item_add.tech_collor}', \
                                             f'Цена: {item_add.price}'
        self.item_id += 1
        print(f'\n{item_add.tech_type}', f'Вид: {add_change}',
              f'Модель: {item_add.tech_model}', f'Цвет: {item_add.tech_collor}',
              f'Цена: {item_add.price}'.replace('(', '').replace(',', '').replace(')', '').replace("'", ""))
        return print(f'Успешно добавлен на склад\n')

    def transfer(self):
        print('======== Склад ========')
        for i in self.warehouse_items:
            print(f'ID {i}')
            for el in self.warehouse_items[i]:
                a = ''.join(map(str, el))
                print(a)
            print('\n')
        print('======== Склад ========')
        adress = input('Введите название подразделения получателя: ')
        while True:
            try:
                trans = int(input('Введите ID позиции для отправки: '))
                print(f'{self.warehouse_items[trans]}\nУспешно отправлен {adress}')
                self.warehouse_items.pop(trans)
                break
            except KeyError:
                print('Такой позиции не существует. Повторите ввод')
                continue
        return self.warehouse_items

    def __str__(self):
        print('======== Остаток ========')
        if not self.warehouse_items:
            print('\tСклад пустой')
        for i in self.warehouse_items:
            print(f'ID {i}')
            for el in self.warehouse_items[i]:
                a = ''.join(map(str, el))
                print(a)
            print('\n')
        return '^^^^^^^^ Остаток ^^^^^^^^'


class Technics:
    tech_type = ''
    tech_model = ''
    tech_collor = ''
    price = 0


class Printer(Technics):
    name = 'Принтер'
    printer_type = ['Лазерный', 'Струйный', 'Матричный']


class Scanner(Technics):
    name = 'Сканер'
    scanner_type = ['Ручной', 'Планшетный', 'Проекционный']


class Xerox(Technics):
    name = 'Ксерокс'
    xerox_type = ['Портативный', 'Стационарный']


warehouse_1 = Warehouse()
while True:
    print(
        '\n===== Склад товаров =====\n1)Получить товар\n2)Отправить товар\n3)Товары в наличии\nДля выхода введите Q/q')
    target = input('\nВыберите пункт меню: ')
    print('\n')
    if target == '1':
        warehouse_1.reception()
    elif target == '2':
        warehouse_1.transfer()
    elif target == '3':
        print(warehouse_1)
    elif target == 'Q' or target == 'q':
        break
    else:
        print('Введите корректное значение')
