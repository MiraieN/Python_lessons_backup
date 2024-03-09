# Slicing Strings

# b = "Hello, World!"
# b = ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']
# print(b[5])   # index
# print(b[-6])       # negative index
# print(b[2:6])    # slicing
# print(b[:6])
# print(b[2:12:2])     # [start:end:step]
# print(b[::2])        # [::]
# print(b[6:2:-1])
# print(b[::-1])
# print(b[-2:-6:-1])
# print(b[-6::1])

# txt = "I love apple, apple are my favorite fruit"
#
# x = txt.count("a")
#
# print(f"a is figured in txt: {x} times")

# for z in range(10):
#     print(z)

# for z in input():
#     pass

# lst = [1, 2, True, '4', 1]
# 1 changeable
# lst[0] = 4
# 2 ordered
# lst[0], lst[0:2], lst[::-1]
# print(lst[::-1])
# 3 duplicates
# lst = [1, 1, 1, 1, 1, 1, 1, 1]
# print(list(input()))
# print(len(lst))
# print(lst[len(lst)-1])
# print(lst.count(1))
# if True == 1:
#     print("hm")

# while True:
#     a = input("gimme num (5..10) (even)\n")
#     try:
#         a = int(a)
#         if not 5 < a < 10:
#             print("(5..10)!")
#             continue
#         if a % 2 == 1:
#             print("only even numbers")
#             continue
#         break
#     except ValueError:
#         print("You wrote a string, not a number\n")

# print(f"This is definitely a num (5..10): {a}")

# a = None
# while not isinstance(a, int):
#     a = input("gimme num\n")
#     try:
#         a = int(a)
#     except:
#         print("You wrote a string, not a number\n")
#
# print(f"This is definitely a num: {a}")

# 1 (1-2 раз або робимо багато об'єктів, або багато функцій)
# import random
# print(random.randint(0, 1))
# import math
# print(math.factorial(5))
# import turtle
# a = turtle.Turtle()
# b = turtle.Turtle()

# 2
# from random import randint, shuffle, randrange
# randint(0, 1)
# 2.1
# from random import randint as rdi, shuffle as shf
# rdi(0, 1)
# 2.2
# from turtle import *
# fd(100)
# done()

# ans = input("1")
# while ans != "1":
#     ans = input("1")

# Try, except, random, while

# lst = ["apple", "banana", "grape", "pear", "ap"]
# lst.append("plum")        - додає в кінець
# for z in range(10):
#     lst.append(input())
# lst.clear()
# x = lst.copy()            - повертає об'єкт-копію
# backup_lst = lst
# lst.append("1")
# apple_num = lst.count("apple")    - підрахунок к-ст елемента
# l = [1, 2, 3, 4]
# lst.extend(l)               - додає в кінець іншу колекцію
# lst.extend("Hello")
# lst = lst + l
# num = lst.index("apple", 2, 5)    - повертає індекс елемента
# lst.insert(1, "plum")       - вставляє елемент на позицію
# deleted_el = lst.pop(2)     - видаляє і повертає елемент по індексу
# lst.remove('apple')         - видаляє елемент по назві
# lst.reverse()               - перевертає
# nums = [1,2,3,56,7,6,2]
# nums.sort(reverse=True)       - сортує
# print(lst)
# from random import shuffle
# lst = [0, 2, 4, 6, 8, 10, 12, 14]
# shuffle(lst)
# for z in range(25):
#     if z % 2 == 0:
#         lst.append(z)
# print(lst)
# for z in lst:
#     if z % 4 == 0:
#         lst.remove(z)

# for z in range(4):
#     lst.pop(z)

# print(lst)
# for ind, elem in enumerate(lst):
#     if lst[ind-1] < lst[ind]:
#         print(lst[ind-1])


# print(lst)
from random import shuffle

# lst = [1, -1, 2, 3, 4, 5, 6]
# shuffle(lst)
# print(lst)
# for i in range(len(lst)-1):
#     if not lst[i] < lst[i+1]:
#         print(False)
#         break

# if int(input()) in lst:
#     print(True)
# else:
#     print(False)

# list methods, for, for in list, in lst and range(len(lst)), if in,


# lst = []
# while True:
#     z = input("фыв")
#     if z == "список":
#         print(lst)
#     elif z == "стоп":
#         print(lst)
#         break
#     if z not in lst:
#         lst.append(z)

# lst1,lst2,lst3 = [],[],[]
# print("......")
# while True:
#     name = input()
#     print("..")
#     while True:
#         which_list = input()
#         if which_list == "anime":
#             while True:
#                 # добавляяяяяяємо і перевіряємо
#                 if input() == 'stop':
#                     break
#         if which_list == "anime":
#             while True:
#                 # добавляяяяяяємо і перевіряємо
#         if which_list == "anime":
#             while True:
#                 # добавляяяяяяємо і перевіряємо
#         break
#     if input() == 'stop':
#         print("з цим юзером кінець. Очікую нового юзера")
#         continue


# # list generator
# from random import randint
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print([randint(0, 150) for z in range(10)])

# from random import randint as rdi
# ls = [rdi(1, 100) for z in range(10)]
# print(ls)
#
# lst = [z for z in ls if z % 2 == 1]
# lst = [z for z in ls if len(str(z)) and str(z)[0] == '2']
# lst = [ls[i-1] for i in range(1, len(ls)) if ls[i] % 2 == 0 and ls[i-1] % 2 == 0]
# print(lst)
# for i in range(1, len(ls)):
#     if ls[i] % 2 == 0 and ls[i-1] % 2 == 0:
#         print(lst.append(ls[i-1]))
#
# print(f"default list {ls}")
# print(f"modified     {lst}")

# imb for in list(tasks in course),

# запитати юзера номер телефону. Кожна цифра - окремий елемент в списку
# multiassign, enumerate,
# new import
# задача з шансом рандому 1/0, find, [],
# import random as rd
#
# ls = [rd.randint(-100, 100) for z in range(10)]
# print(ls)
# print([ls[i] for i in range(0, len(ls) - 1) if ls[i] > 0 and ls[i+1] > 0 or ls[i] < 0 and ls[i+1] < 0])

# for i, z in enumerate(ls):
#     if ls[i] * ls[i-1] > 0:
#         print(ls[i-1], ls[i])

# l = [int(input("Ur number?")) for z in range(int(input("range?")))]
# print(l)


# string = '12345435'
# string = list(string)
# lst = []
# for elem in string:
#     lst.append(elem)
# lst[0] = int(lst[0])
# print(lst)

# mail = "random.mail@gmail.com"
# mail_2 = "random1@ukr.net"
# mail.find()

# lst = []
# lst.clear()
# lst = [0, 1, 1, 1, 0]
# ln = len(lst)
# percent = lst.count(0) * 100 / ln
# print(f'''
# amount: {ln}
#                 0 -  {lst.count(0)} -  {percent} %
# ''')

