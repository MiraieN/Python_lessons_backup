# txt = 'Hello I am Brian'
# txt[0] # indexing
# txt[0:4]   # slicing
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

# розказати про генератори

# пропорції
# середнє арифметичне

# звертання до списку через for 2 способами
# задача на зростання в списку/спадання
# створення списків двома способами


# lst = [11, 22, 33, 44, 55]
# l_len = len(lst)
# for z in range(l_len):
#     if z+1 != l_len:
#         if lst[z] > lst[z+1]:
#             print("нестабільний")
#         else:
#             print("стабільний")

# for elem in lst:
#     if lst.index(elem)+1 != len(lst):
#         if elem > lst[lst.index(elem)+1]:
#             print("нестабільний")
#         else:
#             print("стабільний")

# lst = [11, 22, 33, 44, 55, 11]
# lst_1 = [elem for elem in lst if elem == 11]
# print(lst_1)
#
# lst_2 = []
# for elem in lst:
#     lst_2.append(elem)
# print(lst_2)

# lst = [111, 11, 11, 22, 33, 44, 55, 11]
# print([lst[elem] for elem in range(len(lst)) if lst[elem] < lst[elem-1]])

# print(len(str(111)) == 3)

# print(sum([1, 2, 3]) / 3)
# lst = ["asd", "asdd"]
# print(sum([len(elem) for elem in lst]) / len(lst))

# вивести варіант і студента
# задача на унікальність елементів
# список без повторень
# лямбда

# функції
# кортеж, сет


# fruits = [1,4,56,1,23,4,6,]
#
# fruits.sort()
# print(fruits)

# def func(word):
#     return word[::-1]
#
# print(func("Hello"))

# c = lambda txt: print(txt.center(45, "_"))

# c("Hello, I am bot")
# c("Nice to meet u")

# a = lambda word: word[::-1]
# print(a("hello"))

# from random import shuffle
# num = [1,2,3,4,5]
#
# shuffle(num)
# print(num)


# sols = (1,0,3,4)
# a = - 1
# while a not in range(1, len(sols)+1):
#     print("ques")
#     print("for z in ...")
#     a = input()
#     while True:
#         try:
#             a = int(a)
#             break
#         except ValueError:
#             print("again")
#             a = input()
#     if a not in range(1, len(sols)+1):
#         print("wrong num, again. Type 1-", len(sols))


# from random import shuffle
#
# def func(q, ifcor, ifnotcor, *don):
#     global result
#     correct = don[0]
#     don = list(don)
#     shuffle(don)
#     a = - 1
#     while a not in range(1, len(don) + 1):
#         # вивід питання і варіантів
#         print(q)
#         for A in range(len(don)):
#             print(f"{A + 1}) {don[A]}")
#         a = input()
#         try:
#             a = int(a)
#         except (ValueError, IndentationError):
#             print("error, Type 1-", len(don), "\n")
#             continue
#         if a not in range(1, len(don) + 1):
#             print("wrong num, again. Type 1-", len(don), "\n")
#             continue
#         if correct == don[a-1]:
#             print(f"{ifcor}\n")
#             result += 1
#         else:
#             print(f"{ifnotcor}\n")
#
#
# result = 0
# func("Сколько патронов в одной обойме Ak-47:", "малалдэц", "це знать нада",
#      "30 патронов", "27 патронов", "25 патронов", "35 патронов")
# func("ти куриш?", True, False,
#      "да", "возможно", "не точно", "чучуть", "інколи")
# print(f"you scored {result} point")


# complete the task above

# lst = [4, 8, 5, 6, 2]
# lst1 = tuple(filter(lambda elem: elem > 3 and elem % 2 == 0, lst))
# print(lst1)

# dicts


# import turtle
# t1 = turtle.Turtle()
# t2 = turtle.Turtle()
# t3 = turtle.Turtle()
#
# t1.color("red")
# t2.color("black")
# t3.color("green")
#
# t1.lt(120)
# t2.lt(240)
# t3.lt(0)
#
# t1.speed(0)
# t2.speed(0)
# t3.speed(0)
#
# t1.width(4)
# t2.width(4)
# t3.width(4)
#
# for z in range(30, 1000):
#     t1.fd(abs(25-z))
#     t2.fd(abs(25-z))
#     t3.fd(abs(25-z))
#
#     t3.left(45)
#     t1.left(45)
#     t2.left(45)
# turtle.done()

# import random
# from random import randint
# list = ("rock", "scissors", "paper")
# # list.choise()
# for z in range(10):
#     print(random.choice(list))

# 1..3 random picking with stats
# RCP game

# from time import sleep
#
# for z in range(3, 0, -1):
#     print(f"\n{z}", end="")
#     for i in range(3):
#         print(".", end="")
#         sleep(0.3)

