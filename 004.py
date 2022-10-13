# Лекция №4 От простого к сложному
# Написать программу сложения двух чисел

# Три самых простых варианта
# a = int(input('a = '))
# b = int(input('b = '))
# print(f'{a} + {b} = {a + b}')

# def sum(x, y):
#     return x + y
# print(f'{a} + {b} = {sum(a, b)}')

# sum = lambda a, b: a + b
# print(f'{a} + {b} = {sum(a, b)}')

# первый файл model.py
x = 0
y = 0
def  init(a, b):
    global x
    global y
    x = a
    y = b
init (10, 20)
def sum():
    return x + y
# второй файл view.py
def view(data):
    print(data)
# третий файл controller.py
import model
import view
# все файлы собраны в папке calc

# Задача №2 Сбор информации с датчиков
# Модуль 1 - сбор информации с датчиков dataProvider
# Модуль 2 - логирование logger
# Модуль 3 - UI userInterface
# Модуль 4 - HTML генератор htmlCreater
# Модуль 5 - главный модуль main
