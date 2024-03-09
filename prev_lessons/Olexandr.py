import tkinter

## int
# num = "5"
# num = int(num)
# print(type(num))

## float
# print(5.5)

# txt = "some text"
# print(type(txt))

# +                         # add
# print("5 + 5 =", 5 + 5)
# print(f"5 + 5 = {5+5}")

# -                         # sub - subtraction
# print(5 - 2)

# *                         # mult - multiply
# print(5 * 2)
# print("a" * 20)

# /                         # division
# print(10 / 2)


# //                        # div
# print(10 // 3)
# print(10 // 4)
# print(10 // 6)
# print(100 // 13)

# %                         # mod
# print(10 % 3)
# print(10 % 4)
# print(100 % 13)

# var - variable
# num = 5
# txt = "some text"
# bill_for_electricity = 13.2
# billForElectricity = 13.2

# NameError
# 2var = 1

# =
# var = 1
# # var = var + 5
# var += 1    # 2
# var -= 1    # 1
# var *= 2    # 2
# var /= 2    # 1

# boolean - bool  (True/False)
# > < == >= <= !=
# op = input()
# if op == "+":
#     print("sum")
# elif op == "-":
#     print("sub")
# elif op == "*":
#     print("mult")
# else:
#     print("I don't know this command")

# embedded if
# num1 = int(input())
# num2 = int(input())
# op = input()
# if op == "+":
#     print("sum")
# elif op == "-":
#     print("sub")
# elif op == "*":
#     print("mult")
# elif op == '/':
#     if num2 == 0:
#         print("Cannot div by zero")
#     else:
#         print("div")
# else:
#     print("I don't know this command")

# hello

# rules

# if
# x = 3
# if 2 <= x <= 4:
#     print()

# while             # iterator
# x = 0
# while x < 10:       # iterations
#     print(x)
#     x += 1

# ques = input("Zimoy i letom odnim zhvetom\n")
# while ques != "doter":
#     print("Wrong! Try again")
#     ques = input("Zimoy i letom odnim zhvetom\n")
# print("Correct")

# q = input('yes or no?')
# while q.lower() != "yes":
#     print("again. Yes or no?")
#     q = input()

# q = "YES".lower()
# print(q)

# print("hello")

# break
# x = 0
# while x < 10:
#     if x == 5:
#         break
#     print(x)
#     x += 1

# continue
# x = 0
# while x < 10:
#     x += 1
#     if x == 5:
#         continue
#     print(x)
# print(1)

# x = 0
# if x == 0:
#     print('0')
# elif x % 2 == 0:
#     print("parne")
# else:
#     print("neparne")

# from random import randint, shuffle   # коли треба 1-3 функцій
# print(randint(1, 10))

# import random           # коли багато функцій треба
# print(random.randint(1, 999))
# print(random.randint(1, 999))

from random import *  # імпортує все з модуля (коли треба дуже багато функцій)

# from random import randint
# lst = []
# for z in range(10):
#     lst.append(randint(0, 1))
#
# print(f"1: {lst.count(1)}\n0: {lst.count(0)}")


# while True:
#     num = input("Input the num. 0..5\n")
#     try:
#         num = int(num)
#         if num < 0 or num > 5:
#             print("Error. Not in 0..5")
#         break
#     except (ValueError, TypeError):
#         print("This is not a num. Try again")
#
# my_num = randint(0, 6)
# if num == my_num:
#     print("Mice")
# else:
#     print("No")

# txt = 'Hello I am Brian'
# print(txt[4])       # indexing
# print(txt[-1])      # negative indexing
# print(txt[4:10])    # slice
# print(txt[:10])
# print(txt[4:])
# print(txt[2:16:2])
# print(txt[16:2:-1])
# print(txt[::-1])
# print(len(txt))
# print(txt.count("o"))


# txt = "There was a Hole with Hobbits in there. They lived in there"
# print(txt[-2::-2])
# print(txt.count(' '))

# from - з
# import - додати


