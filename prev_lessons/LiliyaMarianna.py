# ctrl + / - commenting
# win + shift + s - for print screen
# variable var
# print in console each of 4 types we've learned
# a = 5           # int  Integer
# txt = "apple"   # str  String
# num = 5.0       # float
# bool = True     # bool boolean
# print(type(a))


# a = "today"
# num = 5
# print(a + ".")      #             sum
# print(num - 1)      # subtraction sub
# print(num * 4)      # multiplying mult
# print(num / 2)      # division    div

# num += 1
# num -= 1
#
# num *= 3
# num /= 2


# TYPE CAST         - перетворення типу
# int()       # to integer
# str()       # to string
# input()     # user in

# num = '1'     # to 1
# num = 2.8       # to 2
# num = 1       # to 1
# num = '33'      # to 33
# num = 'a'     # ValueError
# num = input()
# num = True
# print(int(num))

# txt = 2.5       # to '2,5'
# txt = True      # to 'True'
# print(str(txt))
# num = int(input())
# num1 = int(input())
# sum = num + num1
# print(num, "+", num1, "=", sum)
# print(f"{num} + {num1} = {num + num1}")
# print("{0} + {1} = {2}".format(num, num1, sum))
# 5 + 6 = 11

# ValueError(TypeError)  - помилка значення
# num = int("2")

# IndentationError (IndentError) - неочікуваний відступ
#                         num = 4

# Redundant variables - непотрібні змінні
# age = input("fill in your age")
# print(f"Hello, {input('fill in your name ')}.\nUr age: {input('ur age ')}")

# boolean   True   False

# True False
#   1    0

# >
# and or  &  ||(|)
# x = int(input())
# if x > 5 and x < 10:               # if
#     print("6..9")
# elif x == 5:                # else if
#     print(0)
# else:
#     print(-1)

# x, y
# if
# if
# if

# > < >= <= != ==
# if x == 5:
#     print()
# first = int(input("..."))

# if True:
#     print(1)
# x = int(input())
# print("parne" if x % 2 == 0 else "this is zero" if x == 0 else "neparne")
# print('parne') if int(input()) % 2 == 0 else print("neparne")

# if x % 2 == 1:
#     print("neparne")
# elif x == 0:
#     print("this is zero")
# else:
#     print("parne")

# print(0 if 0 % 2 == 0 else 1)

# ans = input("Morty?").lower()
# if ans == "morty":
#     print(True)
# else:
#     print(False)
# input()


# # embedded or nested
# if 5 > 2:
#     print("5 > 2")
# elif 5 == 2:
#     print("5 == 2")
# else:
#     print('5 < 2')

# num1 = 10
# num2 = 0
# op = "/"
# if op == "/":
#     if num2 != 0:
#         print(num1 / num2)
# if op == "*":

# all = 32
# items = input()
# if items_order < 32:
#     =1:
#         print("1 item")
#     else:
#         print(f"we will need {int(x / 10) + 1} packages to full this")
# else:
#     print("in stock 32. resupply...")
#
# # _______________________________
# # hello
# print("hi, I am bot...")
# # rules
# print('''I can:
#                 1. run
#                 2. jump
#                 3. calculator   (calc)
#                 4. fast calculator
#                 ....
# ''')
# a = input("вибираєш?").lower()
# if a == 'run' or a == '1':
#     print(".....")
# ....
# if a == '3' or a == 'calc':
#     op = input("")
#     num1 =
#     num2 =
#     if op == "+":
#         print("+")
#     if op...
#
# # bye

# # і це і це
# True and True   - виводить
# False and True    - не виводить
# False and False   - не виводить

# # або це або хоч це
# True or True    - виводить
# True or False   - виводить
# False or False  - не виводить

# # Iterator, counter, Iterations
# counter = 0
# while counter < 5:
#     print(counter)
#     print("Hello world")
#     counter += 1

# zag = "At winter and summer it colors the same"
# print(zag)
# ans = input()
# while ans != "christmas tree":
#     print("Wrong\n")
#     print(zag)
#     ans = input()
# print("U matched")

# user_in = input("number? 1 - 4")
# while True:
#     try:
#         user_in = int(user_in)
#         if user_in <= 0 or user_in >= 5:
#             print("1-4")
#             continue
#         break
#     except ValueError:
#         user_in = input("number? 1 - 4")


