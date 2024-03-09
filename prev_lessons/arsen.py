# txt = "Today was a good day in a hospital"
# txt_f = list(filter(lambda elem: elem in "oauie", txt))
# print(txt_f)

# def func(elem):
#     return elem.lower()
#
# print(func("TODAY IS FRIDAY"))


# txt_low = lambda txt, txt1: txt.lower()
#
# print(txt_low("TODAY IS Sunday"))


# print(254 % 2 == 0)

# txt = "otorhinolaryngologist"
# fun = list(filter(lambda elem: elem in "aueioy", txt))
# fun.sort()
# print(fun)
# for z in fun:
#     print(z, fun.count(z))

# розказати про сети, про сорт і сортед і вивести скільки яких букв в рядку

# plus = lambda x, y: x + y
# minus = lambda x, y: x - y
# print(plus(2, 4))
# print(minus(2, 4))

# c = lambda txt: txt.center(30)
# print(c("Hello i am bot"))
# print(c("Hello i am bot"))
# print(c("Hello i am bot"))
# print(c("Hello i am bot"))
#
# print("Hello i am bot".center(30))

# lst = ["north", "east", "south", "west"]

# # змінює початковий список
# lst = [11, 33, 1666, 45, 62, -44, -933, 200]
# lst.sort()
# print(lst)
#
# # робить ще один відсортований список
# lst_1 = [11, 33, 1666, 45, 62, -44, -933, 200]
# lst_2 = sorted(lst_1)


# lst = [11, 33, 1666, 45, 62, -44, -933, 200]
# print(sorted(lst, key=lambda elem: len(str(elem))))


# # відсортувати список за сумою цифр кожного числа (11 = 1 + 1 == 2, 1666 = 1 + 6 + 6 + 6 = 19)
# lst = [11, 33, 1666, 45, 62, 44, 933, 200]


# sorted_lst = sorted(lst, key=lambda num: sum([int(elem) for elem in str(num)]))
# print(sorted_lst)

# # len
# lst = [11, 33, 1666, 45, 62, 44, 933, 200]
# lst = ["", ]
#
# # sum(elem)
#
# # спадання
#
# # зростання

# get_cube = lambda x: x ** 3
#
# get_cube(4)
#
#
# welcome = lambda user: print('Welcome, ' + user + '!')
# welcome('Anon')

# numbers = [1, 2, 4, 5, 7, 8, 10, 11]
#
# # функция, которая проверяет числа
# def filter_odd_num(in_num):
#     if(in_num % 2) == 0:
#         return True
#     else:
#         return False

# Применение filter() для удаления нечетных чисел
# out_filter = filter(filter_odd_num, numbers)
#
# print("Тип объекта out_filter: ", type(out_filter))
# print("Отфильтрованный список: ", list(out_filter))

# out_filter = list(filter(lambda elem: elem % 2 == 0, numbers))
# print(out_filter)

# numbers1 = [1, 2, 4, 2, 7, 6, 10, 15]
# numbers2 = [1, 5, 4, 5, 7, 8, 1, 11]
# same_num = []
# # if numbers1 in numbers2:
# #     print(True)
# # else:
# #     print(False)
# for i in numbers1:
#     if i in numbers2:
#         same_num.append(i)
# print(same_num)
# out = list(filter(lambda it: it in numbers1, numbers2))
# bools = ['bool', 0, None, True, False, 1, 1-1, 2%2]
# print(list(filter(None, bools)))

# # lambda:
# + # add
# - # sub - subtract
# * # mult - multiply
# / # div - divide             #
# ** # 2 in the power of 4     # pow(2, 4)
# factorial() # factorial
# % # mod  # остача
# // # div # ціла частинка

# [] # list()    # список          # все в одному
# {} # set()     # сет             # немає дублікатів
# () # tuple()   # кортеж          # незмінний
# {} # frozenset # заморожений сет # сет, але незмінний
# {} # dict      # словник         # має і ключі і значення

# string = lambda txt: txt + ', please'
# print(string("give me chocolate"))

# print(help(divmod))

# tupl = divmod(16, 5)
# print("16 div 5 is", tupl[0])

# print(help(pow))
# print(pow(2, 4, 5))


# from math import factorial as f
# print(f(5))

# elem_summ = lambda *args: sum(args)
# print(elem_summ(1,2,3,4,5,6,7))

# x = 4.2
# print(isinstance(x, list))
#
# if isinstance(x, list):
#     pass
# lst = [1,2,3,3.4,5.2]
# lst_1 = list(filter(lambda elem: isinstance(elem, float), lst))
# print(lst_1)

# from turtle import *
# from math import sqrt
# a = int(input("Введи сторону катета\n"))
# rt(90)
# forward(a)
# left(90)
# fd(a)
# lt(135)
# fd(sqrt(a**2+a**2))
# ht()
# exitonclick()

