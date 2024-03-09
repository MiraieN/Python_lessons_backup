# from turtle import *
# colors = ("green", "red")
# width(2)
# lt(5)
# for square in range(4):
#     color(colors[square % 2])
#     for side in range(4):
#         fd(100)
#         lt(90)
#     lt(26.5)
# exitonclick()

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
# exitonclick()

# from turtle import *
# shape("turtle")
# stamp()
# pu()
# goto(0, -100)
# pd()
# speed(10)
# color("black", "yellow")
# begin_fill()
# circle(100)
# end_fill()
#
# color("black", "blue")
# pu()
# home()
# bk(70)
# lt(45)
# fd(50)
# pd()
# begin_fill()
# circle(13)
# end_fill()
# pu()
#
# home()
# fd(70)
# rt(45)
# bk(50)
# pd()
# begin_fill()
# circle(13)
# end_fill()
# pu()
#
# goto(0, -10)
# width(8)
# pd()
# goto(0, 18)
# width(1)
# pu()
#
# width(9)
# goto(-50, -40)
# rt(40)
# color("red")
# pd()
# circle(50, 170)
#
# exitonclick()

# from turtle import *
# speed(5)
# shape("turtle")
# for line in range(12):
#     fd(150)
#     stamp()
#     bk(150)
#     lt(30.5)
# shape("circle")
# exitonclick()

# from turtle import *
# speed(2)
# rt(90)
# for x in range(5):
#     circle(40, -180)
#     if x != 4:
#         circle(6, -180)
# exitonclick()

# from turtle import *
# speed(0)
# a = 30
# lt(150)
# heading = 135
# for angles in range(3, 15):
#     for side in range(angles):
#         fd(a)
#         lt(360/angles)
#     pu()
#     goto(xcor()+10, ycor())
#     pd()
#     a += 10
#     setheading(heading)
#     heading -= 3.5
# exitonclick()

# from turtle import *
# speed(10)
# for x in range(3):
#     circle(50)
#     rt(180)
#     circle(50)
#     rt(60)
# exitonclick()


# #лаб 2
# #1
# x = int(input("x?\n"))
# y = 10 * x - 5
# print(y)
#
# #2
# a = float(input("a?\n"))
# b = float(input("b?\n"))
# y = 6 * a**4 + 10 * a * b + 4 * b**2
# print(y)
#
# #3
# a = int(input("a?\n"))
# z = 101 * a - 48
# print(z)
#
# #4
# x = int(input("x?\n"))
# y = int(input("y?\n"))
# z = x**2 + y * (3 + x)**3
# print(z)
#
# #5
# a = int(input("a?\n"))
# b = int(input("b?\n"))
# x = 2 * a + b
# print(x)
#
# #6
# y = int(input("y?\n"))
# x = 3 * y + ((3 + y)/(2 * y))
# print(x)
#
# #7
# x = int(input("x?\n"))
# y = x * (2 - x)
# print(y)
#
# #8
# a = int(input("a?\n"))
# b = int(input("b?\n"))
# y = ((3 - a + b)/(2 * (a + b)))
# print(y)
#
# #9
# a = int(input("a?\n"))
# z = 56*a**2-48
# print(z)
#
# #10
# a = int(input("a?\n"))
# b = int(input("b?\n"))
# z = ((20 + a)**2 + b)/(5 * (a + b)**2)
# print(z)
#
# #11
# a = int(input("a?\n"))
# b = int(input("b?\n"))
# x = 20 * b**6 + b - a**2
# print(x)
#
# #12
# y = int(input("y?\n"))
# x = ((10 + y**2)/(4 * y)) + 2 * y**4
# print(x)
#
#
# # скільки гарячої води взятої при температурі
# # 60 градусів Цельсія потрібно додати до 120 л
# # холодної води температури 20 градусів,
# # щоб підготувати ванну темп 36 градусів
# # теплообміном з довкіллям знехтувати
#
# #лаб 3
# #Завдання 12-15-1-с
# a = int(input("сторона?+\n"))
# h = int(input("висота?\n"))
# s = a * h
# print("площа паралелограма:", s)
#
# #Завдання 12-15-2-с
# a = 2
# b = 3
# a, b = b, a
#
# # Завдання 12-15-3-с
# summ = 0
# for num in range(1, int(input("Кількість вічок: "))+2):
#     summ += num
# print("Кількість пластинок:", summ)

