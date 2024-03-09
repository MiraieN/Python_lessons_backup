# int: 1
# float: 1.2
# string: 'asd'
# this-numm this_num, thisNum
# if, bool

# zagadka = "Що ходить вранці на чотирьох, вдень на двох, а ввечері на трьох ногах?"
# print(zagadka)
# ans = input()
# while ans != "людина":
#     print("Невірно. Спробуй ще раз!")
#     print(zagadka)
#     ans = input()
# print("вірно!")


# a = "тАк"
# if a.lower() == "так":
#     print(True)
# a.swapcase()


# from turtle import *
# shape("turtle")
# width(2)
# for z in ["red", "green", "blue", "purple", "black"]:
#     color(z)
#     fd(100)
#     lt(360/5)
# exitonclick()

# # String - str - рядок (текстовий)
# hello = "Hello"
#
# # Integer - int - число (числовий)
# num = 10000

# Operations - операції - "+ - * /"
# print(2+2)
# print(1-2)
# print(2/1.5)
# print(2*2)
# print("Hello, " + "world")
# print("Hello " * 2)
# print("I am " + str(22))

# з черепашки додати все
# from turtle import *
# forward(200)
# color("red")
# exitonclick()

# # програма для додавання чисел
# print("Привіт. Ця програма знайде суму чисел а і б")
# print("введи а")
# a = int(input())
# print("введи б")
# b = int(input())
# print("Їх сума:")
# print(a + b)

# # привітання з користувачем
# print("Привіт. Як тебе звати?")
# user_name = input()
# print("Hello " + user_name)

# op = '/'
# if op == "+":
#     print(1+2)
# elif op == "-":
#     print(1-2)
# elif op == "/":
#     print(1/2)
# elif op == "*":
#     print(1*2)

# from math import factorial
# print(factorial(3)) # 1 * 2 * 3
# print(factorial(10)) # 1 * 2 * 3 * ... * 8 * 9 * 10
# print(factorial(100000))

# ** # 2 ** 4 = 2 * 2 * 2 * 2
# % # 5 % 3 = 2
# // # 5 // 4 = 1

# 5! = 1*2*3*4*5
# user_num = ""
# while isinstance(user_num, str):
#     try:
#         user_num = int(input())
#     except:
#         print("type num")
# print("thanks for num")

# a = 0
# while a > -1:
#     print(a)
#     a = a + 1
#     if a == 10:
#         break


# zagadka = "Що ходить вранці на чотирьох, вдень на двох, а ввечері на трьох ногах?"
# print(zagadka)
# ans = input()
# while ans != "людина":
#     print("Невірно. Спробуй ще раз!")
#     print(zagadka)
#     ans = input()
# print("вірно!")

# txt = "I love apples apples are. my favorite fruit"
#
# print(txt.count('a', 0, txt.find('.')))
# # print()
# email = 'vladbondar493@gmail.com'
# ukr = 'vladbondar@ukr.net'
# k = "asdasd@ukr.net"
# txt = "apple"
# txt_1 = txt[0:3]
# print(txt_1)


# txt = "hello"
# print(txt.find('l'))
# print(txt[3])
# num_hello = txt.count("hello")
# if num_hello:
#     print("я знайшов hello")
# if "hello" in txt:
#     print("я знайшов hello")

# x, y = 1, 2
# print(f"x:{x}\ny:{y}")
# x, y = y, x
# print(f"\nx:{x}\ny:{y}")

# indexing (slicing) (tasks)
# words/characters/special letters amount in text

# txt = "I have a garden with apples. It is great"
# num = txt.find('g')
# num1 = txt.find(" ", num)
# txt_1 = txt[num1:]
# print(txt_1)

# for z in range(3):
#     num = txt.find('g')
#     num1 = txt.find(" ", num)
#     txt_1 = txt[num:num1]
#     print(txt_1)
# txt_1 = txt[num:]

# txt = "hello I am here "
# a = txt.rfind("h")
# s = txt.find(" ", a)
# print(txt[a:s])

# mail = 'vladbonda493@gmail.com'
# mail[]
#
# domen_name = 'gmail.com'

# for, while


# lst = ["asd@asd", "qwe@qwe", "rty@rty"]
# for elem in lst:
#     print(elem)