# import locale
#
# locale.setlocale(locale.LC_ALL, "ua-UA.UTF-8")
# amount = 1000000000
# print(f"{amount:n}")

# # phone num
# nmb = list(input())
# print(nmb)
# nmb = list(map(int, nmb))
# nmb = [int(z) for z in nmb]
# # nmb = [int(input("number?")) for z in range(int(input("how much?")))]
# print(nmb)

# # locale
# import random as rd, time, locale
#
# locale.setlocale(locale.LC_ALL, "ua-UA.UTF-8")
# l = []
# amount = 10
# for x in range(6):
#     for j in range(5):
#         for z in range(amount):
#             l.append(rd.randint(0, 1))
#         l0, l1 = l.count(0), l.count(1)
#         print(f'''{amount:n} numbers:
#                         0 - {l0} - {round(l0 * 100 / amount, 4)}%
#                         1 - {l1} - {round(l1 * 100 / amount, 4)}%\n''')
#         l.clear()
#         time.sleep(0.1)
#     amount *= 10
#     time.sleep(0.1)

# for z in range(1, int(input("до скількох?"))+1, 2):  # 1,3,5,7,9... - непарні(перші)
#     print(f"{z} - перший\n{z+1} - другий")

#

# mails = ['Qw.e@ukr.net', 'asdasd@mail.ru', 'asdasd@gmail.com']
# txt = 'qweasdzxcasd@ukr.net'
# num = txt.find('@')
# print(txt[0:num])
# num1 = txt.rfind('.')
# print(txt[num:num1])
# статистика почт,
# vars


# import random as rd
#
# students = ['Mayakovskiy', 'Bairon', 'Shekspier', 'Ya']
# #
# ## варіанти variants
# # 1 генерувати число і додавати в список. Якщо воно вже є в списку - генеруй нове
# # 2 генерувати список з числами. Виводити елемент з рандомним індексом і видаляти його (праву межу задавати динамічно через довжину списку)
# # 3 перемішати список з числами
# # # 1
# nums = []
# for student in students:
#     z = rd.randint(1, len(students))
#     while z in nums:
#         z = rd.randint(1, len(students))
#     nums.append(z)
#     print(f"{student} - {z}")
# #2
# nums = [z for z in range(1, len(students)+1)]
# for student in students:
#     print(nums)
#     ind = rd.randint(1, len(nums)) - 1
#     # print(f"{student} - {nums[ind]}")
#     #     # nums.pop(ind)
#
#     print(f"{student} - {nums.pop(ind) + 1}")

# #3
# nums = [z for z in range(1, len(students)+1)]
# rd.shuffle(nums)
# for i in range(len(students)):
#     print(f"{students[i]} -  {nums[i]}")
# #3.1
# for student in students:
#     print(f"{student} - {nums.pop()}")
# #3.2
# import random
# sn = input("surnames").split()
# l = list(range(1, (len(sn)+1)))
# random.shuffle(l)
# for x in sn:
#     print(x, "-", l.pop())


# import numpy
# print(numpy.arange(10))

# # ______________________________
# # ___important functions info___
# # ______________________________

# # # global
# x = 0
# def bill_electricity():
#     # outerscope
#     # global x
#     x = 0
# bill_electricity()
# # print(x)

#
# for z in range(10):
#     bill_electricity()
# print(x)
# global outerscope

# def bill_count(rastoch, tariff):  # rastoch = rastoch_A
#     res = rastoch * tariff
#     return res
#
# gs_Andriy = 8000
# rastoch_Andrew = 230
# lit = 6
#
# electricty = bill_count(rastoch_Andrew, 1.5)
# gas = bill_count(gs_Andriy, 0.15)
# liter = bill_count(lit, 55)
# zhutie = (electricty + gas + liter) / 100
#
#
# print(f"ти не з'їси {zhutie} гамбургерів")
# print(f"ти прожив би {zhutie / 3} днів якби був бездомним")


# def calc_simple(num1,num2,op):
#
#     return num1 + num2
#
# print(calc_simple(1,2,3))


# def is_year_leap(year):
#
#     if year % 400 == 0:
#         return True
#
#     if year % 4 == 0 and year % 100 != 0:
#         return True
#
#     return False


# # Простые числа
# # =============
# # Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000 и возвращающую True,
# # если оно простое, и False - иначе.
# # """
# def is_prime(num):
#     if num in (0, 1):
#         return "0 or 1"
#     if num < 0:
#         return "< 0"
#     count = 2
#     # while count < int(num/2):
#     #     if num % count == 0:
#     #         return False
#     #     count += 1
#     # else:
#     #     return True
#     for count in range(2, int(num/2)+1):
#         print(f"{num} % {count} == {num/count}")
#         if num % count == 0:
#             return False
#     return True


# print(is_prime(67))

# def dyadya_ni_nado():
#     print("\nWhat a great day for a loop")
#     print("It would be shame if I got into one\n")
#     return dyadya_ni_nado()
#
#
# dyadya_ni_nado()


# def fact(num):
#     if num == 0:
#         return 1
#     if num < 0:
#         return "Invalid"
#     if num == 1:
#         return num
#     return num * fact(num-1)
#
# print(fact(6))


# 5! = 1*2*3*4*5
# 5! = 5*4*3*2*1
# func:

# for i in range(1, 5):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print(end='\n\n')
#
# for i in range(4, 0, -1):
#     for j in range(1, i+1):
#         print('*', end=' ')
#     print()

# def get_gcd(x, y):
#     # переменная для меньшего числа
#     s = x
#     if x > y:
#         s = y
#     for i in range(1, s + 1):
#         if (x % i == 0) and (y % i == 0):
#             # в данном случае мы можем "переиспользовать" переменную `s`
#             s = i
#     return s
#
#
# print(get_gcd(333, 999))  # 12

# d = "a*hj?"
#
# print(list(d))

# print(list(input("Enter any String")))

# a = [1,2,3,4,5]
# print(a[0])
# print(a[-1])
# print(a[2])
# print(a[-2])
# print(a[1])

# list1 = "Practice QuesTions of List in pythoN"
# list2 = list(list1)
#
# print(list2[0])
# print(list2[9])
# print(list2[-14])
# print(list2[-1])
# print(list2[13])
#
# print(list2[-14:-10])

# print([1,2,3,4] == [4,3,2,1])
# print([1,2,3,4] > [4])
# print(	[1,2,3,4] != [1,2,3,4])
# print([1,2,3,4] == [1,2,[3,4]])
# print([1,2,3] == [1.0,2.0,3.0])
# a = [1,2,3,4]
# b = [5,6,7,8]
# print(a+b)