# def func(question, answer):
#     global score
#     if input(question) == answer:
#         score += 1
#     else:
#         score -= 1
#
# score = 0
# func("yes or no?", "yes")
# func("1 or 2?", "1")
# func("apple or pineapple", "apple")
# print(f"your score is {score}")
#
# def func(question, *answers):
#     print(question)
#     print(f"the right answer was: {answers[0]}")
#     print("all possible chooses were:")
#     for z in answers:
#         print("-", z)
#
# func("which fruit can be orange, green, red or yellow?",
#      "apple", "orange", "grapes", "pear")
# for i in range(len(answer)):
#     answer[i]

# age = 11
# print(f"Hello my name is {name}. I am {age}")

# def people(*child):
#     for z in range(len(child)):
#         print(f"{z+1}) {child[z]}")
#
# people('Ron', 'Jany', 'Ostin', 'Bill')

# for user in range(len(users)):
#     print(f"{user+1}) {users[user]}")


# num = 1
# for z in child:
#     print(f"{num}) {z}")
#     num += 1
# name = "Bill"


# def lang_sort(*args):
#     for i in args:
#         if i[0] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
#             eng_words.append(i)
#         elif i[0] in '1234567890':
#             numbers.append(i)
#         else:
#             ukr_words.append(i)
#     eng_words.sort()
#     ukr_words.sort()
#     print(f"eng list:{eng_words}\nukr list:{ukr_words}\nnum list:{numbers}")
#
#
# numbers = []
# eng_words = []
# ukr_words = []
# lang_sort('apple', 'паляниця', 'understandable', 'Apple', "123", "asd123")

# import random
#
#
# def people(*child):
#     print("Who is ur child?")
#     child = list(child)
#     random.shuffle(child)
#     for z in child:
#         print(z)
#     if input() == child[0]:
#         print(True)
#     else:
#         print(False)
#
#
# people('Ron', 'Jany', 'Ostin', 'Bill')

# import random
#
# for u in (10, 100, 1000, 10000, 100000, 1000000, 10000000):
#     a = 0
#     b = 0
#     print("Було спроб: ", u)
#     for z in range(u):
#         if random.randint(0, 1) == 0:
#             a += 1
#         else:
#             b += 1
#     print(a, b)
#     print(f'0: {a / u * 100} %')
#     print(f'1: {b / u * 100} %')


# # ПЛАН ПРОГРАМИ:
# # 1. Підключаємо потрібні модулі.
# from random import randint
# import turtle
#
# turtle.ht()
# # 2. Заводимо змінні для розміру ігрового поля
# def winner(t):
#     t.goto(-50, 80)
#     t.write("    I'M THE WINNER!!!", font=("Arial", 12, "bold"))
#     t.pendown()
#     t.left(90)
#     t.forward(20)
#     t.right(90)
#     t.forward(180)
#     t.right(90)
#     t.forward(30)
#     t.right(90)
#     t.forward(180)
#     t.right(9 * 95)
#
#
# finish = 200
#
# # 3. Створюємо об'єкти типу "Черепашка" і запам'ятовуємо їх в змінних
# x, y = turtle.Turtle(), turtle.Turtle()
#
# scr = turtle.getscreen()
# scr.bgcolor("grey")
#
# # 4. Тепер на старт виходять черепашки.
# # Які установки їм запам'ятати?
# x.pu()
# y.pu()
# x.goto(-200, 100)
# y.goto(-200, 0)
# x.color("red")
# y.color('brown')
# x.shape('turtle')
# y.shape('turtle')
# # 5. А ось і гонка!
# while x.xcor() < finish or y.xcor() < finish:
#     x.fd(randint(3, 6))
#     y.fd(randint(3, 6))
#
# # #простіший варіант - до 2-3 черепашок
# # max_x = max(x.xcor(), y.xcor())
# # if x.xcor() == max_x:
# #     winner(x)
# # elif y.xcor() == max_x:
# #     winner(y)
#
# # складніший варіант - для любої к-сті черепашок
# d_cors = {}
# d_cors[x] = x.xcor()
# d_cors[y] = y.xcor()
# max_x = max(d_cors.values())
# for k, v in d_cors.items():
#     if v == max_x:
#         winner(k)






# d = {
#     "Kiev": 330,
#     "Uman": 450
# }
#
# for k in d.items():
#     print(k)

# d["Chercassy"] = 654
#
# print(d)

# import turtle, random
# x = turtle.Turtle()
# y = turtle.Turtle()
# x.turtlesize(10)
# x.goto(-400, -300)
# y.goto(-400, -300)
#
# turtle.done()

# def func(**kwargs):  # args - arguments, kwargs - key word arguments
#     # keys
#     # values
#     # items
#     pass
#
# func(num=1, num2=2)


# from Human import *
# Director = Human("Oleg", 21, "Male", "director", 13100)
# Director.getValues()
#
# class Worker(Human):
#     def workerGetValues(self):
#         print("\nWorker")
#         self.getValues()
#
#
# Misha = Worker("Misha", 22, "Male", "Engineer", 9600)
# Misha.workerGetValues()
#
# Misha.getSalary()
#
# Misha.setJob("Miner")
# Misha.getValues()
#
# def salary_change(target, amount):
#     print(f"\n{target.name} had salary of: {target.salary}")
#     print(f"after the conversation his salary was changed by {amount}")
#     target.salary += amount
#     print(f"now he is getting salary of: {target.salary}")
#
# while Misha.salary > 0:
#     salary_change(Misha, -300)
#     print(Misha.salary)
# print(f"the last value: {Misha.salary}")



