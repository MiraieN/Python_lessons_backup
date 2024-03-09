# print('Hello world')

# # variable - var
# num = 5
# txt = "Hello world"

# # names of variable
# bill_for_electricity = 1.21
# billForElectricity = 1.23
# num1 = 4
# num2 = 5

# # wrong
# bill@for = 1.2
# 123num = 123

# Integer - int
# operations      (+ - / * += -= % // **)
# num1 = 4
# num2 = 5
# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)      # float
# print(num1 / 0)         # ZeroDivisionError

# скорочення
# num1 = num1 + 2
# num1 += 2
# num1 -= 2
# num2 *= 2
# num2 /= 2

# // % **
# num3 = num1 % 2
# num3 = num1 // 3
# num3 = num1 ** 2
# num3 = num1 ** (1/2)
# print(len(str(num3)))

# HW
# input()

# from turtle import *
#
# shape("turtle")
# shapesize(2)
# color("red")
# speed(0)
# ht()
# for z in range(120):
#     color('red')
#     circle(z)
#     color('orange')
#     circle(z*0.8)
#     rt(3)
#     fd(3)
# t1 = Turtle()
# exitonclick()

# txt = 'asd'
# num = 5
# print(txt * num)

# # TYPES OF DATA

# types casting str(), int()

# String - str - текстовий
# print("всі слони живуть на Марсі")

# Integer - int - цілочисельний
# txt = '5'
# num = 3
#
# print(txt + str(num))
# print(int(txt) * num)

# txt = int(txt)
# num = str(num)

# print(txt - num)

# TypeError
# 'asd' - 5

# IndentError
# не відступай пж

# num = 5
# print((num + 1) ** 2)
# name = input("What is ur name?\n")
# print("Hello, I'm " + name)
# print("Hello, I'm", name)
# print('Hello me', name, "I'm", 23, 'years old')

# f-string
# print(f'Hello, I\'m {name}. I\'m {23} years old')

# print(int(input("Ur number?")) + 2)
# name = 'v'
# print(f'''
# name:{name}
#     asd asdasd                  adas
#     asdasd  asdasd
# ''')

# fnum = round(10/6, 4)
# fnum = 33/7
# fnum = fnum - int(fnum)
# print(fnum)


# Boolean - bool:   True   False
# b = True
# print(b)
# > < >= <= != ==
# if int(input("num?\n")) == 5:
#     print("It's five")
# if True:
#     print('It"s five')
# if False:
#     print("It's five")
# if 5 != 5:
#     print(True)

# num = int(input("Num?\n"))
# # and
# if num > 3 and num < 8:
#     print("3...8")

# if True and True:
#     print(True)
# if False and True:
#     print(False)
# if False and False:
#     print(False)
# # і те і те правда
# if "є продукти" and "я голодний":
#     print("готуємо")

# city = input("City?\n")
# # or
# if city == 'Uman' or city == 'uman':
#     print("u r in Uman")
# if True or True:
#     print(True)
# if True or False:
#     print(True)
# if False or False:
#     print(False)

# city = input("City?\n").lower()
# if city == 'uman':
#     print("Hasudu")
#     print()
# elif city == 'chercassy':
#     print("voenkomat")
# elif city == 'kiev':
#     print("Nope thx")
# else:
#     print("I don't knoooow")

# x = int(input("num1?\n"))
# y = int(input("num2?\n"))
# print(f"{x} is bigger" if x > y else f"{y} is bigger")

# # # test create
# # rules
# score = 0
# print("rules: this is smeshariki test: which melanholik u are?")
# # 1
# ans = input("question1: чи любите ви виражати думки в поезії?").lower()
# if ans == 'yes':
#     print("маяковський був алкоголіком")
#     score += 1
# else:
#     print("ті хто не пишуть вірші також алкоголіки")
# #2
# ans = input("question2: r2d2 was a").lower()
# if ans == 'robot':
#     print("bip-bup")
#     score += 1
# else:
#     print("buuuup")
# # .... 12+
# if (mel > sang) and (mel > hol) and (mel > flegm):
#     print("mel")
# if score < 5:
#     print("plox")
# elif score < 10:
#     print("neplox")
#     # ...