# a = "python"
#
# b = list(a)
#
# print(b * 2)
#
# print(b + b)
#
# print(a + a)

# a = [1,2,3,4]
# (a.reverse())
# print(a)
# print(list(reversed(a)))
# print(a)
#
# a = [1, 5, 7, 5]
# a.pop(a.index(5))
# print(a.index(5))

# a = [1,2,3,4]
# a[1] = 'a'
# print(a)

# Q9. Write code to arrange elements of following list in increasing order.
# A = [23,12,45,32,67,33]
# print(sorted(A))
# A.sort()
# print(A)

# nested
# l = [[123,123,345,4356,456,45], [5345,34436,7,567,56]]
# print(max(l[1]))

# a = [[1, 2, 3],
#      [1, 3, 3],
#      [7, 8, 9]]

# print(a[2][2])
# for i in range(len(a)):
#     for j in range(len(i)):
#         print(a[i][j])
# for i in a:
#     print(i)
#     for j in i:
#         print(j, end='')
#     print()


# funcs tasks
# https://habr.com/ru/company/timeweb/blog/579080/
# https://gist.github.com/jigi-33/209ad40c6f9be2f8b9775d28cbc40672

# Q6. Name a function/statement which can delete more than one element from the list.
#
# Q7. Name a function which can delete only one element from the list.
#
# Q8. Write a program to delete/remove all the negative elements from the list.
#
# Q9. Write a program to delete/remove all the odd numbers from the list.
#
# Q10. Write a program to delete/remove all the numbers less than 10 from the list.

# https://habr.com/ru/company/timeweb/blog/579080/
# 27. Функция для транспонирования матрицы
# 28. Функция для определения того, является ли строка палиндромом
# 29. Функция для удаления лишних символов из строки
# 30. Функция для сортировки слов в алфавитном порядке
# 11. Write a Python function to check whether a number is perfect or not
# According to Wikipedia : In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum). Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself).
# Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.

# x = [
#  [1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]
# ]
# x[0][2]
# l = [
#     [3, 3, 3],
#     [2, 4, 3],
#     [4, 5, 6],
#     [6, 5, 4]
# ]
# l_1 = [
#     [0,0,0],
#     [2, 4, 3],
#     [4, 5, 6],
#     [6, 5, 4]
# ]
# for i in range(len(l)):
#     for j in range(len(l[i])):
#         print(l[i][j])
# l_1 = [[1,2],[]]
# l_2 = [[2,3],[]]
# l_3  = [[],[]]
# l_3[0][0] = l_1[0][0] + l_2[0][0]
# 3 3 3
# 2 3 3
# 4 5 6
#
# 6 6 6
# 4 6
# def perf(num):
#     return True if sum(z for z in range(1, num) if num % z == 0) == num else False
#
# print(perf(7))

# def palindrome(string):
#     str_2 = ''
#     for elem in string:
#         if elem != ' ':
#             str_2 += elem
#     return True if str_2[::-1] == str_2 else False
#
#
# print(palindrome("дее е д"))


## def assign in (=)
## args
## func that takes args and displays their sum, average, sort in asc/des(true/false)


# def print1(args, end='\n', sep=' '):
#     for elem in args:
#         print(elem)
#         print(end)
#
#
# print1([1,2,3],end='g')
# print(1,1,1, sep='')

# def f(mama, papa, *l):               # *args - arguments  # **kwargs - key word arguments
#     for z in l:
#         print(z)
# f("mom", "papa", 2, 3, 4)


# print(sorted((1,2,3,4), reverse=True))

## lambda
## https://www.w3resource.com/python-exercises/lambda/index.php

# def f(a):
#     return a+2
# print(f(3))
#
# l = lambda a: a+2
# print(l(3))
#
# perf = lambda num: True if sum(z for z in range(1, num) if num % z == 0) == num else False
# print(perf(7))

# def len_sort(elem):
#     return len(elem)
#
#
# lst = ['journo', "dio", "polnareff", "iggy"]
# lst.sort(key=len_sort)
# print(lst)
# lst = ['journo', "dio", "polnareff", "iggy"]
# print(sorted(lst, key=lambda elem: len(elem)))


# sort
# https://holypython.com/intermediate-python-exercises/exercise-15-python-sorted-function/

# map
# https://www.w3resource.com/python-exercises/map/index.php


# from time import sleep
#
# for z in range(5, 0, -1):
#     sleep(1)
#     print(f"Hacking Pentagon in {z}...")
# print("Hacked")

# rsp game

# def factorial(n):
#     match n:
#         case 0 | 1:
#             return 1
#         case _:
#             return n * factorial(n - 1)
#     # if n == 0:
#     #     return 1
#     # else:
#     #     return n * factorial(n - 1)
#
#
# factorial(5)

# math funcs:
# https://www.w3schools.com/PYTHON/module_math.asp
# https://pythonist.ru/test-math-v-python/

# import math
# print(math.acos(-0.5))
# print(math.ceil(2.2))
# print(math.floor(2.8))

# a = 2
# while a < 3:
#     print(f"{a}:\n\t {round(a, 3)}")
#     a += 0.1

# num = 2.3
# num = num - int(num)
# print(round(num, 2))

# print(math.degrees(math.pi))

# print(math.fabs(-25))
# print(math.fabs(25))

# print(math.fmod(20, 3))
# print(divmod(20, 3))
# print(20 % 3)

# print(math.sqrt(2))   # square root
# print(2**(1/2))

# print(math.pow(2, 6))   # power # 2 in the power of 6
# print(2**6)

# print([1,2,3].pop(2))
# def f():
#     a = 2
#     a += 2
#     return a
# print(f())


# # MAP
# lt = [str(z) for z in range(10)]
# lt = list(map(int, lt))
# print(lt)

# items = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, items))
#
# sq = []
# a = lambda x: x**2
# for elem in items:
#     sq.append(a(elem))
# print(squared, sq)

# def filt_nums(elem):
#     if elem % 2 == 1:
#         return True
#
# nums = [z for z in range(-5, 5)]
# filtered_nums = list(filter(filt_nums, nums))
# print(filtered_nums)

# nums = [z for z in range(-5, 5)]
# filtered_nums = list(filter(lambda e: e >= 0, nums))
# print(filtered_nums)

# txt = "Sun in skies in Florida".split()
# print(list(filter(lambda elem: elem[0].casefold() == 'i', txt)))
# a = []
# for e in txt:
#     if e[0].casefold() == 'i':
#         a.append(e)
# print(a)


# filter
# https://pavel-karateev.gitbook.io/intermediate-python/funkcionalnoe-programmirovanie/map_filter
# https://pythonru.com/uroki/funkcija-filter-dlja-nachinajushhih
# Напишите функцию, которая принимает на вход список с именами людей и возвращает новый список с именами, которые начинаются на гласную букву. В новом списке имя должно начинаться с прописной буквы, даже если изначально было написано со строчной.