# txt = 'Hello I am Brian'
# txt[0] # indexing
# txt[0:4]   # slicing
# print(txt[0:4])
# print(txt[-2]) # negative indexing
# print(txt[::2]) # step

# # 1. delete @
# email = 'vl@d.bondar@gmail.com'
# sob = email.rfind("@")
# dot = email.rfind(".")
# print(email[sob:dot])
# email = 'vl@d.@ukr.net'
# sob = email.rfind("@")
# dot = email.rfind(".")
# print(email[sob:dot])
# # 2. https://www.w3schools.com/python/python_variables_exercises.asp
# # 3. for z in txt:   what is z?

# lst = ['asdasd@gmail.com', 'qweasdas@ukr.net', 'zxcasd@gmail.com']
# users = []
# domens = []
# for z in lst:
#     print(z[:z.rfind("@")])

# module random guess the number (повторити while, 2..10, if, %, from i to j)

# boolean
# if 4 > 2:
#     print("interesting")
# elif 4 == 4:
#     print(True)
# else:
#     print(False)

# ques = input('How much\n')
# while ques != "10":
#     print("Wrong pick! Try again")
#     ques = input('How much\n')
# print("Correct!")


from random import randint
import random

# for _ in range(10):
#     print(randint(0, 1))

# num = input("1:?")
# try:
#     num = int(num)
# except ValueError:
#     print("Ти написав не число. Пиши число")


# print(random.randint(0, 1000))
# z = 0
# while z < 10:                   # iterator, iterations
#     z += 1
#     if z in (2, 4, 8, 10):
#         continue
#     print(z)

# for z in range(1, 13, 2):    # для z в діапазоні від 1 до 13 з кроком 2    # range - діапазон
#     print(z)
#
# for letter in "Hello":
#     print(letter)
#
# for color in ['red', 'green']:
#     print(color)

# ques = input('How much\n')
# while ques != "10":
#     print("Wrong pick! Try again")
#     ques = input('How much\n')
# print("Correct!")


# print("Hello, I am")
# name = input("you are?")
# print("rules")
# ans = ''
# # TypeError (check int and str)
# while ans != "Bye":
#     print('''
#     I can:
#              1) словник з діапазоном (пиши "словник" або "1")
#              2)
#              3)
#              4)
#                     ''')
#     ans = input("What u want?").lower()
#     if ans in ('1', 'словник'):
#         from math import sqrt
#         while True:
#             try:
#                 X = int(input("від?"))
#                 Y = int(input('до?'))
#                 break
#             except ValueError:
#                 print(False)
#         print({z: sqrt(z) for z in range(X, Y+1)})
#     elif ans == '2':
#         import turtle
#         turtle.fd(100)
#         turtle.exitonclick()
#
#         # pass            # дозволити
#     #...
#     elif ans == '3':
#         # ques = input('How much\n')
#         # while ques != "10":
#         #     print("Wrong pick! Try again")
#         #     ques = input('How much\n')
#         # print("Correct!")
#     else:
#         print("Невірно. Спробуй ще раз")


# while, for
# складаємо бота

# txt = ["h", "e", "l", "l", "o"]
# txt = "hello"
# txt[2] = 3
# print(txt)
# list()
# txt = list(txt)

# Indexing
# print(txt[2])
# print(txt[2:4])
# print(txt[1::3])
# print(txt[::-1])


# особливості списків


# methods(functions)
# len, pop, remove, index
# txt.pop()

# lst = [1, 2, 3, 4, True]
# lst.append(6)  # додає в кінець списку
# lst.insert(3, True)  # додає в конкретну позицію
# lst_extend = [True, True, True, False]
# lst.extend(lst_extend)  # з'єднує списки
# lst = lst + lst_extend
# print(lst)
# lst.clear()           # очищає список
# print(f"lst.pop видалило {lst.pop(2)}")     # видаляє елемент по індексу
# lst.remove(3)         # забирала вказаний елемент
# lst.reverse()         # перевертає список
#
# for elem in [0, 1, 2, 3, 4, 5]:
#     print(elem)
#
# print(lst[len(lst) - 1])