# while user_in <= 0 or user_in >= 5:
#     user_in = input("1-4")

# user_in = int(user_in)
# if user_in > 2:
#     print()
# if False and True:
#     print(1)

# c = 0
# while c < 10:
#     c += 1
#     if c == 7:
#         continue
#     print(c)

# user = input("?\n")
# while user != 'stop':
#     print("I can..")
#     print("U pick....")
#     if user == '1':
#         print(1)
#     user = input("?\n")

# i, j = int(input("від:")), int(input("до:"))
#
# while i <= j:
#     i += 1
#     if i % 2 == 1:
#         print(f"{i} - Odd")

# i, j = int(input("від:")), int(input("до:"))
#
# while j >= i:
#     j -= 3
#     print(j)

# break continue in while
# else in while
# capital with hints

# embedded


# counter = 0
# while counter != 3:
#     counter += 1
#     ans = input("Назвіть єдине вцілівше із чудес світу\n").lower()
#     if ans == 'піраміда хеопса':
#         print("вірно")
#         print(f"тобі знадобилось {counter} спроб")
#         break
#     print("невірно")
#     if counter == 1:
#         print("це в Єгипті")
#
# if counter == 3:
#     print("ти програв")

# c = 0
# while c < 10:
#     c += 1
#     print(c)
#     if c == 5:
#         break
# else:
#     print(True)

# iterator
# for z in range(10):
#     print(z)
# for z in range(5, 25):
#     print(z)

# for z in range(int(input()), int(input())+1):
#     if z == 5:
#         continue
#     print(z)

# for z in range(int(input()), 50):
#     if z % 2 == 0:
#         for x in range(z, 50, 2):
#             print(x)
#         break

# for num in range(1, 10, 3):
#     print(num)

# c = 0
# for letter in 'Hello, I am ...':
#     if letter == " ":
#         c += 1
#     print(letter)
# print(c, "слів")

# # 2 випадки використання while
# user = input("?\n")
# while user != 'stop':
#     print("I can..")
#     print("U pick....")
#     if user == '1':
#         print(1)
#     user = input("?\n")

# while True:
#     print()

# range step, continue, break, else, sum, factorial , if in for,  skip letter in word,

# for z in range(1, 10, 2):
#     if z > 5:
#         continue
#     print(z)

# user_num = int(input("?\n"))
# for num in range(3, 33, 2):
#     if num > user_num:
#         break
#     print(num)
# else:   # ЯКЩО НЕ ЗАКІНЧИВСЯ ЦИКЛ З BREAK, ТО РОБИМО ELSE
#     print("діапазон пройдено, break не спрацював")

# накопичувач
# Sum = 0
# for z in range(1, 10+1):
#     print(f"{Sum} + {z} = {Sum+z}")
#     Sum += z
# print(Sum)

# dob = 1
# for z in range(1, 10+1):
#     print(f"{dob} * {z} = {dob*z}")
#     dob *= z
# print(dob)

# # check 3
# i = 0
# num = 33
# if str(num).count('3') > 0:
#     i += 1
# ______________________
# i = 0
# num = 44
# if '3' in str(num):
#     i += 1
# print(i)
# підрахувати кількість чисел що містять в собі 3 від 1 до 100

# print(len('car'))

# row = "Hello I am car"
# word = input("?\n")     # car
# word_len = len(word)
# for z in row:
#     if z == word[0]:    # c
#
#     print(z)
# вивести текст по букві без слова яке написав юзер

# row = "Hello I am car"
# word = input("?\n")     # car  word[0] = c   word[1] = a
# word_len = len(word)    # 3
# c = -1
# for z in row:
#     if z == word[0]:    # z == 'c'
#         c += 1
#     if -1 < c <= word_len:
#         c += 1
#         continue
#     print(z)

# c = 0
# for z in range(1, 1000+1):
#     z_str = str(z)
#     if '3' in z_str:
#         c += z_str.count('3')
# print(f"3 is mentioned between 1 and 1000 {c} times")

# 1 - перший
# 2 - другий
# 3 - перший
# ...

