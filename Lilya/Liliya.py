# def bill_count(type, rastoch, tariff):
#     res = rastoch * tariff
#     return f"U consumed {rastoch} of {type} for {res} hrn"
#
# print(bill_count("water", 6, 50))

# def bill_count(rastoch, tariff):
#     res = rastoch * tariff
#     return res
#
#
# water = bill_count(6, 50)
# gas = bill_count(35, 0.15)
# electricity = bill_count(200, 2.5)
#
# zhuttya = water + gas + electricity
# print(f"ти не з'їси {int((zhuttya+1500)/80)} шаурм")

# def func(a, b, c=(0, 0)):
#     print(f"{a} + {b} + {c}")
#
#
# func(2, 3, (1, 2))

# print()


# def print(values=(), end="\n", sep=" "):
#     return

# def is_year_leap(year):
#
#     if year % 400 == 0:
#         return True
#
#     if year % 4 == 0 and year % 100 != 0:
#         return True
#
#     return False
#
#
# print(is_year_leap(2000))

# def question(a, *d, b, c):
#     global result, average
#     if True:
#         result += 1
#
#
# result = 0
# average = 0
# question(
#     "question1", "1", "2", "3", "4",
#     "correct", "wrong")
# question(
#     "question2", "1", "2", "3", "4", "5"
#     "correct", "wrong")
#
# print(result)
#
# def func(mom, dad, *vars):
#     print(mom)
#     print(dad)
#     return vars

#
#
# res = 0
# func("quest", "correct", 1, 2, 3, 4)
# func("quest", "correct", 1, 2, 3, 4)
# print(res)

# print(f"")
# print("{0} {0} {1}".format("asd", "1"))     # f-string

# import math
# print(math.factorial(5))
# garbage collector


## objects
# import turtle
# t = turtle.Turtle()
# t.fd(10)

# def is_palin(string):
#     string = string.replace(" ", "")
#     return string == ''.join(reversed(string))
#
#
# print(is_palin("is ninsi"))
# print("did" == "d id".replace(" ", ""))

# lst = [1,3,2,3,3,3]
# # lst.sort()
# lst = sorted(lst)
# print(lst)

# values = input().split(',')
# values = list(map(int, values))
# print(values)
# lst = []
# for elem in values:
#     lst.append(int(elem))
# print(lst)


# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#
#
# print(twoSum([3, 4, 2], 6))

# # https://leetcode.com/problems/palindrome-number/
# from horology import Timing
# from time import sleep


# def isPalindrome(x):
#     if x >= 0:
#         rev = 0
#         temp = x
#         while temp != 0:       # temp = 121  # temp = 12  # temp = 1
#             rev *= 10          # rev = 0     # rev = 10   # rev = 120
#             rev += temp % 10   # rev = 1     # rev = 12   # rev = 121
#             temp = temp // 10  # temp = 12   # temp = 1   # temp = 0
#         if x == rev:
#             return True
#     return False


# def isPalindrome(x):
#     x = str(x)
#     return x == x[::-1]


# with Timing(name="time: "):
#     print(isPalindrome(121))


# for _ in range(10):
#     with Timing(name='time: '):
#         # sleep(0.0001)
#         for z in range(19000, 20000):
#             isPalindrome(z)

# x = [
#  [1, 2],
#  [4, 5],
#  [7, 8]
# ]

# result = [
#  [0, 0],
#  [0, 0],
#  [0, 0]
# ]

# result = [
#  [0, 0, 0],
#  [0, 0, 0]
# ]
#
#
# for i in range(len(x)):
#     for j in range(len(x[i])):
#         result[j][i] = x[i][j]
#
# print(result)

# my_list = [
#  [1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]
# ]
# t = my_list[0][0]
# for row in my_list:
#     for elem in row:
#         print(t < elem)


# flat_list_1 = [elem for row in my_list for elem in row]
# print(flat_list_1)
# x_1 = []
# for row in my_list:
#     for elem in row:
#         x_1.append(elem)
# print(x_1)

### ______________________________
#### FILES
### ______________________________
# with open("abc.txt", "r") as file:
#     print(file.read())
# # ось тут файл вже закритий
# file.read()

# file = open("C:/Users/vladb/PycharmProjects\\abc.txt")
# print(file.read())

# 123asdzxc
# file = open("abc.txt", "r")
# print(file.read())
# file.seek(4)
# print(file.read(2))
# print(file.read(4))


# print(file.readlines())

# for line in file.readlines():
#     print(len(line))
#     print(len(line.strip()))
# lines = [line.strip() for line in file.readlines()]
# for line in lines:
#     for elem in line:
#         print(f"{elem} is upper: {elem.isupper()}")

# якщо не відкриваєш через with, то потрібно файл і закрити
# file.close()

# file = open("abc.txt", "r+")  # для читання і запису(файл не чиститься)
# file = open("de.txt", "w+")    # для читання і запису(файл очищається)
# print(file.read())
#
# for x in range(10):
#     for c in range(5):
## перший варіант запису в файл
# file.write(str(x)*c+"\n")

# file.write(str(x))
# file.write(f"{x}")

## другий варіант запису в файл
# print(x, file=file)
# file.seek(0)
# print(file.read())

## об'єкт створився відразу
# from turtle import *
# lt(90)
# done()


# його треба створити
# import turtle
# t = turtle.Turtle()
# a = turtle.Turtle()
# t.speed(0)
# a.speed(0)
# for x in range(100):
#     t.rt(90)
#     t.fd(100)
#     a.lt(90)
#     a.fd(100)
# # turtle.lt(90)
# turtle.done()


# import turtle as t
#
#
# def f(p=True):
#     if p:
#         file.write(f"{round(t.xcor(), 2)} {round(t.ycor(), 2)} ")
#     else:
#         file.write(f"{round(t.xcor(), 2)} {round(t.ycor(), 2)}\n")
#
# # def s():
# #     file.write(f"{round(t.xcor(), 2)} {round(t.ycor(), 2)}\n")
#
# # x, y = t.xcor(), t.ycor()
# # t.fd(500)
# # x1, y1 = t.xcor(), t.ycor()
# # print(x1-x + y1-y)
# file = open("x_and_y.txt", "w+")
# # print(t.xcor(), t.ycor(), file=file)
#
# t.lt(90)
#
# f()
# t.fd(100)
# f(False)
#
# # s()
#
#
# file.write(f"{round(t.xcor(), 2)} {round(t.ycor(), 2)} ")
# t.fd(100)
# file.write(f"{round(t.xcor(), 2)} {round(t.ycor(), 2)}\n")
#
# t.lt(90)
#
# file.write(f"{round(t.xcor(), 2)} {round(t.ycor(), 2)} ")
# t.fd(100)
# file.write(f"{round(t.xcor(), 2)} {round(t.ycor(), 2)}\n")
#
# file.seek(0)
# print(file.read())