# func(list)    # список не змінюється
# list.func()   # список змінюється
# nums = [0, 9, 8, 7, 6]
# nums = nums[::-1]
# for num in nums:
#     lst.insert(3, num)
# print(lst)
# lst.sort(reverse=False)
#
# txt = ["h", "e", "l", "l", "o"]
# txt.sort()
# print(txt)

# word = "Hello"
# for letter in word:
#     if letter == "H":

# for num in numbers

# list, list slice, list methods, len, count, in, for

# word = "Good morning people"
# if 'people' in word:
#     print("people in word")

# lst = [1, 2, 3, 4, True]
#
# if '1' in lst:
#     print('1')

# lst = [6, 3, 8, 0, 7, 1]
# for z in range(5):
#     elem = input("?\n")
#     lst.append(elem)
# print(lst)

# for i in range(len(lst)):
#     if lst[i] > lst[i-1]:
#         print(lst[i], lst[i-1])

# for, for in list, in lst and range(len(lst)), if in,

# lst = [555, -99, 7, 88]
# for elem in lst:
#     if len(str(elem)) == 2 and elem > 0:
#         print(elem)
# for elem in lst:
#     if elem == 5:
#         continue
#     print(elem)
# for ind in range(len(lst)-1):
#     if lst[ind] > lst[ind+1]:
#         print("не зростає")
#         break
# else:
#     print("зростає")
# num = 33
# print(len(str(num)))


# # games in list bot
# import time
# lst = ['brawl stars', 'standoff 2']
# print('Привіт! Я бот який колекціонує назви ігор і мені потрібна допомога. Я вже знаю такі ігри як Brawl stars and Standoff 2. Введи ті, які знаєш ти')
# time.sleep(2)
# print('Якщо захочеш подивитися мою колекцію то введи lst')
# time.sleep(2)
# print('Якщо захочеш вийти чи закінчити діалог зі мною напиши "exit"')
# time.sleep(1)
# user_action = input('Приймаю дані:\n').lower()
# while user_action != 'exit':
#     if user_action in lst:
#         print('В мене вже є така гра в колекції')
#     elif user_action == 'lst':
#         print(lst)
#     elif user_action not in lst:
#         lst.append(user_action)
#         for z in (3, 2, 1):
#             print(f"{z}", end='')
#             for dot in range(3):
#                 time.sleep(0.3)
#                 print(".", end='')
#             time.sleep(0.7)
#             print()
#         print('Записано!')
#     time.sleep(0.5)
#     user_action = input('Приймаю дані:\n').lower()
# time.sleep(0.7)
# print(f"Роботу завершено. Кінцевий список: \n{lst}")



# # list generators
# default = [2, 555, 6, -7, 90, 88]
# lst = [elem for elem in default if len(str(elem)) == 2 and elem > 0]
# lst = [default[ind] for ind in range(len(default))]
#
# print([z for z in range(10)])
# print([lst[z] for z in range(len(lst))])
#
# lst = []
# for ind in range(len(default)-1):
#     if default[ind] == default[ind+1]:
#         lst.append(default[ind])
#
# print(lst)
#
# num = int(input())
# if num % 2 == 0 and num != 0:
#     print("parne")

# from time import sleep
#
# sleep(1)
# lst = [z for z in range(10)]
# print(lst)
# print([lst[z] for z in range(1, len(lst)-1)])
# range(len(lst)-1)   lst[i] > lst[i+1]
# range(1, len(lst))  lst[i] > lst[i-1]


# string = "100f"
# print(string[0:-1])
# print(string[-1])

# The temperature in Celsius is 40 degrees.


# imb for in list(tasks in course)


# запитати юзера номер телефону. Кожна цифра - окремий елемент в списку

# new import
# задача з шансом рандому 1/0,

# lst = [z for z in range(10)]
# print(lst)
# lst.clear()
# print(lst)


# lst = ['1', '2', '3', '4', '6']
# lst[0] = int(lst[0])
# for z in range(len(lst)):
#     lst[z] = int(lst[z])
# print(lst)

# txt = input()
# lst_txt = txt.split(" ")
# lst_txt = list(map(int, lst_txt))
# print(lst_txt)
#
# lst = [int(input()) for z in range(int(input("range")))]


# find, [], статистика почт