# for z in range(1, int(input("до скількох?"))+1, 2):  # 1,3,5,7,9... - непарні(перші)
# print(f"{z} - перший\n{z+1} - другий")

# порахувати скільки разів зустрічається 3 в діапазоні від 1 до 1000

# # module (packages)

# # 1 - майже завжди, підключає всі функції
# import random
# print(random.randint(1, 10))

# # 2 - небагато функцій (1-3), які багато разів використовуються
# from random import randint, shuffle, choice
# print(randint(1, 10000))

# # 3 - коли дуже багато разів використовується 1 функція(не робити так(мені можна))
# from random import randint as rdi
# print(rdi(1, 1000))

# # 4 - найгірший(тільки з черепашкою)
# from turtle import *
# fd(1000)
# done()

# # 5 - найкращий
# import random as rd
# rd.randint(1, 1000)

# import numpy as np
# np.arange()

# import random as rd
#
# num = rd.randint(1, 10)
# tries = int(input("скільки спроб"))
# attempts = 0
# while attempts < tries:
#     # num check
#     while True:
#         try:
#             user = int(input("NUM?\n"))
#             break
#         except ValueError:
#             print("Need ints")
#     attempts += 1
# # check if bigger or less
#     if num > user:
#         print("try bigger")
#     # if <
#     if num == user:
#         print("correct")
#         print(f"u guessed with {z+1} tries")
#         break
# else:
#     print("u lost")

# n = 0
# for z in range(1, 1001):
#     z_str = str(z)
#     n += z_str.count('3')
#
# print(f"3 in range(1,1000) is figured {n} times")

# # Strings
# txt = 'Still remember? Always.'
# # positive indexing
# print(txt[2])
# # negative indexing
# print(txt[-2])
# # slice
# print(txt[:5])
# print(txt[:-2])
# # step
# print(txt[2::2])
# print(txt[1::2])
# # neg slice
# print(txt[::-1])
# print(txt[::-2])
# print(len(txt))

# txt = 'Still remember? Always.'
# len(txt)            100 %
# txt.count('s')      x   %

# for elem in txt:
#     if elem == 'e':
#         print(elem, end=' ')


# for elem in range(len(txt)):
#     if elem % 3 == 0 and txt[elem] == 'e':
#         print(txt[elem], end=' ')
#
# print()
# print(txt[3::3])
#        012345

# txt = 'today was a great morning'       # перебор іднекса елемента
# for l in range(1, len(txt)):
#     if l % 5 == 0:
#         print(txt[l])
# print(txt[5::5])

# Q5. Accept the number of days from the user and calculate the charge for library according to following:
#
# Till five days : Rs 2 hruvni /day.
#
# Six to ten days  : Rs 3/day.
#
# 11 to 15 days  : Rs 4/day
#
# After 15 days    : Rs 5/day


# def is_valid_triangle(a, b, c):
#     if a + b >= c and b + c >= a and c + a >= b:
#         return True
#     else:
#         return False
#
#
# # Reading Three Sides
# side_a = int(input('Enter length of side a: '))
# side_b = int(input('Enter length of side b: '))
# side_c = int(input('Enter length of side c: '))
#
# # Function call & making decision
#
# if is_valid_triangle(side_a, side_b, side_c):
#     print('Triangle is Valid.')
# else:
#     print('Triangle is Invalid.')

# # 1 3 5 7 9
# x = int(input("from?"))      #1
# y = int(input("step"))       #2
# z = int(input("how much"))   #5
# for i in range(z):
#     print(x)
#     x += y

# # Q2. Find errors in the following code:
# #
# a = int(input("“Enter any number”"))
# for i in range(2, 6):
#     if a == i:
#       print("“A”")
#     else:
#       print("“B”")

# a=True
# b=True
# c=False
# d=True
# 1.         print(c)
# 2.         print(d)
# 3.         print(not a)
# 4.         print(not b )
# 5.         print(not c )
# 6.         print(not d)
# 7.         print(a and b )
# 8.         print(a or b )
# 9.         print(a and c)
# 10.       print(a or c )
# 11.       print(a and d )
# 12.       print(a or d)
# 13.       print(b and c )
# 14.       print(b or c )
# 15.       print(a and b or c)
# 16.       print(a or b and c )
# 17.       print(a and b and c)
# 18.       print(a or b or c )
# 19.       print(not a and b and c)
# 20.       print(not a or b or c )
# 21.       print(not (a and b and c))
# 22.       print(not (a or b or c) )
# 23.       print(not (True and not (True and not False)))
# 24.       print(not a or not b or not c )
# 25.       print(not (not a or not b or not c))