# from horology import Timing
# for x in range(10, 90, 5):
#      with Timing(name="time: "):
#          for i in str(x):
#             user_input = list(str(i))
#             summa = 0
#             dob = 1
#             for i in user_input:
#                 i = int(i)
#                 summa += i
#                 dob *= i
#          print(f"Sum:{summa} Dob:{dob}")
# print()
# print()
#
# import math
# for x in range(10, 90, 5):
#      with Timing(name="time: "):
#          user_input = [int(i) for i in str(x)]
#          print(f"Sum:{sum(user_input)} Dob:{math.prod(user_input)}")


# #порівняти 2 файли і знайти лишній символ
# file_1 = open("123.txt", "r")
# file_2 = open("1.txt", "r")
# h = file_1.readline()
# f = file_2.readline()
# if len(h) < len(f):
#     h, f = f, h
# for i in range(len(h)):
#     if f[i] != h[i]:
#         print(f"file: {file_1.name}\nindex: {i}\nelement: {h[i]}")
#         break
# file_1.close()
# file_2.close()


# import random
# print(random.choice({1, 2, 3, 4}))
# print(random.choice({1:"as", 2:'asd'}))
# for i in 123:
#     if i == '2':
#         continue
#     else:
#         print(i)

# print('12312'[2])
# print([1, 2, 3][3-1])

# iterable (subscriptable)
# str list tuple dict
# not iterable (not subscriptable)
# set int frozenset

# a = 2
# b = 3

# temp = a
# a = b
# b = temp
# print(a, b)

# a, b = b, a

# 00
# 01 11
# 02 12 22
# 03 13 23 33
# 04 14 24 34 44
# print("Кількість пластинок:", sum([num for num in range(1, int(input("Кількість вічок: "))+2)]))

# number = input("число: ")
# number = ''.join((number[0], number[3], number[2], number[1]))
# print(int(number))

# l = ['apple', 'plum', 'grapes', 'apricot']
# # s = ''
# # for elem in l:
# #     s += elem
# #     s += ", "
# # print(s)
# print(', '.join(l))

# lst = [1]
#
# # виводить якщо пустий
# if not lst:
#     print("1")
#
# # виводить якщо щось є в списку
# if lst:
#     print("1")

# groshi = 30
# p = 1.20
# e = 0.20
# amount = 0
# while groshi > 0:
#     c = groshi // p
#     groshi -= c * 1.20
#
#     groshi += c * 0.2
#
#     amount += 1
# print(amount)

# print(int(input()) - 1)

# a = int(input("?"))
# print(len([1 for num in range(100, 1000) if sum([int(n) for n in str(num)]) == a]))
# print(True if 2 == 2 else False)
# def f():
#     return True if a == 2 else False
# l = []
# for num in range(100, 1000):
#     lst = [int(n) for n in str(num)]
#     if sum(lst) == a:
#         l.append(num)
# print(len(l))
#
# print(len([num for num in range(100, 1000) if sum([int(n) for n in str(num)]) == a]))


# def merge(list1, list2):
#     return sorted(list1 + list2)
#
#
# print(merge([1,2,4],[1,3,4]))

# def regular_factorial(n):
#     f = 1
#     for x in range(1, n+1):
#         f *= x
#     return f
#
#
# def recur_factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n * recur_factorial(n - 1)
#
#
# def list_factorial(n):
#     import math
#     return math.prod([x for x in range(1, n+1)])
#
#
#
# from horology import Timing
#
#
# def for_Timing(func, num):
#     with Timing(unit="ms"):
#         return func(num)
#
#
# for num in range(900, 998):
#     for_Timing(regular_factorial, num)
#     for_Timing(recur_factorial, num)
#     for_Timing(list_factorial, num)
#     print()

# a = [1, 2, 3, 4]
# b = [1, 2, 3]
# print(type(a))
# print(len(a))
# len("123")
# len([1,2,3])

# from tkinter import *
#
# window = Tk()
# window.title("┐(￣ヘ￣)┌")
# window.geometry("530x800+600+200")
#
# # # Label(text="^--^", font="ComicSans 222").pack()
# # # Label(text="-__-", font="ComicSans 222").pack()
# #
# # lbl1 = Label(text="^--^", font="ComicSans 222")
# # lbl2 = Label(text="-__-", font="ComicSans 222")
# #
# # ent = Entry(font=("comic sans ms", 22, "bold", "underline"))
# # # ent = Entry(font="arial 22 bold underline")
# #
# # but = Button(text="OK",
# #              font=("arial", 22, "bold"),
# #              bg="white", foreground="red")
# #
# # lbl1.pack()
# # ent.pack()
# # lbl2.pack()
# # but.place(x=50, y=100, width=220, height=40)
#
# import re
#
# def summer():
#     lbl['text'] = "june\njuly\naugust"
#
#
# def autumn():
#     lbl['text'] = "september\noctober\nnovember"
#
#
# def checking():
#     def isValid(email):
#         if re.fullmatch(regex, email):
#             print(True)
#         else:
#             print(False)
#
#     regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
#
#     isValid(ent.get())
#
#
#
#
# summer = Button(text="summer",
#              font=("arial", 22, "bold"),
#              bg="white", foreground="red",
#              command=summer)
#
# autumn = Button(text="autumn",
#              font=("arial", 22, "bold"),
#              bg="white", foreground="red",
#              command=autumn)
#
# check = Button(text="ok",
#              font=("arial", 22, "bold"),
#              bg="white", foreground="red",
#              command=checking)
#
# lbl = Label(text="asd", font=("comic sans ms", 22, "bold", "underline"), relief="raised")
#
# ent = Entry(font=("comic sans ms", 22, "bold", "underline"))
#
#
# lbl.place(x=340, y=10, width=170, height=400)
# summer.pack()
# autumn.pack()
# ent.pack()
# check.pack()
#
# mainloop()


# from tkinter import *
# from tkinter.simpledialog import *
#
# window = Tk()
# window.title("┐(￣ヘ￣)┌")
# window.geometry("530x800+600+200")
#
#
# def show(event):
#     lbl1['text'] = "непонімаєме"
#
#
# lbl = Label(text="font", font=("comic sans ms", 22, "bold", "underline"), relief="raised")
# lbl1 = Label(text="asd", font=("comic sans ms", 22, "bold", "underline"), relief="raised")
# lbl2 = Label(text="main", font=("comic sans ms", 22, "bold", "underline"), relief="raised")
# ent = Entry(font=("comic sans ms", 22, "bold", "underline"))
#
#
# lbl.pack()
# lbl1.pack()
# lbl2.pack()
# ent.pack()
#
#
# lbl.bind('<Button-1>', show)
#
#
# mainloop()