# user_action = None
# lst = ['Brawl stars, Standoff 2']
# print('Я бот який коликціонує назви ігор допоможи мені будь ласка! Я вже знаю такі ігри як Brawl stars and Standoff 2')
# print('Якщо захочеш подивитися мою колекцію то введи lst')
# print('Якщо захочеш вийти чи заінчити діалог зі мною напиши "exit"')
# while user_action != 'exit':
#     user_action = input('Вводь сюди:\n').lower
#     if user_action in lst:
#         print('Вибач, але в мене вже є така гра в колекції')
#     elif user_action == 'lst':
#         print(lst)
#     elif user_action not in lst:
#         lst.append(user_action)
#         print('Дякую!')

# for z in range(int(input("vid?")), 100):
#     if z % 2 == 0:
#         for x in range(z, 100, 2):
#             print(x, "parne")
#             print(x+1, "neparne")
#         break


# mails = ['Qw.e@ukr.net', 'asdasd@mail.ru', 'asdasd@gmail.com']
# mails.sort()

# for z in mails:
#     sobch = z.find('@')
#     dot = z.rfind('.')
#     domen = z[sobch+1:dot]
#     print(domen)

# num = [1, 2, 1, 4, 5, 4]
# for z in set(num):
#     print(z)
# print(num)

# thisset = {"apple", "banana", "cherry", "apple"}
#
# print(thisset)

import random as rd

# students = ['Mayakovskiy', 'Bairon', 'Shekspier', 'Ya']
# vars = [z for z in range(1, len(students) + 1)]
# print(vars)
#
# print(vars[rd.randint(0, len(vars))])
# vars.pop(rd.randint(0, len(vars)-1))
# print(vars)

# nums = [1, 2, 3, 4, 5]
# for z in range(len(nums)):
#     print(z)
# for num in nums:
#     print(num)

# for color in (3,6,7):
#     print(color)

# nums = [z for z in range(1, len(students)+1)]
# for student in students:
#     ind = rd.randint(1, len(nums)) - 1
#     print(f"{student} - {nums[ind]+1}")
#     nums.pop(ind)

# print(f"{student} - {nums.pop(ind) + 1}")
# nums = [z for z in range(1, len(students)+1)]
# import random as rd
# rd.shuffle(nums)
# print(nums)
# print(students)
# for
#     print(nums)

# 1 генерувати число і додавати в список. Якщо воно вже є в списку - генеруй нове
# 2 генерувати список з числами. Виводити елемент з рандомним індексом і видаляти його (праву межу задавати динамічно через довжину списку)
# 3 перемішати список з числами

# func
# іменована частина коду

# # outer scope
# def this_func(num, num2):   # отримує 2 аргументи      # g = x = 45
#     return num * num2       # повертає значення
#
#
# second_x_third_user = 45
# y = 5
# print(this_func(second_x_third_user, y))


## global (outer scope)
# x = 5
#
# def func():
#     global x
#     x += 1
#
# func()
# print(x)

# def func(n,n2,op):
#     return n + n2
# x = int(input())
# func(x, 4, 6)


# d = "a*hj?"
#
# print(list(d))

# a = list()
#
# print(a)

# a = input("Enter any String")
#
# print(list(a))

# list1 = "Practice QuesTions of List in pythoN"
# list2 = list(list1)
#
# print(list2[0])
# print(list2[9])
# print(list2[-14])
# print(list2[-1])
# print(list2[13])
# print(list2[-14:-10])
# P
# Q
# L
# N
# T

# b = ['p', 'r', 'a', 'c', 't', 'i', 'c', 'e']
# for i in b:
#     print(i, end="\n")

# Q2. Write a program to print all the elements of given list using for loop.

# A = ['a', 'b', 'c', 'd', 'e']
# for z in A:
#     print(z)

# print([1,2,3,4] == [4,3,2,1])
# print([1, 2, 3, 4] > [4])
# print([1,2,3,4] != [1,2,3,4])
# print([1, 2, 3, 4] == [1, 2, [3, 4]])
# print([1, 2, 3] == [1.0, 2.0, 3.0])

# a = [1,2,3,4]
# b = [5,6,7,8]
#
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

# b = "PracticeQuestionsofList in Python"
# a = list(b)

# print(a)
#
# print(len(a))

# print(a[1:4])
#
# print(a[1:7])
#
# print(a[3:])
#
# print(a[:5])
#
# print(a[4:17])
#
# print(a[-2:-5:-1])