# # відсортувати список за сумою цифр кожного числа (11 = 1 + 1 == 2, 1666 = 1 + 6 + 6 + 6 = 19)
# lst = [11, 33, 1666, 45, 62, 44, 933, 200]
# https://tproger.ru/problems/python-3-exercises-for-beginners-geekbrains/

# dicts

# Правила игры сводятся к тому, что вам дают две карты и вы должны приблизится к числу 21. Вы можете брать дополнительные карты из колоды, но если вы получите число более 21, то автоматически проиграли. Кроме того, если число получилось наименьшим из тех, которые есть у ваших соперников, то вы также проиграли.
# Для реализации вам понадобится колода карт, из которой вы каждый раз будете вынимать по карте и прибавлять к результату. Представим, что у нас есть следующие карты: шестерка, семерка, восьмерка, девятка, десятка, валет (его значение равно числу 2), дама (3), король (4), и туз (11).
# Ваша задача разработать программу для игры в «Блэкджек».

# mails with dict
# kwargs

# files
# person = {
#     'user_1': {
#         'first_name': 'John',
#         'last_name': 'Marley',
#         'age': 45,
#         'address': ('г. Москва', 'ул. Какая-то', '45'),
#         'grades': {'math': 5, 'physics': 3}
#     },
#     'user_2': {
#         's': 'd',
#         'h': 'g'
#     }
# }
#
# for key in person['user_1'].keys():
#     print(person['user_1'][key])

# e = "olga"
# print(e)
# e = e.replace(e[0], e[0].upper())
# print(e)

# lst = ["джолін", 'джорно', 'джованна', 'Діо', 'абдул', 'арнольд', "ясухо"]
# Diabolo = list(filter(lambda a: a[0].lower() in 'аеуєяюїіои', lst))
#
# print([(Diabolo[ind][0].upper() + Diabolo[ind][1:]) for ind in range(len(Diabolo)) if Diabolo[ind][0].islower()])


# for a in range(len(Diavolo)):
#     if Diavolo[a][0].islower():
#         Diavolo[a].replace(Diavolo[a][0],Diavolo[a][0].upper())
#         print(Diavolo)

# list1 = ["Python", "CSharp", "Java", "Go"]
# list2 = ["Python", "Scala", "JavaScript", "Go", "PHP", "CSharp"]
#
# l_1 = list(filter(lambda e: e not in list2, list1))
# l_2 = list(filter(lambda e: e not in list1, list2))
# print(l_1 + l_2)
#
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# same_items = set(filter(lambda elem: elem in b, a))
# print(same_items)

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# print(list(set(a) & set(b)))
#
# print(set([elem for elem in a if elem in b]))
#
# result = list(filter(lambda elem: elem in b, a))


# out_filter = list(filter(lambda elem: elem in b, a))
#
# out_filter = list(filter(lambda elem: elem in a, b))
# print(out_filter)

## dictionary
## {keys:values}:items
# d = dict(WWI=1914, WWII=1939)
# print(d["WWI"])
# l = [["WWI", 1914], [1939, "WWII"]]
# d = dict(l)
# print(d)

# d = {'WWI': 1914, 1939: 'WWII'}

# d = dict.fromkeys(['a', 'b', 'c'], 100)
# print(d)
# def func(b, a = 2, c = 3):
#     return True
# func(3, a = 7, c = 8)

# d = dict(1914=WWI, 1939=WWII)

# d = {
#     1914: "WWI",
#     1939: "WWII",
#     1999: "Smash mouth: All stars"
# }
# print(d[1914])
# d_1 = {
#     "Skyrim 1": "mnogo",
#     "skyrim 2": "mnogo",
#     "skyrim aniversary edition": 10000000000000000
# }
# d_1["Skyrim 1"] = "och mnogo"
# print(d_1["Skyrim 1"])

# chars = {
#     "hp": {"mob": 5, "player": 3},
#     "armor": 2
# }
#
# hp = 100
# hp += chars["hp"]["player"]
# print(hp)
# hp_mob = 70
# hp_mob += chars["hp"]["mob"]

# d = {}
# d["asd"] = 123
# print(d)

## count number of each letter in string and print out
# s = "ununderstandable"
# d = {}
# for elem in s:
#     if elem in d:
#         d[elem] += 1
#     else:
#         d[elem] = 1
# print(d)

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# car_copy = car.copy()           # копія
# car_copy["brand"] = 123
# car_copy["123123123"] = 123123
# del car_copy['year']
#
# print(car.get("brand"))
# print(car['brand'])
# print(car.get("asd", "No asd"))  # виводить по ключу, може вивести дефолт
# try:
#     print(car["asd"])
# except:
#     print("no asd")

# print(car.pop("asd"))           # попає елемент по ключу. Може вивести дефолт
# print(car.pop("asd", "Nope asd"))
#
# del car['asd']

# car.popitem()                 # видаляє останній елемент

# print(car.setdefault("brand12", "brocoli"))       # виводить елемент по ключу. Якщо немає такого ключа то створює ключ із знченням дефолт
# print(car)

# print(car)
# print(car_copy)
# car.update(car_copy)        # додає словник в кінець словника але перезаписує ключі що повторюються
#
# print(car)

# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964,
#     12: 123
# }

# print([elem for elem in car.keys() if isinstance(elem, str)])
# a = list(car.keys())
# a[2] = 5

# print(car.values())
# print(list(car.items()))

# for key, value in car.items():
#     print(f"key: {key}\tvalue: {value}")
#
# for key in car.items():
#     print(f"key: {key[0]}\tvalue: {key[1]}")

# vars with dicts

# BLACK JACK GAME
# one with me at the lesson
# second for self at home (Правила игры сводятся к тому, что вам дают две карты и вы должны приблизится к числу 21. Вы можете брать дополнительные карты из колоды, но если вы получите число более 21, то автоматически проиграли. Кроме того, если число получилось наименьшим из тех, которые есть у ваших соперников, то вы также проиграли. Для реализации вам понадобится колода карт, из которой вы каждый раз будете вынимать по карте и прибавлять к результату. Представим, что у нас есть следующие карты: шестерка, семерка, восьмерка, девятка, десятка, валет (его значение равно числу 2), дама (3), король (4), и туз (11). # # Ваша задача разработать программу для игры в «Блэкджек».


# staff = {
#      'Смирнов': {
#          'посаду': 'менеджер з продажу',
#          'ефективність': 86
#      },
#      'Колягина': {
#          'посаду': 'менеджер з продажу',
#          'ефективність': 69
#      },
#      'Костін': {
#          'посаду': 'менеджер з продажу',
#          'ефективність': 78
#      },
#      'Щербаков': {
#          'посаду': 'менеджер з продажу',
#          'ефективність': 91
#      },
#      'Борисова': {
#          'посаду': 'менеджер з продажу',
#          'ефективність': 99
#      }
# }