# print("Кількість пластинок:", sum([num for num in range(1, int(input("Кількість вічок: "))+2)]))
#
#
# # Завдання 12-15-4-с
# from turtle import *
# color("red")
# lt(90)
# b = int(input("довжина лінії: "))
# fd(b)
# pu()
# home()
# done()
#
# # Завдання 12-15-5-с
# number = int(input("число: "))
# print("перша цифра:", number//10, "друга цифра:", number%10)
#
# #Завдання 12-15-6-с
# summ = 0
# dob = 0
# number = input("число: ")
# if number.isdigit():
#     for elem in number:
#         elem = int(elem)
#         summ += elem
#         dob += elem
#     print(f"Сума: {summ}"
#           f"Добуток:{dob}")
#
# #Завдання 12-15-7-с
#
# number = input("число: ")
# if number.isdigit():
#     names = ("Перше", "Друге", "Третє", "Четверте")
#     for i in range(len(number)):
#         print(f"{names[i]} число: {int(number[i])}")
#
# #Завдання 12-15-8-с
# summ = 0
# dob = 0
# number = input("число: ")
# if number.isdigit():
#     for elem in number:
#         elem = int(elem)
#         summ += elem
#         dob += elem
#     print(f"Сума: {summ}"
#           f"Добуток:{dob}")
#
# #Завдання 12-15-9-с
# number = input("число: ")
# if number.isdigit():
#     number = ''.join((number[0], number[3], number[2], number[1]))
#     print(int(number))
#
# #Завдання 12-15-10-с
# from horology import Timing
# n = int(input("Вартість шоколадки: "))
# p = int(input("Відсоток подорожання: "))
# s = int(input("Сума грошей: "))
# with Timing():
#     print("Кількість яку зможе купити", int(s//(n+n*p/100)))
# n = int(input("Вартість шоколадки: "))
# p = int(input("Відсоток подорожання: "))
# s = int(input("Сума грошей: "))
# print("Кількість яку зможе купити", int(s//(n+n*p/100)))


# лаб 4
# #Завдання 12-15-11-с
# n = int(input("Кількість рівних частин: "))
# print("Кількість рівних трикутників", n ** 2)
#
# #Завдання 12-15-12-с
# summ = 1
# n = int(input("Кількість ярусів: "))
# for c in range(n+1):
#     summ += c*2
# print("Кількість літрів: ", summ)

# #Завдання 12-15-13-с
# num = int(input('Введіть кількість грошей: '))
# print(f"Ви можете купити {num - 1} пляшок води")
#
# #Завдання 12-15-14-с
# n = int(input("n: "))
# vid = "1"*n
# do = "9"*n
# # for x in range(n):
# #     vid += '1'
# #     do += "9"
# vid = int(vid)
# if vid % 2 == 0:
#     vid += 1
# count = 0
# for num in range(vid, int(do)+1, 2):
#     pretty = True
#     for elem in str(num):
#         if elem in "02468":
#             pretty = False
#             break
#     if pretty:
#         count += 1
# print(f"кількість гарних {n}-значних чисел: {count}")

# #Завдання 12-15-15-с
# n = int(input("n: "))
# vid = ""
# do = ""
# for x in range(n):
#     vid += '1'
#     do += "9"
# count = 0
# for num in range(int(vid), int(do)+1, 2):
#     pretty = False
#     for elem in str(num):
#         if elem == '7':
#             pretty = True
#     if pretty:
#         count += 1
# print(f"кількість {n}-значних чисел що містять в собі 7: {count}")
#
# #Завдання 12-15-16-с
# a = int(input("вартість пиріжка в грн: "))
# b = int(input("вартість пиріжка в копійках: "))
# n = int(input("кількість пиріжків до покупки: "))
# res = (a + b / 100) * n
# print(int(res), int((res - int(res)) * 100))
#
# #Завдання 12-15-17-с
# n = int(input("Кількість хлопців: "))
# m = int(input("Кількість дівчат: "))
# k = int(input("кількість місць в кімнаті: "))
# print((n // k + int(n % k != 0)) + (m // k + int(m % k != 0)))
#
# #Завдання 12-15-18-с
# num = input("Число: ")
# print(sum([int(n) for n in num]))
#
# #Завдання 12-15-19-с
# num = input("Число: ")
# num = ''.join((num[2], num[1], num[0]))
# print(num)
#
# #Завдання 12-15-20-с
# num = input("Число: ")
# print(sum([int(n) for n in num])**2)