# d = {
#     range(10, 21): "років",
#     range(2, 5): "роки",
#     (1, 3): "рік",
#     range(5, 10): "років"
# }

# d = {1: "рік",
#      2: "роки",
#      3: "роки",
#      4: "роки",
#
#      5: "років",
#      6: "років",
#      7: "років",
#      8: "років",
#      9: "років"}
#
# age = 11
# for key in d.keys():
#     if age%10 in key:
#         print(f"Вам {age} {d[key]}")
#         break
# print(f"Вам {age} {d[age % 10]}")


# from tkinter import *
# from tkinter.simpledialog import *
# from tkinter.messagebox import *
# from tkinter import messagebox
#
# pr = askstring("Name", "Name")
#
# print(messagebox.askokcancel("title", "message"))
# print(messagebox.askretrycancel("title", "message"))

#
# while True:
#     pr = askstring("Name", "Name")
#     if not pr.isalpha():
#         showerror("Error", "Only letters")
#         continue
#     elif not pr[0].isupper():
#         showerror("Error", "First is upper")
#         continue
#     break
#
# sr = askstring("surname", "surname")
#
# print(pr, sr)
#
# x = showinfo("Gratz", "You are in")

# file = open('abc.txt', 'r')
# file_1 = open('abc1.txt', 'w+')
#
# c = [line.strip() for line in file.readlines()]
# for i in set(c):
#     file_1.write(f"{i}\n")
#
# file.close()
# file_1.close()

# print(eval("2*4+6*2"))

# from tkinter import *
# from tkinter.messagebox import showinfo
#
# window = Tk()
# window.title("┐(￣ヘ￣)┌")
# window.geometry("530x800+600+200")
#
# def f():
#     if var.get() == 1:
#         print("1")
#
# var = IntVar()
#
# r = Radiobutton(text="Київ", variable=var, value=1, command=f)
# r1 = Radiobutton(text="Умань", variable=var, value=2, command=f)
# r2 = Radiobutton(text="Черкаси", variable=var, value=3, command=f)
#
# r.pack()
# r1.pack()
# r2.pack()
#
# d1_var = IntVar()
# d2_var = IntVar()
#
# d1 = Checkbutton(text='Морозиво "Казка"', variable=d1_var)
# d2 = Checkbutton(text="Морозиво з шоколадом", variable=d2_var)
#
# d1.deselect()
# d1['state'] = NORMAL
# d1.select()
# d1['state'] = DISABLED
#
# mainloop()

# from tkinter import *
#
# window = Tk()
# window.title("┐(￣ヘ￣)┌")
# window.geometry("530x800+600+200")
# t = ("1", "2", "3")
# var = Variable(value=t)
#
# a = Listbox(listvariable=var)
# b = Listbox(height=3)
#
# b.insert(END, '1')
# # for elem in ("1", "2", "3"):
# #     a.insert(END, elem)
#
# for elem in range(a.size()):
#     print(a.get(elem))
#
# # a.delete(1)
#
#
# def abc():
#     try:
#         n = a.curselection()
#         n1 = a.get(n)
#     except:
#         n = a.get(0)
#         n1 = a.get(0)
#
#     b.insert(END, n1)
#     a.delete(n)
#
# but = Button(command=abc)
#
# a.pack()
# but.pack()
# b.pack()
#
# mainloop()


# # # Canvas
# from tkinter import *
# from tkinter import messagebox
#
# def click():
#     global img
#     window.geometry("1200x1000+200+0")
#     img = PhotoImage(file='Cat.png')
#     canvas.config(width=975, height=973)
#     canvas.create_image(0, 0, anchor=NW, image=img)
#
#
# window = Tk()
# window.title("┐(￣ヘ￣)┌")
# window.geometry("700x500+600+200")
# window.iconbitmap('g_icon_254085.ico')
# messagebox.showerror(message="asdas")
#
# canvas = Canvas(window)
# canvas.place(x=400, y=80, width=100, height=100)
#
# img = PhotoImage(file='S:\\arts\\Коть.png')
#
# canvas.create_image(0, 0, anchor=NW, image=img)
#
#
# but = Button(text="OK",
#              font=("arial", 22, "bold"),
#              bg="white", foreground="red",
#              command=click)
# but.pack()
# mainloop()


# # bot with questions with tkinter (tkinter questions)
# from tkinter import *
# from tkinter import messagebox
#
#
# def create_window(ques, correct):
#     def check_ans():
#         global success, failed, checks
#
#         if ent_ans.get() == correct:
#             messagebox.showinfo(message="Вірно")
#             success += 1
#             window.destroy()
#             return
#         else:
#             messagebox.showerror(message="Невірно")
#             checks -= 1
#             print(checks)
#
#         if checks == 0:
#             messagebox.showerror(message="Закінчились спроби")
#             failed += 1
#             window.destroy()
#             return
#
#     global checks
#     checks = 3
#     # print(checks)
#
#     window = Tk()
#     window.title("┐(￣ヘ￣)┌")
#     window.geometry("530x800+600+200")
#
#     lbl_ques = Label(text=ques, font=("comic sans ms", 22, "bold", "underline"), relief="raised")
#     ent_ans = Entry(font=("comic sans ms", 22, "bold", "underline"))
#     but_ans = Button(text="OK", font=("arial", 22, "bold"), bg="white", foreground="red", command=check_ans)
#
#     lbl_ques.pack()
#     ent_ans.pack()
#     but_ans.pack()
#
#     mainloop()
#
#
# success = 0
# failed = 0
#
# quess = {"ques1": "correct1",
#          "ques2": "correct2",
#          "ques3": "correct3",
#          "4": "4"}
#
# for ques, correct in quess.items():
#     create_window(ques, correct)
#
# print(f"success: {success}")
# print(f"failed: {failed}")


# from tkinter import *
# from tkinter import messagebox
#
# window = Tk()
# window.title("┐(￣ヘ￣)┌")
# window.geometry("700x500+600+200")
#
#
# def show(event):
#     messagebox.showerror(message="text")
#
#
# label = Label(text="^--^", font="ComicSans 222")
# label.pack()
# label.bind('<Motion>', show)
#
# mainloop()