# # generators dict
# d = {
#     100: 'a',
#     200: 'b'
# }
# d[100] = 'c'
# d = {z: 100 for z in 'abc'}
# l = [z for z in range(10)]
# print(d)

# s = [(1, 1), (3, 4), (2, 9)]
# a = dict(s)
# print(a)
# for k, v in s:
#     print(k, v)
# print({k: v for k, v in s})

# l = [2, 1, 3, 9, 8, 7, 4]
# l.sort(key=lambda elem: elem % 3)
# print(l)
# dict1 = {1: 1, 2: 9, 3: 4}

# dict1 = {5: 1, 2: 9, 3: 4}
# sorted_tuples = sorted(dict1.items(), key=lambda dinozavrik: dinozavrik[1])
# print(sorted_tuples)


# import operator
#
# dict1 = {1: 1, 2: 9, 3: 4}
# sorted_tuples = sorted(dict1.items(), key=operator.itemgetter(1))
# print(sorted_tuples)  # [(1, 1), (3, 4), (2, 9)]
# sorted_dict = {k: v for k, v in sorted_tuples}
#
# print(sorted_dict) # {1: 1, 3: 4, 2: 9}
# name = "asdasd"
# dict1 = {1: 1, 2: 9, 3: 4}
# print(f"first elem {dict1[1]}, Name: {name}")
# sorted_tuples = sorted(dict1.items(), key=lambda item: item[1])
# print(sorted_tuples)  # [(1, 1), (3, 4), (2, 9)]
# sorted_dict = {k: v for k, v in sorted_tuples}
#
# print(sorted_dict)  # {1: 1, 3: 4, 2: 9}


# # ПЛАН ПРОГРАМИ:
# # 1. Підключаємо потрібні модулі.
# # Згадай, які модулі потрібні: черепашки будуть робити кроки випадкової довжини.
# # Напиши тут команди підключення цих модулів:
#
# from random import randint
# import turtle
#
# # 2. Заводимо змінні для розміру ігрового поля,
# # Так буде простіше управляти черепашками!
# turtle.ht()
#
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
#     t.right(9*95)
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
# max_x = max(x.xcor(), y.xcor())
# if x.xcor() == max_x:
#     winner(x)
# elif y.xcor() == max_x:
#     winner(x)
# #
# # складніший варіант - для любої к-сті черепашок
# d_cors = {x: x.xcor(), y: y.xcor()}
# max_x = max(d_cors.values())
# for k, v in d_cors.items():
#     if v == max_x:
#         winner(k)

import operator

# dict1 = {1: 1, 9: 1, 3: 4}
# sorted_tuples = sorted(dict1.items(), key=lambda d: d[1])
# sorted_tuples = sorted(dict1.items(), key=operator.itemgetter(1))
# print(sorted_tuples)
# sorted_tuples = {k: v for k, v in sorted_tuples}
#
# d = {}
# for k in sorted_tuples:
#     d[k[0]] = k[1]
# print(d)
# for k, v in sorted_tuples:    d[k] = v
# sorted_tuples = d
# print(sorted_tuples)

###########
### OOP ###
###########
# kirk = ["James Kirk", 34, "Captain", 2265]
# spock = ["Spock", 35, "Science Officer", 2254]
# mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]


# # kirk[0]
# print(f"name: {kirk[0]}\n\t age:{kirk[1]}")
# print(f"name: {spock[0]}\n\t age:{kirk[1]}")
# for elem in kirk, spock, mccoy:
#     print(f"name: {elem[0]}\n\t age:{elem[1]+1}\n")

# описати як змінні, показати що немає примусовості а потім переописати як ініт
# class HumanWorker:
#     name = ""
#     age = 0
#     work = ""
#     salary = 0
#
#
#
# Kirk = HumanWorker
# Kirk.name = "James Kirk"
# # print(Kirk.name)
# Spock = HumanWorker
# Spock.name = "Spock"
# for o in (Kirk, Spock):
#     print(f"name: {o.name}")
# print(Kirk.name)

# class HumanWorker:
#     specie = "Human spies"
#
#     def __init__(self, _name, _age, _work, _salary):
#         self.name = _name
#         self.age = _age
#         self.worksAt = _work
#         self.salary = _salary
#
#     def povis_zp(self, amount):
#         self.salary += amount
#
# Kirk = HumanWorker("James Kirk", 34, "Captain", 2265)
# Spock = HumanWorker("Spock", 35, "Science Officer", 2254)
# Mccoy = HumanWorker("Leonard McCoy", 27, "Chief Medical Officer", 2266)
# print(Mccoy.specie)

## static function - не впливає напряму на клас
# def povis_zp(who, amount):
#     who.salary += amount
#
# povis_zp(Kirk, 1000)
# povis_zp(Spock, 500)
#
## визиваємо метод
# Spock.povis_zp(1500)
# for obj in Kirk, Spock, Mccoy:
#     print(f"name: {obj.name}\n\tage: {obj.age}\n\tworks as: {obj.worksAt}\n\tSalary: {obj.salary}\n")


# class Dog:
#     species = "Canis familiaris"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print(self.name + " is created")
#
#     def speak(self, sound='woof'):
#         print(f"{self.name} says {sound}")
#
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"
#
#
# bobik = Dog("Bobik", 6)
#
#
# # print(bobik)
# # bobik.speak("Gutten tak")
#
# class Shpitzh(Dog):
#     pass
#
#
# class Korgi(Dog):
#     def __init__(self, name, age, obhvat_zhopi):
#         super().__init__(name, age)
#
#     def speak(self, sound="fresh meat"):
#         super().speak(sound)
#
#
# class Dachshund(Dog):
#     pass
#
#
# Pudge = Korgi("Pudgik", 2, 13.7)
# Pudge.speak()
# print(Pudge)
#
# bh = Korgi("BH", 13, 5.7)
# bh.speak(sound="Golllllld")
# print(bh)
# https://realpython.com/python3-object-oriented-programming/#how-to-define-a-class

# як зробити обмеження ніг у людини(дз) я поясню із температурою
## Using @property decorator
# class Celsius:
#     def __init__(self, temperature=0):
#         self.temperature = temperature
#
#     def to_fahrenheit(self):
#         return (self.temperature * 1.8) + 32
#
#     @property
#     def temperature(self):
#         print("Getting value...")
#         return self._temperature
#
#     @temperature.setter
#     def temperature(self, value):
#         print("Setting value...")
#         if value < -273.15:
#             raise ValueError("Temperature below -273 is not possible")
#         self._temperature = value
#
#
# # create an object
# human = Celsius(37)
#
# print(human.temperature)
#
# print(human.to_fahrenheit())
#
# coldest_thing = Celsius(-300)