# class Cat:
#     def __init__(self, name, age, isSleep, isAlive = True):
#         self.name = name
#         self.age = age
#         self.isSleep = isSleep
#         self.isAlive = isAlive
#
#     def getValue(self):
#         print("\nName:", self.name)
#         print("age:", self.age)
#
#     def setAge(self, age):
#         self.age = age
#
#     def setSleep(self, isSleep):
#         self.isSleep = isSleep
#
#     def getParams(self):
#         print("\nAge:", self.name)
#         print(f"{self.name} sleeps now" if self.isSleep else f"{self.name} is awake")
#
#     @staticmethod
#     def able(year_of_birth):
#         if 2022 - year_of_birth >= 18:
#             print("\nable to do")
#         else:
#             print("\nnot able to do")
#
#
# Barsik = Cat("Barsik", 4, False)
# Barsik.getValue()
# Barsik.setAge(5)
# Barsik.getParams()
# Barsik.setSleep(True)
# Barsik.getParams()

# Barsik.able(Barsik.age)

# from random import randint
# def heal(deff):
#     fruits = {"apple": 2, "banana": 5}
#     lst = list(fruits.keys())
#     fruit = lst[randint(0, len(lst)-1)]
#     deff.hp += fruits[fruit]

# class Car:
#     def __init__(self, wheels, engine, windows, seats):
#         self.wheels = wheels
#         self.engine = engine
#         self.windows = windows
#         self.seats = seats
#
#
#     def getValue(self):
#         print(f"wheels: {self.wheels}")
#         print(f"engine: {self.engine}")
#         print(f"windows: {self.windows}")
#         print(f"seats: {self.seats}")
#
# class Limuzin(Car):
#     print("Limuzin is created")
#
#
# class Truck(Car):
#     print("Truck is created")
#
#
# Limz = Limuzin(4, True, 6, 8)
#
# Tr = Truck(4, True, 6, 6)
#
# Limz.seats = 6

# books = {
#     "It falls you miss it":     350,
#     "It":                       1040,
#     "The Tower":                1300
# }
#
# for key, value in books.items():
#     print(key, value)

# while True:
#     book = input("Book?\n")
#     if book in books.keys():
#         print(f"\nBook: {book}. Page amount is {books[book]} pages")
#         books[book] += 10
#         print('+10')
#         print(f"Book: {book}. Page amount is {books[book]} pages\n")


# print([oct(int(elem)) for elem in list(input("pass?"))])

# import random
# l = list(input("pass?"))
# for elem in range(len(l)):
#     l[elem] = random.randint(1, 1000)
# print(l)

# file = open("C:/Users/vladb/PycharmProjects\\abc.txt")
#1
# file = open("abc.txt", "r")
#
# print(file.read())
# file.seek(0)
# print(file.read())
#
# обов'язково закривати файл
# file.close()

# #2
# with open("abc.txt", "r") as file:
#     print(file.read())
#     file.seek(0)
#     print(file.read())
# # тут файл вже закрився автоматично


# check time of program
# from horology import Timing
# with Timing(name="time: "):
#     for elem in range(10000, 1000000):
#         elem if len(str(elem)) % 2 == 0 else ""

# file = open("abc.txt", "r+")
# for line in file.readlines():
#     print(len(line))
#     print(len(line.strip()))
# print(file.readlines())

# file = open("abc.txt", "r")
# file = [line.strip() for line in file.readlines()]
# # print(file)
# # line_1 = file[0]
# # print(line_1.replace("e", "@"))
# file[0] = file[0].replace("e", "@")
# print(file)


# file = open("abc.txt", "r")

# for line in file.readlines():
#     for elem in line.strip():
#         print(f"{elem} is upper" if elem.isupper() else f"{elem} is lower")


# lst = [elem for line in file.readlines() for elem in line.strip()]
# lst_1 = [elem for elem in lst if elem.isupper()]
# print(round(len(lst_1) * 100 / len(lst), 2), "%")


# file = open("abc.txt", "w+")
# for elem in range(20):
#     file.write(f"{elem} {elem+1}")
#     # print(elem, elem+2, file=file, end="")
#
# file.close()
# file.write()

# from turtle import *
# import pandas
# def start():
#     file.write(f'{xcor()} {ycor()} ')
# def end():
#     file.write(f'{xcor()} {ycor()}\n')
#
#
# file = open("abc.txt", "w+")
# for y in range(-50, -300, -50):
#
#     start()
#     fd(100)
#     end()
#
#     pu()
#
#     start()
#     goto(0, y)
#     end()
#
#     pd()
#
# file.close()
# reset()
#
# #2
# file = open("abc.txt", "w+")
# for y in range(-50, -350, -50):
#
#     start()
#     fd(100)
#     end()
#
#     pu()
#
#     start()
#     goto(0, y)
#     end()
#
#     pd()
#
# exitonclick()