# num = "asd"
# lst = "0246d8"

# def gimme(n, bukva):
#     string = ''
#     for x in range(n):
#         string += bukva
#     return string
#
#
# print(gimme(int(input(": ")), input(": ")))


## лаб 5
# #Завдання 8.1
# print("ділиться на 7" if int(input("Введіть число: ")) % 7 == 0 else "не ділиться на 7")

# #Завдання 8.2
# a = int(input('a: '))
# b = int(input('b: '))
# print(f"x = {-b/a}")

# #Завдання 8.3
# print(f"Більше число: {max(int(input('Перше число: ')), int(input('Друге число: ')))}")

# #Завдання 8.4
# x = int(input('x: '))
# y = int(input('y: '))
# if x > 0 and y > 0:
#     print("I чверть")
# elif x < 0 and y > 0:
#     print("II чверть")
# elif x < 0 and y < 0:
#     print("III чверть")
# elif x > 0 and y < 0:
#     print("IV чверть")
# else:
#     print("Невалідний ввід")

# #Завдання 8.5
# print("Сума є двозначним число" if len(str(sum([int(elem) for elem in input("Введіть двозначне число: ")]))) == 2 else
#       "Сума не є двозначним числом")

# #Завдання 8.6
# number = input("Введіть число: ")
# if int(number[0]) > int(number[1]):
#     print("Цифра десятків більша за цифру одиниць")
# elif int(number[0]) < int(number[1]):
#     print("Цифра одиниць більша за цифру десятків")
# else:
#     print("цифра одиниць і цифра десятків рівні")

# #Завдання 8.7
# num = input("Введіть число: ")
# print("Це паліндром" if num == num[::-1] else "Це не паліндром")

# #Завдання 8.8
# x = int(input("Введіть число: "))
# if x < 0:
#     print(x - 7)
# elif 0 <= x <= 5:
#     print(5)
# elif x > 5:
#     print(x*x + 5)

# #Завдання 8.9
# lst = [int(input("Введіть перше число: ")), int(input("Введіть друге число: ")), int(input("Введіть третє число: "))]
# print(f"Середнє з них: {sorted(lst)[1]}")
#
# #Завдання 8.10
# lst = sorted([int(input("Введіть перше число: ")), int(input("Введіть друге число: ")), int(input("Введіть третє число: "))])
# print(f"Добуток двох найбільших: {lst[1]*lst[2]}")
#
# # #Завдання 8.11
# x = input("Введіть число: ")
# print("4 входить до цього числа" if '4' in x else "4 не входить до цього числа")
#
# #Завдання 8.12
# x = input("Введіть число: ")
# print("5 і 7 входять до цього числа" if '5' in x and '7' in x else "5 і 7 не входить до цього числа")
#
# #Завдання 8.13
# for elem in [int(input(f"Введіть {n} число: ")) for n in ("перше", "друге", "третє")]:
#     if elem > 0:
#         print(elem * elem)
#     elif elem < 0:
#         print(elem)