# 1 # коли використ 1-3 функції з модуля
# from random import randint, shuffle
# print(randint(1, 100))

# 2 # коли багато функцій
# import random
# print(random.randint(1, 100))
# import math
# print(math.factorial(6))

# 3 # не використовувати
# from random import *
# randint()

# 4 # можна але не треба
# from random import randint as rdi, shuffle as shf
# print(rdi(1, 100))
# import random
# r_num = random.randint(1, 100)
# while True:
#     while True:
#         try:
#             u_num = int(input("?\n"))
#             if u_num not in range(5):
#                 print("1-5")
#                 continue
#             break
#         except ValueError:
#             print("Ти ввів щось не те")
#
#
#     if r_num == u_num:
#         print(True)
#         break
#     elif u_num > r_num:
#         print("Спробуй менше")
#
# print("U passed")

# random import packages, different imports, try except, guess the num task
# txt = "Hello"
# for z in range(10):
#     print(z)
#
# c = 0
# for elem in txt:
#     if elem == "l":
#         c += 1
#         continue
#     print(elem)
# print(c)

# ans = input("?\n")
# while ans != "1":
#     ans = input("?\n")
# while True:
#     ans = input("?\n")

# for z in range(9999):
#     print(z)

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for z in lst:
#     if z % 2 == 0:
#         print(z)

# num = int(input("vid?"))
# num1 = int(input("do"))
# for z in range(num, num1):
#     if z % 5 == 0:
#         print(z)

# for z in range(2, 10):
#     if z == 4:
#         continue
#     print(z)

# for, for _ in string:, for num in range(i,j,k), for and while compare, output odd nums, nums of i to j, %3, 2..3 5..10, табл множ
# even, %5, 10..20 22..40, j to i, squares 1...20
# for z in range(1, 11):
#     for x in range(10):
#         print(f"{z} * {x} = {z*x}")
# for z in range(10):
#     print(z, end='')
# print("hello", end="")
# print(". I am")
# list


# txt = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
#
# print(txt[4])       # indexing
# print(txt[-1])      # negative indexing
# print(txt[4:10])    # slice
# print(txt[:10])
# print(txt[4:])
# print(txt[2:16:2])
# print(txt[16:2:-1])
# print(txt[::-1])
# print(len(txt))
# print(txt.count(10))

# # list methods
# lst = [1000, 10, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
# print(len(lst))
# lst.append(2)
# for z in range(10):
#     lst.append(z)
# lst.insert(1, "h")
# lst.clear()
# lst2 = lst.copy()
# print(lst.count(10))
# lst.extend([1, 2, 3, 45])
# print(lst.index(10))
# print(lst.pop(3))
# lst.remove(30)
# lst.reverse()
# print(list(reversed(lst)))
# lst.sort()
# print(sorted(lst, reverse=True))
# print(lst)

# lst = [1000, 10, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
# for z in lst:
#     print(f"-{z}")
# num = int(input())
# if num not in lst:
#     lst.append(num)
# print(sorted(lst))

# from random import randint as rdi
#
# # generator
# ls = [rdi(1, 200) for z in range(10)]
# lst = [z for z in ls if z % 2 == 1]
# lst = [z ** 2 for z in ls]
# lst = [z for z in ls if len(str(z)) == 2 and str(z)[0] == '2']  # 20-29
# lst = [ls[i-1] for i in range(1, len(ls))if ls[i] % 2 == 0 and ls[i-1] % 2 == 0]
#
#
# print(f"default list   {ls}")
# print(f"modified list  {lst}")

# list methods, for, for in list, games list tasks in lst and range(len(lst)),
# if in, imb for in list(tasks in course)

# import random as rd
# lst = [rd.randint(-100, 100) for z in range(10)]
# print("default", lst)
# ls = [lst[i] for i in range(len(lst)-1) if lst[i] > lst[i+1]]
# lst[i] > lst[i+1]
# range(len(lst)-1)
# lst[i] > lst[i-1]
# range(1, len(lst))