# from tkinter import *
#
#
# def locate_xy(work):
#     global current_x, current_y
#
#     current_x, current_y = work.x, work.y
#
#
# def add_line(work):
#     global current_x, current_y
#
#     canvas.create_line((current_x, current_y, work.x, work.y), width=1, fill=color,
#                        capstyle=ROUND)
#
#     current_x, current_y = work.x, work.y
#
#
# def change_color(new_color):
#     global color
#     color = new_color
#
#
# def display_palette():
#
#     colors.tag_bind(colors.create_rectangle((10, 10, 30, 30), fill="red"), btn1, lambda event: change_color("red"))
#
#     id = colors.create_rectangle((10, 40, 30, 60), fill="purple")
#     colors.tag_bind(id, btn1, lambda event: change_color("purple"))
#
#
# color = "black"
# btn1 = "<Button-1>"
# current_x = 500
# current_y = 500
#
# root = Tk()
# root.title("White Board")
# root.geometry("1050x570+150+50")
# root.resizable(False, False)
# root.configure(bg="#f2f3f5")
#
#
# colors = Canvas(root, width=37, height=300, bd=0, background="#ffffff")
# colors.place(x=30, y=60)
#
# display_palette()
#
# canvas = Canvas(root, width=930, height=500, background="white", cursor="hand2")
# canvas.place(x=100, y=10)
#
# eraser = PhotoImage(file="eraser.png")
# Button(root, image=eraser, bd=0).place(x=30, y=400)
#
# canvas.bind("<Button-1>", locate_xy)
# canvas.bind('<B1-Motion>', add_line)
#
#
# #canvas.delete("all") - очищає все полотно
#
# mainloop()

# from tkinter import *
#
# window = Tk()
# # window.geometry("1050x570+150+50")
#
# window.eval('tk::PlaceWindow . center')
#
# but1 = Button(text="!")
# but2 = Button(text="@")
# but3 = Button(text="#")
# but4 = Button(text="$")
# but5 = Button(text="%")
# but6 = Button(text="^")
# but7 = Button(text="*")
#
# # row - ряд
# # column - колонка
# # padx, pady - відступ по х і по у від краю комірки
# # ipadx, ipady - розміри комірки
# # об'єкт розтягується по всій комірці з відступом padx pady
# # span - об'єднання комірок ряду або колонки
# but1.grid(row=0, column=0, ipadx = 30, ipady=30, padx=10, pady=10)
# but2.grid(row=1, column=0, ipadx = 30, ipady=30, padx=10, pady=10)
# but3.grid(row=1, column=1, ipadx = 30, ipady=30, padx=10, pady=10)
# but4.grid(row=1, column=2, ipadx = 30, ipady=30, padx=10, pady=10)
# but5.grid(row=0, column=1, ipadx = 30, ipady=30, padx=10, pady=10)
# but6.grid(row=2, columnspan=3, ipadx=80)
# but7.grid(column=3, row=0, rowspan=3, ipady=80)
#
# but1['text'] = "asd"
#

# mainloop()


# ### surname vars with tkinter ###
# from random import shuffle
# from tkinter import *
#
# root = Tk()
# root.eval('tk::PlaceWindow . center')
#
# d = {}
# d_1 = {}
#
#
# def pressed():
#     global d, d_1
#     if d:
#         for key in d.values():
#             key.destroy()
#         for key in d_1.keys():
#             d_1[key].destroy()
#     d = {}
#     d_1 = {}
#     r = 2
#     c = 0
#     splitted = entry.get().split()
#     rand_list = [num for num in range(1, len(splitted) + 1)]
#     shuffle(rand_list)
#
#     for n in range(len(splitted)):
#         d[n] = Label(text=splitted[n], font=("comic sans ms", 22))
#         d[n].grid(row=r, column=c, padx=15, pady=15)
#         d_1[n] = Label(text=rand_list[n], font=("comic sans ms", 22))
#         d_1[n].grid(row=r, column=c + 1, padx=15, pady=15)
#         r += 1
#
#
# entry = Entry(font=("Comic sans ms", 22))
# entry.grid(row=0, columnspan=2)
# button = Button(text="OK", command=pressed)
# button.grid(row=1, columnspan=2)
#
# mainloop()


# nums = [1, 2, 3, 4]
# vars = ["a", "b", "c", "d"]

# c = 0
# for num in nums:
#     print(num, end="")
#     for var in vars:
#         a = c
#         while a != 0:
#             a -= 1
#             continue
#         print(var)
#         c += 1
#         break

# if len(nums) == len(vars):
#     for i in range(len(vars)):
#         print(f"{vars[i]} - {nums[i]}")


# from tkinter import *
# root = Tk()
# # root.eval('tk::PlaceWindow . center')
# root.geometry("800x600+500+500")
#
#
# def blink_in(event):
#     for val in dict.values():
#         val['bg'] = "yellow"
#     button["bg"] = "yellow"
#
#
# def blink_out(event):
#     for val in dict.values():
#         val['bg'] = "gray"
#
#
# lbl = Label()
# lbl.place(x=0, y=0, width=800, height=600)
#
# button = Button(text="OK", font=88, bg="gray")
# button1 = Button(text="OK", font=88, bg="gray")
# # button.place(x=390, y=290)
#
# dict = {}
# dict["but1"] = button
# dict["but1"].place(x=390, y=290)
# dict["but2"] = button1
# dict["but2"].place(x=390, y=390)
# # dict[i] = id
#
# l = [button]
# l[0].place(x=390, y=290)
#
# button.bind("<Motion>", blink_in)
# lbl.bind("<Motion>", blink_out)
# mainloop()

### DICTIONARY ###
# a = (1, 2, 3)
# dict()
# d = {"033": "Uman",
#      "034": "Chercassy",
#      35: "Kyiv",
#      True: "Lviv",
#      a: "Symu"}
# # print(type(d))
# print(d[a])
# print(a)

# d = {"emails": ["1@gmail.com", "2@gmail.com"],
#      "users": ("Nick", "Stephania")}
# print(d["users"])

# users = {"Nick": {"email": "nick_online@gmail.com",
#                   "username": "Nick_the_Best",
#                   "phone": "+102245784",
#                   "ad_status": False},
#          "Stephania": {"email": "stepha_niiia@gmail.com",
#                        "username": "Stephania_Queen",
#                        "phone": "+102241784",
#                        "ad_status": True},
#          }
# print(users["Nick"]["email"])
# for v in users.values():
#     print(v['phone'])
# for k, v in users.items():
#     print(k, v["phone"])
# for k in users.keys():
#     print(k)

# https://realpython.com/python-dicts/