# #Завдання 8.14
# x1 = int(input("x1: "))
# y1 = int(input("y1: "))
# x2 = int(input("x2: "))
# y2 = int(input("y2: "))
# x = int(input("x: "))
# y = int(input("y: "))
# way = ''
# if y > y2:
#     way = "N"
# if y < y1:
#     way = "S"
# if x < x1:
#     way += "W"
# if x > x2:
#     way += "E"
# print(way)
#
# #Завдання 8.15
# card = ''
# while len(card) != 16:
#     card = input("Введіть номер вашої карти: ")
# while True:
#     print('''Виберіть команду відповідною цифрою:
#                 1. Вивести поточний баланс на карті
#                 2. Переслати кошти на іншу карту
#                 3. Поповнити картку іншого банку
#                 4. Поповнити баланс смартфона
#                 5. Зняти кошти
#                 напишіть "вихід" - щоб завершити роботу''')
#     command = input()
#     if command == "вихід":
#         print("роботу завершено")
#         break
#     elif command == '1':
#         print("Ваш баланс <<balance>>")
#     elif command == '2':
#         card_to = input("Введіть номер карти на яку хочете зробити переказ")
#         amount = input("Введіть суму переказу")
#         print("Переказ успішний. Ваш поточний баланс <<balance-amount>>")
#     elif command == '3':
#         card_to = input("Введіть номер карти, яку хочете поповнити")
#         amount = input("Внесіть суму для поповнення")
#         print("Поповнення успішне")
#     elif command == '4':
#         card_to = input("Введіть номер телефона, який хочете поповнити")
#         amount = input("Введіть суму переказу")
#         print("Переказ успішний. Ваш поточний баланс <<balance-amount>>")
#     elif command == '5':
#         amount = input("Введіть суму, яку хочете зняти")
#         print("Зняття успішне. Ваш поточний баланс <<balance-amount>>")
#
# #Завдання 8.16
# print("Ви подорожуєте степом. На дорозі зустрічаєте вказівник. На вказівнику 3 шляхи")
# num = input("Виберіть вказівник(1/2/3): ")
# if num == '1':
#     print("Не п'є — живе, а нап'ється — умре")
#     if input("Ваш варіант: ") != "сніг":
#         print("Далі пройти не вдалося")
#         print("Підказка для наступного проходження:"
#               "умре = зміна агрегатного стану")
# elif num == '2':
#     print("Який годинник показує вірно час лише двічі на добу?")
#     if input("Ваш варіант: ") != "зламаний":
#         print("Далі пройти не вдалося")
#         print("Підказка для наступного проходження:"
#               "показує правильно 1 раз до обіду і 1 після")
# elif num == '3':
#     print("Жувати не жую, а все поїдаю, все тільки їм, а з голоду помираю")
#     if input("Ваш варіант: ") != "вогонь":
#         print("Далі пройти не вдалося")
#         print("Підказка для наступного проходження:"
#               "помираю = зникаю")
# print("Правильно! Ви пройшли далі")


# Лаб 6
# #Завдання 18.1
# print(sum([n**3 for n in range(1, int(input("n: "))+1)]))

# #Завдання 18.2
# N = input("N:")
# print([n for n in range(10, 100) if N in str(n) or n % int(N) == 0])

# #Завдання 18.3
# N = int(input("N:"))
# print([n for n in range(100, 1000) if sum([int(e) for e in str(n)]) == N])

# #Завдання 18.4
# print(sum([n**3 for n in range(25, 56)]))

# #Завдання 18.5
# print([n for n in range(10, 100) if sum([int(e)**2 for e in str(n)]) % 13 == 0])

# #Завдання 18.6
# print([n for n in range(10, 100) if sum([int(e) for e in str(n)]) + sum([int(e) for e in str(n)]) ** 2 == n])

# #Завдання 18.7
# print([n for n in range(100, 1000) if (str(n**2)[-3:]) == str(n)])

# #Завдання 18.8
# print([n for n in range(1000, 10000) if n % 133 == 125 and n % 134 == 111])

# #Завдання 18.9
# print(sum([n for n in range(int(input("A: ")), int(input("B: "))) if n % 4 == 0]))

# #Завдання 18.10
# print(sum([n for n in range(21, 100) if n % 3 == 0 and (str(n)[-1] in '248')]))

# #Завдання 18.11
# print([n for n in range(100, 1000) if int(str(n)[1:]) * 7 == n])

# #Завдання 18.12
# side = float(input("Довжина сторони: "))
# amount = int(input("кількість квадратів: "))
# angle = float(input("Кут повороту: "))
# from turtle import *
# speed(0)
# for kvadrat in range(amount):
#     for storona in range(4):
#         fd(side)
#         rt(90)
#     rt(angle)
# done()

# Завдання 18.13
# print([n for n in range(1000, 10000) if len(set(str(n))) == len(str(n))])

# #Завдання 18.14
# N = int(input("N: "))
# q = int(input("q: "))
# print([n for n in range(10, 100) if n % q == 0 and sum([int(e) for e in str(n)]) == N])

