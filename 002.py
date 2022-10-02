# Лекция №2
# Хранение данных. Передача данных. Хранение конфигов. Логирование действий
# Файлы.
# Как работать с файлами:
# Связать файловую переменную с файлом, определив модификатор работы
# a - открыие для добавления данных;
# r - открытие для чтения данных;
# w - открытие для записи данных
# w+ r+

# colors = ['red', 'blue', 'white', 'green']
# data = open('file.txt', 'w')
# data.writelines(colors) # запись будет без разделителей
# data.write('\nLINE 2\n')
# data.write('LINE 3\n')
# data.close()

# другой вариант записи с тем же результатом и автоматическим закрытием файла

# with open('file.txt', 'a') as data:
#     data.write('line4\n')
#     data.write('line5\n')

# чтение данных из файла

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# Функции

# import 001 as f
# print(f.f(1))

# Функция перемножает символ и число

# def new_string(symbol, count = 3):
#     return symbol * count
# print(new_string('!', 5))   # !!!!!
# print(new_string('!'))      # !!!
# print(new_string(4))        # 12

# Функция склеивает строки

# def concatenatio(*params):
#     res: str = ""                       # указание типа данных переменной (int = 0) не обязательно, также работает res = 0
#     for item in params:
#         res += item
#     return res
# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1'))           # a1
# print(concatenatio(1, 2, 3, 4))         # TypeError:...

# Рекурсия

# def fib(n):                                # функция описывает последовательность Фиббоначе
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)

# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)                                 # 1 1 2 3 5 8 13 21 34

# Кортеж - это неизменяемый  список

# a = (3, 4, 55, 6)
# print(a)
# print(a[1])
# print(a[-2])

# for item in a:
#     print(item)

# Словарь - неупорядоченные коллекции произвольных объектов с доступом по ключу

# dictionary = {}
# dictionary = \
#     {
#         'up': 'w'
#         'left': 'a'
#         'down': 's'
#         'right': 'd'
#     }
# # print(dictionary)           # { 'up': 'w', 'left': 'a', 'down': 's', 'right': 'd'}
# # print(dictionary['left'])   # a

# for k in dictionary.keys():
#     print(k)                  # up left down right

# for v in dictionary.values():
#     print(v)                   # w a s d

# Множества

# Списки