# https://pythonexercises.rozh2sch.org.ua/

# variable - var

# # integer - int - ціле число 1 2 3 -22000
# number = 5
# number = 1
# # string - str - рядок
# number = 'word'
# number = "word"
# print(number)

# num = 2 + 2 * 2
# print(num)

# num = 2
# num = "text" + "text1"
# num = 5
# num = 5 + "txt"
# print(num)

# txt = '!@#%&*^&*^ASDLASDJalsdkjasl    5' + 'txt'
# print(txt)

# roses = "rose " * 222222222
# print(roses)

# # IndentationError - indent - відступ
#  name = "Vlad"
# print(name)

# # SyntaxError - порушені правила запису
# name = "Vlad"
# print(name)

# # НЕ ТРОГАТИ
# expectedValueAtStation = True

# # comments ctrl + /
# print(5)

# # arithmetics
# # sum
# print(2 + 3)
# print("text" + "second text")
# # subtraction
# print(2 - 3)
# print("text" - "second text")   # TypeError
# print(2 - "text")               # TypeError
# # division
# print(6 / 2)
# print("text" / "t")               # TypeError
# print(2 / "t")                    # TypeError
# # multiplying
# print(2 * 2)
# print("text" * "t")                 # TypeError

# num = input("num?")
# print("text" * num)

# print(12345678987654321**10000)

# # Type casting

# name1 = input("What is your first cat's name?")
# name2 = input("What is your second cat's name?")
#
# # print("Your first cat is:", name1, ".", "Your second cat is:", name2, ".")
# print("Your first cat is: " + name1 + "." + "Your second cat is: " + name2 + ".")
#
#
# txt = "5" + " apples"
# print(txt)

# string
# hamburgers = input("How many hamburgers did you eat this month?")
# print("So usually, you eat", int(hamburgers) / 30, "hamburgers per day.")

# number = input("How many goal have scored Ronaldo today?")
# print("It is great! But I know that you scored only", 1 - int(number), "goals today.")
# # "It is great! But I know that you scored only <number> goals today."


# "What year were you born"
# "You are <number> years old"

# # + - / * // %
# num1 = input("Num1?")
# num2 = input("Num2?")
# print(num1 + " % " + num2 + " =", int(num1) % int(num2))

# # табличка множення
# n = 2
# print(str(n) + " * " + "1" + " =", n*1)

# name = input()
# age = input()
# hobby = input()
# print("My name is " + name + ". I am " + age + " and my hobby is " + hobby + ".")

# print("My name is " + input() + ". I am " + input() + " and my hobby is " + input() + ".")
# print(0.05 * 100)

# num = int(input("num?"))
# print("Наступне число після", num, "це",  num + 1)

# num = int(input("num?"))
# print(82 // 10)

# print(3*4/2)


# base = int(input("base?"))
# height = int(input("height?"))
# s = 1/2 * base * height
# print("Square:", s)


# # float - число з плаваючою точкою (не ціле число)
# float_num = 5.8
# print(int(float_num))   # 5
# # print(10 / 2)
# num = 2
# print(float(num))   # 2.0

# float_num = 1.2
# print(float_num+1.2)
# print(float_num+1)
# print(float_num-1.2)
# print(float_num*1.2)
# print(float_num/1.2)
# print(float_num//1.2)

# base = float(input("base?"))
# height = float(input("height?"))
# s = 1/2 * base * height
# print("Square:", s)

# # приклад програми де треба int а не float
# apples = int(input("скільки яблук з'їв Микола?"))
# print(apples)

# # net work network
# network = input("What is your network?")             # net?
# balance = float(input("And what is your balance?"))  # balance?

# feet = float(input("Feet: "))
# inches = float(input("Inches: "))
# res_feet = feet * 30.48
# res_inches = inches * 2.54
# res = res_feet + res_inches
# print("Your height is:", res)
#
# feet = float(input("Feet: "))
# inches = float(input("Inches: "))
# res = feet * 30.48 + inches * 2.54
# print("Your height is:", res)

# num1 = int(input("How many hours do you sleep at night?"))
# num2 = int(input("How many minutes do you sleep during the day?"))
# result = num1 * 60 + num2
# print("You sleep", result, "minutes both day and night")

# # піднести число в степінь
# print(2**5)

# https://pythonexercises.rozh2sch.org.ua/
# 48, 49,  91

# num = int(input("Скільки пінгвінів?"))
# print(" (o o)  "*num)
# print("/  V  \\ "*num)
# print("""
#     _~_
#    (o o)
#   /  V  \\
#  /(  _  )\\
#    ^^ ^^
#    """)

# 51
# if then else >_<
# > < == != >= <=

# letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# # letters = "АБВ"
# for letter in letters:
#     print(letter + ":")
#     for letter_reversed in reversed(letters):
#         print(f"{letter} > {letter_reversed} = {letter > letter_reversed}")


### РОЗГАЛУЖЕННЯ ###
# print(True)
# print(False)
### SYNTAX ###
# if   - якщо
# :    - то
# else - інакше
# elif - інакше якщо


