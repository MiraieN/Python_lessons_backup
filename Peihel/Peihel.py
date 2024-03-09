# ctrl + ?: #
# num = 5  # int Integer
# txt = "some random text"      # str String
# electricity_per_month = 24.5
# electricityPerMonth = 12.5

# that-val = 5                # NameError
# that val
# 1val

# print(1, 2, 3)                # IndentationError

# operators
# =
# num = 5

# +               # sum
# print("a"+"b")  # str + str

# -               # sub - subtraction
# print(10-5)

# *               # mult - multiplying
# print(10*5)
# print("_asd_" * 5)

# /               # div - division
# print(10 / 4)   # float

# **              # 2 in the power of 4
# print(2**4)

# //              # div (ціла частина від ділення)

# %               # mod

# +=, -=, /=, *=
# num = 5
# num *= 10


# # type casting      #  зміна типу
# int(), str()
# x = 2
# y = "O"
# y = int(y)
# print(x + y)
# print(type(y))


# # ValueError - помилка значення
# x = int(input("Input num1\n"))
# y = int(input("Input num2\n"))

# IndentationError
#                  num = 5

# print(f"")
# print(x, '-', y, '=', x-y)
# print(f"{x} - {y} = {x - y}")

# str()
# num = 5
# num = str(num)
# print(num + 'a')
# txt = 'a'
# print(5, 2, 3, 4)

# reduntant
# age = input("ur age?")
# print("ur age is", age)

# # # boolean bool True False     - логічний тип
# num1 = int(input("num1"))
# if num1 > 5:
#     print("Bigger than 5")
# elif num1 < 5:
#     print("Less than 5")
# else:
#     print("This is 5")

# num1 = int(input("num1"))
# if num1 > 5:
#     print("Bigger than 5")
# elif num1 < 5:
#     print("Less than 5")
# elif num1 % 2 == 0:
#     print("parne")
# print("\n\n\n")
# if num1 > 5:
#     print("Bigger than 5")
# if num1 > 5:
#     print("Bigger than 5")

# # > < >= <= == !=(! =) and or
# num1 = int(input("num1"))
# if num1 <= 5:
#     print("Less or equal 5")
# if num1 == 5:
#     print("Is 5")
# if num1 != 5:
#     print("This is not 5")

# # or
# txt = input("Input smth:\n")
# if txt == "Hello" or txt == "Hi":
#     print("Hello you too")

# # and
# num1 = int(input("num1"))
# if num1 < 5 and num1 > 0:
#     print("is between 0 and 5 (0..5)")

# # перевірити чи парне число
# if num1 % 2 == 0:
#     print("parne")
# elif num1 % 2 == 1:
#     print("neparne")

# num = int(input("Введи число\n"))
# if num == 0:
#     print(0)
# elif num % 2 == 0:
#     print("parne")
# elif num % 2 == 1:
#     print("neparne")


# sc = 0
# ans = input("понеділок на англ\n").lower()
#
# if ans == "monday":
#     print("True")
#     sc += 1
# else:
#     print("False")

# ans = input()
# if ans == "1":
#     print(True)
# elif ans == '2':
#     print(True)

# degree = input("Input the  temperature you like to convert? (e.g., 45, 102 etc.) : ")
# i_convention = input("F, C")

# if i_convention.upper() == "C":
#   result = int(round((9 * degree) / 5 + 32))
#   o_convention = "Fahrenheit"
# elif i_convention.upper() == "F":
#   result = int(round((degree - 32) * 5 / 9))
#   o_convention = "Celsius"
# else:
#   print("Input proper convention.")
#   quit()
# print("The temperature in", o_convention, "is", result, "degrees.")

# # embedded if (nested)

# t = int(input("Temperature?\n"))
# if t > 20:          # 20 ...
#     if t > 35:      # 35 ...
#         print("Hot")
#     if t < 35:      # 20 ... 35
#         print("Warm")
# elif t < 20:        # ... 20
#     print("Cold")


# age = int(input("age?\n"))
# if age >= 18:
#     print("U are big boy")
#     if age >= 23:
#         print("u can drive a car")
# elif age < 18:
#     print("U are small boy")

# ans = input("1 2 3 4 5")
# if ans == "1":
#     num1 = int(input())
#     num2 = int(input())
#     if num1 > num2:
#         print(num1, "bigger")
# if ans == "2":
#
# if ans == "3":

# num1 = int(input())
# num2 = int(input())
# op = input("+ - / *")
# if op == "+":
#     print(num1 + num2)
# if op == "/":
#     if num2 == 0:
#         print("Error")
#     elif num2 != 0:
#         print(num1 / num2)

# ans = input("?\n")
# if ans == "calc":
#     num1 = int(input("num1: "))
#     num2 = int(input("num2: "))
#     op = input("+-/*")
#     if op == "+":
#         print(f"num1 + num2 = {num1 + num2}")
#         print(f"num1 / num2 = {num1 / num2}")
#     if op == "/":
#         if num2 == 0:
#             print("На нуль ділити не можна")
#         else:
#             print(f"num1 / num2 = {num1 / num2}")
# if ans == "sing a song":
#     print("...")

# itemsInStock = 32
# itemsOrdered = int(input("How many items to order?\n"))
#
# # перевірити чи достатньо на складі запасів. Якщо ні - написати про це
#
# # якщо достатньо запасів, то вивести в скільки пакунків це треба буде впакувати
# print(round(itemsOrdered / 8))
#
# # якщо треба більше одного пакунка, то виводиш про це інформацію
# print('потрібно більше 1 пакунка')

# bot start(give a skelet), implement calculator in bot

# # # hello phase
# # hello ia am bot *name*
# # what is your name?
# print("...")
# print("....")
# name = input("...")
#
# # rules
# # i can....
# while True:
#     # print (1,2,3,4,5 or calc, zag, capitals, cities.....)
#     print("1,2,3,4,5 or calc, zag, capitals, cities.....")
#     ans = input("...")
#     if ans == '1' or ans.lower() == 'calc':
#         # calculator
#         num1 = int(input("num1: "))
#         num2 = int(input("num2: "))
#         op = input("+-/*")
#         if op == "+":
#             print(f"num1 + num2 = {num1 + num2}")
#             print(f"num1 / num2 = {num1 / num2}")
#         if op == "/":
#             if num2 == 0:
#                 print("На нуль ділити не можна")
#             else:
#                 print(f"num1 / num2 = {num1 / num2}")
#
#     elif ans == '2' or ans.lower() == 'capitals':
#         # questions about capitals
#         print("...")
#         answer = input("...")
#
#     elif ans == '3' or ans.lower() == 'zag':
#         # zagadka
#         print("1,2,3,4,5")
#         a = input('1,2,3,45,')
#         if a == '1':
#             print("...")
#         answer = input("...")
#
#     elif ans == 'exit':
#         break
#
#     else:
#         print("Невірний ввід")
# # Goodbay phase
# print("...")

# txt = 'Hello'
# letter = 'o'
# if letter in txt:
#     print(f"{letter} is in {txt}")

# mail = 'username@gmail.com'
# if '@gmail.com' in mail or '.net' in mail:
#     print(mail, 'is a mail')
# else:
#     print(mail, 'is not a mail')
#
# number = input("")
# 1 kyivstar

# 2 life

# 3 vodafone

# 4 mts

# 5 unrecognizable number


# op = input()
# if op == '!':
#     print()
# elif op == '/':
#     print()
# elif op == '*':
#     print()
# elif op == '+':
#     print()
# else:
#     print()

# print('''
#     Hello
#     I can to do:
#     Type:
#             1 or calc
#             2 or zag
#             ...
# ''')

# iterator  -  Ітератор
# while
# for

# i = 0               # counter - лічильник
# while i < 5:        # голова циклу (while - ітератор)
#     print(i)        # тіло циклу
#     i += 1          # збільшення лічильника

# i = 10
# while i != 0:
#     if i == 5:
#         break
#     print(i)
#     i -= 1

# i = 10
# while i != 0:
#     i -= 1
#     if i == 5:
#         continue
#     print(i)

# ans = input("сама загадка")
# attempt = 1
# while ans != 'відповідь':
#     print("ні")
#     if attempt == 2:
#         print("1 підказка")
#     elif attempt == 4:
#         print("2 підказка")
#     elif attempt == 5:
#         print("attempts lost")
#         break
#     attempt += 1
#     ans = input("сама загадка")
# else:
#     print("правильно")

# while True:
#     print('asd')
#     break
#     print('asdagvxcvsg')

# number = input()
# if '097' in number:
#     print("Kiyvstar")

# повтор while, continue, break, else
# i, j = int(input("num1\n")), int(input("num2\n"))
# # 5, 10: 5,6,7,8,9,10
# while i <= j:
#     print(i)
#     i += 1

# i, j = int(input("num1\n")), int(input("num2\n"))
# # 5, 10: 5,6,7,8,9,10
# print("even numbers:")
# while i <= j:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# i, j, c = 2, 10, 5
# while i <= j:
#     if i == c:
#         i += 1
#         continue
#     print(i)
#     i += 1

# while syntax, if in while, while with str, output odd nums, i to j, step


# factorial

# num = int(input("num?"))
# c = 1
# s = 1
# while c <= num:
#     print(f"{s} * {c} = {s * c}")
#     s = s * c
#     c += 1
# print(f"{num}! = {s}")

# консоль - again
# %3
# квадрати чисел 1...20
# sum of numbers
# factorial


# print("прийняття чисел почато")
# ask = -1
# while ask != 0:
#     ask = int(input("num?"))
#     print("число прийнято")
# print("прийняття чисел закінчено")

# i = 1
# while i < 11:
#     print(i)
#     i += 1
#
# # перебирає заданий діапазон
# # і присвоєю z кодному значенню із діапазона
# for z in range(1, 11):     # range - діапазон  (2,5) = 2,3,4
#     print(z)

# # використовуєтсья коли ти не знаєш кількість разів виконання циклу
# a = 10
# while True:
#     print(a)
#     a += 1
#     if a == 15:
#         break

# # коли знаєш скільки разів буде виконуватися цикл
# for z in range(1, 11):
#     print(z)

# print(range(1, 15))

# zag = input("фіолетовий на англійській?")
# while zag != 'purple':
#     print("невірно, ще раз")
#     zag = input("фіолетовий на англійській?")
# print("Так!")

# for z in range(10):
#     zag = input("фіолетовий на англійській?")
#     if zag == 'purple':
#         print("так!")
#         break
#     print("невірно, ще раз")

# i = 2
# for x in range(i):
#     i += 1              # i = 5
#     print(x)            # 2

# for z in range(1, 21):
#     print("перевіряю число", z)
#     if z % 2 == 0:
#         print(f"{z} - even")

# крок
# for z in range(2, 21, 2):
#     print(z)


# i = 7
# for z in range(1, 10):
#    print(f'{i} * {z} = {i*z}')

# i = 0
# for z in range(5):
#     num = int(input("Num?"))
#     i += num            # додавати в себе числа         i = 0+1+5+5+6+4
# print(i)

# факторіал 7
# i = 1
# for z in range(1, 7):
#     i *= z            # додавати в себе числа         i = 1*1*2*3*4*5*6*7*8*9*10
# print(i)

# - step in for
# for in str


# for z in range(2, 11, 2):
#     print(z)


# mult table for (1-9)

# for j in range(1, 12):
#     for i in range(1, 20):
#         print(f"{j} * {i} = {j*i}")
#     print()


# Q4. Write a program to display sum of odd numbers and even numbers that fall between 12 and 37(including both numbers)

# print(sum([z for z in range(13,37,2)]))


# for z in range(1, 20):
#     if z % 2 != 0 and z % 3 != 0:
#         print(z)
#     if z % 11 == 0 and z % 2 != 0:


# word = input()
# print(word[0])
# print(word[1])
# print(word[2])
# if word == word[::-1]:
#     print("it is palindrome")
# else:
#     print("It isn't palindrome")
# word = input()
# print("it is palindrome" if word == word[::-1] else "It isn't palindrome")
# txt = "some random text"
# print(txt[5])
# print(txt[5:15])
# print(txt[1:15:2])
# print(txt[1:-15:-1])
# print(txt[-16])
# print(txt[0])
# txt = 'somerandommail@gmail.com'
# txt = "asdasdasds@mail.com"
# print(txt[txt.find('@')+1:txt.rfind(".")])
# print(txt[:txt.find('@')])
# txt = 'https://csiplearninghub.com/practice-questions-of-loops-in-python/'
# print(txt[txt.find("//")+2:txt.find(".com")+4])