# діапазон ввиведення в рядку [0:5:2]
# range(len(str))
# statistic of letter in txt
# #1 collection, lists
# html


# дати задачу з відділенням частин від почти і функції з w3

#
# Q1. Write the output of the following:
#
# 1.
# for i in "Myblog":
#     print(i, '?')
#
# Show Answer
#
#
# 2.
# for i in range(5):
#     print(i)
#
# Show Answer
#
#
# 3.
# for i in range(2, 7):
#     print(i)
# Show Answer
#
#
# for i in "csiplearninghub":
#     print(i)
# Show Answer
#
#
# 5.
# for i in "python":
#     # print(i, 2, end='e\n', sep='s ') # separator
#     print(f"{i} - {2}", end="")
# Show Answer
#
#
# Q2. Write a program to print first 10 natural number.
# for i in range(1, 11):
#     print(i)

# Show Answer
#
#
# Q3. Write a program to print first 10 even numbers.
# for i in range(2,22,2):
# for i in range(0,22,2):
#     print(i)

# Show Answer
#
#
# Q4. Write a program to print first 10 odd numbers.
# for i in range(1,21,2):
#     print(i)
# Show Answer
#
#
# Q5. Write a program to print first 10 even numbers in reverse order.
# Show Answer
# for i in range(21,1,-2):
#     print(i)
#
#
# Q6. Write a program to print table of a number accepted from user.

# Show Answer
#

# Q8. Write a program to find the factorial of a number.

# Show Answer
#
#
# Q9. Write a program to find the sum of the digits of a number accepted from user
# a = int(input())
# first = a // 1000
# second = a // 100 % 10
# third = a % 100 // 10
# fourth = a % 10
# print(first)
# print(second)
# print(third)
# print(fourth)

# num = int(input("Enter any number"))
# s = 0
# while num != 0:
#     r = num % 10
#     s = s + r
#     num = num // 10
# print("Sum of digits is", s)
#
# num = input("Enter any number")
# s = 0
# for letter in num:      # 1234
#    s += int(letter)
#
# print(s)


# Show Answer *
#
#
# Q10. Write a program to check whether a number is prime or not.
# Show Answer **

# for num in range(1,5):
#
#     for i in range(1, num + 1):
#         print(i, end=' ')
#     print(end="\n")
#
# for num in range(1,5):
#
#     for i in range(1, num + 1):
#         print(i, end=' ')
#     print()

# string slicing    (indexing)
# txt = "Hello It is me"
# print(txt[5:10:3])
# range(5, 10, 5)
# mail = 'vladbondar493@gmail.com'
#
# mail1 = 'ddddd123456@ukr.net'
#
# print(mail1[:30])

# for elem in mail1:
#     if elem == "@":
#         break
#     print(elem, end='')

# mail1_sobch = 0
# for ind in range(len(mail1)):
#     if mail1[ind] == "@":
#         mail1_sobch = ind
#         print(f"@ in the index: {ind}")
#         break
#     # print(mail1[ind], end="")
# print(mail1[:mail1_sobch])
# print(mail1[mail1_sobch+1:])
# string[]
# funcs fo, mails cut


# str1 = 'MyBLog'
# a = len(str1)
# for i in range(a):
#     print((i+1) * str1[i])

# s = 'My'
# s1 = 'Blog'
# s2 = s[:1] + s1[3:]   # mg
# print(s2)

# x = "Blog"
# y ='7'
# for z in range(10):
#     x.join(y)
#     x += y
# print(x)

# https://csiplearninghub.com/practice-questions-of-string-in-python/


# string = "laeHJLogiko"
# str1 = string[-9] + string[-2] + string[4] + string[:1] + string[-2]
# str2 = string[5:7] + string[-3] + string[-4]
# str3 = string[7:8] + string[1]
# print(str1 + string[-1] + str2 + str3)