#  задача з шансом рандому 1/0, local, статистика
# phys


# mail = ['random.user@gmail.com', 'user@ukr.net']
# for elem in mail:
#     windranger = elem.find('@')
#     print(windranger)
#     print(elem[:windranger])
# BH = mail.find('@')
# print(mail[:BH])
# print(mail[0:11])
# riki = mail.rfind('.')
# print(mail[BH:riki])
# print(mail[12:17])
# mail = 'user@ukr.net'
# BH = mail.find('@')
# print(mail[:BH])
# print(mail[0:11])

# print(mail[12:17])

# find to home

# wk = ["asdasd", "asdas", 'asdasd']
# s = []
# for elem in wk:
#     s.append(len(elem))
# print(sum(s)/len(wk))
# print(sum([len(elem) for elem in wk])/len(wk))

# 1 check = []
# check = []
# mails = ['gmail', 'gmail', 'mail', 'mail']
# print(mails[0])
# mails[1] = 5
# print(mails)
# for elem in mails:
#     if elem not in check:
#         print(elem)
#         check.append(elem)
# print(check)

# 2 set: всі елементи, треба видалити дублікати, інші
# mails = ['gmail', 'gmail', 'mail', 'mail']
# print(list(set(mails)))
# print(mail_set[0])
# mail_set[1] = 5
# mails.add(2)
# mails.add("fghfghgf")
# for elem in set(mails):
#     print(elem)
# print(mails)

# # rozrahunok
# for x in range(1, int(input())+1):
#     print(f"{x} - другий" if x % 2 == 0 else f"{x} - перший")
#
# for z in range(1, int(input("до скількох?"))+1, 2):  # 1,3,5,7,9... - непарні(перші)
#     print(f"{z} - перший\n{z+1} - другий")

# emails, find, [],
# vars for students
# students = ['wk', 'wk bez ulta', 'riki 3 invisa', 'bf na 15', 'wk bez twiksa']


# func
# a = [1, 2].count(1)
# print(a)
# a = print()
# print(a)

# # global outerscope
# x = 5
# def func():         # define
#     x = 10
#     print(x)
# print(x)
# func()

# x = 5
# def func():
#     global x
#     x = 10
# func()
# print(x)

# імпорт з іншого файлу
# import Peihel
# print(Peihel.hello())

# def bill_electricity(kw):       # kw = my_kwat
#     amount = kw * 1.8
#     return amount
#
# def bill_gas(gas):
#     amount = gas * 0.6
#     return amount
#
# def bill_water(water):
#     amount = water * 52
#     return amount

# my_kwat = 250
# kwat_Andrew = 200
# kwat_trf = 1.8
#
# my_gas = 1500
# gas_Anrew = 10
# gas_trf = 0.6
#
# my_water = 6
# water_trf = 52


# print(bill_electricity(my_kwat))
# print(bill_electricity(kwat_Andrew))
# print(bill_gas(my_gas))
# print(bill_water(my_water))

# def bill(rastoch, tariff):       # kw = my_kwat
#     amount = rastoch * tariff
#     return amount

# def calc(x,y,op):
#     a = a * 0.1


# calc()

# bill_water = bill(my_water, water_trf)
# bill_kwat = bill(my_kwat, kwat_trf)
# bill_gas = bill(my_gas, gas_trf)
# zhuttya = (bill_water + bill_kwat + bill_gas + 4000) / 100
# print(f"ти не з'їси {zhuttya} бургерів")
# print(f"ти прожив би {zhuttya / 3} днів якби жив на вулиці")

# def date(day, month, year):
#     if not isinstance(year, int):
#         return "year not valid"
#     if month not in range(1, 12):
#         return "month not valid"
#     if month in (7, 8):
#         if day not in range(1, 32):
#             return "day not valid"
#     elif month in (6, 4):
#         if day not in range(1, 31):
#             return "day not valid"
#     else:
#         return f"{day}.{month}.{year} is a valid date"
#
#
# print(date(31, 6, 2022))