# # import package
# import turtle
#
#
# # method to action
# def fxn(x, y):
#     # some motion
#     turtle.right(90)
#     turtle.forward(100)
#
#
# # turtle speed to slowest
# turtle.speed(1)
#
# # motion
# turtle.fd(100)
#
# # allow user to click
# # for some action
# turtle.onclick(fxn)
#
# turtle.done()


## Ukraine flag
# from turtle import *
# for col in ("blue", "yellow"):
#     fillcolor(col)
#     begin_fill()
#     for side in range(2):
#         fd(180)
#         rt(90)
#         fd(60)
#         rt(90)
#     end_fill()
#     rt(90)
#     pu()
#     fd(60)
#     pd()
#     lt(90)
# exitonclick()

## визначити як швидше: так, чи без goto
# from turtle import *
# width(5)
# y_pos = 0
# for y in range(-50, -300, -50):
#     fd(400)
#     pu()
#     goto(0, y)
#     pd()
# pu()
# home()
# exitonclick()

# counter = 0
# num = 12345
# while num != 0:
#     num //= 10
#     counter += 1
# print(counter)

# def palindrome(string):
#     return string == string[::-1]
#
# def palindrome_(string):
#     return string[0:int(len(string)/2)] == string[int(len(string)/2):0]
#
# from horology import Timing
# with Timing(name="time: "):
#     palindrome("dedoded")
#
# with Timing(name="time: "):
#     palindrome("dedoded")
#
# with Timing(name="time: "):
#     palindrome_("dedoded")


######################
# import turtle
#
# def linia(start=True):
#     t.write(f"{round(t.xcor(), 3)}, {round(t.ycor(), 3)}")
#     if start == True:
#         file.write(f"{round(t.xcor(), 3)} {round(t.ycor(), 3)} ")
#     else:
#         file.write(f"{round(t.xcor(), 3)} {round(t.ycor(), 3)}\n")
# t = turtle.Turtle()
# file = open("a.txt", "w+")
# t.speed(0)
# for z in range(2):
#     linia()
#     t.forward(400)
#     linia(False)
#     t.rt(90)
#     t.penup()
#     linia()
#     t.forward(40)
#     linia(False)
#     t.rt(90)
#     t.pendown()
#     linia()
#     t.forward(400)
#     linia(False)
#     t.lt(90)
#     t.penup()
#     linia()
#     t.forward(40)
#     linia(False)
#     t.lt(90)
#     t.pendown()
# linia()
# t.forward(400)
# linia(False)
# turtle.exitonclick()
#
# for line in file.readlines():
#     print(line)
#
# file.close()

############## comparing two ways with pandas
# from turtle import *
# import pandas
#
#
# def first_mark():
#     x1 = str(round(xcor(), 3))
#     y1 = str(round(ycor(), 3))
#     file.write(f"{x1} {y1 + ' '}")
#     write(f"{x1},{y1}")
#
# def last_mark():
#     x2 = str(round(xcor(), 3))
#     y2 = str(round(ycor(), 3))
#     file.write(f"{x2} {y2}\n")
#     write(f"{x2},{y2}")
#
#
# file = open("coors.txt", "w+")
#
# # speed(0)
# width(5)
# for y in range(2):
#
#     first_mark()
#     fd(400)
#     last_mark()
#
#     pu()
#
#     rt(90)
#
#     first_mark()
#     fd(50)
#     last_mark()
#
#     rt(90)
#
#     pd()
#
#     first_mark()
#     fd(400)
#     last_mark()
#
#     lt(90)
#     pu()
#     first_mark()
#     fd(50)
#     last_mark()
#     lt(90)
#     pd()
# first_mark()
# fd(400)
# last_mark()
# pu()
#
# first_mark()
# home()
# last_mark()
#
# pd()
#
# file.close()
#
# df = pandas.read_csv('coors.txt', delim_whitespace=True, names=['x1', 'y1', 'x2', 'y2'])
# df = df.eval("dist = ((x1-x2)**2 + (y1-y2)**2) ** 0.5")
# print(df)
# res_without_go = df['dist'].sum()
# print(f"res_without_go = {res_without_go}")
#
# ## with go
# file = open("coors.txt", "w+")
#
# reset()
# # speed(0)
# width(5)
# y_pos = 0
# for y in range(-50, -300, -50):
#
#     first_mark()
#     fd(400)
#     last_mark()
#
#     pu()
#
#     first_mark()
#     goto(0, y)
#     last_mark()
#
#     pd()
# pu()
#
# first_mark()
# home()
# last_mark()
#
# pd()
#
# file.close()
#
# df = pandas.read_csv('coors.txt', delim_whitespace=True, names=['x1', 'y1', 'x2', 'y2'])
# df = df.eval("dist = ((x1-x2)**2 + (y1-y2)**2) ** 0.5")
# print(df)
# res_with_go = df['dist'].sum()
# print(f"res_with_go = {res_with_go}")
#
# exitonclick()
#
# print(f"\nres_without_go = {round(res_without_go, 3)}"
#       f"\nres_with_go = {round(res_with_go, 3)}")

# d = {"I": 1,
#      "V": 5,
#      "X": 10,
#      "C": 100,
#      "M": 1000}
# s = "MMXCIX" # 1000 - 100 + 1000 = 1901
# s = list(s)
# for i in range(len(s)):
#     s[i] = d[s[i]]
#     if i == 0:
#         continue
#     if s[i-1] < s[i]:
#         s[i-1] = -s[i-1]
# # for i in range(len(s)-1):
# #     if s[i] < s[i+1]:
# #         s[i] *= -1
# print(s)
# print(sum(s))


# def longestCommonPrefix(strs):
#     # this will be an answer
#     pref = ''
#     # find min and max words among strs
#     minWord = min(strs)
#     maxWord = max(strs)
#
#     # for iteration
#     i = 0
#     N = min(len(minWord), len(maxWord))
#
#     while i < N:
#         # if chars are equal
#         if minWord[i] == maxWord[i]:
#             # add this char to the answer
#             pref += minWord[i]
#         else:
#             # if not, break
#             break
#         i += 1
#
#     return pref
#
#
# print(longestCommonPrefix(["dorafdfd", "ghfgg", "dod"]))


## a net 400x400
# from turtle import *
# setup(400, 400)
# speed(0)
# pu()
# x, y = -200, 200
# for column in range(4):
#     pu()
#     goto(x, y)
#     pd()
#     for row in range(4):
#         for side in range(4):
#             fd(100)
#             rt(90)
#         pu()
#         fd(100)
#         pd()
#     y -= 100
# pu()
# home()
# done()

# file = open("coors.txt", "w+")
# file.write("asdasd")
# file.seek(0)
# print(file.read())
# file.close()