# slice thisisdefinetly.mail@gmail.com to the parts (vars)
# print out random number 0..1 10 times. print how much times which num is generated, make the test 10 times with one start up    if rdi == 1: c += 1

# capitalize()    # перший елемент ВЕЛИКИЙ

# import time
# for z in range(10,-1, -1):
#     time.sleep(0.1)
#     print(f"hacking Pentagon in {z}...")
# print("Wakey Wakey it's time for schoool")

# while True:
#     num = input("Number?\n")
#     if num.isdigit():
#         num = int(num)
#         print("It is a num")
#         break
#     else:
#         print("Error! Input a num")

# while True:
#     try:
#         num = int(num)
#         break
#     except ValueError:
#         print("Error! Input a num")
#         num = input("Number?\n")
# print("It is a num")

# https://www.w3schools.com/python/python_strings_methods.asp
# let fo what is working and how with comms and then explain to me
# some info of lists(index, compare to strs, how looks, what can do, other collections)
# same as strs
# txt = "123123123123"
# a = txt.count("1")
# print(a)

# txt = "H\te\tl\tl\to"
# # print(txt)
# x = txt.expandtabs(0)
#
# print(x)

# txt = "Hello, welcome to my world."
#
# x = txt.index("!")
#
# print(x)

# myDict = {"name": "John", "country": "Norway"}
# mySeparator = "TEST"
#
# x = mySeparator.join(myDict)
#
# print(x)
# a = 1
# b = 2
# c = [z**2 for z in range(100) if z % 2 == 0]
# print(c)

# mylist = ["apple", "banana", "cherry"]
# #ordered - всі елементи проіндексовані(apple з індексом 0)
# print(mylist[0])
# print(mylist[-1])
# ## index error
# # print(mylist[5])
# # changable (змінні елементи)
# mylist[0] = 1
# print(mylist)
# #allow duplicate values
# mylist = ["apple", "banana", "cherry", "apple", "banana", "cherry"]
# print(mylist)


# x, y = 1, 2
# l = ('cherry', 'watermelon', 'strawberry', 'cherry')
# l = list(l)
# l[0] = 1
# # indexing - звернення по номеру елемента(індексу)
# print(l[0:3])
# l[0] = "raspberry"
# print(l)


# # tuple - кортеж
# t = (1, 2, 3, 1)
# # # t[-1]
# # print(t[0])
# # # unchangable
# # # t[0] = "raspberry"
# # print(t)
# t = list(t)
# t[0] = 4
# t = tuple(t)
# print(t)

# s = [z for z in range(5)]
# s = [1, 2, 3, 1, 3, 3, 3, 3, 3, 3]
# print(s)
# print(set(s))
# s = set(s)
# print(s)
# # unordered, unchangeable, and unindexed
# del s[0:6]
# a = 2
# del a
# print(a)
# s.pop(0)
# s.remove(3)
# print(s)

# print(s)
# print(frozenset((1, 2, 3)))         # найменша колекція(за пам'яттю)
# not indexed
# s[0]

# d = {1: 1,
#      2: 2,
#      3: 3}
#      0  1  2             -1
# lst = [2, 3, 4, 5, 6, 7, 8, 9]
# print(lst)
# # СПИСКИ
# I
# set(lst)
# length_lst = len(lst)
# print(f"Довжина списку {lst}: {length_lst} елементів")
# print(f"сумма всіх елементів: {sum(lst)}")

# II    self - не чіпаємо
# lst.append("apple")
# lst.clear()
# lst.insert(2, 10)
# print(lst.count(4))
# fruits = ['apple', 'banana', 'cherry']
#
# cars = ['Ford', 'BMW', 'Volvo']

# fruits.extend(cars)
#
# print(fruits+cars)
#
# print(lst.index(8))

# a = lst.pop(5)
# lst.remove(2)
# lst_copy = lst.copy()
# lst_copy = lst
# print(lst_copy)

# lst.reverse()
# print(reversed(lst))
# print(lst[::-1])

# lst.sort(reverse=True)
# print(lst)
# lst = [5, 6, 7, 8, 9, 5]
# # # перебор по елементах
# c = 0
# for elem in lst:
#     if elem == 5:
#         c += 1
# print(c)