# import datetime
# def date_cheat(day, month, year):
#
#     try:
#         datetime.date(year, month, day)
#         return True
#     except ValueError:
#         return False
#
#
# print(date_cheat(32, 8, 2022))
# print(datetime.date(2022, 8, 31))

# def func(start, end):


# def glimpse():
#     print("Летим на вишку")
#     print("опять вернули\n")
#     return glimpse()
#
#
# glimpse()

# def fact(num):
#     if num == 0:
#         return 1
#     elif num < 0:
#         return "Invalid"
#     elif num == 1:
#         return num
#     return num * fact(num-1)
#
#
# print(fact(5))
# #0! = 1
# #5! = 1*2*3*4*5
# #5! = 5*4*3*2*1

# * * * *
# * * *
# * *
# *
import random as rd


# stars = int(input("?\n"))
# for i in range(stars, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()


# d = "a* hj?"
# print(list(d))
# print(list(range(10)))
# a = input("Enter any String")
# # Enter any String : Practice
# print(list(a))

# a = [1, 2, 3, 4, 5]
# print(a[0])   # 1
# print(a[-1])  # 5
# print(a[2])   # 3
# print(a[-2])  # 4
# print(a[1])   # 2
#
#
# list1 = "Practice QuesTions of List in pythoN"
# list2 = list(list1)
# # P
# # Q
# # L
# # N
# # T
# print(list2[0])
# print(list2[9])
# print(list2[22])
# print(list2[-1])
# print(list2[13])

# b = ['p', 'r', 'a', 'c', 't', 'i', 'c', 'e']
# for i in b:
#     print(i, end="?")

# print([1, 2, 3, 4] == [4, 3, 2, 1])
# print([1, 2, 3, 4] > [4])
# print([1, 2, 3, 4] != [1, 2, 3, 4])
# print([1, 2, 3, 4] == [1, 2, [3, 4]])
# print([1, 2, 3] == [1.0, 2.0, 3.0])
# a = [1,2,3,4]
# b = [5,6,7,8]
# print(a+b)
# a.extend(b)
# a = "python"
#
# b = list(a)
#
# print(b * 2)
#
# print(b + b)
#
# print(a + a)


# a = [1, 2, 3, 4]
# b = a.copy()
# b = list(a)
# print(b)

# a = [1,2,3,4]
#
# a.append(7)
#
# print(a)
# a = [1, 2, 3, 4]
# del a[0:2]
# print(a)

# a.append([7, 8])
#
# print(a)

# ls = [1, 2, 2, 2, 3, 4, 5]
# ls = "aa aaa aa"
# print(ls.count(" ")+1)
# ls.find()
# for z in range(4):
#     print(ls)
#     ls.clear()
# print(ls.pop(4))
# print(ls)
# ls.remove(2)
# print(ls)
# del ls
# print(ls)

# # nested collections: list
# score = [[[73, 75], [65, 60], 85],
#          [78, 80, 75, 68, 90],
#          [78, 85, 80, 69, 99]]
# print(score[1][0])

# z = 1
# for elem in score:
#     print(f"Train_{z}: {max(elem)}")
#     z += 1

# a = [[1, 2, 3],
#      [1, 3, 3],
#      [7, 8, 9]]
# # print(a[1][1])
# # for i in a:
# #     for j in i:
# #         print(j)
# x = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# y = [[3, 3, 3],
#      [2, 4, 3],
#      [4, 5, 6]]
#
# c = [[0, 0, 0],
#      [0, 0, 0],
#      [0, 0, 0]]
#
# for i in range(len(x)):
#     for j in range(len(x[i])):
#         c[i][j] = x[i][j] + y[i][j]

# def stepin(num1, num2):
#     return num1 ** num2
#
# # def stepin2():
# #     num1, num2 =
# #     return num1 ** num2
#
# x,y=int(input()),int(input())
# print(stepin(x,y))

# print(stepin)


# def f(num):
#     return True if num == sum([z for z in range(2) if 2 == 2]) else False