# import turtle
# def start():
#     x1, y1 = round(turtle.xcor(),2), round(turtle.ycor(),2)
#     turtle.write(f"{x1} {y1}")
#     file.write(f"{x1} {y1} ")
# def final():
#     x1, y1 = round(turtle.xcor(), 2), round(turtle.ycor(), 2)
#     turtle.write(f"{x1} {y1}")
#     file.write(f"{x1} {y1}\n")
# file = open("cord.txt", "w+")
# for i in range(5):
#
#     start()
#     turtle.forward(100)
#     final()
#
#     start()
#     turtle.back(100)
#     final()
#
#     turtle.right(90)
#     start()
#     turtle.forward(35)
#     final()
#
#     turtle.left(90)
# file.seek(0)
## lst = [line.split() for line in file.readlines()]
## print(sum([((float(line[2]) - float(line[0]))**2 + (float(line[3]) - float(line[1]))**2)**0.5 for line in lst]))
# lst = []
# for line in file.readlines():
#     line = line.split()
#     res = ((float(line[2]) - float(line[0]))**2 + (float(line[3]) - float(line[1]))**2)**0.5
#     lst.append(res)
# print(sum(lst))


## https://leetcode.com/problems/add-two-numbers/description/
# l1 = [2,4,3]
# l2 = [5,6,4]
# l1 = [str(elem) for elem in reversed(l1)]
# num = int(''.join(l1))
# l2 = [str(elem) for elem in reversed(l2)]
# num2 = int(''.join(l2))
# l3 = list(map(int, list(str(num + num2))))
# print(l3)


## https://leetcode.com/problems/two-sum/
# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]


# print(twoSum([2, 7, 11, 15], 9))


# def twoSum(nums, target):
#     for i in nums:
#         nums1 = nums.copy()
#         nums.remove(i)
#         for j in nums:
#             if i + j == target:
#                 l = [nums1.index(i)]
#                 nums1.remove(i)
#                 l.append(nums1.index(j) + 1)
#                 return l


# print(twoSum([2, 7, 11, 15], 9))


# from horology import Timing
# for z in range(10000):
#     with Timing(name="time: "):
#         twoSum([2, 7, 11, 15], 9)

# https://leetcode.com/problems/palindrome-number/
# from horology import Timing
# from time import sleep


# def isPalindrome(x):
#     if x >= 0:
#         rev = 0
#         temp = x
#         while temp != 0:        # temp = 123    temp = 12   temp = 1
#             rev *= 10           # rev  = 0      rev  = 30   rev = 320
#             rev += temp % 10    # rev  = 3      rev  = 32   rev = 321
#             temp = temp // 10   # temp = 12     temp = 1    temp = 0
#         if x == rev:
#             return True
#     return False

# def isPalindrome(x):
#     x = str(x)
#     return x == x[::-1]


# with Timing(name="time: "):
#     print(isPalindrome("asddsa"))

# for _ in range(10):
#     with Timing(name='time: '):
#         # sleep(0.0001)
#         for z in range(19000, 20000):
#             isPalindrome(z)

# x = 2
# if x == 2:
#     print(True)
# print(x == 2)
# # 2 + 2  = 4
# # 2 == 2 = True # 2 == 3 = False
# # > < == != >=_<=
# # + - * / % //
#
# print(bool(0))  # 100010101011010

# print(3 == 2)
# def foo():
#     if 3 == 2:
#         return True
#     else:
#         return False
#
# def foo():
#     return 3 == 2
# print(foo())

# https://leetcode.com/problems/palindrome-number/
# from horology import Timing
#
#
# def isPalindrome(x):
#     x = str(x)
#     return x == x[::-1]
#
#
# with Timing(name='time: '):
#     for z in range(100, 200):
#         isPalindrome(z)

## https://leetcode.com/problems/roman-to-integer/
# from horology import Timing
# def romanToInt(s):
#     let = {
#         "I": 1,
#         "V": 5,
#         "X": 10,
#         "L": 50,
#         "C": 100,
#         "D": 500,
#         "M": 1000
#     }
#     s = list(s)
#     for i in range(len(s)):
#         s[i] = let[s[i]]
#     for i in range(len(s) - 1):
#         if s[i] < s[i + 1]:
#             s[i] *= -1
#     return sum(s)
#
#
# romanToInt("MXIV")
#
# for z in range(10):
#     with Timing(name="time: "):
#         romanToInt("III")
#         romanToInt("LVIII")
#         romanToInt("MCMXCIV")
#
# # faster romanToInt
# def romanToInt(s):
#     d = {"C": 100,
#          "D": 500,
#          "M": 1000,
#          'L': 50,
#          'X': 10,
#          'V': 5,
#          'I': 1,
#          }
#     result = 0
#     value = 0
#     for i in range(len(s) - 1, -1, -1):
#         curr_value = d[s[i]]
#         if curr_value < value:
#             result -= curr_value
#         else:
#             result += curr_value
#         value = curr_value
#     return result
#
# romanToInt("MXIV")
#
# for z in range(10):
#     with Timing(name="time: "):
#         romanToInt("III")
#         romanToInt("LVIII")
#         romanToInt("MCMXCIV")
# from random import shuffle
# from horology import Timing

# def isSorted(lst):
#     while True:
#         for ind in range(len(lst)-1):
#             if lst[ind] < lst[ind+1]:
#                 return False
#         return True


# lst = [3, 4, 1, 6, 9, 10, 2, 0, 5]
# print("bagRand")
# for z in range(10):
#     shuffle(lst)
#     with Timing(name="time: "):
#         while not isSorted(lst):
#             shuffle(lst)


# def bubbleSort(arr):
#     n = len(arr)
#     swapped = False
#     for i in range(n - 1):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 swapped = True
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#         if not swapped:
#             return
#
# print("bubble")
# for z in range(10):
#     shuffle(lst)
#     with Timing(name="time: "):
#         bubbleSort(lst)

################
#### FILES #####
################
# print(file.read(2))
# file.seek(0)
# print(file.read(5))
# print(file.read(6))
# counter = 0
# for line in [line.strip() for line in file.readlines()]:
#     for elem in line:
#         print(f"{elem} is upper: {elem.isupper()}")


# f = open("123.txt", "w+")
# for x in range(10):
#     # print(x, file=f)
#     f.write(f"{str(x)}\n")
# f.seek(0)
# # print(f.read())
# # f.seek(0)
# # print(len(f.readlines()))
#
# lens = 0
# for line in f.readlines():
#     lens = len(line.strip())
#     print(f"len of line:{len(line.strip())} len of all:{lens}")
#     lens += lens
#     lens *= 100000
# # print(f.read())


# def func(lst):
#     if len(lst) == 1:
#         return lst[0]
#     s = ""
#
#     nums =
#     i = 0
#     for num in nums:
#         if [lst[elem][i] for elem in lst]
#             s += lst[0][i]
#             i += 1