# print(lst)


## запитувати у юзера стільки елементів скільки він вкаже, кожен елемент додавати в список. Після цього вивести 2 списки:
## перший: тільки з не цифрами, другий тільки з цифрами(всі елементи повинні бути перетворені в int і відсортовані)
# l = []
# l_nums = []
# l_abc = []
# count = int(input("how much"))
# for z in range(count):
#     l.append(input("What?"))
# print(l)
# for elem in l:
#     if тут перевірка чи це число:
#         l_nums.append()

# int(elem) - перетворення в elem

# # tell about locale

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

# s = "TajMahal"
# print(list(s))


## 0-1 random
# # locale
# import locale
# import random as rd
# import time
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

# print("Odd" if int(input()) % 2 == 1 else "even")

# l = [x for x in range(10)]

# print(l)

# s = []
# for x in range(10):
#     s.append(x)
#
# print(l)
# print(s)

# num = 1111
# print([c for c in range(num, num*3+1) if c % num == 0])

# # bot with games (languages)
# l = []
# while True:
#
#     ans = input("?\n")
#     if ans == "exit":
#         break
#     if ans in l:
#
#     l.append("1")

# l = "3"
# l = int(l)
# print(l)


# ans = input("?\n")
# while ans != 'exit':


# #1
# 1. Заповніть список елементами в діапазоні від i до j (їх вам вказує юзер)
# 2. виведіть з цього списку елементи які кратні 3
# 3. виведіть з цього списку елементи які кратні 5

# lst = []
# lst_3, lst_5 = [], []
# for c in range(int(input("From")), int(input("To"))+1):
#     lst.append(c)
# print(lst)
# for elem in lst:
#     if elem % 3 == 0:
#         lst_3.append(elem)
#     if elem % 5 == 0:
#         lst_5.append(elem)

# # [(що додаємо) (в якому діапазоні/списку) {при яких умовах}]
# a, b = int(input("From")), int(input("To"))+1
# lst = [c for c in range(int(input("From")), int(input("To"))+1)]
# lst_3 = [elem for elem in lst if elem % 3 == 0]
# lst_5 = [elem for elem in lst if elem % 5 == 0]
# print(lst_3, lst_5)

# from random import randint
# for elem in [randint(1, 10) for c in range(10)]:
#     if elem % 2 == 0:
#         print(elem)

# lst = [randint(1, 10) for c in range(10)]
# # приклад зміни того що записуємо в список і приклад створення списку(в дз так само)
# print([c**2 for c in lst if c == 2 or c == 3])

# lst_sorted = lst.copy()
# lst_sorted.sort()
# lst_2 = []
# for c in lst_sorted:
#     if c % 2 == 0:
#         lst_2.append(c)
# print(lst_2)
# print(lst)
#
# print([elem for elem in sorted(lst) if elem % 2 == 0], "\n", lst)

# # звернення до індексів елементів в циклі for
# print(lst)

# # ind < ind + 1
# for ind in range(len(lst)-1):
#     if lst[ind] < lst[ind+1]:
#         print(lst[ind])
# # ind > ind - 1
# print()
# for ind in range(1, len(lst)):
#     if (lst[ind] > lst[ind-1]):
#         print(lst[ind])
#
# print([lst[ind] for ind in range(1, len(lst)) if lst[ind] > lst[ind-1]])


# # це копія але тут показано синтаксис and
# for ind in range(1, len(lst)):
#     if (lst[ind] > lst[ind-1]) and True:
#         print(lst[ind])
#
# print([lst[ind] for ind in range(1, len(lst)) if lst[ind] > lst[ind-1] and True])

# from random import randint
# ls = [randint(-100, 100) for z in range(10)]
# print([elem for elem in ls if elem % 3 == 0])
# print([11 % elem for elem in ls])
# print([ls[ind] for ind in range(len(ls)) if ls[ind] * ls[ind-1] > 0])
# print([ls[ind] for ind in range(len(ls)) if (ls[ind] > 0 and ls[ind-1] > 0) or (ls[ind] < 0 and ls[ind-1] < 0)])


# # map with phone number
# number = input("?")
# number = list(number)
# # number = [int(elem) for elem in number]
# number = list(map(int, number))
# print(number)