# if True:
#     print("Hi!")
# if 2 > 1:
#     print("2 > 1")
# if 2 > 2:
#     print("2 > 2")

# age = int(input("your age?"))
# if age > 18:
#     print("Ти можеш гуляти навулиці до ночі")
# else:
#     print("Ти не можеш гуляти навулиці до ночі")
# if age < 18:
#     print("Ти не можеш гуляти навулиці до ночі")

# if age > 18:
#     print("Ти можеш гуляти навулиці до ночі")
# elif age < 18:
#     print("Ти не можеш гуляти навулиці до ночі")
# else:
#     print("Я ще не знаю чи ти можеш гуляти навулиці")

# num = int(input("Скільки в тебе друзів"))
# if num == 1:
#     name1 = input("Як його звати?")
#     if name1 == "Олег":
#         print("Таааак, не пощастило з Олегом")
#     elif name1 == "Маша":
#         print("О, Маші це найкращі друзі!")
#     else:
#         print("Ого, 1 друг, дуже добре що його звати", name1)
# elif num == 2:
#     name1 = input("Як звати першого?")
#     name2 = input("Як звати останнього?")
#     print("Двоє друзів:", name1, "і", name2, "супер!")
# elif num > 100:
#     print("Ти мабуть підбріхуєш -_- так багато бути не може")
# elif num > 2:
#     print("Ого, багато друзів, Супер!")
# else:
#     print("Некоректний ввід, введіть число від 1 до багато")

# login = input("Введіть логін?")
# if login == "starlink":
#     password = input("Введіть пароль?")
#     if password == "464657":
#         print("Ви ввійшли в систему")
#     else:
#         print("Пароль не вірний")
# else:
#     print("Логін не вірний")

# 103 порівняння букв
# if "a" < "c":
#     print("c")
# if "Masha" > "Sasha":
#     print("Sasha")
#     print("Masha")
# else:
#     print("Masha")
#     print("Sasha")

# _____________________________________________
# 106
# temperature = int(input("What is the temperature outside?"))
# if temperature <= 0:  # -9999999 ... 0
#     print("It's pretty cold out there, hope you got your coat and scarf")
# elif 0 < temperature < 10:  # 1 ... 9
#     print("Not a bad weather, don't forget your jacket btw")  # by the way
# elif temperature >= 10:  # 10 ... 999990
#     print("It's okay")
# else:
#     print("Error")

# 105
# letter1 = input("Give me your letter!")
# letter2 = input("Give me another letter!")
# if letter1 > letter2:
#     print(letter1, "comes after", letter2)
# else:
#     print(letter2, "comes after", letter1)

# 111
# done

# 115

# 114
# num = int(input("Gimme ur num FAST pls"))
# if num > 0:
#     print("It is positive number")
# elif num < 0:
#     print("It is a negative number")
# elif num == 0:
#     print("Is is Zero")

# 119

# or - чи, або
# and - і, та

# # or
# mark = int(input("What is your mark?"))
# if mark == 11 or mark == 12:
#     print("Great! Mom will bake you a pie!")
# string = "Chopetto"
# string1 = "chopetto"
# if string == string1:
#     print("Вони однакові ж!")
# answer = input("Що зелене зимою і літом?")
# if answer == "ялинка" or answer == "Ялинка":
#     print("Правильно!")
# else:
#     print("Не правильно :(")

# # приклад використання lower
# answer = input("Що зелене зимою і літом?")
# if answer.lower() == "ялинка":
#     print("Правильно!")
# else:
#     print("Не правильно :(")

# # and
# age = int(input("What is your age?"))
# age1 = int(input("What is your friend's age?"))
# if age >= 18 and age1 >= 18:
#     print("You both can go into the club")
# elif age >= 18:
#     print("Only you are allowed")
# elif age1 >= 18:
#     print("Only your friend is allowed")
# else:
#     print("Noone is allowed")

# 116
# done

# # 117 переписати
# num1 = int(input("First num?"))
# num2 = int(input("Second num?"))
# num3 = int(input("Third num?"))
# if num1 == num2 and num2 == num3:
#     print(3)
# elif num1 == num2 or num1 == num3 or num2 == num3:
#     print(2)
# else:
#     print(0)

# 131
# done

## While
## cycle - цикл, або повторення якихось дії

# # приклад безкінечного циклу
# while 2 < 4:
#     print("HELLO")

# # 0 - 10
# num1 = 0
# while num1 < 11:
#     print(num1)
#     num1 = num1 + 1

# # output all the even numbers between 0 and 20
# # виведіть всі парні числа від 0 до 20
# # 0 - 20 (2 .. 4 .. 6 .. 8 ..)
# num = 0
# while num < 20:
#     num += 2
#     print(num)

# # запитати 2 числа у користувача і вивести всі числа від першого до другого 5 10: 5 6 7 8 9 10
# num1 = int(input("num1?"))
# num2 = int(input("num2?"))
# while num1 <= num2:     # < =
#     print(num1)
#     num1 += 1

# # написати програму яка 5 разів виводить фразу "Hello, World!" кожна з нового рядочку
# c = int(input())
# while c < 5:
#     print()
#     c += 1