# #Завдання 18.15
# step = int(input("n: "))
# print([n for n in range(100, 10000) if sum([int(e) ** step for e in str(n)]) == n])

# #Завдання 18.16
# n = int(input("Кількість штрихів: "))
# d = int(input("Довжина кожного штриха: "))
# from turtle import *
# for x in range(n):
#     pu()
#     fd(d)
#     pd()
#     fd(d)
# done()

# #Завдання 18.17
# print([n for n in range(100, 1000) if sum(int(e) for e in str(n)) % 7 == 0 and n % 7 == 0])

# #Завдання 18.18
# num = int(input("n: "))
# lst = [n for n in range(1, num+1) if num % n == 0]
# print(lst)
# print(sum(lst))

# #Завдання 18.19
# from turtle import *
# color("green", "yellow")
# width(3)
# begin_fill()
# for side in range(7):
#     fd(50)
#     rt(360/7)
# end_fill()
# done()

# #Завдання 18.20
# from turtle import *
# n = int(input("Кількість кутів: "))
# d = int(input("Довжина сторони: "))
# color("green", "yellow")
# width(3)
# begin_fill()
# for side in range(n):
#     fd(50)
#     rt(360/n)
# end_fill()
# done()

# #Завдання передбачає пошук "щасливих" квитків. "Щасливим" називається такий тролейбусний квиток, в якому сума перших трьох цифр дорівнює сумі останніх трьох. Наприклад 030111 (0+3+0 = 1+1+1), 902326 (9+0+2 = 3+2+6), 001100 (0+0+1 = 1+0+0).
# #Вхідні дані: два цілих невід'ємних числа (0<=a1<=a2<=999999) - аргументи командного рядка.
# #Результат роботи: кількість "щасливих квитків", чиї номери лежать на проміжку від a1 до a2 включно. Якщо число на проміжку має менше 6 розрядів, вважати, що на його початку дописуються нулі у необхідній кількості, як це і відбувається при нумерації квитків. Виводити номери квитків не треба.
# num1 = 1001
# num2 = 1122
# c = 0
# for num in range(num1, num2+1):
#     lst = [int(e) for e in str(num)]
#     while len(lst) != 6:
#         lst.insert(0, 0)
#     if sum(lst[:3]) == sum(lst[3:]):
#         c += 1
# print(c)

# #видаляє повтори
# def clean_list(lst):
#     return list(set(lst))
# print (clean_list([1, 1.0, '1', -1, 1]))

# #Розробити функцію counter(a, b),
# # яка приймає 2 аргументи -- цілі невід'ємні числа a та b,
# # та повертає число -- кількість різних цифр числа b, які містяться у числі а.
# # Наприклад
# # Виклик функції: counter(12345, 567)
# # Повертає: 1
# # Виклик функції: counter(1233211, 12128)
# # Повертає: 2
# # Виклик функції: counter(123, 45)
# # Повертає: 0
# def counter(n):
#     return len([1 for elem in str(n[0]) if elem in str(n[1])])
#
# print(counter((123456, 57)))

# # лабораторна робота 11

# # 1
# import math
# print("7! =", math.factorial(7))

# # 2
# import math
# print("f(x) = sin(x)+cos^2(x)")
# x = int(input("x = "))
# print("f(x) =", math.sin(x) + math.cos(x) ** 2)

# # 3
# import math
# print("f(y) = tg(y^2) + |5y| - y^3")
# y = int(input("y = "))
# print("f(y) =", math.tan(y) + abs(y) - y**3)

# # 4
# import math
# print("f(z) = cos(z^2)+(z**5)*0.5")
# z = int(input("z = "))
# print("f(z) =", math.cos(z**2) + (z**5)**0.5)

# # 5
# n = int(input("Вартість шоколадки: "))
# p = int(input("Відсоток подорожання: ")) / 100 + 1
# s = int(input("Сума грошей Степана: "))
# print("Кількість шоколадкок які купить Степан:", int(s//(n*p)))


# # лабораторна робота 12

# # 1
# print(2 ** int(input("n=")))

# # 2
# print("S =", int(input("a=")) * int(input("h=")))

# # 3
# a = 5
# b = 10
# a = a + b
# b = a - b
# a = a - b
# print("a:", a)
# print("b:", b)