# for z in range(5):
#     if z == 2:
#         continue
#     print(z)

# # perfect num
# for num in range(2, 1000):
#     sum = 0
#     for div in range(1, num):
#         if num % div == 0:
#             sum += div
#     if sum == num:
#         print(num)
# else:
#     print(f"{num} not")


# if True and True:      # і: перевіряє щоб і те і те було правдою
#     print(1)
# if False or True:       # або: перевіряє щоб хоч одне було правдою
#     print(1)
# if True or True:
#     print(1)

# print(True and True)    # True
# print(False and True)   # False
# print(False and False)  # False
#
# print(True or True)     # True
# print(True or False)    # True
# print(False or False)   # False

# a = True
# b = True
# c = False
# d = True
#
# # 1.
# print(c)
# # 2.
# print(d)
# # 3.         print(not a)
# # 4.
# print(not b)
# # 5.         print(not c )
# # 6.
# print(not d)
# # 7.
# print(a and b)
# # 8.
# print(a or b)
# # 9.
# print(a and c)
# # 10.
# print(a or c)
# # 11.
# print(a and d)
# # 12.       print(a or d)
# # 13.       print(b and c )
# # 14.       print(b or c )
# # 15.
# print(a and b or c)
# # 16.
# print(a or b and c)
# # 17.
# a = True
# b = True
# c = False
# d = True
# print(a and b and c)
# # 18.
# print(a or b or c)
# # 19.
# print(not (a and b and c))
# # 20.
# print(not (a or b or c))
# # 21.
# print(not (a and b and c))
# # 22.
# print(not (a or b or c))
# # 23.
# print(not (True and not (True and not False)))
# # 24.
# print(not (a or (not (b or not c))))
# # 25.
# print(not (not (a or not (b or not c))))

# True or/and False

# https://csiplearninghub.com/practice-questions-of-loops-in-python/


# # strings
#      0123456789
# txt = "Some random string"

## subscriptable  - звернення по індексу
# txt[0]
# print(txt[8])
# print(txt[-2])
# print(txt[-1])

# txt = "Some random string"

# slice          - відрізок
# print(txt[5:9])     # - права межа не включно
# print(txt[0:4])
# print(txt[:4])
# print(txt[5:])
# print(txt[:14:2])   # 0 2 4 6 8 10 12
# print(txt[5::3])
# print(txt[::5])
# print(txt[10:4:-1])
# print(txt[-3:-7:-1])
# print(txt[::-1])

# s = "Keyboard"
# l = len(s)
# print(s[l-1])       # length

# s = "Keyboard"
# c = 0
# for elem in s:
#     if elem == "k" or elem == "K":
#         c += 1
# print(f"in string '{s}' k is found {c} times")

# s = "Keyboard"
# if "o" in s:
#     print("o in s found")

# c = 0
# s = "Keyboard"
# letters = "qwrtpsdfghjklzxcvbnm"
# for elem in s:
#     if elem.lower() in letters:
#         c += 1
# print(f"'{s}' contains {c} приголосних")

## case sensitive - чутливий до регістру(великі/маленькі букви)
# print("K".lower() == "k")
# print('k123'.upper())       # робить великим
# print("Ka123".lower())      # робить маленькими
# print("ASDzxcERTdfgcvb123".swapcase())  # змінює великі на малі і навпаки
# s = "1dfg"
# numbers = '1234567890'

# s = "Abcde"
# print("starts with upper: "+s[0] if s[0].isupper() else "starts with lower: "+s[0])


# string funcs

# mails
# mail = "somerandommail@gmail.com"
#
# mail_name = mail[]
# mail_domen =
# print(f"name: {mail_name}\ndomen: {mail_domen}")
#
#
# mail = "goodmail@yahoo.com"
#
#
#
# mail = "THIS.MAIL@ukr.net"

# name = input("Your name?")
# print("Only letters pls" if not name.isalpha() else "Good name, thx")
# name_len = len(name)
# print(f"Ur name length is {name_len} elements")

# txt = "H1el2lo w3orl5d"
# number = 0
# for elem in txt:
#     if elem.isdigit():
#         number += 1
# print(f"number of digits: {number}")

# print("string" in "substring")
# print("str1ing" not in "substring")
# print("o" in "Hello")
#
# txt = "qweoiuertgspdmsifu"
# for elem in txt:
#     if elem in "eyuioa":
#         print(elem, "- це голосна")

# x = "Asd".istitle()
# print(x)
# x = "AsDf".swapcase()
# print(x)

# x = 1
# y = "asd"
# z = True
# l = [1, "asd", True]    # list(список)  # дозволяє змінювати елементи, впорядковані елементи
# t = (1, "asd", True)    # tuple(кортеж) # не дозволяє змінювати елементи але займає менше пам'яті
# s = {2, "asd", True}    # set(набір)    # не впорядковані елементи, також займає менше пам'яті
# print(l, t, s)
# from turtle import *
# colors = ["red", "green", "yellow", "purple"]
# # print(colors[0])
# for z in range(0, 4, 1):  # 0 1 2 3
#     width(z+1*10)
#     color(colors[z])
#     forward(50)
# done()
# from turtle import *
# colors = ["red", "green", "yellow", "purple"]
# for elem in colors:
#     color(elem)


# list tasks from logika, turtle tasks
# from turtle import *


# # define - визначати(описувати)
# def func_name():
#     for z in range(4):
#         fd(100)
#         lt(90)
# speed(0)


# def func_name(side, radius, color):
#     for z in range(4):
#         fd(side)
#         lt(90)
#     circle(radius)


# func_name(400, 400)
# func_name(200, 200)
# func_name(100, 100)

# from turtle import *
#
# def kvadrat(side, col, sp, wd, fc):
#     width(wd)
#     speed(sp)
#     color(col, fc)
#     begin_fill()
#     for z in range(4):
#         fd(side)
#         lt(90)
#     end_fill()
#
# kvadrat(150, "red", 2, 5, "yellow")
# kvadrat(100, "black", 2, 15, "white")
#
# done()


# from turtle import *


# def kvadrat():
#     for z in range(4):
#         fd(100)
#         rt(90)
#
#
# def triangle(x, y):
#     speed(0)
#     pu(); goto(x, y); pd()
#     for z in range(3):
#         fd(100)
#         lt(120)
#
#
# def house(x, y):
#     triangle(x, y)
#     kvadrat()
#
# house(-350, 50)
# house(-200, -50)
# house(-50, 0)
# house(100, -50)
# house(250, 0)
#
# for x, y in [[-350, 50], [-200, -50], [-50, 0], [100, -50], [250, 0]]:
#     house(x, y)
#
#
# x = -400
# y = 300
# sign = 1
# for z in range(7):
#     house(x, y)
#     x += 120
#     sign *= -1
#     y = y + 100 * sign
#
# done()

# def sun():
#     pu(); goto(350, 300); pd()
#     color("yellow")
#     begin_fill()
#     for z in range(18):
#         fd(100)
#         lt(100)
#     end_fill()

# speed(0)
# sun()
# done()

# def star():
#     pu()
#     goto(random.randint(-400, 400), random.randint(200, 300))
#     pd()
#     color("yellow")
#     begin_fill()
#     for z in range(5):
#         fd(50)
#         lt(144)
#     end_fill()
#
#
# import random
# speed(0)
# for z in range(random.randint(25, 30)):
#     star()
# done()

# 1. намалювати одну зірку
# 2. малювати зірку в рандомному місці
# 3. рандомна кількість зірок

# from turtle_funcs import *
#
# sky("purple")
# stars(35)
# moon()
# done()

## randint and choice in turtle
# from random import randint

# a = randint(0, 100)
# print(a)
#
#
# def foo(num1, num2):
#     print(f"{num1} + {num2} = {num1+num2}")
#
#
# foo(randint(0, 10), randint(0, 10))
#
#
# def rand_foo():
#     num1 = randint(0, 10)
#     num2 = randint(0, 10)
#     print(f"{num1} + {num2} = {num1 + num2}")
#
#
# rand_foo()

# from random import randint, choice
# from turtle import *

# lst = [1, 2, 3, 4, 5, 6]
# index = randint(0, 5)
# print(lst[index])
#
# lst = [1, 2, 3, 4, 5, 6]
# print(choice(lst))

# colors = ["plum", "palegreen", "khaki", "skyblue"]
# width(10)
# for x in range(5):
#     color(choice(colors))
#     fd(50)
# done()

# default parameters and return
# def power(a, b):
#     return a ** b
#
#
# b = power(2, 3)
#
#
# import math
# a = math.factorial(5)

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     return False
#
#
# print(is_even(3))


# string = "dad"
# rev_str = ""
# for i in range(len(string)-1, -1, -1):
#     rev_str += string[i]
#     print(rev_str)
# print(rev_str == string)

# def bigger_than_five(num):
#     return 46 > 5
# if num > 5:
#     return True
# else:
#     return False

# 46 + 5 = 51
# 46 - 5 = 41
# 46 >= 5 = True
# 5 == 5 = True
# 46 <= 51 = True
# 46 != 47 = True
# print(bool(0))

# print(bigger_than_five(46))


### додає параметри і повертає число
# def add_3(a, b, c):
#     return a+b+c
#
#
# print(add_3(1, 2, 3))

## перевіряє і повертає True/False
# def is_1_5(num):
#     # if 5 >= num >= 1:
#     #     return True
#     # else:
#     #     return False
#     return 5 >= num >= 1
#
#
# print(is_1_5(6))


## модифікує і повертає рядок
# def hello_name(name):
#     return "Hello, " + name
#
#
# print(hello_name("Egor"))


# def check_list_more_than_five(array):
#     res_array = []
#     for elem in array:
#         if elem < 5:
#             res_array.append(elem)
#     return res_array
#     # for elem in array:
#     #     if elem == 5:
#     #         array.remove(elem)
#     # return array
# print(check_list_more_than_five([1, 6, 7, 3, 7, 5, 3, 10, 5]))


# №1
# написати функцію, яка отримує список  [1,2,3,3,3,3,4,5] і повертає список з парними елементами з нього


# l = [1, 5, 7, 3, 5, 6]
# print(max(l))


##
# написати функцію, яка отримує список і повертає найбільший елемент з нього
# def max(l):
#
#     max_elem = l[0]
#     for elem in l:
#         if max_elem < elem:
#             max_elem = elem
#     return max_elem
#
#
# print(max(l))


## повернути кожен другий елемент переданий в функцію
# def every_second(a, b, c, d, e, f):
#     l = [a, b, c, d, e, f]
#     l_2 = []
#     for x in range(1, 6, 2):
#         l_2.append(l[x])
#     return l_2
#
#
# lst = every_second(1, 2, 3, 4, 5, 6)
# print(lst)


# # №1
# # написати функцію, яка отримує список  [1,2,3,3,3,3,4,5] і повертає список з парними елементами з нього
# def parni_elementu(l):
#     spusok = []  # оголосили список який повернемо
#
#     # тут додати в список тільки парні елементи зі списку l
#     for elem in l:
#         if elem % 2 == 0:
#             spusok.append(elem)
#
#     return spusok  # тут повернули його
#
#
# print(parni_elementu([1, 2, 3, 3, 3, 3, 4, 5]))


# # №2
# # Написати функцію яка отримує список [-2,5,7,8,9,-10,-12] і повертає список з елементами які більше 0
# def bigger_than_zero(lst):
#     lst2 = []
#
#     for elem in lst:
#         if elem > 0:
#             lst2.append(elem)
#
#     return lst2
#
#
# print(bigger_than_zero([-2, 5, 7, 8, 9, -10, -12]))


# # №3
# # Написати функцію яка отримує список [2,4,6,10] і повертає True, якщо в ньому всі елементи парні
# def is_list_parnui(lst):
#     for elem in lst:
#         if elem % 2 != 0:
#             return False
#     else:
#         return True
#
#
# print(is_list_parnui([2, 4, 6, 10]))


## №4
## Написати функцію яка отримує рядок і повертає цей же рядок, але з крапкою в кінці
# def add_dot(string):
#     return string + "."
#
#
# print(add_dot("Hello a nice furry animal"))