# lists bot improvement
# list generators tasks(189)


# vars (300)


# g = []
# s = []
# d = []
#
# while True:
#     ans_1 = input("Which list do u pick?{g\s\d}")
#     if ans_1 == "stop":
#         break
#     elif ans_1 == "list":
#         print(g, s, d)
#     elif ans_1 == "g":
#         print("picking g list")
#         while True:
#             ans = input("?")
#             if ans == 'stop':
#                 break
#             elif ans == 'list':
#                 print(g)
#             elif ans in g:
#                 print("already in list")
#             else:
#                 g.append(ans)
#     elif ans_1 == "s":
#         print("picking s list")
#         while True:
#             ans = input("?")
#             if ans == 'stop':
#                 break
#             elif ans == 'list':
#                 print(s)
#             elif ans in s:
#                 print("already in list")
#             else:
#                 s.append(ans)
# print("Program has ended")

# вивести прізвища і варіанти для контрольної
# 1) варіанти не повинні повторюватись
# 2) варантів стільки ж, скільки й прізвищ
# 3) варіанти кожного разу випадкові
# Шевченко - 2
# Франко - 4
# Рильський - 1
# Подрев'янський - 5
# Коцюбина - 3
# import random
# x = ["Шевченко", "Франко", "Рильський", "Подрев'янський", "Коцюбина"]
# a = x.pop()
# print(a)


# #3
# на вхід отримується номер телефону як рядок. Вам потрібно перетворити його в список з int елементів
# #3.1*
# тепер на вхід дається номер телефону з + спочатку +3806532453
# number = input("?")
# number = list(number)
# if "+" in number:
#     # number.pop(0)
#     number.remove("+")
#     # del number[0:5]
#
# number = list(map(int, number))
# print(number)
# print()

# from turtle import *
# import turtle as t
# from turtle import forward, left, right
# for z in ['red', 'blue', 'green', 'black']:
#     color(z)
#     fd(100)
#     rt(90)
# done()

# colors = ['red', 'blue', 'green', 'black']
# for z in range(4):
#     color(colors[z])
#     pensize((z+1)*2)
#     fd(100)
#     rt(90)
# done()

# from turtle import *
#
#
# def ship(col, wid, num):     # тут аргументи які функція хоче прийняти
#     for z in range(num):
#         color(col)
#         speed(0)
#         width(wid)
#         pendown()
#         forward(50)
#         left(135)
#         forward(70)
#         left(135)
#         forward(50)
#         color("green")
#         width(3)
#         right(90)
#         forward(50)
#         left(135)
#         forward(50)
#         left(45)
#         forward(80)
#         left(45)
#         forward(50)
#         left(135)
#         forward(110)
#         left(180)
#         penup()

# goto(100,200)
# pu()
# pd()
# c = "black"
# ship(c, 7)  # аргументи які функція вона отримує
# ship("red", 4)
# for z in range(10):
#     ship()
#     forward(100)
# for z in range(5):
#     ship("red", 4)
#     lt(90)
# ship("yellow", 6, 1)
# ship("black", 6)
# ship("red", 6)

# done()

from turtle import *

# def ship():
#     color("red")
#     width(4)
#     forward(50)
#     left(135)
#     forward(70)
#     left(135)
#     forward(50)
#
#     color("red")
#     width(3)
#     right(90)
#     forward(50)
#     left(135)
#     forward(50)
#     left(45)
#     forward(80)
#     left(45)
#     forward(50)
#     left(135)
#     forward(110)
#     left(180)
#
# speed(0)
# for x, y in ((-100, -100), (-100, 100), (100, -100), (100, 100)):
#     ship()
#     penup()
#     goto(x, y)
#     pendown()
# done()

# def triangle(side):
#     for z in range(3):
#         fd(side)
#         lt(120)
#
#
# def square(side):
#     for z in range(4):
#         fd(side)
#         rt(90)
#
#
# def house():
#     triangle(100)
#     square(100)
#
#
# speed(0)
# house()
# pu()
# goto(150, 0)
# pd()
# house()
# done()

# for z in (1, 2, 3, 4, 5):
#     print(z)