# # calculator with button blinks
# from tkinter import *
#
# root = Tk()
#
# # root.title("Paint")
# # root.geometry("410x500+450+150")
#
#
# window_width = 410
# window_height = 500
#
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
#
# center_x = int(screen_width / 2 - window_width / 2)
# center_y = int(screen_height / 2 - window_height / 2)
# root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
# root.resizable(False, False)
# # root.attributes('-alpha', 0.8)
# root.attributes('-topmost', 1)  # stay at top
#
# root['bg'] = 'snow'
# root.resizable(False, False)
#
# var = StringVar()
# global_txt = ""
#
#
# def var_add_text(txt):
#     if txt == "=":
#         equals()
#         return None
#     if txt == "C":
#         clear()
#         return None
#     if var.get() == "Error":
#         var.set("")
#     global global_txt
#     print(txt, global_txt)
#     if txt in "+-*/" and global_txt[-1] in "+-*/":
#         return
#     global_txt += txt
#     var.set(global_txt)
#
#
# def blink_in(txt):
#     global buts
#     buts[txt]['bg'] = "red"
#
#
# def blink_out(event):
#     global buts
#     for k, v in buts.items():
#         if buts[k]['bg'] == "red":
#             buts[k]['bg'] = 'snow'
#
#
# def val():
#     def button(txt, row, col):
#         global buts
#         buts[txt] = Button(text=txt, command=lambda: var_add_text(txt), bg="snow")
#         buts[txt].grid(row=row, column=col, ipadx=30, ipady=30, padx=10, pady=5)
#         buts[txt].bind('<Motion>', lambda x: blink_in(txt))
#
#     values = ("9", "8", "7", "+", "6", "5", "4", "*", "3", "2", "1", "-", "0", "/", "=", "C")
#     row = 1
#     col = 0
#     for i in values:
#         button(i, row, col)
#         if col == 3:
#             row += 1
#             col = 0
#         else:
#             col += 1
#
#
# def equals():
#     global global_txt
#     try:
#         expression = eval(global_txt)
#         var.set(expression)
#     except (SyntaxError, ZeroDivisionError):
#         global_txt = ""
#         var.set("Error")
#
#
# def clear():
#     global global_txt
#     global_txt = ""
#     var.set(global_txt)
#
#
# lbl_out = Label()
# lbl_out.place(x=0, y=0, width=window_width, height=window_height)
# lbl_out.bind("<Motion>", blink_out)
#
# buts = {}
# val()
#
# lbl_1 = Entry(textvariable=var, font=("Roboto", 15, "bold"), fg="black")
# lbl_1.grid(row=0, column=0, columnspan=6, ipady=35, ipadx=80)
#
#
# mainloop()


# def find_lowest(staff):
#     minn = 100
#     sur = ""
#     for k, v in staff.items():
#         if v['ефективність'] < minn:
#             minn = v['ефективність']
#             sur = k
#     print(sur, minn)
#
#     # s = []
#     # for k in staff.keys():
#     #     s.append(staff[k]['ефективність'])
#     # a = min(s)
#     # for k, v in staff.items():
#     #     if v['ефективність'] == a:
#     #         print(k, a)
#     #         break
#
#
# staff = {
#     'Смирнов': {
#         'посаду': 'менеджер з продажу',
#         'ефективність': 86,
#         'налоги': {'january': 10,
#                    'june': 12,
#                    'october': 15}
#     },
#     'Колягина': {
#         'посаду': 'менеджер з продажу',
#         'ефективність': 69,
#         'налоги': {'january': 15,
#                    'june': 11,
#                    'october': 13}
#     },
#     'Костін': {
#         'посаду': 'менеджер з продажу',
#         'ефективність': 78,
#         'налоги': {'january': 17,
#                    'june': 16,
#                    'october': 11}
#     },
#     'Щербаков': {
#         'посаду': 'менеджер з продажу',
#         'ефективність': 91,
#         'налоги': {'january': 18,
#                    'june': 18,
#                    'october': 14}
#     },
#     'Борисова': {
#         'посаду': 'менеджер з продажу',
#         'ефективність': 99,
#         'налоги': {'january': 12,
#                    'june': 12,
#                    'october': 15}
#     }
# }


# import tkinter as tk
#
# root = tk.Tk()
# root.geometry("600x400+200+300")
#
#
# lblvar = tk.StringVar()
#
# lbl = tk.Label(textvariable=lblvar)
# lbl.pack()
#
# while True:
#     for milsec in range(1000):
#         lblvar.set(str(milsec))
#         # root.after(5)
#         root.update()
#
#
# root.mainloop()

# d = {0: 0,
#      1: 1}

# d[-1]
# d.pop(-1)
# del d[-1]

# d.popitem()
# print(d)

# d = {
#     'Colorado': 'Rockies',
#     'Boston': 'Red Sox',
#     'Minnesota': 'Twins',
#     'Milwaukee': 'Brewers',
#     'Seattle': 'Mariners'
#     # 1:1, 0:0
# }

# for k in MLB_team.items():
#      print(k)
# print((1, 1) in MLB_team.keys())
# print(MLB_team.get(8, 1))
# d_1 = {1: 1, 0: 0}
# MLB_team.update(d_1)
# d_1 = {1: 2, 0: 0}
# MLB_team.update(d_1)
# print(MLB_team)

# for k, v in d_1.items():
#      d[k] = v
#
# print(d)

# d_1 = [(1, 1), (0, 0)]
# # for k, v in d_1:
# #      print(k, v)
# d.update(d_1)
# print(d)
# d.update(Colorado=1)
# print(d)


# d = {0: 10,
#      2: 9,
#      1: 7}
# lst = [7, 0, 2, 5, 1, 1]
# print(sorted(lst, key=lambda elem: elem % 2))

# lst = ["abc", "abcde", "a"]
# print(sorted(lst, key=lambda e: len(e), reverse=True))

# from operator import itemgetter

# lst = [(1, 1000), (0, 500), (2, 100)]
# lst = dict(lst)
# print(lst)
# print(dict(sorted(lst.items(), key=lambda e: e[0])))
# print(dict(sorted(lst.items(), key=itemgetter(1))))

# # perform 2 times: with itemgetter and without
# sort dict by the len of words in it`s keys
# sort dict by the len of words in it`s values

# sort the list by the first letter of each word, Upper first

# filter list keeping only words starting with upper letter

# filter dict keeping item only if key is str and value is int and in range(0,5)

# filter this dict keeping only dicts with effectivness 80+
# staff = {
#     'Смирнов': {
#         'посаду': 'менеджер з продажу',
#         'ефективність': 86,
#         'налоги': {'january': 10,
#                    'june': 12,
#                    'october': 15}
#     },
#     'Колягина': {
#         'посаду': 'менеджер з продажу',
#         'ефективність': 69,
#         'налоги': {'january': 15,
#                    'june': 11,
#                    'october': 13}
#     },
#     'Костін': {
#         'посаду': 'менеджер з продажу',
#         'ефективність': 78,
#         'налоги': {'january': 17,
#                    'june': 16,
#                    'october': 11}
#     },
#     'Щербаков': {
#         'посаду': 'менеджер з продажу',
#         'ефективність': 91,
#         'налоги': {'january': 18,
#                    'june': 18,
#                    'october': 14}
#     },
#     'Борисова': {
#         'посаду': 'менеджер з продажу',
#         'ефективність': 99,
#         'налоги': {'january': 12,
#                    'june': 12,
#                    'october': 15}
#     }
# }