# def mult_str(string, number):
#     new_str = ""
#     # for x in range(number):
#     #     new_str += string
#     count = 0
#     while count < number:
#         new_str += string
#         count += 1
#
#     return new_str
#
#
# print(mult_str("Hi! ", 5))

# повертає рядок що скаладаєтсья з кожного третього елемента рядка
# def func(string):
#     # middle_of_str = int(len(string)/2)  # знаходить індекс середини рядка
#
#     # new_str = string[::3]
#     # return new_str
#
#     new_str = ''
#     for ind in range(len(string)):
#         if ind % 3 == 0:
#             new_str += string[ind]
#     return new_str
#
# print(func("print out random number 0..1 10 times. print how much times which num is generated"))


# string = "asdqweert"
# new_string = ''
# for elem in string:
#     if elem == "e" or elem == "t":
#         new_string += elem
#
# print(new_string)

# string = "asdqweertADKMNQRW"
# s = ""
# for letter in string:
#     # if <щось маленьке> in <щось велике>:
#     # if letter.lower() in 'qwrtpsdfghjklzxcvbnm':
#     #     print(letter, end="")
#     if letter.lower() == "a":
#         s += letter

# перевіряємо який варіант довший
# from horology import Timing
# #------------First-------------
# print("First".center(30, "-"))
# for times in range(20):
#     with Timing(name="time: "):
#         string = """Mr and Mrs Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much. They were the last people you’d expect to be involved in anything strange or mysterious, because they just didn’t hold with such nonsense.Mr Dursley was the director of a firm called Grunnings, which made drills. He was a big, beefy man with hardly any neck, although he did have a very large moustache. Mrs Dursley was thin and blonde and had nearly twice the usual amount of neck, which came in very useful as she spent so much of her time craning over garden fences, spying on the neighbours. The Dursleys had a small son called Dudley and in their opinion there was no finer boy anywhere.        The Dursleys had everything they wanted, but they also had a secret, and their greatest fear was that somebody would discover it. They didn’t think they could bear it if anyone found out about the Potters. Mrs Potter was Mrs Dursley’s sister, but they hadn’t met for several years; in fact, Mrs Dursley pretended she didn’t have a sister, because her sister and her good-for-nothing husband were as unDursleyish as it was possible to be. The Dursleys shuddered to think what the neighbours would say if the Potters arrived in the street. The Dursleys knew that the Potters had a small son, too, but they had never even seen him. This boy was another good reason for keeping the Potters away; they didn’t want Dudley mixing with a child like that.        When Mr and Mrs Dursley woke up on the dull, grey Tuesday our story starts, there was nothing about the cloudy sky outside to suggest that strange and mysterious things would soon be happening all over the country. Mr Dursley hummed as he picked out his most boring tie for work and Mrs Dursley gossiped away happily as she wrestled a screaming Dudley into his high chair.        None of them noticed a large tawny owl flutter past the window.At half past eight, Mr Dursley picked up his briefcase, pecked Mrs Dursley on the cheek and tried to kiss Dudley goodbye but missed, because Dudley was now having a tantrum and throwing his cereal at the walls. ‘Little tyke,’ chortled Mr Dursley as he left the house. He got into his car and backed out of number four’s drive.Mr and Mrs Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much. They were the last people you’d expect to be involved in anything strange or mysterious, because they just didn’t hold with such nonsense.Mr Dursley was the director of a firm called Grunnings, which made drills. He was a big, beefy man with hardly any neck, although he did have a very large moustache. Mrs Dursley was thin and blonde and had nearly twice the usual amount of neck, which came in very useful as she spent so much of her time craning over garden fences, spying on the neighbours. The Dursleys had a small son called Dudley and in their opinion there was no finer boy anywhere.        The Dursleys had everything they wanted, but they also had a secret, and their greatest fear was that somebody would discover it. They didn’t think they could bear it if anyone found out about the Potters. Mrs Potter was Mrs Dursley’s sister, but they hadn’t met for several years; in fact, Mrs Dursley pretended she didn’t have a sister, because her sister and her good-for-nothing husband were as unDursleyish as it was possible to be. The Dursleys shuddered to think what the neighbours would say if the Potters arrived in the street. The Dursleys knew that the Potters had a small son, too, but they had never even seen him. This boy was another good reason for keeping the Potters away; they didn’t want Dudley mixing with a child like that.        When Mr and Mrs Dursley woke up on the dull, grey Tuesday our story starts, there was nothing about the cloudy sky outside to suggest that strange and mysterious things would soon be happening all over the country. Mr Dursley hummed as he picked out his most boring tie for work and Mrs Dursley gossiped away happily as she wrestled a screaming Dudley into his high chair.        None of them noticed a large tawny owl flutter past the window.At half past eight, Mr Dursley picked up his briefcase, pecked Mrs Dursley on the cheek and tried to kiss Dudley goodbye but missed, because Dudley was now having a tantrum and throwing his cereal at the walls. ‘Little tyke,’ chortled Mr Dursley as he left the house. He got into his car and backed out of number four’s drive.Mr and Mrs Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much. They were the last people you’d expect to be involved in anything strange or mysterious, because they just didn’t hold with such nonsense.Mr Dursley was the director of a firm called Grunnings, which made drills. He was a big, beefy man with hardly any neck, although he did have a very large moustache. Mrs Dursley was thin and blonde and had nearly twice the usual amount of neck, which came in very useful as she spent so much of her time craning over garden fences, spying on the neighbours. The Dursleys had a small son called Dudley and in their opinion there was no finer boy anywhere.        The Dursleys had everything they wanted, but they also had a secret, and their greatest fear was that somebody would discover it. They didn’t think they could bear it if anyone found out about the Potters. Mrs Potter was Mrs Dursley’s sister, but they hadn’t met for several years; in fact, Mrs Dursley pretended she didn’t have a sister, because her sister and her good-for-nothing husband were as unDursleyish as it was possible to be. The Dursleys shuddered to think what the neighbours would say if the Potters arrived in the street. The Dursleys knew that the Potters had a small son, too, but they had never even seen him. This boy was another good reason for keeping the Potters away; they didn’t want Dudley mixing with a child like that.        When Mr and Mrs Dursley woke up on the dull, grey Tuesday our story starts, there was nothing about the cloudy sky outside to suggest that strange and mysterious things would soon be happening all over the country. Mr Dursley hummed as he picked out his most boring tie for work and Mrs Dursley gossiped away happily as she wrestled a screaming Dudley into his high chair.        None of them noticed a large tawny owl flutter past the window.At half past eight, Mr Dursley picked up his briefcase, pecked Mrs Dursley on the cheek and tried to kiss Dudley goodbye but missed, because Dudley was now having a tantrum and throwing his cereal at the walls. ‘Little tyke,’ chortled Mr Dursley as he left the house. He got into his car and backed out of number four’s drive.Mr and Mrs Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much. They were the last people you’d expect to be involved in anything strange or mysterious, because they just didn’t hold with such nonsense.Mr Dursley was the director of a firm called Grunnings, which made drills. He was a big, beefy man with hardly any neck, although he did have a very large moustache. Mrs Dursley was thin and blonde and had nearly twice the usual amount of neck, which came in very useful as she spent so much of her time craning over garden fences, spying on the neighbours. The Dursleys had a small son called Dudley and in their opinion there was no finer boy anywhere.        The Dursleys had everything they wanted, but they also had a secret, and their greatest fear was that somebody would discover it. They didn’t think they could bear it if anyone found out about the Potters. Mrs Potter was Mrs Dursley’s sister, but they hadn’t met for several years; in fact, Mrs Dursley pretended she didn’t have a sister, because her sister and her good-for-nothing husband were as unDursleyish as it was possible to be. The Dursleys shuddered to think what the neighbours would say if the Potters arrived in the street. The Dursleys knew that the Potters had a small son, too, but they had never even seen him. This boy was another good reason for keeping the Potters away; they didn’t want Dudley mixing with a child like that.        When Mr and Mrs Dursley woke up on the dull, grey Tuesday our story starts, there was nothing about the cloudy sky outside to suggest that strange and mysterious things would soon be happening all over the country. Mr Dursley hummed as he picked out his most boring tie for work and Mrs Dursley gossiped away happily as she wrestled a screaming Dudley into his high chair.        None of them noticed a large tawny owl flutter past the window.At half past eight, Mr Dursley picked up his briefcase, pecked Mrs Dursley on the cheek and tried to kiss Dudley goodbye but missed, because Dudley was now having a tantrum and throwing his cereal at the walls. ‘Little tyke,’ chortled Mr Dursley as he left the house. He got into his car and backed out of number four’s drive."""
#         s = ""
#         for letter in string:
#             if letter.lower() == "a":
#                 s += letter
# #------------Second------------
# print("Second".center(30, "-"))
# for times in range(20):
#     with Timing(name="time: "):
#         string = """Mr and Mrs Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much. They were the last people you’d expect to be involved in anything strange or mysterious, because they just didn’t hold with such nonsense.Mr Dursley was the director of a firm called Grunnings, which made drills. He was a big, beefy man with hardly any neck, although he did have a very large moustache. Mrs Dursley was thin and blonde and had nearly twice the usual amount of neck, which came in very useful as she spent so much of her time craning over garden fences, spying on the neighbours. The Dursleys had a small son called Dudley and in their opinion there was no finer boy anywhere.        The Dursleys had everything they wanted, but they also had a secret, and their greatest fear was that somebody would discover it. They didn’t think they could bear it if anyone found out about the Potters. Mrs Potter was Mrs Dursley’s sister, but they hadn’t met for several years; in fact, Mrs Dursley pretended she didn’t have a sister, because her sister and her good-for-nothing husband were as unDursleyish as it was possible to be. The Dursleys shuddered to think what the neighbours would say if the Potters arrived in the street. The Dursleys knew that the Potters had a small son, too, but they had never even seen him. This boy was another good reason for keeping the Potters away; they didn’t want Dudley mixing with a child like that.        When Mr and Mrs Dursley woke up on the dull, grey Tuesday our story starts, there was nothing about the cloudy sky outside to suggest that strange and mysterious things would soon be happening all over the country. Mr Dursley hummed as he picked out his most boring tie for work and Mrs Dursley gossiped away happily as she wrestled a screaming Dudley into his high chair.        None of them noticed a large tawny owl flutter past the window.At half past eight, Mr Dursley picked up his briefcase, pecked Mrs Dursley on the cheek and tried to kiss Dudley goodbye but missed, because Dudley was now having a tantrum and throwing his cereal at the walls. ‘Little tyke,’ chortled Mr Dursley as he left the house. He got into his car and backed out of number four’s drive.Mr and Mrs Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much. They were the last people you’d expect to be involved in anything strange or mysterious, because they just didn’t hold with such nonsense.Mr Dursley was the director of a firm called Grunnings, which made drills. He was a big, beefy man with hardly any neck, although he did have a very large moustache. Mrs Dursley was thin and blonde and had nearly twice the usual amount of neck, which came in very useful as she spent so much of her time craning over garden fences, spying on the neighbours. The Dursleys had a small son called Dudley and in their opinion there was no finer boy anywhere.        The Dursleys had everything they wanted, but they also had a secret, and their greatest fear was that somebody would discover it. They didn’t think they could bear it if anyone found out about the Potters. Mrs Potter was Mrs Dursley’s sister, but they hadn’t met for several years; in fact, Mrs Dursley pretended she didn’t have a sister, because her sister and her good-for-nothing husband were as unDursleyish as it was possible to be. The Dursleys shuddered to think what the neighbours would say if the Potters arrived in the street. The Dursleys knew that the Potters had a small son, too, but they had never even seen him. This boy was another good reason for keeping the Potters away; they didn’t want Dudley mixing with a child like that.        When Mr and Mrs Dursley woke up on the dull, grey Tuesday our story starts, there was nothing about the cloudy sky outside to suggest that strange and mysterious things would soon be happening all over the country. Mr Dursley hummed as he picked out his most boring tie for work and Mrs Dursley gossiped away happily as she wrestled a screaming Dudley into his high chair.        None of them noticed a large tawny owl flutter past the window.At half past eight, Mr Dursley picked up his briefcase, pecked Mrs Dursley on the cheek and tried to kiss Dudley goodbye but missed, because Dudley was now having a tantrum and throwing his cereal at the walls. ‘Little tyke,’ chortled Mr Dursley as he left the house. He got into his car and backed out of number four’s drive.Mr and Mrs Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much. They were the last people you’d expect to be involved in anything strange or mysterious, because they just didn’t hold with such nonsense.Mr Dursley was the director of a firm called Grunnings, which made drills. He was a big, beefy man with hardly any neck, although he did have a very large moustache. Mrs Dursley was thin and blonde and had nearly twice the usual amount of neck, which came in very useful as she spent so much of her time craning over garden fences, spying on the neighbours. The Dursleys had a small son called Dudley and in their opinion there was no finer boy anywhere.        The Dursleys had everything they wanted, but they also had a secret, and their greatest fear was that somebody would discover it. They didn’t think they could bear it if anyone found out about the Potters. Mrs Potter was Mrs Dursley’s sister, but they hadn’t met for several years; in fact, Mrs Dursley pretended she didn’t have a sister, because her sister and her good-for-nothing husband were as unDursleyish as it was possible to be. The Dursleys shuddered to think what the neighbours would say if the Potters arrived in the street. The Dursleys knew that the Potters had a small son, too, but they had never even seen him. This boy was another good reason for keeping the Potters away; they didn’t want Dudley mixing with a child like that.        When Mr and Mrs Dursley woke up on the dull, grey Tuesday our story starts, there was nothing about the cloudy sky outside to suggest that strange and mysterious things would soon be happening all over the country. Mr Dursley hummed as he picked out his most boring tie for work and Mrs Dursley gossiped away happily as she wrestled a screaming Dudley into his high chair.        None of them noticed a large tawny owl flutter past the window.At half past eight, Mr Dursley picked up his briefcase, pecked Mrs Dursley on the cheek and tried to kiss Dudley goodbye but missed, because Dudley was now having a tantrum and throwing his cereal at the walls. ‘Little tyke,’ chortled Mr Dursley as he left the house. He got into his car and backed out of number four’s drive.Mr and Mrs Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much. They were the last people you’d expect to be involved in anything strange or mysterious, because they just didn’t hold with such nonsense.Mr Dursley was the director of a firm called Grunnings, which made drills. He was a big, beefy man with hardly any neck, although he did have a very large moustache. Mrs Dursley was thin and blonde and had nearly twice the usual amount of neck, which came in very useful as she spent so much of her time craning over garden fences, spying on the neighbours. The Dursleys had a small son called Dudley and in their opinion there was no finer boy anywhere.        The Dursleys had everything they wanted, but they also had a secret, and their greatest fear was that somebody would discover it. They didn’t think they could bear it if anyone found out about the Potters. Mrs Potter was Mrs Dursley’s sister, but they hadn’t met for several years; in fact, Mrs Dursley pretended she didn’t have a sister, because her sister and her good-for-nothing husband were as unDursleyish as it was possible to be. The Dursleys shuddered to think what the neighbours would say if the Potters arrived in the street. The Dursleys knew that the Potters had a small son, too, but they had never even seen him. This boy was another good reason for keeping the Potters away; they didn’t want Dudley mixing with a child like that.        When Mr and Mrs Dursley woke up on the dull, grey Tuesday our story starts, there was nothing about the cloudy sky outside to suggest that strange and mysterious things would soon be happening all over the country. Mr Dursley hummed as he picked out his most boring tie for work and Mrs Dursley gossiped away happily as she wrestled a screaming Dudley into his high chair.        None of them noticed a large tawny owl flutter past the window.At half past eight, Mr Dursley picked up his briefcase, pecked Mrs Dursley on the cheek and tried to kiss Dudley goodbye but missed, because Dudley was now having a tantrum and throwing his cereal at the walls. ‘Little tyke,’ chortled Mr Dursley as he left the house. He got into his car and backed out of number four’s drive."""
#         s = ""
#         for letter in string:
#             if letter.lower() in "a":
#                 s += letter