# temp = 36
#
# if temp > 20:
#     if temp > 35:
#         print("Hot!")
#     else:
#         print("warm")
# else:
#     print("Cold!")

# age = 21
# if age >= 18:
#     if age >= 21:
#         print("u r allowed to drink alcohol")
#     else:
#         print("U r not allowed for alcohol")
#     print("U can drive a car if u have a licence")
# else:
#     print("U r less than 18")

# num1 = 2
# num2 = 0
# op = "/"
# if op == "*":
#     print(f"{num1} * {num2} = {num1 * num2}")
# if op == "/":
#     if num2 != 0:
#         print(f"{num1} / {num2} = {num1 / num2}")
#     else:
#         print("0 error")

# print('''
# Розробка та впровадження принципово нових технологій, заснованих на останніх досягненнях науки і техніки, – головна риса теперішнього ета- пу развитку виробництва. Серед різних видів сучасних технологій особлива роль належить променевим технологіям, які полягають у впливі на поверхню матеріалу висококонцентрованих променевих потоків або високоенергетичних стру- менів. Дані методи набули інтенсивного розвитку у другій половині XX століття і сьогодні займають повноправне місце серед інших технологій, що застосовуються в різних галузях, у тому числі в машинобудуванні. Носіями енергії в цих методах є світловий промінь високої енергії, потік прискорених заряджених частинок – електронів, а також плазмо- вий струмінь. Відмінною рисою променевих методів обробки є відсутність тради- ційного робочого інструменту, роль якого виконує безпосередньо викорис- товуване випромінювання, яке надає теплового впливу на матеріал. Променеві технології досить широко вже застосовуються у багатьох процесах машинобудування:  у технологіях отримання конструкційних та інструментальних мате- ріалів із заданими властивостями – переплавленні металу з метою рафіну- вання, а також у термообробці і легуванні;  у технологіях виготовлення заготовок та деталей машин – промене- вих способах зварювання, розмірній обробці;  при нанесенні зносостійких покриттів, у тому числі на різальний ін- струмент, відновленні зношених поверхонь виробів;  у сучасних методах вимірювальної техніки та контролю якості і т. д. Важливу роль відіграють променеві методи в технологіях розмірної обробки заготовок деталей машин. Як відомо, за видом використовуваної енергії методи розмірної об- робки поділяють на механічні, фізико-хімічні та комбіновані, рис.1.1.
# '''.replace("-", ""))
# txt = "Лазер – це один з найбільш значущих винаходів минулого столі-ття.Лазери знайшли застосування в самих різних областях – від корекції зору до космічних по-льотів від керування транспортними засобами до термоядерного синтезу.Найбільш затребувані промисловістю лазерні методи обробки матеріалів – це різання, зва-рювання та маркування. При зварюванні сталей, які можуть вийти на структуру мартенситу,краще використовувати гібридну технологію зварювання. Методи гібридного зварювання забез-печують великі часи термічних циклів, по продуктивності випереджають електродугове зварю-вання і задовольняють вимогам поточного виробництва. В основному їх застосовують в автомо-білебудуванні. Лазерне зварювання найбільш підходить до аустенітних сталей. Використання ска-нуючих пристроїв, що забезпечують коливання лазерного пучка, дозволяє зварювати деталі навітьпри великих зазорах, при неточній підгонці стику."
# txt1 = ""
# for i, e in enumerate(txt):
#     if e == "-":
#         if txt[i-1] != " " and txt[i+1] != " ":
#             txt1 += ""
#     elif e == "." and i != len(txt)-1 and txt[i+1] != " ":
#         txt1 += ". "
#     else:
#         txt1 += e
#
# print(txt1)