# print(f(2))


# def palindrome(string):
#     string_2 = ''
#     for elem in string:
#         if elem != ' ':
#             string_2 += elem
#     return True if string_2 == string_2[::-1] else False
#
# print(palindrome("дуо а о у д "))

# def palindrome(string):
#     l = list(string)
#     while ' ' in l:
#         l.remove(' ')
#     return True if l == l[::-1] else False
#
# print(palindrome("дуо а о у д "))

## def assign in (=)
## args
## func that takes args and displays their sum, average, sort in asc/des(true/false)

# print(1, 2, 3, sep = ', ', end ="*")


# def print1(args, sep1=' ', end1='\n'):
#     print(args, sep=sep1, end=end1)
#
#
# print1(1, end1='*')
# sorted([1, 2, 3])

# def f(*l, s=False):
#
#     return sorted(l, reverse=s)
#
#
# print(f(1, 2, 3, 4, 5, 5, 6, 7, 8, 98))

# def f(num):
#     return num + 1
# print(f(13))
#
# # lambda
# a = lambda num: num + 1
# print(a(13))
#
# def len_sort(elem):
#     return len(elem)
#
#
# lst = ['journo', "dio", "polnareff", "iggy"]
# print(sorted(lst, key=len_sort))
#
# print(sorted(lst, key=lambda elem: len(elem)))


# a = lambda num1, num2, op: num1 + num2
# print(a(2, 3))


# Cezar to def
# questions

# math funcs:
# https://www.w3schools.com/PYTHON/module_math.asp
# https://pythonist.ru/test-math-v-python/


# import math
# print(math.ceil(2.1))
# print(math.floor(2.9))
# print(int(2.1)+1)
# step = 0.1
# num = 2
# while num < 3:
#     print(round(num))
#     print(num)
#     num += 0.1
# print(math.copysign(2, -4))
# a, b = -2, 4
# if b < 0:
#     if a > 0:
#         a *= -1
# elif b > 0:
#     if a < 0:
#         a *= -1
# print(a, b)
# print(math.fabs(-20))
# print(math.fabs(20))        # |-x+y|  -x+y >= 0
# print(math.fmod(20, 3))
# print(20 // 3)
# print(20 % 3)
#
# print(divmod(20, 3))
# a, b = 3, 6
# for z in range(1, a*b+1):
#     if z % a == 0 and z % b == 0:
#         print(z)
#         break
# for z in range(1, b+1):
#     if a % z == 0 and b % z == 0:
#         print(z)
#         break
# print(math.gcd(a, b))

# print(math.pow(2, 6)) # 2 in the power of 6
# print(2**6)
# print(math.sqrt(25))  # square root
# print(25**(1/2))
# print(2.5**(3/7))
# def f():
#     x = 2
#     return
# print(f())
# print([1,2,3].remove(2))

# # MAP
# lt = [z for z in range(10)]
# print(list(map(int, lt)))
# def for_map(elem):
#     return elem**2
# print(list(map(for_map, lt)))
# print(list(map(lambda e: e ** 2, lt)))

# map
# https://www.w3resource.com/python-exercises/map/index.php

# nums = [z for z in range(-10, 10)]
# print(nums)
# print(list(filter(lambda e: e % 2 == 1, nums)))
# def filt_nums(elem):
#     if elem % 2 == 1:
#         return True
# print(list(filter(filt_nums, nums)))
# l = []
# for z in nums:
#     if z % 2 == 1:
#         l.append(z)
# print(l)

# txt = "Сонце освітлює твій башер. Добре башиш".split()
# print(list(filter(lambda elem: elem[0].lower() == "б" and len(elem) == 5, txt)))
# a = []
# for elem in txt:
#     if elem[0].lower() == "б" and len(elem) == 5:
#         a.append(elem)
# print(a)