# from horology import Timing
# #------------First-------------
# print("First".center(30, "-"))
# for times in range(20):
#     with Timing(name="time: "):
#         string = """Mr and Mrs Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much. They were the last people you’d expect to be involved in anything strange or mysterious, because they just didn’t hold with such nonsense.Mr Dursley was the director of a firm called Grunnings, which made drills. He was a big, beefy man with hardly any neck, although he did have a very large moustache. Mrs Dursley was thin and blonde and had nearly twice the usual amount of neck, which came in very useful as she spent so much of her time craning over garden fences, spying on the neighbours. The Dursleys had a small son called Dudley and in their opinion there was no finer boy anywhere.        The Dursleys had everything they wanted, but they also had a secret, and their greatest fear was that somebody would discover it. They didn’t think they could bear it if anyone found out about the Potters. Mrs Potter was Mrs Dursley’s sister, but they hadn’t met for several years; in fact, Mrs Dursley pretended she didn’t have a sister, because her sister and her good-for-nothing husband were as unDursleyish as it was possible to be. The Dursleys shuddered to think what the neighbours would say if the Potters arrived in the street. The Dursleys knew that the Potters had a small son, too, but they had never even seen him. This boy was another good reason for keeping the Potters away; they didn’t want Dudley mixing with a child like that.        When Mr and Mrs Dursley woke up on the dull, grey Tuesday our story starts, there was nothing about the cloudy sky outside to suggest that strange and mysterious things would soon be happening all over the country. Mr Dursley hummed as he picked out his most boring tie for work and Mrs Dursley gossiped away happily as she wrestled a screaming Dudley into his high chair.        None of them noticed a large tawny owl flutter past the window.At half past eight, Mr Dursley picked up his briefcase, pecked Mrs Dursley on the cheek and tried to kiss Dudley goodbye but missed, because Dudley was now having a tantrum and throwing his cereal at the walls. ‘Little tyke,’ chortled Mr Dursley as he left the house. He got into his car and backed out of number four’s drive.Mr and Mrs Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much. They were the last people you’d expect to be involved in anything strange or mysterious, because they just didn’t hold with such nonsense.Mr Dursley was the director of a firm called Grunnings, which made drills. He was a big, beefy man with hardly any neck, although he did have a very large moustache. Mrs Dursley was thin and blonde and had nearly twice the usual amount of neck, which came in very useful as she spent so much of her time craning over garden fences, spying on the neighbours. The Dursleys had a small son called Dudley and in their opinion there was no finer boy anywhere.        The Dursleys had everything they wanted, but they also had a secret, and their greatest fear was that somebody would discover it. They didn’t think they could bear it if anyone found out about the Potters. Mrs Potter was Mrs Dursley’s sister, but they hadn’t met for several years; in fact, Mrs Dursley pretended she didn’t have a sister, because her sister and her good-for-nothing husband were as unDursleyish as it was possible to be. The Dursleys shuddered to think what the neighbours would say if the Potters arrived in the street. The Dursleys knew that the Potters had a small son, too, but they had never even seen him. This boy was another good reason for keeping the Potters away; they didn’t want Dudley mixing with a child like that.        When Mr and Mrs Dursley woke up on the dull, grey Tuesday our story starts, there was nothing about the cloudy sky outside to suggest that strange and mysterious things would soon be happening all over the country. Mr Dursley hummed as he picked out his most boring tie for work and Mrs Dursley gossiped away happily as she wrestled a screaming Dudley into his high chair.        None of them noticed a large tawny owl flutter past the window.At half past eight, Mr Dursley picked up his briefcase, pecked Mrs Dursley on the cheek and tried to kiss Dudley goodbye but missed, because Dudley was now having a tantrum and throwing his cereal at the walls. ‘Little tyke,’ chortled Mr Dursley as he left the house. He got into his car and backed out of number four’s drive.Mr and Mrs Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much. They were the last people you’d expect to be involved in anything strange or mysterious, because they just didn’t hold with such nonsense.Mr Dursley was the director of a firm called Grunnings, which made drills. He was a big, beefy man with hardly any neck, although he did have a very large moustache. Mrs Dursley was thin and blonde and had nearly twice the usual amount of neck, which came in very useful as she spent so much of her time craning over garden fences, spying on the neighbours. The Dursleys had a small son called Dudley and in their opinion there was no finer boy anywhere.        The Dursleys had everything they wanted, but they also had a secret, and their greatest fear was that somebody would discover it. They didn’t think they could bear it if anyone found out about the Potters. Mrs Potter was Mrs Dursley’s sister, but they hadn’t met for several years; in fact, Mrs Dursley pretended she didn’t have a sister, because her sister and her good-for-nothing husband were as unDursleyish as it was possible to be. The Dursleys shuddered to think what the neighbours would say if the Potters arrived in the street. The Dursleys knew that the Potters had a small son, too, but they had never even seen him. This boy was another good reason for keeping the Potters away; they didn’t want Dudley mixing with a child like that.        When Mr and Mrs Dursley woke up on the dull, grey Tuesday our story starts, there was nothing about the cloudy sky outside to suggest that strange and mysterious things would soon be happening all over the country. Mr Dursley hummed as he picked out his most boring tie for work and Mrs Dursley gossiped away happily as she wrestled a screaming Dudley into his high chair.        None of them noticed a large tawny owl flutter past the window.At half past eight, Mr Dursley picked up his briefcase, pecked Mrs Dursley on the cheek and tried to kiss Dudley goodbye but missed, because Dudley was now having a tantrum and throwing his cereal at the walls. ‘Little tyke,’ chortled Mr Dursley as he left the house. He got into his car and backed out of number four’s drive.Mr and Mrs Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much. They were the last people you’d expect to be involved in anything strange or mysterious, because they just didn’t hold with such nonsense.Mr Dursley was the director of a firm called Grunnings, which made drills. He was a big, beefy man with hardly any neck, although he did have a very large moustache. Mrs Dursley was thin and blonde and had nearly twice the usual amount of neck, which came in very useful as she spent so much of her time craning over garden fences, spying on the neighbours. The Dursleys had a small son called Dudley and in their opinion there was no finer boy anywhere.        The Dursleys had everything they wanted, but they also had a secret, and their greatest fear was that somebody would discover it. They didn’t think they could bear it if anyone found out about the Potters. Mrs Potter was Mrs Dursley’s sister, but they hadn’t met for several years; in fact, Mrs Dursley pretended she didn’t have a sister, because her sister and her good-for-nothing husband were as unDursleyish as it was possible to be. The Dursleys shuddered to think what the neighbours would say if the Potters arrived in the street. The Dursleys knew that the Potters had a small son, too, but they had never even seen him. This boy was another good reason for keeping the Potters away; they didn’t want Dudley mixing with a child like that.        When Mr and Mrs Dursley woke up on the dull, grey Tuesday our story starts, there was nothing about the cloudy sky outside to suggest that strange and mysterious things would soon be happening all over the country. Mr Dursley hummed as he picked out his most boring tie for work and Mrs Dursley gossiped away happily as she wrestled a screaming Dudley into his high chair.        None of them noticed a large tawny owl flutter past the window.At half past eight, Mr Dursley picked up his briefcase, pecked Mrs Dursley on the cheek and tried to kiss Dudley goodbye but missed, because Dudley was now having a tantrum and throwing his cereal at the walls. ‘Little tyke,’ chortled Mr Dursley as he left the house. He got into his car and backed out of number four’s drive."""
#         s = 0
#         for letter in string:
#             if letter.lower() == "e" or letter.lower() == "y" or letter.lower() == "u" or letter.lower() == "i" or letter.lower() == "o" or letter.lower() == "a":
#                 s += 1
# #------------Second------------
# print("Second".center(30, "-"))
# for times in range(20):
#     with Timing(name="time: "):
#         string = """Mr and Mrs Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much. They were the last people you’d expect to be involved in anything strange or mysterious, because they just didn’t hold with such nonsense.Mr Dursley was the director of a firm called Grunnings, which made drills. He was a big, beefy man with hardly any neck, although he did have a very large moustache. Mrs Dursley was thin and blonde and had nearly twice the usual amount of neck, which came in very useful as she spent so much of her time craning over garden fences, spying on the neighbours. The Dursleys had a small son called Dudley and in their opinion there was no finer boy anywhere.        The Dursleys had everything they wanted, but they also had a secret, and their greatest fear was that somebody would discover it. They didn’t think they could bear it if anyone found out about the Potters. Mrs Potter was Mrs Dursley’s sister, but they hadn’t met for several years; in fact, Mrs Dursley pretended she didn’t have a sister, because her sister and her good-for-nothing husband were as unDursleyish as it was possible to be. The Dursleys shuddered to think what the neighbours would say if the Potters arrived in the street. The Dursleys knew that the Potters had a small son, too, but they had never even seen him. This boy was another good reason for keeping the Potters away; they didn’t want Dudley mixing with a child like that.        When Mr and Mrs Dursley woke up on the dull, grey Tuesday our story starts, there was nothing about the cloudy sky outside to suggest that strange and mysterious things would soon be happening all over the country. Mr Dursley hummed as he picked out his most boring tie for work and Mrs Dursley gossiped away happily as she wrestled a screaming Dudley into his high chair.        None of them noticed a large tawny owl flutter past the window.At half past eight, Mr Dursley picked up his briefcase, pecked Mrs Dursley on the cheek and tried to kiss Dudley goodbye but missed, because Dudley was now having a tantrum and throwing his cereal at the walls. ‘Little tyke,’ chortled Mr Dursley as he left the house. He got into his car and backed out of number four’s drive.Mr and Mrs Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much. They were the last people you’d expect to be involved in anything strange or mysterious, because they just didn’t hold with such nonsense.Mr Dursley was the director of a firm called Grunnings, which made drills. He was a big, beefy man with hardly any neck, although he did have a very large moustache. Mrs Dursley was thin and blonde and had nearly twice the usual amount of neck, which came in very useful as she spent so much of her time craning over garden fences, spying on the neighbours. The Dursleys had a small son called Dudley and in their opinion there was no finer boy anywhere.        The Dursleys had everything they wanted, but they also had a secret, and their greatest fear was that somebody would discover it. They didn’t think they could bear it if anyone found out about the Potters. Mrs Potter was Mrs Dursley’s sister, but they hadn’t met for several years; in fact, Mrs Dursley pretended she didn’t have a sister, because her sister and her good-for-nothing husband were as unDursleyish as it was possible to be. The Dursleys shuddered to think what the neighbours would say if the Potters arrived in the street. The Dursleys knew that the Potters had a small son, too, but they had never even seen him. This boy was another good reason for keeping the Potters away; they didn’t want Dudley mixing with a child like that.        When Mr and Mrs Dursley woke up on the dull, grey Tuesday our story starts, there was nothing about the cloudy sky outside to suggest that strange and mysterious things would soon be happening all over the country. Mr Dursley hummed as he picked out his most boring tie for work and Mrs Dursley gossiped away happily as she wrestled a screaming Dudley into his high chair.        None of them noticed a large tawny owl flutter past the window.At half past eight, Mr Dursley picked up his briefcase, pecked Mrs Dursley on the cheek and tried to kiss Dudley goodbye but missed, because Dudley was now having a tantrum and throwing his cereal at the walls. ‘Little tyke,’ chortled Mr Dursley as he left the house. He got into his car and backed out of number four’s drive.Mr and Mrs Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much. They were the last people you’d expect to be involved in anything strange or mysterious, because they just didn’t hold with such nonsense.Mr Dursley was the director of a firm called Grunnings, which made drills. He was a big, beefy man with hardly any neck, although he did have a very large moustache. Mrs Dursley was thin and blonde and had nearly twice the usual amount of neck, which came in very useful as she spent so much of her time craning over garden fences, spying on the neighbours. The Dursleys had a small son called Dudley and in their opinion there was no finer boy anywhere.        The Dursleys had everything they wanted, but they also had a secret, and their greatest fear was that somebody would discover it. They didn’t think they could bear it if anyone found out about the Potters. Mrs Potter was Mrs Dursley’s sister, but they hadn’t met for several years; in fact, Mrs Dursley pretended she didn’t have a sister, because her sister and her good-for-nothing husband were as unDursleyish as it was possible to be. The Dursleys shuddered to think what the neighbours would say if the Potters arrived in the street. The Dursleys knew that the Potters had a small son, too, but they had never even seen him. This boy was another good reason for keeping the Potters away; they didn’t want Dudley mixing with a child like that.        When Mr and Mrs Dursley woke up on the dull, grey Tuesday our story starts, there was nothing about the cloudy sky outside to suggest that strange and mysterious things would soon be happening all over the country. Mr Dursley hummed as he picked out his most boring tie for work and Mrs Dursley gossiped away happily as she wrestled a screaming Dudley into his high chair.        None of them noticed a large tawny owl flutter past the window.At half past eight, Mr Dursley picked up his briefcase, pecked Mrs Dursley on the cheek and tried to kiss Dudley goodbye but missed, because Dudley was now having a tantrum and throwing his cereal at the walls. ‘Little tyke,’ chortled Mr Dursley as he left the house. He got into his car and backed out of number four’s drive.Mr and Mrs Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much. They were the last people you’d expect to be involved in anything strange or mysterious, because they just didn’t hold with such nonsense.Mr Dursley was the director of a firm called Grunnings, which made drills. He was a big, beefy man with hardly any neck, although he did have a very large moustache. Mrs Dursley was thin and blonde and had nearly twice the usual amount of neck, which came in very useful as she spent so much of her time craning over garden fences, spying on the neighbours. The Dursleys had a small son called Dudley and in their opinion there was no finer boy anywhere.        The Dursleys had everything they wanted, but they also had a secret, and their greatest fear was that somebody would discover it. They didn’t think they could bear it if anyone found out about the Potters. Mrs Potter was Mrs Dursley’s sister, but they hadn’t met for several years; in fact, Mrs Dursley pretended she didn’t have a sister, because her sister and her good-for-nothing husband were as unDursleyish as it was possible to be. The Dursleys shuddered to think what the neighbours would say if the Potters arrived in the street. The Dursleys knew that the Potters had a small son, too, but they had never even seen him. This boy was another good reason for keeping the Potters away; they didn’t want Dudley mixing with a child like that.        When Mr and Mrs Dursley woke up on the dull, grey Tuesday our story starts, there was nothing about the cloudy sky outside to suggest that strange and mysterious things would soon be happening all over the country. Mr Dursley hummed as he picked out his most boring tie for work and Mrs Dursley gossiped away happily as she wrestled a screaming Dudley into his high chair.        None of them noticed a large tawny owl flutter past the window.At half past eight, Mr Dursley picked up his briefcase, pecked Mrs Dursley on the cheek and tried to kiss Dudley goodbye but missed, because Dudley was now having a tantrum and throwing his cereal at the walls. ‘Little tyke,’ chortled Mr Dursley as he left the house. He got into his car and backed out of number four’s drive."""
#         s = 0
#         for letter in string:
#             if letter.lower() in "eyuioa":
#                 s += 1


