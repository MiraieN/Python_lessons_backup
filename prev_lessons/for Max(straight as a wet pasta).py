# d = {
#     "Krym": "nash",
#     "Krym1": "nash1",
#     "Krym2": "nash2",
#     "Krym3": "nash3",
#     "Krym4": "nash4"
#
# }
#
# d["Krym5"] = "nash5"
# print(d.items())


# x = {i: str(i) for i in range(10)}
# for k, v in d.items():
#     print(k, v)

# try:
#     #smoke testing sign in button
#     a = tuple(range(9, -1, -1))
#     b = tuple(range(10, 20))
#     for z in range(len(a)):
#         print(b[z]/a[z])
# except ZeroDivisionError:
#     print("чида 70")
# finally:
#     print("Testcase", 123)

# print(d.keys())

# print(tuple(d.values()))
# print(d.items())
# print(d)
# list = [z for z in range(10)]
# print(list)

# lst = [1, 2, 3, 4, "5", 6]
# for z in lst:
#     if isinstance(z, str):
#         raise ValueError
# else:
#     print("it is int")
# print("checking the tail")

# c = {}
# txt = "Hmelnitzkiy Bogdan Sich SCP 5 5 5 5 5 5 5 0".split()
# lsd = ['Surname', 'Name', 'c', 'u', 'g']
# for z in range(len(lsd)):
#     if not lsd[z] == 'g':
#         c[lsd[z]] = txt[z]
#     else:
#         c['grades'] = []
#         for z in txt[4:]:
#             c["grades"].append(z)

# for k, v in cheloveku.items():
#     print(k, v)
# st = {1, 2, 3, 4}
# d = {1:1, 2:2}
# f = {}
# print(type(f))

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# print([elem for elem in a if elem in b])
#
# print(list(set(a) & set(b)))

# d = {
#     'dict': 1,
#     'dictionary': 2
# }
#
# d = dict(short='dict', long='dictionary')

# lst = [i for i in range(10)]
# lst = [(1, 2), (2, 3)]
# d = dict.fromkeys(lst)

# a = {a: a ** 2 for a in range(5, 10)}
# print(a)
# x = d.copy()
#
# d.update(a)
# print(d)
#
# result = 1
# for z in range(10):
#     result = result * z

# def f(*args):
#     for elem in args:
#         print(elem)
#     # return args
#
#
# print(f(1, 2, 3, 3, 4))


# def func(**kwargs):
#     for num, val in kwargs.items():
#         print(num, val)
#
# func(one=5, two=4)

# name = ('John', 'Nicholas', 'Mercy')
# age = (25, 26, 27)
# dict_sample = {}
# for z in range(len(age)):
#     dict_sample[age[z]] = name[z]
# print(dict_sample)

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
# #простіший варіант - до 2-3 черепашок
# max_x = max(x.xcor(), y.xcor())
# if x.xcor() == max_x:
#     winner(x)
# elif y.xcor() == max_x:
#     winner(x)
#
# # # складніший варіант - для любої к-сті черепашок
# # d_cors = {x: x.xcor(), y: y.xcor()}
# # max_x = max(d_cors.values())
# # for k, v in d_cors.items():
# #     if v == max_x:
# #         winner(k)

# from operator import itemgetter
# d = {'a': 3, 'ab': 2, 'abc': 1, 'abcd': 0}
# print("Dictionary: ", d)
#
# # sort_dict = dict(sorted(d.items(), key=itemgetter(0)))
#
# # print("Sorted Dictionary by key: ", sort_dict)
#
# sort_dict = dict(sorted(d.items(), key=itemgetter(1)))
#
# print("Sorted Dictionary by value: ", sort_dict)

# lst = [1, -5, 4, -3, 2, -5]
# # lst_s = sorted(lst, key=lambda x: abs(x))
# lst_f = list(filter(lambda x: x % 2 == 0, lst))
# # print(lst_s)
# print(lst_f)

# def func(*birds):
#     for bird in birds:
#         print("fuck " + bird + " away")
# func("stork", "sparrow", "raven")

# # args - arguments
# # kwargs - key word arguments
# from operator import itemgetter
#
#
# def func(**jobs):
#     cent = lambda txt: txt.center(35, "♥")
#     jobs_s = dict(sorted(jobs.items(), key=itemgetter(1)))
#     print(cent("Zaporozhye wages"))
#     for k, v in jobs.items():
#         print(cent(f'job: {k}, wage: {v}'))
#
#
# func(barista=9000, guard=8300, nurse=8400, marketer=15000)
# A = dict(zip('abcdef', list(range(6))))
# for key, val in A.items():
#     print(key, val)
