# # variable - var - змінна
# # indent - відступ
# x = 2
# x = '2'
# print(x)    # виводить те що ми їй дали в консоль
#
# name = 'Vlad'
# print(name)
#
# number = 'Vlad ate 5 apples today'
# number = "Vlad"
# number = 'Vlad'
# print(type(number))
# # syntax error - щось написали не так
# # indentation error - помилка відступу
#
# # integer - int - ціле число 2 3 4 5 6 100000000000000000000000
# # string - str - рядок abcdefg Vlad '2'
#
# x = 123456789789456123645 + 987654321
# print(2 + 3)
# print(x)
# x = '2' + 2
# x = 'abc' + 'dce'
# x = 'rose ' * 222222222
# print(x)

# # put put put - класти
# num = input()
# print(num)

# # amount - кількість
# amount = input("How many apples did Masha eat?")    # Past Simple Tense
# print("Masha ate", amount, "apples")
# # Vlad
# # Hello, Vlad!

# name = input("What is your name?")
# print("Hello,", name, "!")
# # Hello, Vlad!

# CTRL + /? - ЩОБ СТЕРТИ КОМЕНТАР
# animal = "cat"
# animal = "dog"
#
# name = "Masha"
# name = "Sasha"

### HOMEWORK ###
# запитати у юзера як звати кожного з його котів(у нього їх два) окремою змінною для кожного кота
# і вивести наступний текст:
# Перший кіт: <ім'я першого кота>. Другий кіт: <ім'я другого кота>.


# word = input("word?")
# num = input("num?")
# print(word * int(num))
#
# # # Redundant variables
# print(input("word?") * int(input("num?")))

# # приклад анкети
# name = input("name?")
# age = input("age?")
# print("| Name:", name, "|")
# print("| -------------")
# print("| Age:", age, "|")


# tup = (1, 2, 3, [4, 5, 6])
# try:
#     tup[3] += [7, 8]
# except TypeError:
#     pass
# print(tup)

from turtle import *

for x in range(4):
    fd(100)
    lt(90)

done()