# d = {
#     'Colorado': 'Rockies',
#     'Boston': 'Red Sox',
#     'Minnesota': 'Twins',
#     'Milwaukee': 'Brewers',
#     'Seattle': 'Mariners'
# }
#
# print(d)
# # print(dict(filter(lambda e: len(e[0]) > 6, d.items())))
# d = dict(filter(lambda e: isinstance(e[0], str) or isinstance(e[0], int), d.items()))
# # print(d)


# # filter this dict keeping only dicts with effectivness 80+
# staff = {
#     'Смирнов': {
#         'посаду': 'менеджер з продажу',
#         'ефективність': 86,
#         'налоги': {'january': 10,
#                    'june': 12,
#                    'october': 15}
#     },
#     'Колягина': {
#         'посаду': 'менеджер з продажу',
#         'ефективність': 69,
#         'налоги': {'january': 15,
#                    'june': 11,
#                    'october': 13}
#     },
#     'Костін': {
#         'посаду': 'менеджер з продажу',
#         'ефективність': 78,
#         'налоги': {'january': 17,
#                    'june': 16,
#                    'october': 11}
#     },
#     'Щербаков': {
#         'посаду': 'менеджер з продажу',
#         'ефективність': 91,
#         'налоги': {'january': 18,
#                    'june': 18,
#                    'october': 14}
#     },
#     'Борисова': {
#         'посаду': 'менеджер з продажу',
#         'ефективність': 99,
#         'налоги': {'january': 12,
#                    'june': 12,
#                    'october': 15}
#     }
# }

# print(staff.items())
# d = dict(filter(lambda k: k[1]['ефективність'] > 80, staff.items()))
# for k, v in d.items():
#     print(k, v)
# print(elem for elem in [1,2,3])

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# c = x.copy()
# # for k, v in x:
# #     c[k] = v
# # for k, v in y:
# #     c[k] = v
# c.update(y)
# print(c)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = {**x, **y}
# print(z)

# from operator import itemgetter
# lang = {'Python': 1990, 'Java': 1995, 'Ruby': 1993, 'C++': 1979}
# print(dict(sorted(lang.items(), key=itemgetter(1))))

# print({k*2: k*4 for k in range(10)})
# print([k*2 for k in range(10)])


# from tkinter import *
# from random import randint, choice
# from resourses.colors import colors_list as colors
#
# root = Tk()
#
# width, height = root.winfo_screenwidth() // 2, root.winfo_screenheight() // 2
# root.geometry(f"{width}x{height}")
#
# root.title('DVD logo')
#
# i = 0
# x = randint(1, 5)
# y = randint(1, 500)
# step_x, step_y = 3, 3
# step_multiplying = 1.05
# # colors = ['black', 'gray', 'brown', 'red', 'orange', 'yellow', 'lime', 'green', 'cyan', 'blue', 'navy', 'magenta', 'purple', 'violet', 'pink']
# lbl_size_x, lbl_size_y = 40, 40
#
# # def l():
# #     global x,y
# #     x += -20
# #     lbl_logo.place(x=x,y=y,width=lbl_size_x,height=lbl_size_y)
#
# def cor():
#     global x, y
#
#     x = randint(1, 500 - lbl_size_x)
#     y = randint(1, 500 - lbl_size_y)
#
#     lbl_logo.place(x=x, y=y, width=70, height=40)
#
# def r():
#     global x, y
#     global step_x, step_y, i, step_multiplying
#
#     while True:
#         if step_x >= 150:
#             step_multiplying = 1
#         if x >= 500 - lbl_size_x or x <= 0:
#             step_x *= -1
#             step_x *= step_multiplying
#         if y >= 500 - lbl_size_y or y <= 0:
#             step_y *= -1
#             step_y *= step_multiplying
#
#         x += step_x
#         y += step_y
#
#         lbl_logo['bg'] = colors[i]
#         lbl_logo.place(x=x, y=y, width=lbl_size_x, height=lbl_size_y)
#
#         Label(bg=colors[i]).place(x=x, y=y, width=lbl_size_x, height=lbl_size_y)
#
#         i += 1
#         if i == len(colors) - 1:
#             i = 0
#
#         root.after(5)
#         root.update()
#
# lbl_logo = Label()
# lbl_logo.place(x=0, y=0, width=lbl_size_x, height=lbl_size_y)
#
# Button(text="Right", command=r).pack()
#
# lbl_logo.bind("<Motion>", lambda event: cor())\
#
#
# try:
#     mainloop()
# except KeyboardInterrupt:
#     exit()

# lst = [1, 2, 3, 4, 5]
# lst.pop(2)
# lst = reversed([1, 2, 3])
# print(lst)
# lst[0] = 1
# # list = [1, 2, 3, 4, 5]
# # list.append(2)

# import tkinter as tk
#
# def move(direction):
#     global x, y
#     if direction == "up":
#         y -= 10
#         lbl_logo.place(x=x, y=y)
#
# def down(event):
#     global y
#     y += 10
#     lbl_logo.place(y=y)
#
# x = 100
# y = 100
#
# root = tk.Tk()
# root.geometry(f"{500}x{500}")
#
# lbl_logo = tk.Label(bg="#E3E3E3")
# lbl_logo.place(x=x, y=y, width=30, height=30)
#
# root.bind("<Up>", lambda event: move("up"))
# root.bind("<Down>", down)
#
# root.mainloop()

# print(type([1,3,3]))

# a = 5
# b = a
# b += 1
# print(a, b)
# txt = "abc"
# txt[0] = "b"
# num = 123
# num[0] = 1

# class Dog:
#     # parameter
#     height = 100
#     width = 50
#     weight = 20
#
# Bullterier = Dog
# print(Bullterier.weight)
#
# Taksa = Dog
# print(Taksa.weight)


# class Dog:
#     # dunder method
#     def __init__(self, height, width, weight):
#         self.height = height
#
# # Bullterier = Dog(height=100, width=50, weight=20)
# Bullterier = Dog(100, 50, 20)
# print(Bullterier.height)

#
# def all_name(*objs):
#     s = ""
#     for obj in objs:
#         s += obj.name
#         s += " "
#     return s
#
#
# class Name:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.alive = True
#         self.salary = 100
#         self.step = 10
#
#     def __str__(self):
#         return f"{self.name} {self.surname} {self.age}"
#
#     def update_age(self, new_age):
#         self.age = new_age
#         return self.age
#
#     def plus_to_age(self, plus):
#         self.age += plus
#         return self.age
#
#     def subtract_age(self, obj):
#         if obj == self:
#             return "same obj twice"
#         return f"Difference in years is: {abs(self.age - obj.age)} between {self.name} and {obj.name}"
#
#     def is_alive(self):
#         return self.alive
#
#     def kill(self):
#         self.alive = False
#
#     def get_salary(self):
#         if self.alive:
#             return self.salary
#
#
#
# name_1 = Name("John","Weit",20)
# name_2 = Name("Liza","Smith",23)
# name_3 = Name("Bob","Brown",19)
# # print(name_1.is_alive())
# name_3.kill()
# print(name_1.get_salary())
# print(name_3.get_salary())
# # print(name_1)
# #
# # name_1.name = "Vlad"
# #
# # name_1.age += 1
# # print(name_1)
# #
# # print(name_1.update_age(22))
# # print(name_1)
# #
# # print(name_1.update_age(name_1.age + 1))
# # print(name_1.plus_to_age(1))
#
# # name_1.age -= name_2.age
# # print(name_1.age)
# # print(name_3.subtract_age(name_3))
# print(all_name(name_1, name_2, name_3))