# про структуру циклу
# 5 ... 10
# n = 10
# while n > 0:
#     print(n)
#     n -= 1
# print("Start!")

# num = 8
# while num > 7:
#     print(num)
#     num -= 1

# не знаємо скільки разів буде виконуватися цикл - while

# коли робимо ігри або завершимо з допомогою break
# while True:

# # приклад загадки
# print("At Winter and Summer \nit has the same color:")
# answer = input("Your answer:\n")    # \n - для того щоб юзер писав відповідь в новому рядочку
# correct_answer = "christmas tree"
# while answer != correct_answer:     # ! =  - разом це "не дорівнює"
#     print("You are not correct -_- Try again =D\n")
#     answer = input("Your answer:\n")
# print("\nYes! It is christmas tree! Happy New Year!")

# # а ти купи слона
# print("Купи слона")
# answer = input("Купляєш?\n")    # \n - для того щоб юзер писав відповідь в новому рядочку
# correct_answer = "добре, я куплю слона"
# while answer != correct_answer:     # ! =  - разом це "не дорівнює"
#     print("Всі кажуть " + answer + " а ти купи слона\n")
#     answer = input("Купляєш?\n")
# print("\nВітаємо вас з покупкою слона, з вас списані гроші")

# # 210 Визначити суму всіх чисел від 1 до n.
# n = int(input("Твоє число?\n"))
# a = 1
# summ = 0
# while a <= n:
#     summ += a
#     a += 1
# print(summ)

# 219 Надрукувати квадрати усіх цілих чисел від 1 до n включно (значення n вводиться з клавіатури користувачем)
# n = int(input("Твоє число?\n"))
# a = 1
# while a <= n:
#     print(a, "*", a, "=", a**2)
#     a += 1

# # коли треба знайти квадратний корінь з числа
# a = 169
# print(a**(1/2))    #  знаходження квадратного кореня з a

# перевірити 2 дз

# # Визначити добуток всіх чисел від 1 до n
# n = int(input("Твоє число?\n"))
# a = 1
# dob = 1
# while a <= n:
#     dob *= a
#     a += 1
# print(dob)


# c = int(input("?"))
# a = 0
# while a < c:
#     print(a)
#     a += 1
#
# print()

# c = int(input("?"))
# for a in range(c):
#     print(a)
# print(range(0, 10))

# range - діапазон - набір чисел від і до
# range(0, 3) - діапазон чисел від 0 до 2
# права межа береться не включно

# # Визначити добуток всіх чисел від 1 до n
# n = int(input("Твоє число?\n"))
# dob = 1
# for a in range(1, n+1):  # ми пишемо +1 тому що права межа не включається, а нам треба
#     dob *= a
# print(dob)


### TURTLE MODULE ###
# https://inform54.wordpress.com/2021/02/24/991/

# from turtle import *        # імпортуєте весь файл черепашки собі в програму
#
# shape('square')              # зробити форму черепашки
# speed(8)                     # швидкість (1-25) (0 - максимальна швидкість)
# width(2)                    # товщина лінії. Ідентична функція: pensize(10)
#
# # color("white")                 # колір. Вказується завжди в лапках "red" "purple" "yellow"
# # for line in range(4):
# #     forward(100)
# #     left(90)
#
# # for x in range(20):
# #     forward(10)
# #     color("white")
# #     forward(10)
# #     color("black")
# #     forward(10)
#
# # for angle in range(360):
# #     forward(1)
# #     left(1)
# color('green')
# for e in range(3):
#     forward(100)
#     lt(120)
# color('red')
# for side in range(4):
#     forward(100)
#     rt(90)
# done()                      # затримати вікно від зникнення

# # декілька черепашок
# import turtle
# t = turtle.Turtle()
# t1 = turtle.Turtle()
# t.forward(10)
# t1.forward(100)
# turtle.done()

# from turtle import *
#
# forward(50)
#
# color("red", "yellow")
#
# begin_fill()  # там де починається фігура, замальовує область
#
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
#
# end_fill()  # там де закінчується фігура
#
# forward(150)
#
# done()


# from turtle import *
#
# shape("turtle")
# shapesize(5)
# width(9)
#
# begin_fill()
# circle(100)
# end_fill()
#
# done()

# from turtle import *
#
# width(9)
# speed(0)
# tracer(5)
# # for x in range(2):
# #     fd(100)
# #     lt(90)
# #     fd(50)
# #     lt(90)
#
# for x in range(360):
#     fd(1)
#     lt(360/360)
#
# done()

# from turtle import *
# width(9)
# shapesize(5)
# # hideturtle()  # ht()
# # showturtle()
# up()
# goto(100, 100)
# down()
# goto(100, -100)
# up()
# goto(-100, 100)
# down()
# goto(-100, -100)
# up()
# goto(0, -100)
# lt(90)
# for x in range(200):
#     fd(1)
#
# done()

# from turtle import *
# shapesize(5)
# width(9)
# up()
# goto(0, -300)
# down()
# for x in range(10):
#     circle(40, 180)
#     lt(180)
#     circle(40, -180)
#     lt(180)
# done()