# a = [True, 1, [1, 2], "asd"]
# l = [[1, 2], [2, 3], [3, 4]]
# t = ((-100, -100), (-100, 100), (100, -100), (100, 100))
# t = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# print(t[2])

# x, y = (4, 40)

# print(x, y)

# from turtle import *
# a = int(input("Number?"))
# color("red")
# lt(90)
# fd(100)
# rt(90)
#
# lt(45)
#
# speed(0)
# for z in range(a):
#     fd(30)
#     rt(90)
#     fd(30)
#     lt(90)
# rt(45)
#
# rt(90)
# fd(100)
# lt(90)
#
# lt(180)
## БЕЗ
## goto(0,0)
## придумайте як повернутися

# done()


# from turtle import *  # DEREVSAD
#
#
# def derevo():
#     color("brown")
#     width(17)
#     left(90)
#     fd(150)
#     lenght = 10
#     for i in range(26):
#         width(10)
#         color("Green")
#         fd(lenght)
#         lenght += 5
#         left(90)
#     penup()
#     fd(150)
#     lt(90)
#     pendown()
#
#
# def sad():
#     speed(0)
#     for x, y in ((-200, 50), (-100, -50), (0, 50), (100, -50), (200, 50)):
#         penup(); goto(x, y); pendown()
#         derevo()
#     done()
#
#
# sad()

# making village
# firecrackers

# def func(a, b=3, c=3):
#     return a + b + c
#
#
# print(func(1, c=2, b=3))
#
#
# def func(a=('\n',), b=3, c=2):
#     return a
#
#
# print(func((1, 2, 3)))

from turtle import *


def build(floors, windows, window_size, coors=(0,0)):
    raws, columns, side, space = floors, windows, window_size, window_size/2
    vert_space = space * 3
    speed(0)
    pu()
    goto(coors[0], coors[1])
    lt(90); fd(space*2); rt(90); fd(space*2)
    pd()
    for raw in range(raws):
        for column in range(columns):
            for _ in range(5):
                fd(side); lt(90)
            rt(90)
            pu(); fd(space); pd()
        pu()
        backward(columns * side + columns * space)
        lt(90); fd(vert_space); rt(90)
        pd()
    pu(); goto(coors[0], coors[1]); pd()

    for _ in range(2):
        fd(space * 3 + columns * side + space * columns)
        lt(90)
        fd(space * 2 + raws * side + space * raws)
        lt(90)


window = Screen()
window.setup(1500, 700)
#
# build(10, 5, 15, (-600, -100))
# build(10, 15, 15, (-300, 0))
# build(10, 5, 15, (300, -100))

for x, y in ((-200, 50), (-100, -50), (0, 50), (100, -50), (200, 50)):
    build(6, 4, 15, (x, y))

done()


## making big building
## making big city

# def bill_count(rastoch, tariff):  # rastoch = rastoch_A
#     res = rastoch * tariff
#     return res
#
# gs_Andriy = 8000
# rastoch_Andrew = 230
# lit = 6
#
# electricty = bill_count(rastoch_Andrew, 1.5)
# # print(electricty)
#
# gs_Andriy = 8000
# rastoch_Andrew = 230
# lit = 6
#
# electricty = bill_count(rastoch_Andrew, 1.5)
# gas = bill_count(gs_Andriy, 0.15)
# liter = bill_count(lit, 55)
# zhutie = (electricty + gas + liter)
# print(zhutie)
#
## НЕ ВІРНИЙ
# def func(name):
#     print("hello " + name)
#
# a = func("Vlad")
# a += "!"
# print(a)

# def func(name):
#     return "hello " + name
#
# a = func("Vlad")
# a += "!"
# print(a)

# # ______________________________
# # ___important functions info___
# # ______________________________

# global outerscope (глобальна зона видимості програми)
# x = 0
# def func():
#     global x
#     x = 0
#     x += 1
#
# func()
# x += 2
# print(x)

# def is_year_leap(year):
#     if year % 400 == 0:
#         return True
#
#     if year % 4 == 0 and year % 100 != 0:
#         return True
#
#     return False
#
# for a in range(100):
#     if a == 45:
#         break
#     print(a)

# DEFAULT FUNCTIONS PARAMETER, OBJECTS

# print(is_year_leap(1900))
# # mails
# # funcs