# from random import choice, randint, shuffle
#
# lst = {'a', 'b', 'c', 'd'}
# print(choice(lst))
#
# print(lst[randint(0, len(lst)-1)])


# def door_picking(att, deff, *args):
#     for z in range(len(args)):
#         args[z]
#
# lst = ['a', 'b', 'c']
# for i, e in enumerate(lst):
#     print(f'index: {i} value: {e}')

# door_picking("Robber", "Guard", 1, 2, 3)

# # embedded collections

# test_results = [
#     [85.4, 71.6, 93.2, 65.8, 45.0],
#     [89.5, 80.0, 95.5, 76.5, 72.0]
# ]


# print('Середній результат «пробного»:', sum(test_results[0]) / len(test_results[0]))
#
#
# print('Середній результат «основного»:', sum(test_results[1]) / len(test_results[1]))
#
#
# departments = {
#     'продажу': {
#         'співробітники': ['Гришин', 'Іванова'],
#         'менеджер': 'Іванова',
#         'завідувач': 'Гришин'
#     },
#     'розробка': {
#         'співробітники': ['Васильєв', 'Єжова', 'Петрова'],
#         'менеджер': 'Єжова',
#         'завідувач': 'Петрова'
#     },
#     'ігровий відділ': {
#         'співробітники': ['Ваас', 'Біла', 'Чорна'],
#         'менеджер': 'Корникова',
#         'завідувач': 'Стус'
#     }
# }
#
# print("Завідуючі відділів:")
# for key in departments.keys():
#     if "завідувач" in departments[key]:
#         print(key, "-", departments[key]['завідувач'])
# print("Проектні менеджери відділів:")
# for key in departments.keys():
#     print("-", departments[key]['менеджер'])
# for key in departments.keys():
#     print("-", departments[key]['завідувач'])
# print("співробітники:")
# for key in departments.keys():
#     for elem in departments[key]['співробітники']:
#         print("-", elem)
# допиши виведення даних
#
#
# trainings = {
#     'Онбордінг': {
#         'відповідальний': 'Єршов В.С.',
#         'теми': ['техніка безпеки', 'робота в команді'],
#         'дата': '15.05'
#     },
#     'Підвищення кваліфікації': {
#         'відповідальний': 'Мішин Н.В.',
#         'теми': ['лідерство', 'комп. грамотність'],
#         'дата': '20.11'
#     }
# }
# print('Тренінги ProTeam')
# print('1-назви тренінгів, 2-інфо про тренінг')
# action = input('Номер дії (off-вийти):')
# while action != 'off':
#     if action == '1':
#         for training in trainings:
#             print('-', training)
#     if action == '2':
#         title = input('Назва тренінга:')
#         if title in trainings:
#             print(trainings[title]['відповідальний'])
#             print(trainings[title]['теми'])
#             print(trainings[title]['дата'])
#         else:
#             print('Такого тренінгу не існує!')
#     action = input('Номер дії (off-вийти):')
#
#
#
# def staff_min_efficiency(staff):
#     # s = []
#     # for key in staff.keys():
#     #     s.append(staff[key]["ефективність"])
#     return min([staff[key]['ефективність'] for key in staff.keys()])
#
#
# def staff_max_efficiency(staff):
#     return max([staff[key]['ефективність'] for key in staff.keys()])
#
#
# staff = {
#     'Смирнов': {
#         'посаду': 'менеджер з продажу',
#         'ефективність': 86
#     },
#     'Колягина': {
#         'посаду': 'менеджер з продажу',
#         'ефективність': 69
#     },
#     'Костін': {
#         'посаду': 'менеджер з продажу',
#         'ефективність': 78
#     },
#     'Щербаков': {
#         'посаду': 'менеджер з продажу',
#         'ефективність': 91
#     },
#     'Борисова': {
#         'посаду': 'менеджер з продажу',
#         'ефективність': 99
#     }
# }
# print('Кращий результат:', staff_max_efficiency(staff))
# print('Найгірший результат:', staff_min_efficiency(staff))
#
# # Допиши висновок даних
#
#
# staff = {
#     'Фролова': {
#         'посаду': 'маркетолог',
#         'ефективність': 71
#     },
#     'Коровін': {
#         'посаду': 'маркетолог',
#         'ефективність': 65
#     },
#     'Пивоваров': {
#         'посаду': 'маркетолог',
#         'ефективність': 49
#     },
#     'Лістьєва': {
#         'посаду': 'маркетолог',
#         'ефективність': 53
#     }
# }
#
#
# def lil_eff(staff):
#     for key in staff.keys():
#         if staff[key]["ефективність"] < 50:
#             print(f"Співробітник {key} рекомендований до звільнення")
#             del staff[key]
#     print("Ефективні співробітники:")
#     for key in staff.keys():
#         print(key)
#
#
# lil_eff(staff)