# from turtle import *
# circle(50)
# lt(180)
# circle(50)
# done()


# from turtle import *
# for c in ["red", "green", "purple", "pink", "black"]:
#     color(c)
#     fd(100)
#     lt(90)
# done()
# # list("red", "green", "purple", "pink"

# from turtle import *
# d = int(input("What is the distance Andromeda passed?"))
#
# forward(d*2)
#
# print("The distance Sirius passed is 2 times bigger and is equal:", d*2)
# # дистанція яку подолав сіріус в 2 рази більша і дорівнює:
# done()

# from turtle import *
#
# # # up()
# # goto(-100, 0)
# # # down()
# #
# # begin_fill()
# # circle(5)
# # end_fill()
#
# for y in range(-200, 101, 100):   # 100 200 300
#     up()
#     goto(0, y)
#     down()
#
#     forward(300)
#
# up()
# right(90)
#
# for x in range(0, 301, 100):
#     up()
#     goto(x, 100)
#     down()
#
#     forward(300)
#
# done()


# from turtle import *
# speed(10)
# #скільки рядів
# for y in range(200, -201, -200): # 1:200 2:0 3:-200
#     up()
#     goto(0, y )
#     down()
#     write(f"{0},{y}")
#     #скільки квадратів в ряду
#     for c in range(3):
#         #квадрат
#         for x in range(4):
#             forward(100)
#             rt(90)
#         forward(100)
#
# done()

# from random import randint
# for x in range(100):
#     print(randint(1, 10))

# # * - це ВСІ функції
# from turtle import *
# # тут тільки ОДНА функція random integer
#
# # це генерує число від 1 до 2 і зберігає в змінну а
# from random import randint
#
# a = randint(1, 2)
# print(a)
#
# # початок ЗАВЖДИ менший ніж кінець
# from random import randint
#
# print(randint(100, 1))
#
# # можна і від'ємні
# from random import randint
#
# print(randint(-100, 100))
#
#
# from turtle import *
# from random import randint
#
# x = randint(-500, 500)
# y = randint(-500, 500)
# goto(x, y)
#
# done()

# from random import randint
# a = randint(0, 50)
# print(a)
# a = randint(0, 50)
# print(a)
# a = randint(0, 50)
# print(a)

# from random import randint
# for s in range(33):
#     a = randint(0, 50)
#     print(a)

# from random import randint
#
# num1 = int(input("From: "))
# num2 = int(input("To: "))
#
# num3 = randint(num1, num2)
# print(num3)

# # 1
# # черепашка повинна пройти випадкову кількість пікселів від 100 до 1000
# from turtle import *
# from random import randint, choice
# colors = ["red", "brown", "cyan", "purple", "pink", "white"]
# speed(10)
# for c in range(10):
#     # нахил зірки
#     left(randint(15, 60))
#
#     # колір
#     rand_color = choice(colors)
#     color(rand_color)
#
#     # жирність
#     width(randint(5,15))
#
#     # переміщення
#     x = randint(-400, 400)
#     y = randint(200, 350)
#     up()
#     goto(x,y)
#     down()
#
#     # зірка
#     for x in range(5):
#         fd(30)
#         rt(144)
#
# # чупачупс
# up()
# goto(0, -300)
# down()
# # установити напрям куди дивиться черепашка (90 - вверх, 0 - вправо, 180 - вліво, -90 - вниз)
# setheading(90)
#
# # палка
# color("brown")
# width(5)
# fd(150)
#
# # голова
# color('yellow')
# width(80)
# forward(30)
#
#
# done()
# # 2
# # черепашка повинна пройти випадкову кількість пікселів від 30 до 70 і повернути на випадковий градус від 30 до 90 вліво. Повторити 15 разів

# import turtle as t
#
# turtles = [t.Turtle() for _ in range(15)]
#
# forw = 120
# lef = 60
#
# for turt in turtles:
#     turt.left(24*turtles.index(turt))
#     turt.ht()
#     turt.speed(0)
#
# for x in range(25):
#     for turt in turtles:
#         turt.forward(forw)
#         turt.left(60)
#     forw -= 6
#     lef += 3
#
# t.done()


# from turtle import *
#
# width(1)
# setheading(0)
# color('black')
# speed(1)
#
# forward(100)
# left(90)
# circle(180)
# goto(100, 100)
#
# done()

# from turtle import *
#
#
# t = Turtle()
# # t1 = Turtle()
# # ...
#
# # forward(100)
# t.left(90)
# t.forward(100)
#
#
# done()

# способи імпортування
# from turtle import *
# from random import randint
# import turtle

# import turtle as t
#
# t1 = t.Turtle()
# t2 = t.Turtle()
#
# t1.forward(100)
# t2.left(90)
#
# t.done()


# 2 черепашки. Кожна їде в свою сторону по 20 пікселів * 10 разів *

# import turtle as t
#
# t1, t2 = t.Turtle(), t.Turtle()
# t1.left(90)
# t2.right(90)
#
# # for x in range(200):
# #     t1.forward(1)
# #     t2.forward(1)
# t1.forward(20)
# t2.forward(20)
# t.done()