# filter
# https://pavel-karateev.gitbook.io/intermediate-python/funkcionalnoe-programmirovanie/map_filter
# https://pythonru.com/uroki/funkcija-filter-dlja-nachinajushhih
# Напишите функцию, которая принимает на вход список с именами людей и возвращает новый список с именами, которые начинаются на гласную букву. В новом списке имя должно начинаться с прописной буквы, даже если изначально было написано со строчной.

# s = "olga"
# print(s)
# s = s.replace(s[0], s[0].upper())
# print(s)

# a = ['абаш', 'башер', 'мортра', 'ушш']
# b = list(filter(lambda x: x[0] in 'аоуіиеАОУІИЕ', a))
# for e in range(len(b)):
#     if b[e][0].islower():
#         b[e] = b[e].replace(b[e][0], b[e][0].upper(), 1)
# print(b)


# list1 = ["Python", "CSharp", "Java", "Go"]
# list2 = ["Python", "Scala", "JavaScript", "Go", "PHP", "CSharp"]
#
# list3 = list(filter(lambda e: e not in list2, list1))


# Отфильтрованный список: [‘Java’, ‘Scala’, ‘JavaScript’, ‘PHP’]

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# print(set(filter(lambda e: e in b, a)))
# print(set([e for e in a if e in b]))
# print(list(set(a) & set(b)))


## dicts
## {keys:values}
# d = {
#     1914: "WWI",
#     1939: "WWII",
#     1999: "Smash mouth: All stars"
# }
# print(d[1914])
# d = {"WWI": 1914, "WWII": 1939}
# print(d["WWI"])
# d = dict(WWI=1914, WWII=1939)
# def func(a, b, c=3, d=5):
#     return True
# func(4, 5, c=6, d=True)
# print(d["WWI"])
# l = [["WWI", 1914], ["WWII", 1939]]
# print(l[0][1])
# d = dict(l)
# print(d)

# d = dict.fromkeys(['a', 'b', 'c'], 100)
# print(d)

# d = {
#     "mom": 1750,
#     "smoke of deceit": 80,
#     "force staff": 2200,
#     "glimmer cape": 1900
# }

# # creation/change
# d["smoke of deceit"] = 90
# print(d["smoke of deceit"])
# d['crystalysx2'] = 1900
# d['a'] = 2
# print(d)

# hp, armor, dmg, crt = 100, 50, 6, 15
# # hp += 5
# # armor += 2
# chars = {
#     "hp": 5,
#     "dmg": 2,
#     "armor": 3
# }
# hp += chars["hp"]
# dmg += chars["dmg"]

# hp, armor, dmg, crt = 100, 50, 6, 15
# hp_, armor_, dmg_, crt_ = 100, 50, 6, 15
# chars = {
#     "hp": (5, 4),
#     "dmg": (2, 1),
#     "armor": (3, 2)
# }
# hp_ += chars['hp'][1]
# hp += chars['hp'][0]
# chars = {
#     "hp": {"player": 5, "mob": 4},
#     "dmg": {"player": 2, "mob": 1},
#     "armor": {"player": 3, "mob": 2}
# }
# armor += chars["armor"]["player"]
# dmg_ += chars["dmg"]["mob"]
# print(armor)
# print(dmg_)

## count number of each letter in string and print out
# s = "ununderstandable"
# d = {}
# for elem in s:
#     if elem in d:
#         d[elem] += 1
#     else:
#         d[elem] = 1
#
# print(d)

# https://pythonist.ru/test-na-znanie-spiskov-i-kortezhej/

# ls = [[1, 2], 3, 5]
# ls[-1:] = [1,2]
# print(ls)

# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964,
#     1234: 12
# }
## .keys()
# print(list(car.keys())[0])
# print([elem for elem in car.keys() if isinstance(elem, str)])
# for key in car.keys():
#     print(key)

## .values()
# print(set(car.values()))

## .items()
# print(list(car.items()))
# for item in car.items():
#     print(f"key: {item[0]}\t value: {item[1]}")
# for x, c in [[1, 2], [3, 4], [5, 6]]:
#     print(f"{x}\t{c}")
# for key, value in car.items():
#     print(f'\na in {key}' if 'a' in str(key) else "", end='')
#     print(f"\n1 in {value}" if '1' in str(value) else "", end='')
#     print(f"\nkey: {key}\t value: {value}")
#

# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964,
#     1234: 12
# }

## copy         # копія
# print(car.copy())
# car_ = car
# print(car_)
# print(car.copy() is car_)

## get      - виводить по ключу може вивести дефолт
# print(car.get(1234))
# print(car[1234])
# print(car.get(12345, "Doesn't exist"))
# try:
#     print(car[12345])
# except:
#     print("Doesn't exist")

## https://www.w3schools.com/python/python_dictionaries_methods.asp

# mails with dict


# import turtle
# turtle.fd(10)
# # kwargs

# from turtle import*
# from random import choice, randint
# colors_window = ["plum", "palegreen", "khaki", "skyblue"]
# bgcolor("indigo")
# penup()
# pendown()
# speed(0)
# def kvadrat(side, rostoanie, kilkisty, etag, koordinaty = (0, 0)):
#     penup()
#     goto(koordinaty[0], koordinaty[1])
#     pendown()
#     color_dom = randint(22, 25)
#     color(f"gray{color_dom}")
#     for f in range(2):          #Osnovadoma
#         begin_fill()
#         fd(((rostoanie + side) * kilkisty))
#         lt(90)
#         fd((rostoanie + side) * etag)
#         lt(90)
#         fd(rostoanie)
#         end_fill()
#
#     a = choice(colors_window)
#     color(a)
#     for f in range(etag): #kilkist_etagiv
#         for a in range(kilkisty):
#             begin_fill()
#             for i in range(4):  #vikno
#                 fd(side)
#                 lt(90)
#             end_fill()
#             penup()
#             forward(rostoanie + side)
#             pendown()
#         penup()
#         backward((rostoanie + side) * kilkisty)
#         lt(90)
#         fd(side + rostoanie)
#         rt(90)
#         pendown()
#     backward(rostoanie)
#
# window = Screen()
# window.setup(1500, 700)
#
# kvadrat(9, 7, 5, 10, (-720, -390)) #1
# kvadrat(10, 6, 6, 12, (-500, -390)) #2
# kvadrat(9, 8, 9, 30, (-310, - 390))#3
# kvadrat(10, 6, 10, 25, (-130, -390))#4
# kvadrat(9, 7, 10, 35, (70, -390))#5
# kvadrat(9, 8, 9, 20, (250, -390))#6
# kvadrat(10, 6, 8, 26, (450, -390))#7
# kvadrat(9, 7, 10, 37, (620, -390))#8
#
# done()


# def twoSum(nums, target):
#     for i in nums:
#         nums1 = nums.copy()
#         nums.remove(i)
#         for j in nums:
#             if i + j == target:
#                 print(nums1)
#                 l = [nums1.index(i)]
#                 nums1.remove(i)
#                 print(nums1)
#                 l.append(nums1.index(j)+1)
#                 return l
#
#
# print(twoSum([3, 1, 3], 6))

# def f(file="",b=3,c=2):
#     pass
# f("asd")

# # file = open("C:/Users/vladb/PycharmProjects\\Maboi.txt", "r")
# file = open("Maboi.txt", "r")
# # print(file. read(2))
# # file.seek(2)
# # print(file.read(2))
#
# for line in [line.strip() for line in file.readlines()]:
#     for elem in line:
#         print(f"{elem} is upper: {elem.isupper()}")
#
#
# file.close()


# file1 = open('file1.txt', 'r')
# # text1 = list(file1.read())
# file2 = open('file2.txt', 'r')
# text2 = list(file2.read())
# print(set(text1 + text2))

# h = file1.readline().split()
# f = file2.readline().split()
#
# r = [x for x in h if x not in f]
#
# print(r)
# file1.close()
# file2.close()

# h = file1.readline().split()
# f = file2.readline().split()
# print(set(h))
# print(set(f))
# r = set(h) - set(f)
#
# print(r)
# file1.close()
# file2.close()