# lst = [[62, 43, 56, 47],
#        [70, 58, 65, 50],
#        [1, 2, 3, 4, 5]]
#
# for z in lst:
#     print()
#     for j in z:
#         print(j)


# dicts

# departments = {
#     'продажу': {
#         'співробітники': ['Гришин', 'Іванова'],
#         'менеджер': 'Іванова',
#         'завідувач': 'Гришин'
#     },
    # 'розробка': {
    #     'співробітники': ['Васильєв', 'Єжова', 'Петрова'],
    #     'менеджер': 'Єжова',
    #     'завідувач': 'Петрова'
    # },
    # 'ігровий відділ': {
    #     'співробітники': ['Ваас', 'Біла', 'Чорна'],
    #     'менеджер': 'Корникова',
    #     'завідувач': 'Стус'
    # }
# }

# for value in departments.values():
#     print(value['завідувач'])


# staff = {
#     'Фролова': {
#         'посаду': 'маркетолог',
#         'ефективність': 71
#     },
#     'Коровін': {
#         'посаду': 'маркетолог',
#         'ефективність': 65
#     },
#     'Пивоваров': {
#         'посаду': 'маркетолог',
#         'ефективність': 49
#     },
#     'Лістьєва': {
#         'посаду': 'маркетолог',
#         'ефективність': 53
#     }
# }
#
# lst = []
# for v in staff.values():
#     lst.append(v['ефективність'])
# print(max(lst))
#
# for k, v in staff.items():
#     if v['ефективність'] == max(lst):
#         print(k)

# class Car:
#     def __init__(self, mark, model, wheels, color, max_speed):
#         self.brand = mark
#         self.model = model
#         self.wheels = wheels
#         self.color = color
#         self.max_speed = max_speed
#
#     def showMark(self):
#         print(f"It's mark is: {self.brand}")
#
#     def showWheels(self):
#         print(f"It has: {self.wheels} wheels")
#
#     def setWheels(self, new_wheels):
#         self.wheels = new_wheels
#
#
# Volvo = Car("volvo", "model", 4, "brown", 290)
#
# Volvo.setWheels(6)
# Volvo.showWheels()
# from time import sleep
#
# class Bomzh:
#     def __init__(self, name, health, stat, power, promile, ca):
#         self.name = name
#         self.hp = health
#         self.stat = stat
#         self.power = power
#         self.promile = promile
#         self.ca = ca
#         self.power_at_start = power
#         self.power_lvl = 15
#
#     def def_power(self):
#         self.power = self.power_at_start
#
#     def up_power(self):
#         self.power_at_start += self.power_lvl
#
# bomzh1 = Bomzh('petr1', 100, 'male', 15, 25, 200)
# bomzh2 = Bomzh('Ekaterina', 85, 'female', 25, 10, 250)
#
# x = input("Fast or slow?\n")
# if x == "slow":
#     mode = 1.5
# elif x == "fast":
#     mode = 0.1
#
# def zaruba(att1, att2):
#     while att1.hp > 0 or att2.hp > 0:
#         if att1.hp <= 0 and att2.hp <= 0:
#             print(f"pobedila druzhba!")
#             break
#
#         att1.def_power()
#         # att1 crit
#         if random.randint(1, 100) in range(1, bomzh1.promile + 1):
#             print("\ncrit nuuuuaaaaa")
#             bomzh1.power *= bomzh1.ca / 100
#
#         # att1 att
#         print(f"{att1.name} attacks {att2.name} with power of {att1.power}")
#         att2.hp -= att1.power
#         print(f"{att2.name} has {att2.hp} now\n")
#
#         att2.def_power()
#         # att2 att
#
#         bomzh1.power = bomzh1.power_at_start
#         sleep(mode)
#         if att2.hp <= 0:
#             print(f"{att1.name} has won with {att1.hp} left")
#             break
#
#         print(f"    {att2.name} attacks {att1.name} with power of {att2.power}")
#         att1.hp -= att2.power
#         print(f"    {att1.name} has {att1.hp} now\n")
#         sleep(mode)
#         if att1.hp <= 0:
#             print(f"{att2.name} has won with {att2.hp} left")
#             break
#
#
#
#
# zaruba(bomzh1, bomzh2)
#
# import random
#
# # for z in range(5):
#     if random.randint(1, 100) in range(1, bomzh1.promile+1):
#         print("crit nuuuuaaaaa")
#         bomzh1.power *= bomzh1.ca / 100
#         print(bomzh1.power)
#         bomzh1.power = bomzh1.power_at_start
# # print(bomzh1.power)