# import turtle as t
#
# turtles = [t.Turtle() for x in range(4)]
#
# for turt in turtles:
#     turt.left(turtles.index(turt)*90)
#     # turt.speed(0)
#
# for side in range(360):
#     for turt in turtles:
#         turt.forward(4)
#         turt.right(1)
#
# t.done()


# import turtle as t
# from resources.colors import colors_list
# from random import choice
#
# turtles = [t.Turtle() for x in range(4)]
#
#
# head = 0
# i = 1
# for x in range(10):
#     w = 1
#     col = choice(colors_list)
#     for turt in turtles:
#         turt.up()
#         turt.goto(0, 0)
#         turt.down()
#         turt.left(turtles.index(turt)*90)
#         turt.speed(0)
#         turt.color(colors_list[i*turtles.index(turt)+100])
#         t.tracer(2)
#         turt.left(head)
#     head += 1.5
#     i += 3
#     for side in range(135):
#         for turt in turtles:
#             turt.width(w)
#             turt.forward(4)
#             turt.right(2)
#         if side % 15 == 0:
#             w += 1
#
# t.done()

# import turtle as t
# from resources.colors import colors_list
# from random import choice, randint
# from time import sleep
#
# turtles = [t.Turtle() for x in range(3)]
# end_line = 300
# winner_one = turtles[0]
#
# t.speed(0)
# t.ht()
# t.up()
# t.goto(end_line, 100)
# t.down()
# t.right(90)
# for x in range(15):
#     t.fd(5)
#     t.up()
#     t.fd(5)
#     t.down()
# t.up()
#
# def start(turt, y):
#     turt.width(3)
#     turt.shapesize(4)
#     turt.color(choice(colors_list))
#     turt.pu()
#     turt.goto(-200, y)
#     turt.pd()
#     for x in range(8):
#         turt.left(15)
#         turt.right(15)
#
# def run(turt):
#     turt.forward(randint(2, 6))
#
# def winner(turt):
#     turt.up()
#     turt.goto(0, 100)
#     turt.left(45)
#     turt.pd()
#     a = 100
#     b = 90
#     turt.width(3)
#     for x in range(20):
#         turt.color(choice(colors_list))
#         turt.fd(a)
#         turt.left(b)
#         a -= 3
#         b += 1
#     turt.setheading(90)
#     turt.up()
#     turt.fd(60)
#     turt.write("WINNER!", font=20)
#     sleep(3)
#
# for turtle in turtles:
#     start(turtle, 50 - turtles.index(turtle) * 50)
#
# game_running = True
#
# while game_running:
#     for turtle in turtles:
#         if turtle.xcor() > end_line:
#             winner_one = turtle
#             game_running = False
#             break
#         run(turtle)
#
# winner(winner_one)
# t.done()

# import turtle as t
# from random import randint
#
# t1 = t.Turtle()
# t1.shapesize(4)
#
# # виганяємо машини на стартові позиції
# t1.penup()
# t1.goto(-200, 50)
# # -200, -50
# t1.pendown()
#
# # розгон
# for x in range(10):
#     t1.left(20)
#     t1.right(20)
#
#
#
# # якщо перша або друга доїхала - стоп
# while True:
#     if t1.xcor() > 200 or t2.xcor() > 200:
#         break
#     t1.forward(randint(1,10))
#
# # якщо перша черепашка стоїть далі ніж друга - вона виграла. Якщо друга стоїть далі ніж перша - виграла друга
# # танцює та що виграла
# t1.shapesize(15)
# for x in range(999):
#     t1.left(5)
#
# t1.write("Hello, This is my text", font=("Apple Chancery", 24, "normal"))
# t.done()

# # # ГОНКА ПЛАН # # #

# # імпортувати потрібні модулі(черепашка і рандом)
# import turtle as t
# from random import randint
#
# finish = 450
# # створення черепашок(2-3)
# t1 = t.Turtle()
# t2 = t.Turtle()
# # і налаштування
# t1.shapesize(4)
# t2.shapesize(4)
# t1.shape("turtle")
# t2.shape("turtle")
#
# # намалювати фініш (і дорогу) (і сонце зверху(зірки))   # зробити красивіше(жирніше чи що)
# t.speed(0)
# full = 1200
# shtrih = 50
# t.hideturtle()
# t.pu()
# t.goto(-600, 100)
# t.pd()
# t.fd(full)
#
# t.pu()
# t.goto(-600, -100)
# t.pd()
# t.fd(full)
#
# t.pu()
# t.goto(-600, 0)
# t.pd()
# c = int(full/(shtrih*2))
# for x in range(c):
#     t.fd(shtrih)
#     t.pu()
#     t.fd(shtrih)
#     t.pd()
#
# # зробіть красивішим фініш
# t.pu()
# t.goto(finish, 120)
# t.pd()
# t.rt(90)
# full = 240
# shtrih = 4
# for x in range(int(full/(shtrih*2))):
#     t.fd(shtrih)
#     t.pu()
#     t.fd(shtrih)
#     t.pd()
#
# # установити стартову точку для кожної черепашки
# t1.penup()
# t1.goto(-500, 50)
# t1.pendown()
# t2.penup()
# t2.goto(-500, -50)
# t2.pendown()
#
# ## дрифт на місці(розігрів шин)
# for x in range(5):
#     t1.left(20)
#     t1.right(20)
# # для другої черепашки також розгон(можна інший!)
#
# # кожну пихаємо вперед на випадкову відстань (1-10) використовуючи функцію randint() в циклі
# # перевіряємо хто доїхав до фініша першим
# while True:
#     if t1.xcor() > finish or t2.xcor() > finish:
#         break
#     t1.forward(randint(1,10))
#     t2.forward(randint(1,10))
#
# # перевіряємо хто виграв і він робить переможний танець
# # доробити переможній танець
# if  t1.xcor() > t2.xcor():
#     t1.write("winner")
# elif t1.xcor() > t2.xcor():
#     t2.write("winner")
#
#
# t.done()