# # 4
# import math
# x = int(input("x="))
# y = int(input("y="))
# print("e^(x+y) + 5/(cos(y-x) + 3) =", math.exp(x+y) + 5 / (math.cos(y-x)+3))


# # лабораторна робота 13

# # 1
# n, m, k = map(int, input().split())
# p = n // k
# if n % k != 0:
#     p = p + 1
# q = m // k
# if m % k != 0:
#     q = q + 1
# print(p + q)

# # 2
# import math
# angle = int(input("Кут:"))
# s = int(input("Площа:"))
# second_angle = 90 - angle
# a = math.sqrt((2*s)/(math.tan(angle)))
# b = math.sqrt((2*s)/(math.cos(angle)/math.sin(angle)))
# c = math.sqrt(a**2+b**2)
# print("катет 1:", a, "катет 2:", b, "катет 3", c)

# # 3
# n = input("Введіть дійсне число:")
# cut = n[n.find(".")+1:]
# print("Дробова частина", cut)


# # лабораторна робота 14

# # 1
# import random
#
# for num in range(3):
#     print(random.randint(3, 56))

# # 2
# import random
# word = input("Введіть ваше слово:")
# for n in range(3):
#     print(random.choice(word))

# # 3
# import math
# import random
#
# num = random.randint(1, 6)
# print(str(num) + "! =", math.factorial(num))

# # 4
# import random
# num = random.randint(100, 999)
# print(num)
# for elem in str(num):
#     print(elem)

# # лабораторна робота 15

# # 1
# import random
# words = input("Введіть словосполучення:")
# for n in range(2):
#     print(random.choice(words))

# # 2
# import random
# import time
# for n in range(7):
#     time.sleep(1)
#     print(random.randint(1, 50), end=" ")

# # 3
# import random
# num = int(input("Кількість символів в паролі:"))
# symbols = "1234567890-!@#$%^&*()_qwertyuiop[]asdfgghjklzxcvbnm,./QWERTYUIOP{}ASDFGHJKL:ZXCVBNM<>?"
# password = ""
# for n in range(num):
#     password += random.choice(symbols)
# print(password)

# # Списки та рядки

# # 1
# amount = int(input("Скільки днів: "))
# data = []
# for n in range(1, amount+1):
#     data.append(float(input(f"Дані за день {str(n)}: ")))
# print("Середня температура: ", sum(data) / len(data), "°", sep="")

# # 2
# import random
# nums = [random.randint(1, 100) for n in range(15)]
# print("Список:", nums)
# print("Сума кратних 10:", sum([num for num in nums if num % 10 == 0]))

# # 3
# import random
# nums = [random.randint(1, 100) for n in range(15)]
# print("Список:", nums)
# m = int(input("Число М: "))
# print(len([num for num in nums if num < m]))

# # 4
# import random
# nums = [random.randint(1, 100) for n in range(7)]
# print("Список:", nums)

# # 5
# import random
# lst = [7, 37, 25, 44, 15, 9, -7, -10, -12, 0]
# nums = [random.randint(-12, 37) for n in range(random.randint(1, 20)) if n in lst]
# print("Список:", nums)
# print("Кількість елементів з другого списку:", len(nums))

# # 6
# import random
# k = int(input("Кількість елементів k: "))
# d = int(input("Мінімальний елемент d: "))
# e = int(input("Максимальний елемент e: "))
# nums = [random.randint(d, e+1) for _ in range(k)]
# nums2 = [random.randint(d, e+1) for _ in range(k)]
# nums3 = [random.randint(d, e+1) for _ in range(k)]
# i = 1
# for n in nums, nums2, nums3:
#     print("Список ", i, ": ", n, sep="")
#     i += 1
# print("Середнє арифметичне цих списків:", sum(nums + nums2 + nums3) / (len(nums) + len(nums2) + len(nums3)))

# # 7
# import random
# n = int(input("Кількість елементів n: "))
# lists_list = [[random.randint(0, 1001) for _ in range(n)] for lst in range(5)]
# i = 1
# for lst in lists_list:
#     print(f"Список {i}: {lst}")
#     i += 1
#     minn = lst[0]
#     for elem in lst:
#         if elem < minn:
#             minn = elem
#     print(f"Мінімальний елемент: {minn}\n")