# if 'a' in 'apple':
#     print("a in apple")

# виводить кількість слів в яких 3 букви
# def func(string):
#     c = 0
#     lst = string.split()
#     for elem in lst:
#         if len(elem) == 3:
#             c += 1
#
#     return "3 букви мають " + str(c) + " слів"
#
#
# print(func("Where you from?"))

# # виводить всі слова в яких 3 букви
# def func(string):
#     l = []
#     lst = string.split()
#     for elem in lst:
#         if len(elem) == 3:
#             l.append(elem)
#
#     return l
#
#
# print(func("Where you from? sds asd qwe"))

# # додає в список слова які починаютсья з "а"
# def func(string):
#     l = []
#     lst = string.split()
#     for elem in lst:
#         if elem[0].lower() == 'a':
#             l.append(elem)
#
#     return l
#
#
# print(func("Ahere you from? ads asdasd qwe"))

# # заміняє букву "b" на "!"
# # b = !
# def func(string):
#     new_str = ''
#     for elem in string:
#         if elem != "b":
#             new_str += elem
#         else:
#             new_str += "!"
#     return new_str
#
# print(func("Ahbere you fbrom? ads basdasd qwe"))

# s = "I have a great green keyboard"
# l = ["great", "green"]
# l = s.split()
# k = []
# print(l)
# for elem in l:
#     if len(elem) == 1:
#         k.append(elem)
# print(k)
# for word in l:
#     # if len(word) > 1 and word[-2] == 'n':
#     # # if word[-2] == 'n' and len(word) > 1:
#     #     k.append(word)
#     if len(word) > 1:
#         if word[-2] == 'g':
#             k.append(word)
# print(k)


# #l = "I a"
# k = ""
# s = "I have a great green keyboard"
# for elem in s.split():
#     if elem[0] == "g":
#         k += elem
# print(k)

# s = "I have a great green keyboard"
# k = []
# for elem in s.split():
#     if elem[0] == "g":
#         k.append(elem)
# print(k)


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

# def func(a, b, c):
#     sum1 = a + b
#     sum2 = b + c
#     # return f'sum1: {sum1}, sum2: {sum2}'
#     return sum1, sum2
#
#
# print(func(1, 2, 3))

# num = 1234

# num = str(num)
#
# number = num[0]
# print(int(number)+2)

# word = "ord"
# if "w" in word:
#     print("w in word is present")
# else:
#     print("no w in word")

# num = 12347
# if "7" in str(num):
#     print("7 is found in num")
# else:
#     print("no 7 in num")

# num = 12347
# num = str(num)
# print("7" in num)
# print("5" in num)


# num = 1234
# s = "apple"
# lst = ['a', 'p', 'p', 'l', 'e']
# print(s[0])
# print(num[0])
# print(lst[0])
# str(num)
# list(num)
# for e in "1234":
#     pass

# lst = ['a', 'p', 'p', 'l', 'e']
# x = 2
# y = 3
# x, y = y, x
# # temp = x
# # x = y
# # y = temp

# print(x, y)
# lst = ['a', 'p', 'p', 'l', 'e']
# lst[0] = "s"
# lst[1] = lst[3]
# lst[0], lst[1] = lst[1], lst[0]
# lst[-1], lst[-2] = lst[-2], lst[-1]
# print(lst)


# міняємо місцями елементи числа
# num = 1234
# print(num)
# num = str(num)
# num = list(num)
# print(num)
# num[0], num[1] = num[1], num[0]
# print(num)

# # list -> num
# s = ''
# for elem in num:
#     s += elem
# print(int(s))


# перетворення елементів списку з рядків числа
# num = 1234
# num = list(str(num))
# print(num)
# summ = int(num[0]) + int(num[1])

# # 1
# num_1 = []
# for elem in num:
#     num_1.append(int(elem))
# print(sum(num_1))

# # 2
# for i in range(len(num)):
#     num[i] = int(num[i])
# print(sum(num))

# # 3
# num_1 = [int(elem) for elem in num]
# print(num_1)

# print(sum([int(elem) for elem in num]))

# from horology import Timing
#
#
# # створює новий список і кладе туди рядки перетворені в числа
# def f1(num):
#     num = list(str(num))
#     num_1 = []
#     for elem in num:
#         num_1.append(int(elem))
#     return sum(num_1)
#
#
# # звертається через індекси і перетворює ті ж елементи на числа
# def f2(num):
#     num = list(str(num))
#     for i in range(len(num)):
#         num[i] = int(num[i])
#     return sum(num)
#
#
# # використовує вбудований список
# def f3(num):
#     return sum([int(elem) for elem in list(str(num))])
#
#
# n = 1234
# for x in range(10000000000000000000000, 10000000000050000000000, 1):
#     with Timing(unit='ms'):
#         f1(x)
#     with Timing(unit='ms'):
#         f2(x)
#     with Timing(unit='ms'):
#         f3(x)
#     print()


# сортування
# lst = [2, 5, 6, 2, 1, 34, 4]
# # lst.sort()
# # print(lst)
#
# print(sorted(lst))
# print(lst)

# print("name" in "asdasasdasndname")
# print('7' in '1234567')
# num = 1
# num1 = 2
# str(num) in str(num1)
# print(str(7) in str(1233455678))
# print(1 in [1, 2, 3, 4])
# print(1 in (1, 2, 3, 4))
# {1, 2, 3}

# num = 1234
# str(num)
# lst = list(str(num))
# print(lst)
# lst = [int(elem) for elem in lst]
# lst_num = []
# for elem in list(str(num)):
#     lst_num.append(int(elem))
# # print(lst_num)
# print(num)
# for x in range(100000):
#     # print(f"{x}: {x in lst_num}")
#     # print(f"{x}: {str(x) in str(num)}")
#     print(x)
#
#     # print(f"{x // 10}: {str(x // 10) in str(num)}")
#     # print(f"{x % 10}: {str(x % 10) in str(num)}")
#
#     for elem in str(x):
#         print(f"{elem}: {elem in str(num)}")