# for i in "MyBlog":
#     print("?", i, "?")
#
# # f-string
# for i in "MyBlog":
#     print(f"?{i}?")
#
# # sep for print
# for i in "MyBlog":
#     print("?", i, "?", sep="")

# for i in range(5):        # 5 разів
#     print(i)

# for i in range(10, 15):     # 5 разів
#     print(i)

# for i in range(1, 11):
#     print(i)

# # print first 10 even numbers:
# for i in range(0, 20, 2):       # від нуля до 20 з кроком 2
#     print(i)
# first 10 odd numbers

# even # 4 # парні
# odd  # 3 # непарне
# # https://csiplearninghub.com/practice-questions-of-loops-in-python/

# program which prints even numbers from 18 to 0
# програма, яка виводить непарні числа від 18 до 0
# (перші 10 непарних чисел в зворотньому порядку)
# for x in range(18, -1, -2):
    # print(x)

# for i in range(30, -4, -3):
#     print(i)

# # запитати 10 чисел від юзера
# int(input())
# 19
# 18
# 10
# 4
# 5
# 6
# 7
# 1
# 2
# 3
# 1

# for x in range(10):
#     number = int(input("Твоє число: "))

# # запитати у юзера число і написати, парне воно чи непарне
# n1 = int(input("Твоє число? "))
# if n1 % 2 == 0:
#     print("парне")
# elif n1 % 2 == 1:
#     print("непарне")

# # запитати у юзера число і написати додатнє воно, від'ємне чи 0
# 20
# "додатнє"
# -20
# "від'ємне"
# 0
# "це нуль"



# txt = "persimmon"
# num = len(txt)
# print(num)

# виведи = print
# довжина = len
#
# а = "persimmon"
# num = довжина(а)
# виведи(num)

# # #  INDEXES

# word = "Tangerine"
# print(word[0])  # перший елемент
# print(word[-1]) # останній елемент
# print(word[4])  # п'ятий елемент

# # # slices
# word = "Tangerine"
# print(word[0:6])   # Tanger   # тут 5 не включається
#
# for x in range(0, 5): # тут 5 не включається
#     print(x)

# print(word[3:7]) # geri

# print(word[-3: ])  # ine     # від -3 елемента до кінця
# print(word[6:9])  # ine

# print(word[0:8])    # Tangerin
# print(word[ :-1])    # від початку до -1
# print(word[ :8])

# # написати код з [] який виведе цю частину зі слова
# word = "ununderstandable" # щось що не піддається розумінню
# # un
# print(word[:2])
# # understand
# print(word[2:-4])
# # able
# print(word[-4:])
# # understandable
# print(word[2:])
# # e - та що в кінці
# print(word[-1])
# # u
# print(word[0])
# # вивести довжину слова
# print(len(word))

# останній елемент не включно

# negative slices
# [менше : більше]
# [більше : менше: від'ємний крок]
# word = "cantaloupe"
# print(word[2:8:2])
# print(word[:9:3])
# print(word[::2])
# print(word[-2:-5:])
# print(word[-5:-1])     # loup
# # puol
# print(word[-2:-6:-1])

# watermelon
# speechless
#1
# wtreo
# secls
#1.1
# aemln
# pehes
#1.2
# tmo
# ehs
#1.3
# wm
# sh

# watermelon
# speechless
#2
# ween
# sels
#2.1
# een
# els

#3
# nolemretaw
# sselhceeps
#3.1
# nlm
# seh
#3.2
# rtw
# ces
#4
# water
# speech
#5
# wat
# spe

# вивести слово навпаки
# print(word[::-1])
# print(word[::-2])

# # palindrom
# word = "шhаш"
# print(word[::-1] == word)

# find indexes .find

# word = "some text"
# print(word[-4:])
# print(word[-1:-4])

# text = "Imaginary unrecognizable little fox"
# print(text[9:])

# # find() шукає вказаний текст і повертає індекс де його знайшло
# text = "Якесь речення. І потім ще одне"
# #
# i = text.find('.')  # 4
# print(text[i+2:])     # Nice to meet you

# text = "Якесь речення. І потім ще одне"
# #
# i = text.find('р')
# d = text.find('я')
#
# print(text[i:d])