# import tkinter as tk
# from resources.colors import colors_list
# from random import choice
# class Label:
#     def __init__(self, x, y, name):
#         self.x = x
#         self.y = y
#         self.name = name
#         self.step_x = 3
#         self.step_y = 3
#         self.color = '#040720'
#         self.size_x = len(name)*25
#         self.label = tk.Label(text=name, foreground=self.color)
#         self.label.place(x=x,y=y,width=self.size_x, height=35)
#
#     def move(self):
#
#         if self.x >= screen_width or self.x <= 0:
#             self.step_x *= 1.05
#             self.step_x *= -1
#             print(self.step_x)
#
#         if self.y >= screen_height or self.y <= 0:
#             self.step_y *= 1.05
#             self.step_y *= -1
#             print(self.step_y)
#         self.label.place(x=self.x, y=self.y)
#
#         self.x += self.step_x
#         self.y += self.step_y
#         root.update()
#         root.after(1)
#
#     def col(self):
#         self.label['foreground'] = choice(colors_list)
#         self.color = self.label['foreground']
#
# root = tk.Tk()
#
#
# root.title("Find")
#
# screen_width = root.winfo_screenwidth()//2
# screen_height = root.winfo_screenheight()//2
#
# root.geometry(f"{screen_width}x{screen_height}")
#
# x, y = 100, 100
# dvd = []
# for i in range(50):
#     dvd.append(Label(x=x, y=y, name="DVD"+"_"+str(i)))
#     y -= 25
#     x += 25
#
#
# tk.mainloop()
# while True:
#     for each in dvd:
#         each.move()
#         each.col()

# dvd = Label(x=10, y=10, name="DVD")
# dvd_1 = Label(x=100, y=100, name="DVD_1")
# dvd_2 = Label(x=120, y=90, name="DVD_2")

# while True: #for object
#     for each in (dvd, dvd_1, dvd_2):
#         each.move()
#         each.col()

# import turtle
# lst = [turtle.Turtle() for each in range(10)]
# for turt in lst:
#     turt.width = 10
#
# lst[3].forward(200)
#
#
# turtle.done()

# import turtle as t
# from resources.colors import colors_list
# from random import choice, randint
# from time import sleep
# class Turtl:
#     def __init__(self,start_y):
#         self.turtle = t.Turtle()
#         self.width = t.width(3)
#         self.shapesize=t.shapesize(4)
#         self.color = t.color(choice(colors_list))
#         self.start_y = start_y
#         # self.winner_one = self.turtles[0]
#     def move(self):
#         self.turtle.fd(randint(2,8))
#
#     def start(self):
#         self.turtle.pu()
#         self.turtle.goto(-200, self.start_y)
#         self.turtle.pd()
#         for x in range(8):
#             self.turtle.left(15)
#             self.turtle.right(15)
#
#     def winner(self):
#         self.turtle.up()
#         self.turtle.goto(0, 100)
#         self.turtle.left(45)
#         self.turtle.pd()
#         a = 100
#         b = 90
#         self.turtle.width(3)
#         for x in range(20):
#             self.turtle.color(choice(colors_list))
#             self.turtle.fd(a)
#             self.turtle.left(b)
#             a -= 3
#             b += 1
#         self.turtle.setheading(90)
#         self.turtle.up()
#         self.turtle.fd(60)
#         self.turtle.write("WINNER!", font=20)
#         sleep(3)
#     def x(self):
#         return self.turtle.xcor()
# END_LINE = 300
#
# t.speed(0)
# t.ht()
# t.up()
# t.goto(END_LINE, 100)
# t.down()
# t.right(90)
# for x in range(15):
#     t.fd(5)
#     t.up()
#     t.fd(5)
#     t.down()
# t.up()
#
#
#
# turtles = [Turtl(y) for y in range(-100, 101, 100)]
# print(len(turtles))
#
#
#
# for turtle in turtles:
#     turtle.start()
#
#
#
# game_running = True
# winner_one = turtles[0]
#
# while game_running:
#     for turtle in turtles:
#         if turtle.x() > END_LINE:
#             game_running = False
#         turtle.move()
#     if not game_running:
#         break
#
# maxi = max([turtle.x() for turtle in turtles])
#
# # for turtle in turtles:
# #     if maxi == turtle.x():
# #         turtle.winner()
# #         break
# # winner_one.winner()
#
# max_x = 0
# for turtle in turtles:
#     if max_x < turtle.x():
#         max_x = turtle.x()
#         winner_one = turtle
#
#
# winner_one.winner()
#
#
# t.done()

# class Human:
#     def __init__(self, age, alive):
#         self.age = age
#         self.alive = alive
#
#     def die(self):
#         if self.alive:
#             self.alive = False
#             print("Another soul to the Kairn")
#
#     def revive(self):
#         if not self.alive:
#             self.alive = True
#             print("Necromancy should be banned")
#
# # neutral = Human(18, True)
# # neutral.die()
# # neutral.revive()
# # # # INHERITANSE - НАСЛІДУВАННЯ
# class Genderized(Human):
#     def __init__(self, gender, age, alive):
#         Human.__init__(self, age, alive)
#         self.gender = gender
#
# class A(Genderized):
#     def __init__(self, gender, age, alive, a):
#         Genderized.__init__(self, gender, age, alive)
#         self.a = a
#
# Annie = Genderized("dworf", 18, True)
# Annie.die()
# Annie.revive()
#
# d = A("dworf", 18, True, 1)

# explain the inheritance with super

# import tkinter as tk
#
# class Label(tk.Label):
#     def __init__(self, x, y):
#         tk.Label.__init__(self)
#         self.x = x
#         self.y = y
#         self.place(x=self.x, y=self.y)
#
#
# tk.mainloop()