# # 8
# import random
# n = int(input("Кількість елементів n: "))
# nums = [random.randint(1, 10) for _ in range(n)]
# print("Список:", nums)
# max_elem = max(nums)
# print(f"Максимальний елемент: {max_elem}")
# print(f"Кількість в списку: {nums.count(max_elem)}")
# print("Індекси: ", end="")
# for i in range(len(nums)):
#     if nums[i] == max_elem:
#         print(i, end=" ")

# # 9
# import random
# n = int(input("Кількість елементів n: "))
# nums = [random.randint(1, 1000000) for _ in range(n)]
# print("Список:", nums)
# count = 0
# for i in range(len(nums)):
#     if nums[i] < 5000:
#         nums[i] = 5000
#         count += 1
# print(f"Список після заміни: {nums}")
# print(f"Кількість замінених елементів: {count}")

# # 10
# import random
# n = int(input("Кількість елементів n: "))
# nums = [random.randint(1, 10) for _ in range(n)]
# print("Список:", nums)
# max_elem = max(nums)
# print(f"Максимальний елемент: {max_elem}")
# print("Сума чисел що не дорівнюють максимальному:", sum([elem for elem in nums if elem != max_elem]))

# # 11
# import random
# n = int(input("Кількість елементів n: "))
# nums = [random.randint(1, 10) for _ in range(n)]
# print("Список:", nums)
# print("Елементи з парними індексами:", end='')
# for i in range(len(nums)):
#     if i % 2 == 0 and i != 0:
#         print(nums[i], end=' ')

# # 12
# import random
# n = int(input("Кількість елементів n: "))
# nums = [random.randint(1, 10) for _ in range(n)]
# print("Список:", nums)
# count = 0
# for i in range(1, len(nums)-1):
#     if nums[i-1] < nums[i] > nums[i+1]:
#         count += 1
# print(f"Кількість елементів що більші своїх сусідів: {count}")

# # 13
# import random
# n = int(input("Кількість елементів n: "))
# nums = [random.randint(1, 10) for _ in range(n)]
# print("Список:", nums)
# minn = min(nums)
# maxx = max(nums)
# for i in range(len(nums)):
#     if nums[i] == minn:
#         nums[i] = maxx
#     elif nums[i] == maxx:
#         nums[i] = minn
# print(f"Максимальний елемент: {maxx}")
# print(f"Мінімальний елемент: {minn}")
# print(f"Список після заміни: {nums}")

# # 14
# import random
# n = int(input("Кількість елементів n: "))
# nums = [random.randint(1, 10) for _ in range(n)]
# print("Список:", nums)
# mid = sum(nums) / len(nums)
# lst = [num for num in nums if num > mid]
# print(f"Середнє арифметичне: {mid}")
# print(f"Кількість елементів, більших за середнє арифметичне: {len(lst)}")
# print(f"Сума елементів, більших за середнє арифметичне: {sum(lst)}")

# # 15
# import random
# n = int(input("Кількість елементів n: "))
# nums = [random.randint(1, 10) for _ in range(n)]
# print("Список:", nums)
# first_min = min(nums)
# nums.remove(first_min)
# second_min = min(nums)
# print(f"Сума найменших елементів: {first_min + second_min}")

# # 16
# n = int(input())
# nums = list(map(int, input().split()))[:n]
# print("Список:", nums)
# dob = 1
# for num in range(3):
#     maxx = max(nums)
#     nums.remove(maxx)
#     dob *= maxx
#     print(maxx)
# print(f"Найбільший добуток з 3 чисел: {dob}")

# # 17
# num = int(input("Введіть число: "))
# bin_num = bin(num)
# bin_num = bin_num[bin_num.find("b")+1:]
# print(f"Бінарний вигляд цього числа:", bin_num)
# print(f"Кількість нулів в цьому числі: {bin_num.count('0')}")

# # 18
# print("Кількість букв 'а' в тексті:", input("Введіть текст:\n").count('а'))

# # 19
# s = input("Введіть текст: ")
# print("Є паліндромом" if s == s[::-1] else "Не є паліндромом")

# # 20
# print("Це число в десятковій формі:", int(input("Введіть бінарне число: "), 2))