# все через find
# "Small sunny capital"
# "Little bushy tree
# 1
# Small
# Little
# 2
# sunny
# bushy
# 3
# capital
# tree
# 4
# Small sunny
# Little bushy
# 5
# ynnus
# yhsub


# text_slice =

# # для центрування тексту
# print("26.01.2024".center(30, "_"))
# print("Bondar Vladyslav".center(30, "_"))
# print("Program 1".center(30, "_"))



# word = "word"
# letter = "w"
#
# if letter in word:
#     print(f"{letter} in {word}")

# перевірили чи персона в країні і вивели її ім'я з країною
# person = "Andriy 16 USA 5 5"
# # person = "Ann 17 Poland 4 4"
#
# # шукаємо маленьке в велике
#
# if "USA" in person:
#     print(f"Name: {person[:person.find(' ')]} lives in USA")
# if "Poland" in person:
#     print(f"Name: {person[:person.find(" ")]} lives in Poland")

# дз
# # mail
# result: "some.mail123 is gmail post"
# mail1 = 'some.mail123@gmail.com'
# if 'gmail.com' in mail1:
#     print(mail1, "is gmail.com")
# elif 'ukr.net' in mail1:
#     print(mail1, "is ukr.net")

# result "some.mail123 is ukr.net post"
# mail2 = 'some.mail123@ukr.net'
#
# mail3 = 'some.mail123@mail.com'
#
# mail4 =


# word = 'perfect'
# if 'e' in word:
#     print('e in word:', word)
# letter = 'w'
# vowel_letters = 'eyuioa'
# consonantal_letters = 'qwrtpsdfghjklzxcvbnm'
# if letter in vowel_letters:
#     print(letter, "is vowel")
# elif letter in consonantal_letters:
#     print(letter, "is consonantal")
# binary
# 0 |   1 -
# octal
# 0 1 2 3 4 5 6 7
# hexadecimal
# 0 1 2 3 4 5 6 7 A B C D E F E G
# word = 'Apple'
# # word[0]
# print(word[0].lower())
# vowel_letters = 'eyuioa'
# consonantal_letters = 'qwrtpsdfghjklzxcvbnm'
# if word[0].lower() in vowel_letters:
#     print(word, "starts with a vowel")
# elif word[0].lower() in consonantal_letters:
#     print(word, "starts with a consonantal")

# h = input("так чи ні?")
# if h.lower() == 'так':
#     print("Yeah")
# elif h.lower() == 'ні':
#     print("Nah")
# print(h)
#
# h = input("так чи ні?").lower()     # так
# if h == 'так':
#     print("Yeah")
# elif h == 'ні':
#     print("Nah")
# print(h)

# # повертає рядок зі зменшеними буквами
# h = "YESYESYES"
# h = h.lower()
# print(h)

# center



# .lower()  .upper()
# txt = "ABc"
# txt = txt.lower()
# print(txt)
# txt = "ABc"
# txt = txt.upper()
# print(txt)


# word = "Differencible"
# for elem in word:
#     if elem == 'D':
#         print("I FOUND D")
#     else:
#         print(elem)

# for елемент in велике:
#     тут щось робимо з елементом

# for e in "world":
#     print(e)

# for e in word:
#     if e != 'e':
#         print(e, end='')

# слово worldless вивести з нього ті букви які == s використовуючи for
# word = 'wordlesss'
# for i in word:
#     if i == 's':
#         print(i, '- це буква s')
#     else:
#         print(i)

# сума чисел від 1 до 10
# s = 0
# for x in range(1, 10):
#     s = s + x
# print(s)

# # слово worldless порахувати кількість s
# w = 0
# d = 0
# s = 0
# word = 'wordlesss'
# for i in word:
#     if i == 's':
#         s += 1
#     elif i == "d":
#         d += 1
#     elif i == "w":
#         w += 1
# print("кількість w:", w)
# print("кількість d:", d)
# print("кількість s:", s)
# print("кількість інших:", len(word)-w-d-s)

# "different" - f, e, n
# "beautiful" - b, i, f
# кількість f: 2
# кількість e: 2
# кількість n: 1
# інших букв: 4

# слово worldless вивести з нього ті букви які приголосні використовуючи for *


# описати указані головні функції


# for mail in 'some.mail@gmail.com','some.mail123@gmail.com','some.mail123@init.ua':
#     dot = mail.rfind('.')
#     print(mail[dot:])

# count = 0
# for letter in "w - o - r - d - ":
#     count += 1
#     print(letter)
# print(count)

# # https:
# for link in 'https://meet.google.com/eba-auzd-off', 'https://meet.google.com/eba-auzd-off', 'https://meet.google.com/eba-auzd-off':
#     dots = link.find(":")
#     print(link[:dots+1])

# # назву сайту
# for link in 'https://meet.google.com/eba-auzd-off', 'https://ek.ua/GOOGLE-PIXEL-7-256GB.htm', 'https://www.youtube.com/watch?v=cImG6T2Vgpo':
#     slash = link.find("/")
#     dot = link.find(".")
#     print(link[slash+2:dot])