# class Creature:
#     def __init__(self, name, npc: bool, **kwargs):
#         self.npc = npc
#         self.killed = False
#         self.name = name
#         super().__init__(**kwargs)
#
#     def convert_to_npc(self):
#         if not self.npc:
#             self.npc = True
#
#     def convert_to_not_npc(self):
#         if self.npc:
#             self.npc = False
#
#     def kill(self):
#         if not self.killed:
#             self.killed = True
#
# class Murloc(Creature):
#     def __init__(self, scales: bool, weapon: str, **kwargs):
#         self.scales = scales
#         self.weapon = weapon
#         super().__init__(**kwargs)
#
#     def swim(self):
#         print(f"{self.name} has swimmed 10 metters")
#
#
# class Demon(Creature):
#     def __init__(self, nails_dmg, higher_demon: bool, **kwargs):
#         self.nails_dmg = nails_dmg
#         self.higher_demon = higher_demon
#         super().__init__(**kwargs)
#
#     def nails_attack(self):
#         print(f"{self.name} deals {self.nails_dmg} damage")
#
# class MurlocDemon(Murloc, Demon):
#     def __init__(self, aura, **kwargs): # key word arguments | ключі слова аргументи
#         super().__init__(**kwargs)
#         self.aura = aura
#
# MRRRRGLDemon = MurlocDemon(True, weapon="Залізний меч", npc=False, name="MRRRRGL", scales=True, nails_dmg=10,
#                            higher_demon=False)
# MRRRRGLDemon.swim()
#
# MRLGL = Murloc(scales=True, weapon="spear", name="mrglg", npc=True)
# print(MRLGL.name)

### REGULAR EXPRESSIONS || REGEX ###
# https://www.w3resource.com/python-exercises/re/
# match - перевіряє початок рядка на співпадіння з паттерном    (після патерна може бути будь-що)
# fullmatch - перевіряє рядок на повне співпадіння з патерном   (повне спіпадіння з паттерном)
# search - просто шукає в рядку будь-де співпадіння
# [] - дужки для формули
# -  - діапазон     [a-z]
# +  - повтор елемента, або формули 1 або більше разів
# *  - повтор елемента, або формули 0 або більше разів
# .  - будь який елемент
# \  - показує що наступний елемент - це просто текст
# |  - вибір із декількох (логічне або) (a|bb|c) - шукає a або bb або c
# {} - використовується для указування кількості повторів елементу або формули
# ?  - повтор елемента, або формули 0 або 1 раз
# $  - позначає кінець рядка

# import re
# txt = "abc"
# if re.fullmatch("[a-z]+", txt):
#     print("matched")
# else:
#     print("not matched")

# import re
# txt = "somemail@"
# if re.fullmatch("[a-z]+@", txt):
#     print("matched")
# else:
#     print("not matched")


# 1. Write a Python program to check that a string contains only a certain set of characters
# (in this case a-z, A-Z and 0-9).
# import re
# def check(string):
#     if re.fullmatch("[a-zA-Z0-9]+", string):
#         return True
#     else:
#         return False
# print(check("1"))

# # 2. Write a Python program that matches a string that has an a
# # followed by zero or more b's.
# import re
#
# test_strings = ["a", "ab", "abb.", "cabbb", "ac", "abc", "b"]
# # Iterate over test strings and check for matches
# for test_string in test_strings:
#     if re.search("ab*", test_string):
#         print(f"'{test_string}' matches the pattern.")
#     else:
#         print(f"'{test_string}' does not match the pattern.")

# # 3. Write a Python program that searches a string for pattern that has an a followed by one or more b's.
# # Click me to see the solution
# import re
# pattern = "ab*"
# test_strings = ["a", "ab", "abb.", "cabbb", "ac", "abc", "b", '.']
# # Iterate over test strings and check for matches
# for test_string in test_strings:
#     if re.search(pattern, test_string):
#         print(f"'{test_string}' matches the pattern.")
#     else:
#         print(f"'{test_string}' does not match the pattern.")


# # 4. Write a Python program that matches a string that has an a followed by zero or one 'b'.
# import re
# pattern = "ab{0,1}"
# test_strings = ["a", "ab", "abb", "cabbb", "ac", "abc", "b", '.']
# # Iterate over test strings and check for matches
# for test_string in test_strings:
#     if re.search(pattern, test_string):
#         print(f"'{test_string}' matches the pattern.")
#     else:
#         print(f"'{test_string}' does not match the pattern.")

# # 5. Write a Python program that matches a string that has an a followed by three 'b'.
# import re
# pattern = "ab{3}"
# test_strings = ["a", "ab", "abb", "cabbb", "ac", "abc", "b", '.']
# # Iterate over test strings and check for matches
# for test_string in test_strings:
#     if re.search(pattern, test_string):
#         print(f"'{test_string}' matches the pattern.")
#     else:
#         print(f"'{test_string}' does not match the pattern.")

# 6. Write a Python program that matches a string that has an a followed by two to three 'b'.
# дз

# # 7. Write a Python program to find sequences of lowercase letters joined by an underscore.
# import re
# pattern = "[a-z]+_"  # [a-z]{1,99999}
# test_strings = ["a_b", "ab", "abb", "cabbb_", "ac__", "Abc_", "b", '.']
# # Iterate over test strings and check for matches
# for test_string in test_strings:
#     if re.search(pattern, test_string):
#         print(f"'{test_string}' matches the pattern.")
#     else:
#         print(f"'{test_string}' does not match the pattern.")

# 8. Write a Python program to find the sequences of one upper case letter followed by one or more lower case letters.
# дз
import re

# зрозуміти і пояснити мені в чому різниця між використанням r'' і просто '' як паттерна(pattern = r"^[a-zA-Z]+" або pattern = "^[a-zA-Z]+"
# def starts_with_word(string):
#     pattern = r"^[a-zA-Z]+(?:\s|$)"
#     if re.match(pattern, string):
#         return True
#     else:
#         return False
#
# # Test the function
# valid_strings = ["word second", "word", "word "]
# invalid_strings = ["123word", ".word", "word. ", " word"]
#

# for string in valid_strings + invalid_strings:
#     if starts_with_word(string):
#         print(f"{string} is a valid row.")
#     else:
#         print(f"{string} is an invalid row.")


# # 9. Write a Python program that matches a string that has an 'a' followed by anything ending in 'b'.
# import re
# pattern = "a.*b$"
# test_strings = ["a_b", "ab", "abb", "cabbb_", "ac__", "Abc_", "b", '.']
# # Iterate over test strings and check for matches
# for test_string in test_strings:
#     if re.search(pattern, test_string):
#         print(f"'{test_string}' matches the pattern.")
#     else:
#         print(f"'{test_string}' does not match the pattern.")

# 10. Write a Python program that matches a word at the beginning of a string.
# дз

# 11. Write a Python program that matches a word at the end of a string, with optional punctuation.
# дз


# have to check
# https://learnxinyminutes.com/docs/python/
# {1, 2, 3, 4} ^ {2, 3, 5}
# a = [1, 2, 3, 4]
# b = [[[1, 2, 3, 4], 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
# print([el for elem in a for el in elem for e in el if el == 1])
# for elem in a:
#     for el in elem:
#         for e in el:


# # tic tac toe
# розібрати джоїн і найти саму прогу