# print(text1)
# print(text2)
# for i in range(min(len(text1), len(text2))):
#     if text1[i] != text2[i]:
#         print(f"Не хватає: '{text1[i]}', на індексі: {i}")
#         break
# file1.close(), file2.close()
# for f in file1, file2:
#     f.close()
# print(file1.read())
# print(file2.read())

# 15 - 100 %
# 5 - x %
# 5 * 100 / 15

# file1 = open('file1.txt', 'r')
# for line in file1.readlines():
#     print(len(line))
# file1.close()
# 27
# 20
# 11
# 1
# 4
# s = 0
# for line in file1.readlines():
#     s += len(line.strip())
# file1.close()
# print(s)


# bukvas = 0
#
# for elem in file1.read():
#     bukvas += 1
# file1.seek(0)
# print(bukvas-1-len(file1.readlines()))
# # print(file1.readlines())
# file1.close()


# def longestCommonPrefix(lst):
#     s = ""
#     for i in range(len(min(lst))):
#         if lst[0][i] == lst[1][i] == lst[2][i]:
#             s += lst[0][i]
#         else:
#             return s

import turtle
# turtle.speed(0)
# turtle.fd(200)
# turtle.lt(90)
# turtle.fd(200)
# turtle.pu()
# turtle.goto(0, -50)
# turtle.done()

# t = turtle.Turtle()
# t.fd(100)
# t1 = turtle.Turtle()
# t1.backward(100)
# turtle.done()

# import turtle
# file = open("coors.txt", "w+")
# t = turtle.Turtle()
# # print(t.xcor(), t.ycor(), "", end="")
# # file.write(f"{str(t.xcor())} {str(t.ycor())} ")
# t.write(f"{str(t.xcor())}  {str(t.ycor())}")
# t.fd(300)
# t.write(f"{str(t.xcor())}  {str(t.ycor())}")
# turtle.done()
# # file.write(f"{str(t.xcor())} {str(t.ycor())}\n")
# # print(t.xcor(), t.ycor())

# file = open("abc.txt", "w+")
# for num in range(10):
#     file.write(f"{num}    {num+1}\n")
# # for num in range(10):
# #     print("num:", num, end="", file=file)
# file.seek(0)
# print(file.read())


# file = open("abc.txt", "w+")
# for num in range(10):
#     file.write(f"{num}  {num+1}\n")
# file.seek(0)
#
# for line in file.readlines():
#     line = line.split()
#     print(int(line[0]) + int(line[1]))

# from turtle import *
# import pandas
# def start():
#     file.write(f"{xcor()} {ycor()} ")
# #1
# file = open("coors.txt", "w+")
# start()
# fd(100)
# file.write(f"{xcor()} {ycor()}\n")
# file.close()
#
# # df = ....
# # print(df)
# # first = fd.sum()
#
# #2
# file = open("coors.txt", "w+")
# file.write(f"{xcor()} {ycor()} ")
# fd(200)
# file.write(f"{xcor()} {ycor()}\n")
# file.close()
# # df = ....
# # print(df)
# # second = fd.sum()
#
# #3
# file = open("coors.txt", "w+")
# file.write(f"{xcor()} {ycor()} ")
# fd(200)
# file.write(f"{xcor()} {ycor()}\n")
# file.close()
# # df = ....
# # print(df)
# # third = fd.sum()
#
# print(min(first, second, third), " is min")

# lines = [line.strip() for line in file.readlines()]
# print(lines)


#1 from math import sqrt # square root
#2 x ** (1/2)
#3 x ** 0.5

# num = int(input("n: "))
# for elem in str(num):
#     print(int(elem) % 2 == 0)

# c = 0
# for num in range(11, 99):
#     pretty = True
#     for elem in str(num):
#         if int(elem) % 2 == 0:
#             pretty = False
#             break
#     if pretty:
#         print(num)
#         c += 1
# print("c =", c)
