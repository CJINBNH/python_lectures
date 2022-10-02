# Лекция №1

# Переменные
# Типы данных: int float boolean str list
# Python - язык с динамической типизацией

# a = 123
# b = 1.23
# s = 'hello world'
# value = None
# value = 'string'
# print(type(a))
# print(type(b))
# print(type(value))
# f = True
# print(f)
# print(type(f))

# интеполяция

# print(a, '-', b, '-', s)
# print('{2} - {1} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# Спики

# list = [1, 2, 3, 1.23, 2.23, 'a', 'b', 'c', True]
# print(list)
# print(type(list))

# Ввод и вывод данных
# print() - отвечает за вывод данных
# input() - отвечает за ввод данных

# print('Введите число a: ')
# a = int(input())                    # float(input()) - если вещественные числа
# print('Введите число b: ')
# b = int(input())                    # float(input()) - если вещественные числа
# print(a, '-', b)
# print('{0} - {1}'.format(a, b))
# print(f'{a} - {b}')
# print(a, '+', b, '=', a + b)

# Арифметические операции
# + , -, *, /, % - остаток от деления, // - деление в целых числах, ** - возведение в степень

# a = 1.3
# b = 3
# c = round(a * b, 4)
# print(c)
# a += 1.7
# print (a)

# Логические выражения
# >, >=, <, <=, ==, !=
# not, and, or - не путать &, |, ^
# is, is not, in, not in

# a = 1 < 2 and 3 < 4
# a = 3 < 5 < 7
# a = 1 != 2
# a = 'asd'
# b = 'asd'
# print(a)

# f = 1 < 2 or 4 > 5
# f = [1, 2, 3, 4]
# print(f)
# print(not 5 in f)
# is_odd = f[1] % 2 == 0
# print(is_odd)

# Управляющие конструкции: if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# name = input('Введите имя: ')
# if name == 'Маша':
#     print('Ура! Маша приехала')
# elif name == 'Марина':
#     print('Добро пожаловать, Марина')
# else:
#     print('Привет, ', name)

# Цикл. Конструкция while

# num = 93
# invert = 0
# while num != 0:
#     invert = invert * 10 + (num % 10)
#     num //= 10
#     print(num)
# print(invert)

# Конструкция while-else

# num = 93
# invert = 0
# while num != 0:
#     invert = invert * 10 + (num % 10)
#     num //= 10
# else:
#     print('Пожалуй \nхватит')
# print(invert)

# Конструкция for

# for i in 1, 2, 3, 4, 5:
# list = [1, 2, 3, 4, 5]
# for i in list:
#     print(i**2)

# r = range(6)
# for i in range(5, 7):
# for i in range(5, 10, 2):
#     print(i ** 2)

# for i in 'hello world':
#     print(i)

# Строки

# text = 'Hello world'
# print(len(text))                        # количество символов в строке
# print('world' in text)                  # проверка наличия подстроки в строке
# print(text.isdigit())                   # являются ли все символы строки числами
# print(text.islower())                   # написаны ли все символы в нижнем регистре
# print(text.replace('Hello', 'HELLO'))   # замена построки в строке

# text = 'Hello world'
# print(text[0])                              # H
# print(text[1])                              # e
# print(text[len(text)])                      # Index error
# print(text[len(text) - 1])                  # d
# print(text[-5])                             # w
# print(text[:])                              # print text
# print(text[len(text) - 2:])                 # ld
# print(text[2:5])                            # llo
# print(text[0:len(text):2])                  # Hlowrd
# print(text[::2])                            # Hlowrd

# Функции

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 'Вещественное'
    else:
        return
arg = 2.3
print(f(arg))