# створити функцію яка отримує 2 числа: діапазон від і до.
# І повертає список усіх чисел в цьому діапазоні в яких є цифра 7

# def f(x,y):
#     for e in range(x, y + 1):
#         if
# x, y = int(input()), int(input())

# num = 1234
# num = list(str(num))
# print(num)
# # x, y = int(input()), int(input())
# x, y = 0, -1
# #
# num[x], num[y] = num[y], num[x]
# print(num)
# s = ""
# for elem in num:
#     s += elem
# print(int(s))


# # num = [9,8,7,6,5,4,3,2,1]
# num = [5, 4, 7, 8, 9, 1, 2, 45]
# # по зростанню
# print(sorted(num))
# # по спаданню
# print(sorted(num, reverse=True))
# print(num)


# for elem in range(10):
#     print(elem)
#     if elem == 15:
#         print(True)
#         break
# else:
#     print(False)
#
# def f():
#     for x in range(10):
#         print(x)
#         if x == 15:
#             return True
#     return False
#
#
# print(f())


# lists

# print out random number 0..1 10 times. print how much times which num is generated,
# make the test 10 times with one start up    if rdi == 1: c += 1

# from random import randint
# import locale
#
# locale.setlocale(locale.LC_ALL, "ua-UA.UTF-8")
#
# times = 10
# for c in range(15):
#
#     times *= 2
#     for v in range(5):
#         nums = []
#         for x in range(times):
#             num = randint(0, 1)
#             nums.append(num)
#         print()
#         print(f"{times:n}")
#         print(f"0: {nums.count(0)}\t1:{nums.count(1)}")
#         print(f"0%: {nums.count(0) * 100 / len(nums)}%", end="")
#         print(f"  1%: {round(nums.count(1) * 100 / len(nums), 1)}%")

# * in defs
# questions

# num1 = 5
# num2 = 6
# num3 = 7
#
#
# def func3(num1, num2, num3):
#     return [num1, num2, num3]
#
#
# print(func3(5, 6, 7))
#
# nums_tuple = (1, 2, 3, 4)
#
#
# def funcs(*nums):
#     return nums
#
#
# print(funcs(5, 6, 7))

# def family(mom, dad, *children, car):
#     return max(children)

# # повернути другу по найстаршу дитину
# def family(mom, dad, *children, car):#
#     return sorted(children)[-2]
#
#
# print(family(42, 37, 13, 18, 6, 24, car=3))


# # вивести всіх дітей в зворотньому порядку
# def family(mom, dad, *children, car):
#     for child in sorted(children, reverse=True):
#         print(child)
#     # # return '\n'.join(str(e) for e in sorted(children))
#
#
# family(42, 37, 13, 18, 6, 24, car=3)

# # [(те що запишемо в список) (умова циклу) (умова(if)\умови(if and if))]
# # [elem for elem in fruits if elem[0] == 'p' and len(elem) == 4]
# def func(*fruits, vegi):
#     return [elem for elem in fruits if elem[0] == 'p' and len(elem) == 4]
#     # lst = []
#     # for elem in fruits:
#     #     if elem[0] == 'p':
#     #         lst.append(elem)
#     # return lst
#
# # перевірка якщо перший елемент слова буде p або a
# def func(*fruits, vegi):
#     return [elem for elem in fruits if elem[0] == 'p' or elem[0] == "a"]
#
#
# # перевірка якщо перший елемент слова голосна буква
# def func(*fruits, vegi):
#     return [elem for elem in fruits if elem[0] in "aeyuio"]
#
# print(func("plum", "apple", 'pineapple', 'orange', vegi="potato"))


# # отримуємо кортеж, перетворюємо в список щоб видалити елемент
# def func(*bools):
#     bools = list(bools)
#     del bools[0]
#     return bools
#
#
# print(func(True, [False, True], True))


# def func(*cars):
#     # 1 варіант
#     return [elem for elem in cars if elem[0] in "aeyuio"]
#     # 2 варіант
#     lst = []
#     for elem in cars:
#         if elem[0] in "aeyuio":
#             lst.append(elem)
#     return lst
#
# print(func("audi", "reno", "mazda"))

# from random import randint
# print(randint(5, 10))
# # from random import *
#
# import random
# print(random.randint(5, 10))


# import random as rd, time, locale

# import locale
# import random as rd
# import time
#
# # print(rd.randint(5, 10))
# # time.sleep(1)
#
# locale.setlocale(locale.LC_ALL, 'ua-UA.UTF-8')
#
# for number in range(1000, 10000000, 10000):
#     print(f"{number:n}")

# lst = [10, 11, 12, 1, 2, 3, 3, 4, 5, 6, 7]
# print(list(filter(lambda e: e < 5, lst)))
# words = ["apple", "plum", "pineapple"]
# # print(sorted(lst, key=lambda n: n%3))
# # print(sorted(words, key=lambda e: len(e), reverse = True))
# print(sorted(words, key=lambda e: e[-1]))
#
#
# def sort_func(e):
#     return e[-1]
# print(sorted(words, key=sort_func))

# questions def
# lambda - функція в один рядок
# filter - фільтрує елементи
# sorted - як вказувати ключ для сортування

# from random import randint, shuffle
# from horology import Timing
# vars = ["Petya", "NePetya", "TochnoNePetya", "BratPeti", "NePetya", "TochnoNePetya", "BratPeti", "NePetya", "TochnoNePetya", "BratPeti", "NePetya", "TochnoNePetya", "BratPeti"]
#
#
# # # 1 генерувати число і додавати в список. Якщо воно вже є в списку - генеруй нове
# for x in range(10):
#     with Timing(name="time: ", unit="ms"):
#         lst = []
#         for elem in vars:
#             num = randint(1, len(vars))
#             while num in lst:
#                 num = randint(1, len(vars))
#                 # print(num)
#             lst.append(num)
#             # print(f"{elem} - {num}")
# print()
# # # 2 генерувати список з числами. Виводити елемент з рандомним індексом
# # і видаляти його (праву межу задавати динамічно через довжину списку)
# for x in range(10):
#     with Timing(name="time: ", unit="ms"):
#         nums = []
#         for n in range(1, len(vars)+1):
#             nums.append(n)
#
#         for elem in vars:
#             num = randint(0, len(nums)-1)
#             # print(f"{elem} - {nums[num]}")
#             del nums[num]
# print()

# # 3 перемішати список з числами
# for x in range(10):
#     with Timing(name="time: ", unit="ms"):
#         nums = []
#         for n in range(1, len(vars)+1):
#             nums.append(n)
#         shuffle(nums)
#         for i in range(len(vars)):
#             print(end='')
#             # print(f"{vars[i]} - {nums[i]}")

# def f(*vars):
#     for elem in vars:
#         print(elem)
#
# f("1","2","3")

# from random import shuffle
# l = ("a", "b", "c")
# shuffle(l)
# l = list(l)
# # l = ["a", "b", "c"]
# shuffle(l)
#
# number = "5"
# print(number - 5)
# number = int(number)
# print(number - 5)


# vars = ["a", "b", "c"]
# while True:
#     try:
#         user_text = int(input("?"))
#         if user_text not in range(1, len(vars)+1):
#             print("Wrong")
#             continue
#         break
#     except ValueError:
#         print("Wrong")
#         continue
# print("out")


# from tkinter import *
#
# window = Tk()
# window.title("(ﾉ◕ヮ◕)ﾉ*:・ﾟ✧")
# window.geometry("600x4000+0+0")
#
#
# label = Label(text="This is definitely a label!\nThis is second row",
#               cursor="hand2", font="ComicSans 42", fg="#8e44ad", background="#fa81b8")
#
# label1 = Label(text="This is the second label",
#               cursor="hand2", font="ComicSans 42", fg="#ffffff", background="#fa81b8")
#
# label.pack()
# label1.pack()
#
# mainloop()

# from tkinter import *
# import time
#
# window = Tk()
# window.title("(ﾉ◕ヮ◕)ﾉ*:・ﾟ✧")
#
# width = 240 # Width
# height = 320 # Heigh
# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight()
# x = int((screen_width/2) - (width/2))
# y = int((screen_height/2) - (height/2))
# window.geometry(f"{width}x{height}+{x}+{y}")
#
# # window.eval('tk::PlaceWindow . center')
#
# lab = Label(cursor="hand2", text="1")
# lab.place(x=0, y=0, width=600, height=400)
# label = Label(text=":", cursor="hand2", font="ComicSans 42", fg="#8e44ad", background="#fa81b8")
#
# label1 = Label(text=":", cursor="hand2", font="ComicSans 42", fg="#ffffff", background="#fa81b8")
#
# label.pack()
# label1.pack()
#
# label.config(width=2)
# # window.after(2000)
# # label['text'] = " "
# # label1['text'] = " "
#
# # time.sleep(2)
# # label['text'] = ":"
# # label1['text'] = ":"
#
# mainloop()

# from tkinter import *
# from tkinter import messagebox      # імпротуємо вспливаючі вікна
#
# window = Tk()
# window.title("(ﾉ◕ヮ◕)ﾉ*:・ﾟ✧")
# window.geometry("600x400+400+350")
# window.resizable(FALSE, FALSE)
# window.iconbitmap('g_icon_254085.ico')  # це іконка
#
#
# def print_entry():
#     # print(f"Hi, {ent.get()}")
#     messagebox.showinfo(message=f"Hi, {ent.get()}, nice to meet u", title="This is info")   # інфо
#     messagebox.showerror(message=f"Hi, {ent.get()}, nice to meet u", title="This is error") # помилка
#
#
# lbl = Label(text="Type in your age", font=("comic sans ms", 22, "bold", "underline"),
#             background="#123321", foreground="white")
# lbl.place(x=230, y=0, width=400, height=40)
#
# ent = Entry(font=("comic sans ms", 22, "bold", "underline"), relief=RAISED)
# ent.place(x=250, y=50, width=200, height=80)
#
# but = Button(text="Submit", font=("comic sans ms", 22, "bold", "underline"),
#              command=print_entry, background="#123456", foreground="white")
# but.place(x=285, y=150)
# # but.pack()
#
#
#
# mainloop()


# from tkinter import *
#
# window = Tk()
# window.geometry("800x600+400+350")
#
# def change():
#     lbl['text'] = "~This label has changed!~\nsecond row\n third"
#     lbl['font'] = ("comic sans ms", 30)
#
# def change1():
#     lbl['text'] = "1~This label has changed!~\nsecond row\n third"
# # Label(text="This is LABEL", font=("comic sans ms", 22)).place(x=280, y=100, width=400, height=40)
#
#
# lbl = Label(text="This is LABEL", font=("comic sans ms", 22), relief="sunken", bg="#AAAAAA")
# lbl.place(x=280, y=0)
#
# Button(text="Change", font=("comic sans ms", 22, "bold", "underline"), command=change).place(x=285, y=150)
# Button(text="Change", font=("comic sans ms", 22, "bold", "underline"), command=change1).place(x=285, y=220)
# Button(text="Change", font=("comic sans ms", 22, "bold", "underline"), command=change).place(x=285, y=290)
#
#
# mainloop()

### dictionary ###
# lst = ["a", "b", "c"]
# print(lst[0])
# d = {"key": "a", 1102: "b", 1103: "c"}
# print(d["key"])

# d = {"Steffany": "mom", "Richard": "dad", "child": "c"}
# print(d["Richard"])

# d = {"mom": "Stef",
#      "dad": "Richard",
#      "child": ["Bob", "Mary", "Steve"],
#      "dogs": ["dog1", "dog2"]}

# print(d["child"])
# print(d["dogs"])
# for name in d.values():
#     print(name)

# for part in d.keys():
#     print(part)

# for key, value in d.items():
#     print(key, value)

# lst = [1, 2, 3, 3]
# lst[1] = 123123
# d["mom"] = "NewMom"
# print(d)


# from tkinter import *
#
# window = Tk()
# window.geometry("800x600+400+350")
#
# lbl = Label(bg="gray", text="lbl", font=("comic sans ms", 14))
# but = Button(bg="gray", text="but", font=("comic sans ms", 14))
# lbl1 = Label(bg="gray", text="lbl1", font=("comic sans ms", 16))
#
# # row, column - рядок і стовпець(місце в таблиці)
# # ipadx, ipady - розміри комірки
# # об'єкт розтягується по всій комірці з відступом padx pady від країв