# # вивести код міту в кожному посиланні
# for link in 'https://meet.google.com/eas-yfor-me', 'https://meet.google.com/did-nfe-el', 'https://meet.google.com/eba-auzd-off':
#     dot = link.rfind('/') + 1
#     # dot = link.find('.com') + 5
#     print(link[dot:])

# for link in 'https://meet.google.com/eas-yfor-me', 'https://eet.google.com/did-nfe-el', 'https://t.google.com/eba-auzd-off':
#     dot = link.find('/') + 2
#     dat = link.rfind('/')
#     print(link[dot:dat])

# # опціонально(для Саші обов'язково) - розібратися як працює, зробити коментарі
# for link in 'https://meet.google.com/eas-yfor-me', 'https://eet.google.com/did-nfe-el', 'https://t.google.com/eba-auzd-off', 'https://osu.ppy.sh/beatmapsets/331190#osu/733753':
#     dot = link.find('/') + 2    # шукає / і присвоєю в dot його індекс + 2
#     link = link[dot:]
#     while '/' in link:
#         dat = link.rfind('/')
#         link = link[:dat]
#     print(link)


# difference
# link = 'https://osu.ppy.sh/beatmapsets/331190#osu/733753'
# link = '://osu.ppy.sh/beatmapsets/https331190#osu/733753'

# if link[0:5] == "https":
#     print(True)
# else:
#     print(False)
#
# if "https" in link:
#     print(True)
# else:
#     print(False)

# remember while

# 1. вивести всі цифри з рядка
# 2. скласти рядок з усіх цифр і вивести його
# row = "He was born in 1964. Jefrey. He is the 1"
# numbers = '123467890'
# #1
# for e in row:
#     if e in numbers:
#         print(e)
# #2
# nums = ''
# for a in row:
#     if a in numbers:
#         nums = nums + a
# print(nums)

# numbers = '123127127390127312003213-128e12ei21yd123'        # рядок, з яким треба щось робити
# lil_nums = ''             # рядок в який ми будемо щось класти
# odd = '13579'             # рядок, в якому є цифри, які ми шукаємо
# for e in numbers:         # цикл, кладемо кожен елемент з рядка numbers в змінну e
#     if e in odd:          # якщо цей елемент є в рядку odd
#         lil_nums += e     # додаємо елемент в рядок lil_nums
# print(lil_nums)           # виводимо рядок lil_nums
# print(len(lil_nums))      # виводимо довждину lil_nums
#
# numbers = '123127127390127312003213-128e12ei21yd123'        # рядок, з яким треба щось робити
# lil_nums = ''             # рядок в який ми будемо щось класти
# odd = '13579'             # рядок, в якому є цифри, які ми шукаємо
# for e in numbers:         # цикл, кладемо кожен елемент з рядка numbers в змінну e
#     if e in odd:          # якщо цей елемент є в рядку odd
#         lil_nums += e     # додаємо елемент в рядок lil_nums
# else:
#     print(lil_nums)           # виводимо рядок lil_nums
# print(len(lil_nums))      # виводимо довждину lil_nums

# задача для класу
# вивести всі парні числа з рядка і вивести кількість парних чисел в рядку
# '123u1d12ke90j2103912'

# дз
# вивести всі голосні букви з рядка         'https://osu.ppy.sh/beatmapsets/331190#osu/733753'
# вивести всі приголосні букви з рядка      'https://osu.ppy.sh/beatmapsets/331190#osu/733753'

# # запитуємо в чому знайти що
# string_to_check = int(input("Рядок який треба перевірити:"))
# string_that_checks = int(input("Рядок який перевіряє:"))
# string_that_keeps = ""
# for e in string_to_check:
#     if e in string_that_checks:
#         string_that_keeps += e
# print(string_that_keeps)
# print(len(string_that_keeps))

# скласти рандомне число з n цифр

# from random import choice
#
# numbers = "1234567890"
# gotove_chuslo = ""
# n = int(input("Скільки цифр в числі?"))
# for e in range(n):
#     random_number = choice(numbers)
#     gotove_chuslo += random_number
# print(f"Ваше число з {n} цифр це: {gotove_chuslo}")

# # скласти рандомне число з n цифр при умові що цифри чередуються: парне, непарне, парне, непарне....
# from random import choice
#
# odd = "135790"
# even = "24680"
# gotove_chuslo = ""
#
# n = int(input("Скільки цифр в числі?"))
#
# for e in range(n//2):                   # // відкидає десяткову частину. Робимо бо треба половину n
#     random_number = choice(odd)
#     gotove_chuslo += random_number
#
#     random_number = choice(even)
#     gotove_chuslo += random_number
# print(f"Ваше число з {n} цифр це: {gotove_chuslo}")

# дз
# скласти рандомне слово з n букв.
# скласти рандомне слово з n букв. (випадкова голосна, випадкова приголосна)
# скласти рандомне слово з n букв 100 разів. (випадкова голосна, випадкова приголосна)


# next lesson

# кількість голосних/приголосних. те ж з count
# bot with all the functionality