# for elem in range(1, len(lst)):
#     for letter in range(len(lst[0])):
#         if lst[0][letter] == lst[elem][letter]:
#             s += lst[0][letter]
#         else:
#             return s


# lst = ["abcasdas", "ab", "abjfgasdasd", "abhgasdasd"]
# def f(lst):
#     i = 0
#     letters = []
#     s = ""
#     for i in range(len(min(lst))):
#         letters = []
#         for elem in lst:
#             letters.append(elem[i])
#         if len(set(letters)) == 1:
#             s += letters[0]
#         else:
#             return s
#     print(s)
#     for i in range(len(lst)):
#         print([lst[elem][i] for elem in lst])
#
# print(f(lst))

# print(func(lst))


## https://leetcode.com/problems/longest-common-prefix/
# def func(lst):
#     s = ""
#     i = 0
#     if lst[0] == "":
#         return ""
#     try:
#         while True:
#             lets = []
#             for elem in lst:
#                 lets.append(elem[i])
#             print(lst)
#             print(lets)
#             if len(set(lets)) == 1:
#                 s += lets[0]
#             else:
#                 return s
#             print(s)
#             i += 1
#     except:
#         return s
#
# print(func(["ab"]))


# import tkinter as tk
# import time
#
# class ClockApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#
#         self.title("Minimalistic Clock")
#
#         self.label = tk.Label(self, font=('Helvetica', 48))
#         self.label.pack(padx=20, pady=20)
#
#         self.update_clock()
#
#     def update_clock(self):
#         now = time.strftime('%H:%M')
#         self.label.configure(text=now)
#         self.after(1000, self.update_clock)
#
# if __name__ == '__main__':
#     app = ClockApp()
#     app.mainloop()




# # вияснення простих комбінацій. list робимо через count
# list = [0, 0, 0, 0, 0, 5]
# elem = max(list)
# # list = [str(e) for e in list]
# # print(''.join(list).rfind(str(elem)))
# index = -1
# for e in range(len(list)-1, -1, -1):
#     if list[e] == elem:
#         index = e
#         break
#
# index += 1
# print(f"ur highest streak is {index}. Ur score is {index * elem}")

# print(sum([n ** 3 for n in range(1, 1 + int(input()))]))

# print([int(num) for num in '1234'])

# def merge(list1, list2):
#     return sorted(list1 + list2)
#
#
# print(merge([4, 2, 1], [2, 6, 7]))


# from horology import Timing
#
# def first():
#         return [num for num in range(100, 1000) if str(num) == str(num**2)[-3:]]
#
# def second():
#     lst = []
#     for a in range(100, 1000):
#         if str(a**2)[-3:] == str(a):
#             lst.append(a)
#     return lst
#
# for x in range(10):
#     with Timing(unit="ms"):
#         first()
#     print("")
#     with Timing(unit="ms"):
#         second()
#
#     print("\n")

# a = 1
# b = 100000
# print(sum([x for x in range(a,b) if x % 4 == 0]))


# from tkinter import *
#
#
# window = Tk()
# window.title("┐(￣ヘ￣)┌")
# window.geometry("350x250+400+500")
#
# def winter():
#     season['text'] = "december\njanuary\nfebruary"
#     # lbl.config(text="chereshen`ka")
#
# def summer():
#     season['text'] = "june\njuly\naugust"
#
# import re
#
# regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
#
# def isValid(email):
#     if re.fullmatch(regex, email):
#       print("Valid email")
#     else:
#       print("Invalid email")
#
# lbl = Label(text="...@domain.us", font="Arial 22")  # можна змінити
# lbl1 = Label(text="^--^", font="Arial 22")  # кінцевий текст
# isValid(lbl['text'])
# log_ent = Entry(font="Arial 22")
#
# btn = Button(text="summer",
#              font=("comic sans", 16, "bold"), bg="green", fg="red",
#              command=summer)
# btn1 = Button(text="winter",
#               font=("arial", 16, "bold"), bg="green", fg="red",
#               command=winter)
#
# season = Label(text="", font=("comic sans", 16, "bold"))
#
#
# lbl.pack()
# lbl1.pack()
# log_ent.pack()
# btn.pack()
# btn1.pack()
# season.place(x=180, y=10, width=150, height=200)
#
#
# mainloop()


# from horology import Timing
# import random
#
# def bogo_sort(arr):
#     while not is_sorted(arr):
#         random.shuffle(arr)
#     return arr
#
# def is_sorted(arr):
#     for i in range(1, len(arr)):
#         if arr[i] < arr[i-1]:
#             return False
#     return True
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n-1):
#         for j in range(n-1-i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
# def python_sort(arr):
#     return sorted(arr)
#
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[0]
#         less = [x for x in arr[1:] if x <= pivot]
#         greater = [x for x in arr[1:] if x > pivot]
#         return quick_sort(less) + [pivot] + quick_sort(greater)
#
# def for_T(func, lst):
#     for c in range(3):
#         with Timing(unit="ms"):
#             func(lst)
#
# lst = [1,31,43,12,7]
# for x in range(5):
#     lst *= 2
#     print(f"len: {len(lst)}")
#     print("\nquick")
#     for_T(quick_sort, lst)
#     print("\nbubble")
#     for_T(bubble_sort, lst)
#     print("\npython")
#     for_T(python_sort, lst)
#     print("\nbogo")
#     for_T(bogo_sort, lst)
#     print()


# # запишіть в новий файл рядки з abc.txt без повторів кодів (обмеж. 0.6 ms)
# from horology import Timing
# for x in range(8):
#     with Timing(unit="ms"):
#         file = open("abc.txt", "r")
#         lst = [line.strip() for line in file.readlines()]
#         file.close()
#         file = open('123.txt', "w")
#         for elem in set(lst):
#             file.write(f'{elem}\n')


# from tkinter import *
#
# window = Tk()
# window.title("┐(￣ヘ￣)┌")
# window.geometry("700x600+400+500")
#
#
# def first(event):
#     lbl1['text'] = "той що не піддається розумінню"
#
#
# lbl = Label(text="Ununderstandable", font="Arial 22", bg="#000F7F")  # можна змінити
# lbl1 = Label(text="", font="Arial 22", bg="#678000")  # можна змінити
#
# # log_ent = Entry(font="Arial 22")
#
# # btn = Button(text="summer",
# #              font=("comic sans", 16, "bold"), bg="green", fg="red")
# # btn1 = Button(text="winter",
# #               font=("arial", 16, "bold"), bg="green", fg="red")
#
#
# lbl.pack()
# lbl1.pack()
#
# lbl.bind('<Double-Button-1>', first)
#
# # log_ent.get()
#
#
# mainloop()