# lbl.grid(row=0, column=0, columnspan=3, ipadx=40, ipady=30)
# but.grid(row=1, column=1, ipadx=80, ipady=30, padx=30, pady=30)
# lbl1.grid(row=2, column=2)
#
# mainloop()

# from tkinter import *
#
# window = Tk()
# # window.geometry("1050x570+150+50")
#
# window.eval('tk::PlaceWindow . center')

# but1 = Button(text="@", font=("comic sans ms", 22), bg="grey")
# but2 = Button(text="@", font=("comic sans ms", 22), bg="grey")
# but3 = Button(text="@", font=("comic sans ms", 22), bg="grey")
# but4 = Button(text="@", font=("comic sans ms", 22), bg="grey")
# but5 = Button(text="@", font=("comic sans ms", 22), bg="grey")
# but6 = Button(text="@", font=("comic sans ms", 22), bg="grey")
#
# but1.grid(row=0, column=0, padx=50, ipadx=30, ipady=30)
# but2.grid(row=0, column=1, padx=50, ipadx=30, ipady=30)
# but3.grid(row=1, column=0, pady=100, ipadx=30, ipady=30)
# but4.grid(row=1, column=1, ipadx=30, ipady=30)
# but5.grid(row=2, column=0, pady=100, ipadx=30, ipady=30)
# but6.grid(row=2, column=1, ipadx=30, ipady=30)

# counter = 0
# color = ""
# num = 0
# for row in range(8):
#     for column in range(8):
#         if row % 2 == 0:
#             num = 0
#         else:
#             num = 1
#         if counter % 2 == num:
#             color = "black"
#         else:
#             color = "white"
#         Label(bg=color).grid(row=row, column=column, ipadx=30, ipady=22)
#         counter += 1

# Entry(font=("comic sans ms", 22), bg="gray").grid(row=0, columnspan=4, ipadx=160)
# row = 1
# column = 0
# for elem in "123456789":
#     Button(text=elem, bg="pink").grid(row=row, column=column, ipadx=30, ipady=22, padx=10, pady=8)
#     column += 1
#     if column == 3:
#         row += 1
#         column = 0
#
# mainloop()

# from tkinter import *
#
# root = Tk()
#
# root.geometry("430x180+40+10")
#
# # Label(text='AAAAAAAAAAAAAAA', font=("", 30, "bold")).grid(row=0, columnspan=2)
#
# new_entry = Entry(font=("", 18, "bold"), relief="sunken", width=15)
# new_entry.grid(row=1, column=0, padx=50)
#
# Label(text="ffffffffff", fg="white", font=("", 18, "bold"), bg="#FA8072").grid(row=1, column=1)
#
# # entry.grid(row=0, column=1, ipadx=80)
# # label.grid(row=0, column=2, padx=150, pady=150, sticky="e")
#
#
# mainloop()

# from tkinter import *
#
# window = Tk()
# window.title("window1")
# window.geometry("400x300")
# Correct_answers = 0
# Fail_answer = 0
#
# def dd():
#     global Correct_answers, Fail_answer
#     if ent.get() == "4":
#         Correct_answers += 1
#         print(Correct_answers)
#         lb1['text'] = f"Correct answers: {Correct_answers}"
#         lb['bg'] = "green"
#     else:
#         Fail_answer += 1
#         lb2['text'] = f"Fail_answers: {Fail_answer}"
#         lb['bg'] = "red"
#
#
# lb = Label(font=("comic sans ms", 15), bg="white", text="2+2=")
# lb.grid(row=0, column=0)
# lb2 = Label(font=("comic sans ms", 15), bg="white", text="Answers: 1")
# lb2.grid(row=2, column=0, padx=0, pady=0, columnspan=2)
# lb1 = Label(font=("comic sans ms", 15), bg="white", text="Correct answers: 0")
# lb1.grid(row=3, column=0, padx=0, pady=0, columnspan=2)
# lb2 = Label(font=("comic sans ms", 15), bg="white", text="Fail answers: 0")
# lb2.grid(row=4, column=0, padx=0, pady=0, columnspan=2)
# ent = Entry(font=("comic sans ms", 15), width=10)
# ent.grid(row=0, column=1)
# but = Button(font=("comic sans ms", 15), bg="red", width=10, text="Ответ", command=dd)
# but.grid(row=1, column=0, ipadx=0, padx=0, pady=0)
# but1 = Button(font=("comic sans ms", 15), bg="red", width=10, text="")
# but1.grid(row=1, column=1, ipadx=0, padx=0, pady=0)
#
# mainloop()

# from tkinter import *
#
#
# def create_window_with_question(name, x, y, question, correct_answer):
#     window = Tk()
#     window.title(name)
#     window.geometry(f"{x}x{y}")
#
#     def add_txt(elem):
#         main_txt.set(ent.get() + elem)
#
#     def solve():
#         main_txt.set(eval(ent.get()))
#
#     def clear():
#         main_txt.set("")
#
#     Label(text=question, font=("comic sans ms", 15)).grid(row=0, column=0)
#
#     main_txt = StringVar()
#
#     ent = Entry(font=("comic sans ms", 15), textvariable=main_txt)
#     ent.grid(row=0, column=1)
#
#     Button(text="7", font=("comic sans ms", 15), command=lambda: add_txt("7")).grid(row=1, column=1)
#     Button(text="8", font=("comic sans ms", 15), command=lambda: add_txt("8")).grid(row=1, column=2)
#     Button(text="+", font=("comic sans ms", 15), command=lambda: add_txt("+")).grid(row=1, column=3)
#     Button(text="C", font=("comic sans ms", 15), command=clear).grid(row=1, column=4)
#     Button(text="=", font=("comic sans ms", 15), command=solve).grid(row=1, column=5)
#
#     mainloop()
#
# create_window_with_question("First question", 700, 400, "What is the name of the longest river?", "Nyl")
# # create_window_with_question("Second question", 500, 400, "What is the name of the highest mountain?", "Everest")

# from tkinter import *
# import random
#
# # тут всі налаштування вікна
# window = Tk()
# window.title("daa")
# window.geometry("500x500")
# window.resizable(False, False)
#
# # тут всі змінні
# l_x = 180
# l_y = 180
# step = 5
#
# # # тут всі функції
# # def moving_up():
# #     global l_y
# #     l_y -= step
# #     label.place(y=l_y)
#
# # def moving_down():
# #     global b
#
# # def moving_left():
# #     global l_x
# #     l_x -= step
# #     label.place(x=l_x)
#
# # def moving_right():
# #     global b
#
# def move(side):
#     global l_y, l_x
#
#     if side == "right":
#         l_x += step
#
#     if side == "left":
#         l_x -= step
#
#     if side == "up":
#         l_y -= step
#
#     if side == "down":
#         l_y += step
#
#     label.place(x=l_x, y=l_y)
#     window.update()
#
# def asign():
#     data = entry.get()
#     if data:
#         entry.delete(0, END)
#         label_data['text'] += str(data) + "\n"
#
#
# # тут всі об'єкти і їх розміщення
# label = Label(text="Snake")
# # but_up = Button(font=("comic sans ms", 12, "bold", "underline"), command=moving_up, text="up")
# # # but_down = Button(font=("comic sans ms", 22, "bold", "underline"), command=moving_down, text="down")
# # but_left = Button(font=("comic sans ms", 12, "bold", "underline"), command=moving_left, text="left")
# # # but_down = Button(font=("comic sans ms", 22, "bold", "underline"), command=moving_down, text="down")
# label_data = Label(text="")
# button_ok = Button(text="Ok")
#
# entry = Entry()
#
# # тут всі розміщення
# label.place(x=l_x, y=l_y)
# # but_up.place(x=200, y=200)
# # # but_down.place(x=200, y=200)
# # but_left.place(x=155, y=240)
# # # but_down.place(x=200, y=200)
# entry.place(x=300, y=200)
# label_data.place(x=350, y=260)
# button_ok.place(x=430, y=195)
#
#
# # він завжди вкінці
# window.bind("<d>", lambda event: move("right"))
# window.bind("<a>", lambda event: move("left"))
# window.bind("<w>", lambda event: move("up"))
# window.bind("<s>", lambda event: move("down"))
# entry.bind("<Return>", lambda event: asign())
# button_ok.bind("<Button-1>", lambda event: asign())
#
# mainloop()

# from tkinter import *
# from resources.colors import colors_list as colors
#
# # тут всі налаштування вікна
# window = Tk()
# window.geometry("500x500")
#
# x, y = 100, 100
# size = 30
#
# label = Label(bg=colors[0])
# label.place(x=x, y=y, width=size, height=size)
#
# mainloop()

# from resources.colors import colors_list
# import random
# window = Tk()
# window.title("daa")
# screen_left = 0
# screen_right = 600
# screen_down = 400
# screen_up = 0
# window.geometry(f"{screen_right}x{screen_down}")
# window.resizable(False, False)
# x = 180
# y = 180
# label_size = 40
# step_x = 3
# step_y = 3
#
# i = 0
# len_list = len(colors_list) - 2
#
#
# def move():
#     global x, y, step_y, step_x, i, label_size
#     while True:
#         if x + label_size + 5 > screen_right or x - 5 < screen_left:
#             step_x *= -1
#             # label["bg"] = colors_list[i]
#             label_size += 2
#             x += step_x * 2
#             # i += 10
#         if y - 5 < screen_up or y + label_size + 5 > screen_down:
#             step_y *= -1
#             label_size += 2
#             # label["bg"] = colors_list[i]
#             y += step_y * 2
#             # i += 10
#         if i == len_list:
#             i = 0
#         x += step_x
#         y += step_y
#         i += 1
#         label["bg"] = colors_list[i]
#         label.place(x=x, y=y, width=label_size, height=label_size)
#
#         # залишає слід з тими ж налаштуваннями що і основний лейбл
#         Label(bg=colors_list[i]).place(x=x, y=y, width=label_size, height=label_size)
#
#         window.update()
#         window.after(5)
#
#
# label = Label(font=("Century", 10), background=colors_list[0])
# label.place(x=x, y=y, width=label_size, height=label_size)
# move()

# from tkinter import *
#
# def check_radiobuttons():
#     # if lbl['text'] != "":
#     #     lbl['text'] = ""
#     #     lbl.place(x=160, y=20)
#     txt = ""
#     if var.get() == 1:
#         txt = "Ви нажали на Київ"
#     if var.get() == 2:
#         txt = "Ви нажали на Одесу"
#
#     lbl['text'] = txt
#
#
# window = Tk()
# screen_right = 600
# screen_down = 400
# window.geometry(f"{screen_right}x{screen_down}")
#
# var = IntVar()     # var - змінна (IntegerVariable)
#
# r1 = Radiobutton(text="Київ", font=22, variable=var, value=1)      # Radiobutton - перемикач
# r1.place(x=20, y=20)
# r2 = Radiobutton(text="Одеса", font=22, variable=var, value=2)
# r2.place(x=20, y=40)
#
# Button(text="Ok", font=22, command=check_radiobuttons).place(x=120, y=40)
# lbl = Label(font=22, text='')
# lbl.place(x=160, y=20)
# mainloop()

# from tkinter import *
#
# window = Tk()
# screen_right = 600
# screen_down = 400
# window.geometry(f"{screen_right}x{screen_down}")
#
# # def f(txt):
# #     lbl['text'] = txt
# def im():
#     lbl['image'] = apercot
#
# apercot = PhotoImage(file="apercot.png")
# cantaloupe = PhotoImage(file="cantaloupe.png")
#
# lbl = Label(image="")
# lbl.place(x=10, y=10)
#
# # lbl['image'] = ""
#
# # f("this is a large text!!!!!!!!!!!")
# # f("this is small text")
# im()
# mainloop()

# from tkinter import *