# a = [1, 2, 3, 4]
#
# a.append([7, 8])
#
# print(a)

# Q3. Write a program to find the largest number from the following list.(without using inbuilt function)

# A = [23, 12, 45, 67, 55]
# print(max(A))

# a = [1, 2, 3, 4]
# a.sort()
# print(sorted(a))
# # a.reverse()
# # print(a)
# print(list(reversed(a)))
# print(reversed(a))
# print(a)
# print(list(range(10)))
# for z in reversed(a):
#     print(z, end=' ')

# r = int(input("Raws?"))
# n = int(input("number?"))
# for i in range(1, r+1):
#     for j in range(n):
#         print("*", end=" ")
#     print(end="\n")
# *
# * *
# * * *
# * * * *

# a = [1, 5, 7, 5, 66, 5, 5, 5, 5]
# while 5 in a:
#     a.pop(a.index(5))
#     # a.remove(5)
# print(a)
# print(b)

# a = [1, 2, 3, 4]
# a[1] = 'a'
# print(a)
# print(sorted(a, reverse=True))

# l = [[1, 2, 3],
#      [3, 4, 5],
#      [5, 6, 7],
#      ]
#
# for i in l:
#     for j in i:
#         print(j, end=' ')
#     print()


# score = [[345, 567, 790, 234],
#          [456, 800, 234]]

# print(score[0][1])
# print(max(score[1]))
# num = 120
# print(max(list(str(num))))
# print(list(str(num)))

# print(score[0].count(345))
# score[0].remove(345)

# a = score[1].pop(0)
# print(score)
#
# del score[1][0]
# print(score)

# import math
#
# def nums_gcd(num1, num2):
#     return math.gcd(num1, num2)
#
# print(nums_gcd(max(score[0]), max(score[1])))

# def real_year(day, month, year):
#     if (-10000 > year or 10000 < year) or (year - int(year) != 0):
#         return f"year {year} is not valid"
#     if 1 > month or 12 < month:
#         return f"month {month} is not valid"
#     if month in (1, 3, 5):
#         if day not in range(1, 32):
#             return f"day {day} is not valid"
#     if month in (4, 6, 8):
#         if day not in range(1, 31):
#             return f"day {day} is not valid"
#
#
# print(real_year(32, 3, 1992))

# l = [15, 43, 6, 78, 345]
# Q6. Name a function/statement which can delete more than one element from the list.
# del l[1:3]
# print(l)
#
# Q7. Name a function which can delete only one element from the list.

#
# Q8. Write a function to delete/remove all the negative elements from the list.
# def list_neg_remove(lst):
#
#     return lst
# lst = [15, -43, 6, -78, -345]
# print(list_neg_remove(lst))
# '[15,6]'

# import turtle
# x = turtle.Turtle()
# y = turtle.Turtle()
# for z in range(1000):
#     x.forward(10)
#     x.left(10)
#     y.fd(5)
#     y.left(5)
# turtle.done()       # затримує закриття вікна
# from turtle import *
# forward(200)
# done()


# Q9. Write a function to delete/remove all the odd numbers from the list.
#
# Q10. Write a program to delete/remove all the numbers less than 10 from the list.

# https://habr.com/ru/company/timeweb/blog/579080/
# 27. Функция для транспонирования матрицы
# 28. Функция для определения того, является ли строка палиндромом
# 29. Функция для удаления лишних символов из строки
# 30. Функция для сортировки слов в алфавитном порядке
# 11. Write a Python function to check whether a number is perfect or not. Go to the editor
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

# def assign in (=)
# args

# lambda
# https://www.w3resource.com/python-exercises/lambda/index.php

# sort
# https://holypython.com/intermediate-python-exercises/exercise-15-python-sorted-function/

# map
# https://www.w3resource.com/python-exercises/map/index.php

# math funcs:
# https://www.w3schools.com/PYTHON/module_math.asp
# https://pythonist.ru/test-math-v-python/

# rsp game
# dicts
# mails with dict
# kwargs


# https://gist.github.com/jigi-33/209ad40c6f9be2f8b9775d28cbc40672
# https://habr.com/ru/company/timeweb/blog/579080/
# turtle визначити координати найдовше проїхавшої черепашки
