# Лекция №3

# Анонимные методы, lambda функции

# def f(x):
#     return x ** 2

# g = f

# print(f(4))
# print(g(4))

# def calc(x):
#     return x + 10
# print(calc(10))
# def calc1(x):
#     return x * 10

# def math(op, x):
#     print(op(x))
# math(calc1, 20)

# Пример функции с двумя аргументами

# def sum(x, y):
#     return x + y
# s = sum
# sum = lambda x, y: x + y

# def mult(x, y):
#     return x * y
# def calc(op, a, b):
#     # return op(a, b)
#     print(op(a, b))

# calc(lambda x, y: x + y, 10, 20)

# List Comprehension

# list = []
# for i in range (1, 101):
#     # if(i % 2 == 0):
#         list.append(i)

# def f(x):
#     return x ** 3
# list = [(i, f(i)) for i in range(1, 101) if(i % 2 == 0)]
# тоже самое для кортежей
# list = [(i, i) for i in range(1, 101) if(i % 2 == 0)]
# print(list)

# Выбрать из файла четные числа и составить кортежи с квадратами этих чисел

# path = 'file.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# f.close()
# list = []
# while data != '':
#     space_pos = data.index(' ')
#     list.append(int(data[:space_pos]))
#     data = data[space_pos + 1:]
# out = []
# for e in list:
#     if not e % 2:
#         out.append((e, e ** 2))
# print(out)

# Решение той жезадачи другим способом

# def select(f, col):
#     return [f(x) for x in col]
# def where(f, col):
#     return [x for x in col if f(x)]
# data = '4 3 9 6 10'.split()
# res = select(int, data)
# print(res)
# res = where(lambda x: not x % 2, res)
# print(res)
# res = select(lambda x: (x, x ** 2), res)
# print(res)

# Функция map

# li = [x for x in range(1, 31)]
# print(li)
# li = list(map(lambda x: x + 10, li))
# print(li)

# data = list(map(int,input().split()))
# print(data)

# data = map(int,'3 4 55'.split())
# for e in data:
#     print(e)
# print('--')
# for e in data:
#     print(e)

#

# def where(f, col):
#     return [x for x in col if f(x)]
# data = '4 3 9 6 10'.split()
# res = map(int, data)
# print(res)
# res = where(lambda x: not x % 2, res)
# print(res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)

# Функция filter
# Применяет указанную функцию к каждому элементу итерируемого объекта и возвращает итератор с теми
# объектами, для которых функция вернула True

# data = [x for x in range(10)]
# res = list(filter(lambda x: not x % 2, data))
# print(res)

# Упрощаем код с помощью встроенных функций map и filter

# data = '4 3 9 6 10'.split()
# res = map(int, data)
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)

# Функция zip
# Применяется к набору итерируемых объектов и возвращает итератор с кортежами из элементов входных
# данных

# users = ['us1', 'us2', 'us3', 'us4', 'us5']
# ides = [11, 22, 33, 44, 55]
# salary = [111, 222, 333]
# data = list(zip(users, ides, salary))
# print(data)

# Функция enumerate
# Применяется к итерируемому объекту и возвращает новый итератор с кортежами из индекса и элементов
# входных данных

cites = ['Kazan', 'Moskow', 'Saratov']
data = list(enumerate(cites))
print(data)