# def dd():
#     text = ""
#     img = ""
#     if var.get() == 1:
#         text = "Ви вибрали кошку"
#         img = PhotoImage(file="apercot.png")
#     # if var.get() == 2:
#     #     text = "Ви вибрали собаку"
#     #     img =
#     # if var.get() == 3:
#     #     text = "Ви вибрали пташку"
#     #     img =
#     # if var.get() == 4:
#     #     text = "Ви вибрали курку"
#     #     img =
#     # if var.get() == 5:
#     #     text = "Ви вибрали черепашка"
#     lbl['text'] = text
#     lbl_image['image'] = img
#     lbl_image.place(x=300, y=90, width=50, height=50)
# def dd():
#     img = PhotoImage(file="apercot.png")
#     lbl_image = Label(image=img)
#     lbl_image.place(x=300, y=40)
#
# window = Tk()
# window.title("daa")
# screen_right = 600
# screen_down = 400
# window.geometry(f"{screen_right}x{screen_down}")

# var = IntVar()
#
# r1 = Radiobutton(text="Кішку", font=22, variable=var, value=1)
# r1.place(x=20, y=40)
# r2 = Radiobutton(text="Собачку", font=22, variable=var, value=2)
# r2.place(x=20, y=80)
# r3 = Radiobutton(text="Патушку", font=22, variable=var, value=3)
# r3.place(x=20, y=120)
# r4 = Radiobutton(text="Курку", font=22, variable=var, value=4)
# r4.place(x=20, y=160)
# r5 = Radiobutton(text="Черепашка", font=22, variable=var, value=5)
# r5.place(x=20, y=200)

# but = Button(text='OK', command=dd)
# but.place(x=20, y=240)

# lbl = Label(font=22, text="")
# lbl.place(x=300, y=40)

# # широта висота проблема з картинкою
# img = PhotoImage(file="apercot.png")
# lbl_image = Label(image=img)
# lbl_image.place(x=300, y=40)
# # dd()
# mainloop()

# from tkinter import *
# window = Tk()
# window.title("daa")
# screen_right = 600
# screen_down = 400
# window.geometry(f"{screen_right}x{screen_down}")
#
# img = PhotoImage(file="dog.png")
# lbl_image = Label(image=img)
# lbl_image.place(x=300, y=40)
#
# mainloop()

# from tkinter import *
# from random import shuffle
#
# def quiz(question, ans1, ans2, ans3, ans4, img):
#     def dd(img):
#         if var.get() == correct:
#             window.destroy()
#
#             window1 = Tk()
#             window1.geometry(f"{600}x{400}+{200}+{200}")
#             # print("Правильно")
#             img = PhotoImage(file=img)
#             Label(text="Правильно!").pack(ipadx=180, ipady=10)
#             Label(image=img).pack(ipady=100, ipadx=150)
#             window1.update()
#             window1.after(3000)
#             window1.destroy()
#
#     correct = ans1
#     answers = [ans1, ans2, ans3, ans4]
#     correct = ans1
#     shuffle(answers)
#
#     window = Tk()
#     window.geometry(f"{1000}x{600}")
#
#     Label(text=question, font=font).pack(ipady=40)
#
#     # img = PhotoImage(file=img)
#     var = IntVar()
#     c = 0
#     for ans in answers:
#         if ans == correct:
#             correct = c
#         Radiobutton(text=ans, font=low_font, variable=var, value=c).pack(ipady=15)
#         c += 1
#
#     # Radiobutton(text=ans1, font=low_font, variable=var, value=1).pack(ipady=15)
#     # Radiobutton(text=ans2, font=low_font, variable=var, value=2).pack(ipady=15)
#
#     Button(text="Answer", command=lambda: dd(img)).pack(ipady=30)
#
#
#     window.mainloop()
#
#
#
# font = "Calibri 24 bold"
# low_font = "Calibri 18 bold"
#
#
# quiz("Нажми на абрикос", "apercot", "plum", "apple", "orange", img="apercot.png")
# mainloop()
#
# # зробити програму quiz де буде для кожного питання вікно, картинка якщо правильно відповів, схоже на quiz questions

# from tkinter import *
#
# def quiz(quest, ans1, ans2, img):
#     def dd(img):
#         if var.get() == 1:
#             root.destroy()
#             root1 = Tk()
#             root1.geometry(f"{800}x{600}+{400}+{400}")
#             img = PhotoImage(file=img)
#             Label(text="Правильно").pack()
#             Label(image=img).pack()
#             root1.update()
#             root1.after(2000)
#             root1.destroy()
#     root = Tk()
#     root.geometry(f"{800}x{600}+{400}+{400}")
#
#     lbl = Label(text=quest)
#     lbl.pack()
#
#     var = IntVar()
#
#     Radiobutton(text=ans1, variable=var, value=1).pack()
#     Radiobutton(text=ans2, variable=var, value=2).pack()
#
#     Button(text="Ok", command=lambda: dd(img)).pack()
#
#     mainloop()
#
# quiz("Question", "ans1", "ans2", "apercot.png")
# quiz("Question", "ans1", "ans2", "apercot.png")



# s = "apples"
# print(s.count("p"))
#
# print("apples".count("p"))

# from tkinter import *
# window1 = Tk()
#
# window1.geometry(f"{600}x{800}+{200}+{200}")
#
# # Label(text="QUESTION1").pack(pady=80)
# #
# # Radiobutton(text="rdbtn").pack(pady=80)
# #
# # Button(text="button").pack()
#
# def d():
#     if var == correct:
#         print("Correct")
#     else:
#         print("not correct")
#
#
# main_canvas = Canvas()
# main_canvas.pack(pady=150)
# # canvas.place(x=400, y=400)
#
# canvas1 = Canvas(main_canvas)
# canvas1.pack(pady=10)
#
# # так ми знайдемо на якому індексі лежить правильна відповідь
# import random
# lst = [1,2,3]
# correct = lst[0]
# random.shuffle(lst)
# correct = lst.index(correct)
# print(correct)
#
# var = IntVar()
#
# Label(canvas1, text="QUESTION1").pack(pady=10)
# Radiobutton(canvas1, text="rdbtn", variable=var, value=0).pack(pady=5)
# Radiobutton(canvas1, text="rdbtn1", variable=var, value=1).pack(pady=5)
# Button(canvas1, text="button", command=d).pack(pady=10)
#
# canvas2 = Canvas(main_canvas, bg="black")
# canvas2.pack(pady=40, ipadx=100)
#
# Label(canvas2, text="QUESTION1").pack(pady=10)
# Radiobutton(canvas2, text="rdbtn").pack(pady=5)
# Radiobutton(canvas2, text="rdbtn1").pack(pady=5)
# Button(canvas2, text="button").pack(pady=10)
#
# mainloop()


# from temporary import *
# print(function_2())
# import temporary
# temporary.function_2()
# import temporary as temp
# temp.function_2()
# from temporary import function_name

# import tkinter as tk
# root = tk.Tk()
# label = tk.Label()
# label.pack()

# from random import randint, shuffle
# import random
# random.shuffle()

# from tkinter import *
#
# root = Tk()
#
# lst = [1, 2, 0, 1, 2, 3, 3]
#
# for i in range(len(lst)):     #
#     Button(text=lst[i]).pack()
#
# mainloop()


# def func(e):
#     return e+2
#
# print(func(2))
#
# a = lambda e: e+2
# print(a(2))

# from tkinter import *
#
# root = Tk()
#
# var = IntVar()
#
# Checkbutton(text="Я хочу отримувати пропозиції на пошту", variable=var).pack()
# # Checkbutton(text="Я не хочу отримувати пропозиції на пошту", variable=var, onvalue=0).pack()
# # Button(text="Ok", command=lambda: print("Він натиснув так" if var.get() == 1 else "Він натиснув ні")).pack()
#
# def func():
#     if var.get() == 1:
#         print("Він натиснув так")
#     elif var.get() == 0:
#         print("Він натиснув ні")
# Button(text="Ok", command=func).pack()
#
# # var1 = IntVar()
# # Checkbutton(text="Вам є 18 років?", variable=var1).pack()
# #
# # def func():
# #     if var1.get() == 1:
# #         print("Йому є 18")
# #     elif var1.get() == 0:
# #         print("Йому немає 18")
# # Button(text="Ok", command=func).pack()
#
# mainloop()

# # коли натискаєш на чекбаттон з'являється лейбл, а коли відтискаєш - зникає
# from tkinter import *
#
# def create_lbl_with_mail(event):
#     global lbl
#     if var.get() == 0:
#         lbl = Label(text="This is mail")
#         lbl.pack()
#     if var.get() == 1:
#         lbl.destroy()
#
# Label(text="This is random text").pack()
# var = IntVar()
# check = Checkbutton(text="Створити лейбл", variable=var)
# check.pack()
#
# check.bind('<Button-1>', create_lbl_with_mail)
#
# mainloop()


# from tkinter import *
#
# def func():
#     # тут запихаємо інфу з ентрі в файл
#     if var.get() == 1:
#         # тут запихаємо інфу з чекбаттона в файл
#         print("Йому є 18")
#     elif var.get() == 0:
#         # тут запихаємо інфу з чекбаттона в файл
#         print("Йому немає 18")
#
# root = Tk()
# var = IntVar()
#
# canvas = Canvas()
#
# # зпакували через side, все вказуємо по черзі вліво
# Label(canvas, text="Прізвище:").pack(side="left", padx=15)
# Label(canvas, text="Ім'я:").pack(side="left", padx=15)
# Label(canvas, text="По батькові:").pack(side="left", padx=15)
#
# # # згрідили через колонки
# # Label(canvas, text="Прізвище:").grid(row=0, column=0, padx=15)
# # Label(canvas, text="Ім'я:").grid(row=0, column=1, padx=15)
# # Label(canvas, text="По батькові:").grid(row=0, column=2, padx=15)
#
#
# canvas.pack()
#
# # ще один канвас для ентрі
#
# # присвоюєш ентрі щоб тоді отримати з них інфу
# entry_name = Entry()
# = Entry()
# = Entry()
#
# # спаковуєш все по черзі вліво і виставляєш відступи (padx)
# entry_name.pack()
#
#
# Checkbutton(text="Вам є 18 років?", variable=var).pack()
#
#
# Button(text="Ok", command=func).pack()
#
#
# mainloop()

# from tkinter import *
# from tkinter import messagebox
#
# def ok():
#     if name.get().isalpha() and surname.get().isalpha() and entry2.get().isalpha():
#         file = open("form data.txt", "a")
#         file.write(f"\nName: {name.get()}\n")
#         file.write(f"Surname: {surname.get()}\n")
#         if var.get() == 1:
#             file.write("More than 18: True\n")
#         else:
#             file.write(f"More than 18: False\n")
#         messagebox.showinfo("it is fine", message="We got your data, thanks")
#     else:
#         messagebox.showinfo("problem detected", message="Check your info")
#
#
#
# root = Tk()
#
# name = Entry()
# name.pack()
# surname = Entry()
# surname.pack()
# entry2 = Entry()
# entry2.pack()
#
# var = IntVar()
# Checkbutton(variable=var).pack()
# Button(command=ok, text="ok").pack()
#
# mainloop()


# описати як зробити зникнення чекбаттона
# WomWom
# https://www.figma.com/file/fgskrF6bKpJHzaasPcXzMx/WomWom?type=design&node-id=0-1&mode=design&t=OggSDCJ5vcjYMAzT-0
# пейнт


### FILE ###
# file = open("назва файлу.розширення", "спосіб відкриття")
# "назва файлу.розширення" - тут вказується адреса до файлу якщо він уже є або де він має бути,
#                                                           якщо не має бути разом з програмою
#                                     якщо разом з програмою - то вказується просто ім'я файлу
#                   наприклад: "text.txt", "file.docx", "excel.rtf" - просто ім'я з типом файлу
#                              "C:\\Users\\Georgiy\\form data.txt" - адреса, ім'я, тип (\\)

# file = open("C:\\Users\\Georgiy\\form data.txt", "r")
# file = open("C:\\Users\\vladb\\PycharmProjects\\pythonProject2\\Masha_and_Sasha\\odd_numbers.txt")
# file = open("form data.txt", "w+")
# file.write("asd")
# "спосіб відкриття" - вказуємо для чого відкриваємо файл:
#                      "r" - для читання (read)
#                      "w" - для запису (write). Вся інфа з файлу видаляється при відкритті
#                      "a" - для запису в кінець файлу (append)
#                      "r+" - відкриває для читання і запису. Інфу не удаляє
#                      "w+" - відкриває для читання і запису. Інфу удаляє

# функція яка записує інфу в файл. Не переносить на новий рядок, треба вручну через \n
# file.write(f"{entry2.get()}\n")


# words api

# parsing site