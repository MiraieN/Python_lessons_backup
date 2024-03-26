# # Напишите функцию, которая принимает аргумент в виде списка
# # и возвращает словарь где каждый элемент это и ключ и значение
# def to_dict(lst):
#     return {elem: elem for elem in lst}
# print(to_dict([1, 2, 3, 4]))

# #Иван решил создать самый большой словарь в мире. Для этого он придумал функцию biggest_dict(**kwargs), которая принимает неограниченное количество параметров «ключ: значение» и обновляет созданный им словарь my_dict, состоящий всего из одного элемента «first_one» со значением «we can do it». Воссоздайте эту функцию.
# my_dict = {"first_one": "we can do it"}
# def biggest_dict(**kwargs):
#     my_dict.update(**kwargs)
# biggest_dict(second_one="good luck", the_third="keep going")
# biggest_dict(k2=2, k3=3, k4=4)
# print(my_dict)

# # Дана строка в виде случайной последовательности чисел от 0 до 9.
# # Требуется создать словарь, который в качестве ключей будет принимать данные числа
# # (т. е. ключи будут типом int), а в качестве значений – количество этих чисел
# # в имеющейся последовательности. Для построения словаря создайте функцию count_it(sequence),
# # принимающую строку из цифр. Функция должна возвратить словарь
# # из 3-х самых часто встречаемых чисел.
# from random import randint as rdi
# def count_it(sequence):
#     num_frequency = {int(item): sequence.count(item) for item in sequence}
#     sorted_num_frequency = sorted(num_frequency.items(), key=lambda element: element[1])
#     return dict(sorted_num_frequency[-3:])
# print(count_it([rdi(0, 9) for x in range(10)]))

# # Создайте словарь с количеством элементов не менее 5-ти.
# # Поменяйте местами первый и последний элемент объекта. Удалите второй элемент.
# # Добавьте в конец ключ «new_key» со значением «new_value». Выведите на печать итоговый словарь.
# # Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
# my_dict = {x: round(x**(1/3)-1, 3) for x in range(5)}
# keys = list(my_dict.keys())
# my_dict[keys[0]], my_dict[keys[-1]] = my_dict[keys[-1]], my_dict[keys[0]]
# my_dict["new_key"] = "new_value"
# print(my_dict)

# # #калькулятор строковой
# stroka = input("ur stroka\n")
# print(f"result: {eval(stroka)}")

### quiz question
# from random import shuffle
#
#
# def question(ques, ans, wrong, *sols):
#     right_sol = sols[0]
#     user_ans = -1
#     sols = list(sols)
#     shuffle(sols)
#     global sum_ans
#     err = "Invalid input. You have to type nums 1-" + str(len(sols))
#     while user_ans not in range(1, len(sols) + 1):
#         print(ques)
#         for z in range(len(sols)):
#             print(str(z + 1) + ")", sols[z])
#         try:
#             user_ans = int(input())
#         except ValueError:
#             print(err)
#             continue
#         if len(sols) < user_ans or user_ans < 1:
#             print(err)
#             continue
#     if user_ans == sols.index(right_sol) + 1:
#         print(ans, "\n")
#         sum_ans += 1
#     else:
#         print(wrong, "\n")
#
#
# sum_ans = 0
# question("What does Slughorn want to collect from Aragog after he dies?",
#          "Yes, his venom has a high price on a black market",
#          "No, it was his venom. It has a high price on a black market",
#          "His venom", "His hair", "His blood", "His thorax"
#          )
#
# question("Where does Mad-Eye Moody's eye wind up",
#          "Yes, the ministry got his eye right after his death",
#          "No, the ministry got his eye right after his death",
#          "ON DOLORES UMBRIDGE'S OFFICE DOOR", "IN THE ROOM OF REQUIREMEN",
#          "ON DUMBLEDORE'S DESK", "IN GRAWP'S STOMACH"
#          )
#
# question("What makes a person feel better after seeing a Dementor??",
#          "Yes, Try some chocolate. It will help",
#          "No, better try some chocolate. It will help",
#          "chocolate", "a nap", "treacle pudding", "chicken soup"
#          )
# print("u got", sum_ans, "points")

# import random
#
# lst = ["r", "p", "s"]
#
# for z in range(10):
#     print(lst[random.randint(0, 2)])

# import operator
#
# dict1 = {1: 1, 2: 9, 3: 4}
# sorted_tuples = sorted(dict1.items(), key=operator.itemgetter(1))
# print(sorted_tuples)  # [(1, 1), (3, 4), (2, 9)]
# sorted_dict = {k: v for k, v in sorted_tuples}
#
# print(sorted_dict) # {1: 1, 3: 4, 2: 9}
# name = "asdasd"
# dict1 = {1: 1, 2: 9, 3: 4}
# print(f"first elem {dict1[1]}, Name: {name}")
# sorted_tuples = sorted(dict1.items(), key=lambda item: item[1])
# print(sorted_tuples)  # [(1, 1), (3, 4), (2, 9)]
# sorted_dict = {k: v for k, v in sorted_tuples}
#
# print(sorted_dict)  # {1: 1, 3: 4, 2: 9}

# names = {"Ivonov": 2334, "Petrov": 3334, "Melnik": 3214, "Kopelnik": 4578}
# st_cards = {}
# for name in range(len(names)):
#     st_cards[names[name]] = {"номер": name+1}
# print(st_cards)

# st_cards = {
#     "Ivonov": {
#         "номер": 1
#
#     },
#     "Petrov": {
#         "номер": 2
#
#     }
# }

# numbers = [23,77,19,310,219]
# numbers.sort(key=lambda x: sum(int (i) for i in str(x)), reverse=True)
# print("sort list:",numbers)

# d = {1:"asd", 2:"asdaasd", 3:"asdasd"}
# for key in d.keys():
#     print(key)

# string = "laeHJLogiko"
# str1 = string[-9] + string[-2] + string[4] + string[:1] + string[-2]
# str2 = string[5:7] + string[-3] + string[-4]
# str3 = string[7:8] + string[1]
# print(str1 + string[-1] + str2 + str3)

# class Count:
#     def _count_(self):
#         print('1')
#     def __init__(self):
#         print('2')
# result = Count()

# user = input("Введи а")
# while user != "a":
#     print("Ні, введи просто а")
#     user = input("Введи а")
# print("Так, це а")

# from turtle import *
# width(2)
# for col in ["red", "green", 'blue']:
#     color(col)
#     fd(100)
# exitonclick()
# for z in range(5, 11):
#     if z % 2 == 0:
#         print(z)


# class Human:
#     def __init__(self, name, posada, age, gender, height, salary):
#         self.name = name
#         self.posada = posada
#         self.age = age
#         self.gender = gender
#         self.height = height
#         self.salary = salary
#
#     def otchet(self):
#         print("Chelovek:")
#         print("Имя: ", self.name, "\nПосада:", self.posada, "\nВозраст: ", self.age, "\nПол: ", self.gender, "\nРост: ",
#               self.height, "\nzp:", self.salary)
#
#
# direktoR = Human("Vaas vaasovich", "direktor", "0 let", "genderfluid", 1500, 22222)
#
#
# # direktoR.otchet()
#
# class robochiy(Human):
#     def stats(self):
#         print("\nRabochiy:")
#         self.otchet()
#
#
# class uchenik(robochiy):
#     def stats_uchenik(self):
#         print("\nuchenik")
#         self.stats()
#
#
# sekretar = robochiy("Sekretar_name", "sekretar", 25, "1/2", 165, 12222)
# sekretar.stats()
#
#
# def poniz_zp(hto, komy):
#     print("\nzp byla", komy.salary)
#     print("ponizhaem zp na", hto.height)
#     komy.salary -= 100
#     print("zp stala", komy.salary)
#
#
# poniz_zp(direktoR, sekretar)
#
# uchenik = uchenik("\nuchenik_name", "uchenik", 25, "1/2", 165, 12222)
# uchenik.stats_uchenik()


# from random import randint as rdi
# class logika:
#     def __init__(self, name, hp, armour, damage, weapon, ulta):
#         self.name = name
#         self.ulta = ulta
#         self.hp = hp
#         self.armour = armour
#         self.damage = damage
#         self.weapon = weapon
#     def print_info(self):
#         print("\nName:", self.name)
#         print("Health:", self.hp)
#         print("Armour:", self.armour)
#         print("Damage:", self.damage)
#         print("Ulta:", self.ulta)
#         print("Weapon:", self.weapon)
# def attack(att, deff, ulta):
#     if rdi(1, 100/ulta) == 1:
#         a, att.damage = att.damage, (100 - att.damage) * 5
#         deff.hp -= att.damage
#         print(f"{att.name} attacks {deff.name} with {att.deff} damage")
#         print(f"{deff.name} now has{deff.hp} hp")
#         att.damage = a
#     else:
#         print(f"{att.name} attacks {deff.name} with {att.def} damage")
#         deff.hp -= att.damage
#         print(f"{deff.name} now has {deff.hp} hp ")
#
#
# vlad = logika("rab", 100, 30, 30, 12,6, "sword")
# vlad.print_info()
#
#
#
# maksim = logika("maksim", 100, 30, 30, 40, "sword")
# maksim.print_info()
#
# while vlad.hp > 0 and maksim.hp > 0:
#     attack(vlad, maksim, vlad.ult)
#     attack(maksim, vlad, maksim.ult)
# if vlad.hp > maksim.hp:
#     print(vlad.name, "Winner" )
# else:
#     print(maksim.name, "Winner")

# lst = [1, 2, [4, 5, 6], 3]
# print(lst[2][0])

# staff = {
#      'Смирнов': {
#          'посаду': [1,2,3,4],
#          'ефективність': 86
#      },
#      'Колягина': {
#          'посаду': 'менеджер з продажу',
#          'ефективність': 69
#      }
# }
#
# print(staff)

# import random
# for z in range(100):
#     count = 0
#     for a in range(1000):
#         lsd = [random.randint(1,1000) for z in range(1000)]
#         if z in lsd:
#             # print("Давай жопу")
#             # print(lsd.index(1))
#             count += 1
#         # print(lsd)
#     print(f"давай в жопу за {z} цілих {count} раз")
# import random
# for _ in range(10):
#     lsd = [random.randint(0, 1) for z in range(10)]
#     print(f"1:{lsd.count(1)} 0:{lsd.count(0)}")
# for _ in range(10):
#     print(_)
# import random
# print(random.randint(1, 2))

# marks = []
# mark = 1
# while mark != 0:
#     mark = int(input("Задай ім`я гри (0 - зупинити запит)"))
#     marks.append(mark)
# marks.pop(-1)
#
# print("список оцінок:", marks)
# print('Успішність:', (marks.count(3) + marks.count(4) + marks.count(5))/len(marks)*100)


# # emails grouping with stats and average len
# mails = ['suchagoodmail@gmail.com', 'qweasdzxcasd@ukr.net', 'asdasd@mail.ru', 'asdasd@gmail.com']
# mails_info = {'domens': [], 'users': []}
# for z in mails:
#     mails_info['domens'].append(z[z.rfind("@")+1:z.rfind(".")])
#     mails_info['users'].append(z[0:z.rfind("@")])
# print(f"domens are: {mails_info['domens']}")
# print(f"users are: {mails_info['users']}")
# print(f"with average name length of: {round(sum([len(z) for z in mails_info['users']])/len(mails_info['users']), 2)}")
# print("\nStatistics")
# for z in set(mails_info["domens"]):
#     print(f"{z}: {int(mails_info['domens'].count(z) * 100 / len(mails_info['domens']))}%")

# x = int(input("Input first number: "))
# y = int(input("Input second number: "))
# print("Sum:", x + y)
# print("Subtraction:", x - y)
# print("Division:", x - y)
# print("Multiplying:", x * y)

# x = int(input("Input first number: "))
# y = int(input("Input second number: "))
# print("First bigger than second" if x > y else "Second bigger than first")

# score = 0
# print("This is a test to check your knowledge at ______")
# ans = input("question 1:\nFinish the title Rick and _____")
# if ans == "Morty":
#     print("You got a point!")
#     score += 1
# else:
#     print("No point for you")
# ans = input("question 2:\n........")
# # .......
# print("Your score is:", score, "correct answer of 15 questions")
# if score < 5:
#     print("you are not really good at this")
# elif score < 8:
#     print("Not bad, not bad")
# # elif ......

# # less 18 task
# age = int(input())
# isGraduated = False
# hasLicense = True
# # Look if person is 18 years or older
# if age >= 18:
#     print("You're 18 or older. Welcome to adulthood!")
#
#     if isGraduated:
#         print('Congratulations with your graduation!')
#     if hasLicense:
#         print('Happy driving!')
# else:
#     print("You are less 18 years old. Come back when you grown up!")

# # items in stock
# itemsOrdered = int(input("items Ordered:\n"))
# itemsInStock = 32
#
# print(f"Got an order for {itemsOrdered} items. In stock: {itemsInStock}")
#
# # Compare order size against inventory
# if itemsOrdered >= itemsInStock:
#     print("Resupply the inventory. We're running out!")
# else:
#     packageCount = round(itemsOrdered / 8)
#
#     if packageCount > 1:
#         print(f"We need {packageCount} packages to fulfil this order!")


# # German capitaly
# question = "What's the capital of Germany? "
# attempts = 0
#
# while True:
#     attempts = attempts + 1
#     response = input("Attempt #" + str(attempts) + " | " + question)
#
#     if response.lower() == "berlin":
#         print("Correct! Thanks for playing")
#         break
#     else:
#         print("Incorrect.")
#         if attempts == 1:
#             print("Hint: An American president once said:",
#                   "Ich bin ein ........")
#         if attempts == 2:
#             print("Hint: In the Cold War, a wall split this city.")
#         if attempts == 3:
#             print("Hint: the city name starts with a 'B'.")

# # Jedi test
# right_answer = "Right!\nYou got 1 point"
# wrong_answer = "You missed!"
#
# import time
#
# user_name = input("Welcome to our Star Wars quiz! What's your name?\n")
# time.sleep(0.3)
# print(f"So, each question will be more difficult than the last... Ready, { user_name}? Here we go!")
#
# score = 0
#
# answer_1 = input("question_1 :\nWhat color was Luke Skywalker's lightsaber?\n").lower()
# if answer_1 == "green":
#     print(right_answer)
#     score += 1
# else:
#     print(wrong_answer)
# time.sleep(0.3)
# answer_2 = input("question_2 :\nOn what day is Star Wars Day celebrated?\n")
# if answer_2 == "4 May" or answer_2 == "May 4":
#     print(right_answer)
#     score += 1
# else:
#     print(wrong_answer)
#
# time.sleep(0.3)
#
# answer_3 = input("question_3 :\nWhat animal was the prototype for the character of Chewbacca?\n").lower()
# if answer_3 == "dog":
#     print(right_answer)
#     score += 1
# else:
#     print(wrong_answer)
# time.sleep(0.3)
# answer_4 = input("question_4 :\nTo whom does the phrase:\n- No. I am your father belong?\n").lower()
# if answer_4 == "darth vader":
#     print(right_answer)
#     score += 1
# else:
#     print(wrong_answer)
#
# time.sleep(0.3)
#
# answer_5 = input("question_5 :\nWhat used to be Darth Vader's name?\n").lower()
# if answer_5 == "anakin":
#     print(right_answer)
#     score += 1
# else:
#     print(wrong_answer)
# time.sleep(0.3)
# answer_6 = input("question_6 :\nHan Solo owned a modified cargo ship. What was its name?\n").lower()
# if answer_6 == "millennium falcon":
#     print(right_answer)
#     score += 1
# else:
#     print(wrong_answer)
# time.sleep(0.3)
# answer_7 = input("question_7 :\nWhat did the Jedi use as their primary weapon?\n").lower()
# if answer_7 == "lightsabers":
#     print(right_answer)
#     score += 1
# else:
#     print(wrong_answer)
# time.sleep(0.3)
# answer_8 = input("question_8 :\nWhat was the name of a race of small furry creatures from the satellite of Endor?\n").lower()
# if answer_8 == "ewoks":
#     print(right_answer)
#     score += 1
# else:
#     print(wrong_answer)
#
# time.sleep(0.3)
#
# answer_9 = input("question_9 :\nWhat color was Mace Windu's sword?\n").lower()
# if answer_9 == "purple":
#     print(right_answer)
#     score += 1
# else:
#     print(wrong_answer)
#
# time.sleep(0.3)
#
# answer_10 = input("question_10 :\nPrincess Leia's last name?\n").lower()
# if answer_10 == "organa":
#     print(right_answer)
#     score += 1
# else:
#     print(wrong_answer)
#
# time.sleep(1)
#
# print("You score is:", score, "correct answer of 10 questions")
#
# time.sleep(1)
#
# if score <= 3:
#     print(f"{user_name} you Padawan")
# elif score <= 8:
#     print(f"{user_name} you Jedi Master")
# elif score <= 10:
#     print(f"{user_name} you Grand-Master")


# # rock paper scissors RSP
# import random
# import time


# # function to center texts
# def center(txt):
#     return txt.center(150)


# def points(point, who):
#     if point == 1:
#         print(center(f'\n{who} have {point} point'))
#     else:
#         print(center(f'\n{who} have {point} points'))


# # meeting
# print(center("Hello!"))
# print(center("I am RSP bot, nice to meet you"))
# user_in = input(center("let's play a game, wanna start? (Y/N)\n")).lower()
# # cycling if no
# while user_in != "y" or user_in != "yes":
#     print(center("hmm... maybe you could overthink?"))
#     print(center("I will give you time"))
#     for count in range(3, 0, -1):
#         print(f'{count}...')
#         time.sleep(1)
#     user_in = input(center("wanna start? (Y/N)\n")).lower()
#     if user_in == "y" or user_in == "yes":
#         break
# else:
#     print(center("Grrrand idea!"))


# #rules
# print(center("So, the rules:"))
# print(center("U pick one of these (rock, paper, scissors) and I pick randomly"))
# # print(center("I generate all of them at once so u can check am I honest with randoming it"))
# # print(center("just type show_items"))

# # generating items for game
# items = ["rock", "scissors", "paper"]
# random.shuffle(items)
# bot_score, user_score, count = 0, 0, -1
# item_pos = 0

# # main game
# while user_score != 3 or bot_score != 3:
#     count += 1
#     print(center(f'Round {count+1}'))
#     print(center("What would u pick? (R/S/P)\n"))
#     user_in = input().lower()
#     # if user_in == "show_items":
#     #     print(center("This game I will pick it next way:"))
#     #     for num in range(3):
#     #         print(center(f'{num+1} round: {items[num]}'))
#     #     user_in = input("So, what would u pick? (R/S/P)\n").lower()
#     poss_items = ("rock", "r", "paper", "p", "scissors", "s")

#     while user_in not in poss_items:
#         print(center("U typed it wrong. Try again"))
#         user_in = input("What would u pick? (R/S/P)").lower()

#     item_pos += 1
#     try:
#         print(center(f'I got {items[item_pos]}'))
#     except IndexError:
#         random.shuffle(items)
#         item_pos = 0
#         print(center(f'I got {items[item_pos]}'))

#     # checking if random got rock
#     if user_in in poss_items[0:2]:
#         if items[item_pos] == "rock":
#             print(center("We've got the same"))
#         elif items[item_pos] == "scissors":
#             user_score += 1
#         elif items[item_pos] == "paper":
#             bot_score += 1
#     # if paper
#     elif user_in in poss_items[2:4]:
#         if items[item_pos] == "paper":
#             print(center("We've got the same"))
#         elif items[item_pos] == "rock":
#             user_score += 1
#         elif items[item_pos] == "scissors":
#             bot_score += 1
#     # if scissors
#     elif user_in in poss_items[4:6]:
#         if items[item_pos] == "scissors":
#             print(center("We've got the same"))
#         elif items[item_pos] == "paper":
#             user_score += 1
#         elif items[item_pos] == "rock":
#             bot_score += 1

#     # printing points
#     points(user_score, "U")
#     points(bot_score, "I")

#     # if someone got 2 points first, finishing game
#     if user_score == 2 and bot_score != 2:
#         print(center("U won. Congratz!"))
#         break
#     if bot_score == 2 and user_score != 2:
#         print(center("I won. He-he"))
#         break

#     print(center("Let's go the next round"))

# # end check. The one with 3 points wins
# if user_score == 3 and bot_score != 3:
#     print(center("U won. Congratz!"))
# elif bot_score == 3 and user_score != 3:
#     print(center("I won. He-he"))


# # # Black Jack Game
# import random
# import time
# import math
#
# # fast_check = 0.07
# fast_check = 0
#
#
# def slow_typing(txt):
#     time.sleep(0.8)
#     print()
#     for letter in txt:
#         print(letter, end="")
#         time.sleep(0.07-fast_check)
#
#
# def hero_says(txt):
#     time.sleep(0.8)
#     print(txt)
#
#
# cards = {
#     "Joker": random.randint(0, 3),
#     "Tuz": 11,
#     "King": 4,
#     "Queen": 3,
#     "Oficer": 2,
#     "Ten": 10,
#     "Nine": 9,
#     "Eight": 8,
#     "Seven": 7,
#     "Six": 6
# }
#
# # deck fill
# deck = []
# for card in cards.keys():
#     for f in range(4):
#         deck.append(card)
# random.shuffle(deck)
#
# slow_typing("Hello traveler. Come play a match with me")
# hero_says("\n>What r we gonna play?")
# hero_says(">Screw u")
# if input().lower() == "what r we gonna play?":
#     slow_typing("Glad u asked! It is called\nBlack..\nJack")
#     slow_typing("Wanna hear the rules?")
#     hero_says("\n>yes")
#     hero_says(">no")
#     if input().lower() == "yes":
#         slow_typing("We have 2 players. U are gonna pick 1 card and sum the value to ur score")
#         slow_typing("U must get the closest to 21 with ur score")
#         slow_typing("U can pass when u want, ur score is saved so the next player starts picking")
#     slow_typing("Ok than\nshall\nWe\nSTART!")
# else:
#     slow_typing("U r DeaD =9")
#
# score_player_1 = 0
# score_player_2 = 0
# player_1 = True
# player_2 = True
#
# # main game
# slow_typing(f"Player_1 picks now")
# while player_1:
#     slow_typing("Take or Pass?\n")
#     if input().lower() == "take":
#         card_picked = deck.pop()
#         card_value = cards[card_picked]
#         score_player_1 += card_value
#         slow_typing(f"U picked {card_picked}\nUr score = {score_player_1}")
#         if score_player_1 > 21:
#             slow_typing(f"U overpicked, ur score is {score_player_1} now")
#             break
#     else:
#         print("Ur pass accepted")
#         player_1 = False
# slow_typing("Next player turn")
# slow_typing(f"Player_2 picks now")
# while player_2:
#     slow_typing("Take or Pass?\n")
#     if input().lower() == "take":
#         card_picked = deck.pop()
#         card_value = cards[card_picked]
#         score_player_2 += card_value
#         slow_typing(f"U picked {card_picked}\nUr score = {score_player_2}")
#         if score_player_2 > 21:
#             slow_typing(f"U overpicked, ur score is {score_player_2} now")
#             break
#     else:
#         print("Ur pass accepted")
#         player_2 = False
# slow_typing("Picking has ended")
#
# if math.fabs(21-score_player_1) < math.fabs(21-score_player_2):     # |(21-25)| = 4     |(21 - 18)| = 3
#     slow_typing("Player_1 wins the game")
# elif math.fabs(21-score_player_1) == math.fabs(21-score_player_2):
#     slow_typing("No one wins. Good match!")
# else:
#     slow_typing("Player_2 wins the game")

# # Dice's
# import time
# from random import randint
#
#
# def s(txt):
#     for raw in txt.slpit("\n"):
#         print(raw)
#         time.sleep(0.3)
#
#
# print("Dice's game is here")
# print("want to hear the rules?(yes/no)")
#
# if input() == "yes":
#
#     print('''
#     the rules are simple:
#         you get five dices dropped
#         you have three rounds to pick dices to reroll
#         just type numbers of dice you want to change the value
#         type "got" if the combination suits you
#         possible combinations can be shown at any moments by typing "combs"
#         then the next player starts rolling
#         at the end your points ar counted to tell which of you wins
#         type "ready" to start the game
#           ''')
#
# dices = []
#
# while True:
#     dices.append()


# The set of words is given. Words are joined if the last letter of one word
# and the first letter of another word are the same.
# Return true if all words of the set can be combined into one word, or return false.
# Set: excavate, endure, desire, screen, theater, excess, night.
# Millipede: desirE EndurE ExcavatE ExcesS ScreeN NighT Theater.


# def millipede_of_words(words):
#     # words = list(words)
#     # for ind in range(len(words)-1):
#     #     if words[ind][-1] != words[ind+1][0]:
#     #         return False
#     # return True
#     # words = list(words)
#     # first = [elem[0] for elem in words]
#     # last = [elem[-1] for elem in words]
#     # sorted_words = []
#     # for word in words:
#     #     sorted_words.append(words[first.pop(first.index(word[-1]))])
#
#     words = list(words)
#     words_2 = words.copy()
#     print(words)
#     print(words_2)
#     final_words = []
#     for elem in words:
#         temp = elem
#         words_2.remove(elem)
#         for elem_2 in words_2:
#             if elem[-1] == elem_2[0]:
#                 # words_2[words_2.index(elem)] = ''
#                 words_2[words_2.index(elem_2)] = ''
#                 final_words.extend([elem, elem_2])
#                 break
#         else:
#             words_2.append(temp)
#
#
# random_set = {"excavate", "endure", "desire", "screen", "theater", "excess", "night"}
# millipede_of_words(random_set)


# # tkinter clock
# import tkinter as tk
# import time
#
#
# class Clock(tk.Label):
#     def __init__(self, parent=None, seconds=True, colon=False):
#         tk.Label.__init__(self, parent)
#
#         self.display_seconds = seconds
#         if self.display_seconds:
#             self.time = time.strftime('%H:%M:%S')
#         else:
#             self.time = time.strftime('%I:%M %p').lstrip('0')
#         self.display_time = self.time
#         self.configure(text=self.display_time)
#
#         if colon:
#             self.blink_colon()
#
#         self.after(200, self.update_time)
#
#     def blink_colon(self):
#         if ':' in self.display_time:
#             self.display_time = self.display_time.replace(':', ' ')
#         else:
#             self.display_time = self.display_time.replace(' ', ':', 1)
#         self.configure(text=self.display_time)
#         self.after(1000, self.blink_colon)
#
#     def update_time(self):
#         if self.display_seconds:
#             new_time = time.strftime('%H:%M:%S')
#         else:
#             new_time = time.strftime('%I:%M %p').lstrip('0')
#         if new_time != self.time:
#             self.time = new_time
#             self.display_time = self.time
#             if ':' in self.display_time:
#                 self.display_time = self.display_time.replace(':', ' ')
#             self.configure(text=self.display_time)
#         self.after(200, self.update_time)
#
#
# if __name__ == '__main__':
#     root = tk.Tk()
#     root.title("Minimalistic Clock")
#
#     clock = Clock(root, seconds=True, colon=True)
#     clock.configure(font=('Helvetica', 48))
#     clock.pack()
#
#     root.mainloop()


# x = -20
# y = 0
# for elem in range(8):
#     x += 30
#     y += 30
#     print((10, x, 30, y))

# check = 0
# all = 0
# num = 111111
# c = 0
# add = 100000
# for n in range(5):
#     for elem in range(5):
#         print(num)
#         if str(num).count("1") + str(num).count("2") > 1:
#             check += 1
#         num += add
#         all += 1
#
#
#     add /= 10
# print(f"check: {check}")
# print(f"all: {all}")

# # doce probability
# check = 0
# num = 111110
# all = 0
# while True:
#     num += 1
#     if len(str(num)) == 7:
#         break
#     pas = False
#     for elem in ('0', '7', '8', '9'):
#         if elem in str(num):
#             pas = True
#             break
#     if pas:
#         continue
#     all += 1
#
#     if str(num).count("1") + str(num).count("2") > 1:
#         check += 1
#         print(num)
#
# print(f"check: {check}")
# print(f"all: {all}")
# print(f"prob of loose: {round(check * 100 / all, 2)} %")


# # # # SIMPLE CALCULATOR # # #
# # Python program to create a simple GUI
# # calculator using Tkinter
#
# # import everything from tkinter module
# from tkinter import *
#
# # globally declare the expression variable
# expression = ""
#
#
# # Function to update expression
# # in the text entry box
# def press(num):
#     # point out the global expression variable
#     global expression
#
#     # concatenation of string
#     expression = expression + str(num)
#
#     # update the expression by using set method
#     equation.set(expression)
#
#
# # Function to evaluate the final expression
# def equalpress():
#     # Try and except statement is used
#     # for handling the errors like zero
#     # division error etc.
#
#     # Put that code inside the try block
#     # which may generate the error
#     try:
#
#         global expression
#
#         # eval function evaluate the expression
#         # and str function convert the result
#         # into string
#         total = str(eval(expression))
#
#         equation.set(total)
#
#         # initialize the expression variable
#         # by empty string
#         expression = ""
#
#     # if error is generate then handle
#     # by the except block
#     except:
#
#         equation.set(" error ")
#         expression = ""
#
#
# # Function to clear the contents
# # of text entry box
# def clear():
#     global expression
#     expression = ""
#     equation.set("")
#
#
# # Driver code
# if __name__ == "__main__":
#     # create a GUI window
#     gui = Tk()
#
#     # set the background colour of GUI window
#     gui.configure(background="light green")
#
#     # set the title of GUI window
#     gui.title("Simple Calculator")
#
#     # set the configuration of GUI window
#     gui.geometry("260x150")
#
#     # StringVar() is the variable class
#     # we create an instance of this class
#     equation = StringVar()
#
#     # create the text entry box for
#     # showing the expression .
#     expression_field = Entry(gui, textvariable=equation)
#
#     # grid method is used for placing
#     # the widgets at respective positions
#     # in table like structure.
#     expression_field.grid(columnspan=4, ipadx=65)
#
#     # create a Buttons and place at a particular
#     # location inside the root window .
#     # when user press the button, the command or
#     # function affiliated to that button is executed .
#     button1 = Button(gui, text=' 1 ', fg='black', bg='red',
#                      command=lambda: press(1), height=1, width=7)
#     button1.grid(row=2, column=0)
#
#     button2 = Button(gui, text=' 2 ', fg='black', bg='red',
#                      command=lambda: press(2), height=1, width=7)
#     button2.grid(row=2, column=1)
#
#     button3 = Button(gui, text=' 3 ', fg='black', bg='red',
#                      command=lambda: press(3), height=1, width=7)
#     button3.grid(row=2, column=2)
#
#     button4 = Button(gui, text=' 4 ', fg='black', bg='red',
#                      command=lambda: press(4), height=1, width=7)
#     button4.grid(row=3, column=0)
#
#     button5 = Button(gui, text=' 5 ', fg='black', bg='red',
#                      command=lambda: press(5), height=1, width=7)
#     button5.grid(row=3, column=1)
#
#     button6 = Button(gui, text=' 6 ', fg='black', bg='red',
#                      command=lambda: press(6), height=1, width=7)
#     button6.grid(row=3, column=2)
#
#     button7 = Button(gui, text=' 7 ', fg='black', bg='red',
#                      command=lambda: press(7), height=1, width=7)
#     button7.grid(row=4, column=0)
#
#     button8 = Button(gui, text=' 8 ', fg='black', bg='red',
#                      command=lambda: press(8), height=1, width=7)
#     button8.grid(row=4, column=1)
#
#     button9 = Button(gui, text=' 9 ', fg='black', bg='red',
#                      command=lambda: press(9), height=1, width=7)
#     button9.grid(row=4, column=2)
#
#     button0 = Button(gui, text=' 0 ', fg='black', bg='red',
#                      command=lambda: press(0), height=1, width=7)
#     button0.grid(row=5, column=0)
#
#     plus = Button(gui, text=' + ', fg='black', bg='red',
#                   command=lambda: press("+"), height=1, width=7)
#     plus.grid(row=2, column=3)
#
#     minus = Button(gui, text=' - ', fg='black', bg='red',
#                    command=lambda: press("-"), height=1, width=7)
#     minus.grid(row=3, column=3)
#
#     multiply = Button(gui, text=' * ', fg='black', bg='red',
#                       command=lambda: press("*"), height=1, width=7)
#     multiply.grid(row=4, column=3)
#
#     divide = Button(gui, text=' / ', fg='black', bg='red',
#                     command=lambda: press("/"), height=1, width=7)
#     divide.grid(row=5, column=3)
#
#     equal = Button(gui, text=' = ', fg='black', bg='red',
#                    command=equalpress, height=1, width=7)
#     equal.grid(row=5, column=2)
#
#     clear = Button(gui, text='Clear', fg='black', bg='red',
#                    command=clear, height=1, width=7)
#     clear.grid(row=5, column=1)
#
#     Decimal = Button(gui, text='.', fg='black', bg='red',
#                      command=lambda: press('.'), height=1, width=7)
#     Decimal.grid(row=6, column=0)
#     # start the GUI
#     gui.mainloop()


# # # # # loops calculator # # #
# from tkinter import *
#
# answerGlobal = ""
#
# root = Tk()
# root.title('Calculator App')
#
# answerEntry = StringVar()
# Label(root, font=('futura', 25, 'bold'),
#       textvariable=answerEntry, justify=LEFT, height=2, width=7).grid(columnspan=4, ipadx=120)
#
# answerFinalLabel = StringVar()
# Label(root, font=('futura', 25, 'bold'),
#       textvariable=answerFinalLabel, justify=LEFT, height=2, width=7).grid(columnspan=4, ipadx=120)
#
#
# def changeAnswer(entry):
#     global answerGlobal
#
#     answerGlobal += str(entry)
#     answerEntry.set(answerGlobal)
#
#
# def allClear():
#     global answerGlobal
#     answerGlobal = ""
#     answerEntry.set("")
#     answerFinalLabel.set("")
#
#
# def clearAnswer():
#     global answerGlobal
#     answerGlobal = ""
#     answerEntry.set(answerGlobal)
#
#
# def evaluateAnswer():
#     global answerGlobal
#     try:
#         evaluatedValue = str(eval(answerGlobal))
#         clearAnswer()
#         answerFinalLabel.set(evaluatedValue)
#
#     except(ValueError, SyntaxError, TypeError, ZeroDivisionError):
#         clearAnswer()
#         answerFinalLabel.set("Error!")
#
#
# def createButton(txt, x, y):
#     Button(root, font=('futura', 15, 'bold'),
#            padx=16, pady=16, text=str(txt),
#            command=lambda: changeAnswer(txt),
#            height=2, width=9).grid(row=x, column=y, sticky=E)
#
#
# buttons = ['AC', '%', '', '/', '7', '8', '9', '*', '4', '5', '6', '-', '1', '2', '3', '+', '', '', '.', '']
# buttonsCounter = 0
#
# for i in range(3, 8):
#     for j in range(0, 4):
#         createButton(buttons[buttonsCounter], i, j)
#         buttonsCounter += 1
#
# Button(root, font=('futura', 15, 'bold'),
#        padx=16, pady=16, text="AC",
#        command=lambda: allClear(),
#        height=2, width=9).grid(row=3, column=0, sticky=E)
# Button(root, font=('futura', 15, 'bold'),
#        padx=16, pady=16, text="0",
#        command=lambda: changeAnswer(0),
#        height=2, width=21).grid(row=7, column=0,
#                                 columnspan=2, sticky=E)
# Button(root, font=('futura', 15, 'bold'),
#        padx=16, pady=16, text="=",
#        command=lambda: evaluateAnswer(),
#        height=2, width=9).grid(row=7, column=3, sticky=E)
#
# mainloop()


# ### for tabletop ###
# from random import randint, choice
#
#
# def ri():
#     return randint(0, 100)
#
#
# mobs = {
#     "goblins": {
#         "amount": 10,
#         "rare": 3,
#         "common": 22},
#     "wyverns": {
#         "amount": 3,
#         "rare": 7,
#         "common": 12},
#     "goblins_mage": {
#         "amount": 5,
#         "mythril": 2,
#         "rare": 12,
#         "common": 15},
#     "goblins_frost": {
#         "amount": 0,
#         "mythril": 7,
#         "rare": 18,
#         "common": 0},
#     "orc_smither": {
#         "amount": 1,
#         "gods": 10,
#         "mythril": 25,
#         "rare": 32,
#         "common": 50}
# }
#
# loot = {
#     "weapon": {
#         "common":
#             ["Залізний меч 60% 1д6 25см",
#              "Залізний спис 55% 1д6 20см",
#              "Клеймор 50% 2д8 50см",
#              "Глефа 60% 2д6 35см",
#              "Дадао 50% 2д10 60см",
#              "Бойовий посох 60% 1д6 20см",
#              "Алебарда 55% 1д8 45см",
#              "Катана 65% 2д8 1зм",
#              "Довгий лук 65% 1д6 30см",
#              "Мисливський лук 70% 2д6 80см",
#              "Залізний лук 60% 1д8 50см",
#              "Парні арбалети 60% 2х1д6 70см",
#              "Важкий арбалет 50% 1д12 85см",
#              "Легкий арбалет 65% 1д8 80см}",
#              "Посох вогню 65% 1д10 40см",
#              "Посох блискавок 55% 1д8 35см",
#              "Проклятий посох 50% 1д12 45см",
#              "Посох ілюзій 60% 1д6 35с"],
#         "rare":
#             ["Загартований меч 60% 1д12 1зм",
#              "Срібний меч 65% 1д10 120см",
#              "Парні мечі 55% 2д12 2зм",
#              "Шуангоу 50% 3д6 2зм",
#              "Гуандао 60% 2д8 150см",
#              "Нагіната 70% 2д12 4зм",
#              "Нефритовий лук 70 % 2д8 4зм",
#              "Срібний арбалет 55 % 3д10 6зм",
#              "Лук вітру 75 % 3д4 5зм",
#              "Мисливський арбалет 60 % 3д8 5зм",
#              "Посох грому 55 % 2д8 2зм",
#              "Посох з кісток 50 % 2д12 3зм",
#              "Дивний посох 70 % 1д6 2зм",
#              "Палаючий посох 60 % 2д10 3зм"],
#         "mythril":
#             ["Нічна жатва Глефа 65% 3д12 40зм",
#              "Срібний кіготь Дадао 65% 3д8 35зм",
#              "Вартові корони Шуангоу 50% 3д10 55зм",
#              "Чорне крило Алебарда 55% 3д12 60зм",
#              "Вбивця драконів Дворучний меч 60% 3д10 55зм",
#              "Північна зоря Меч 65% 3д8 50зм",
#              "Цитадель Арбалет 60% 3д12 60зм",
#              "Клятва свободи Лук 70% 3д6 40зм",
#              "Самостріли Парні арбалети 55% 2х3д6 1пм",
#              "Пісня світанку Посох вогню 60% 3д10 50зм",
#              "Посох відьом Посох ілюзій 70% 3д6 40зм",
#              "Підкорювач тіні Проклятий посох 50% 3д12 60пм",
#              "Посох небес Посох блискавок 55% 3д8 40зм]"],
#         "gods":
#             ["Арбітр Дворучний меч 60% 4д12 25пм",
#              "Подих ночі Спис 65% 4д10 15пм",
#              "Клинок сакури Нагіната 60% 4д12 15пм",
#              "Кривавий ритуал Коса 50% 5д12 20пм",
#              "Білий ворон Подвійна глефа 65% 4д20 20пм",
#              "Світло і тінь Парні нінзято 70% 2х3д12 30пм",
#              "Лісовий вовк Арбалет 60% 4д8 40пм",
#              "Деформатор Арбалет 55% 4д10 45пм",
#              "Зефір Лук 65% 3д8 35пм",
#              "Солов‘їне перо Лук 70% 3д8 40пм",
#              "Посох магми Посох вогню 60% 4д10 50пм",
#              "Чорна троянда Посох ілюзій 70% 4д6 35пм",
#              "Посох шторму Посох блискавок 55% 4д8 40пм",
#              "Череп порчі Проклятий посох 50% 4д12 55пм"],
#         "legendary":
#             ["Тінеріз Катана 75% 6д6 150пм",
#              "Вартовий бурі Сабля 60% 6д8 90пм",
#              "Кривавий жнець Кусарігама 45% 6д12 100пм",
#              "Невагомість Дворучний меч 65% 6д6+20 120пм",
#              "Вогняні рукавиці Бойові кастети 70% 6д6 70пм",
#              "Воля небес Лук 65% 8д6 90пм",
#              "Хелсінг Арбалет 70% 3д6 120пм",
#              "Пожирач душ Демонічна коса 55% 6д12 150пм",
#              "Крила ночі Подвійна глефа 70% 6д20 250пм",
#              "Кіготь дракона Дадао 60% 6д8 80пм",
#              "Врата демонів Парні мечі 65% 10д6 120пм",
#              "Костоправ Дворучна булава 50% 6д12 85пм]"]
#     },
#     "armor": {
#         "common":
#             [
#                 "Обладунок воїна Важка 7од n/a 50см",
#                 "Обладунок паладіна Важка 12од n/a 90см",
#                 "Мантія священника Тканинна 3од n/a 30си",
#                 "Мантія чаклуна Тканинна 2од n/a 25см",
#                 "Одяг демонолога Тканинна 3од n/a 30см",
#                 "Мантія друіда Тканинна 3од n/a 30см",
#                 "Обладунок рейнджера Легка 4од n/a 40см",
#                 "Одяг алхіміка Легка 5од n/a 45см",
#                 "Обладунок тіні Легка 4од n/a 40см",
#                 "Одяг інженера Легка 4од n/a 40см"],
#         "rare":
#             [
#                 "Чорний гладіатор Важка 15од +1 здоров’я 10зм",
#                 "Сталева кираса Важка 10од +1 сили 8зм",
#                 "Мантія чародія Тканинна 5од +20 мани 8зм",
#                 "Зоряний плащ Тканинна 4од +30 мани 10зм",
#                 "Палаюча мантія Тканинна 4од +1 інт 6зм",
#                 "Мантія єпископа Тканинна 4од +1 релігія 6зм",
#                 "Кольчуга тіней Легка 7од +1 здоров’я 10зм",
#                 "Клепаний обладунок Легка 8од +1 спр 7зм",
#                 "Обладунок вартового Легка 6од +20 мани 10зм",
#                 "Бригантина Легка 7од +1 сили 6зм"],
#         "mythril":
#             [
#                 "Вогонь півночі Важка 12од +2 здоров’я 40зм",
#                 "Ліквілатор Важка 17од +2 сили 50зм",
#                 "Ловець зірок Тканинна 3од +40 мани 40зм",
#                 "Творець тіней Тканинна 2од +50 мани 60зм",
#                 "Багрянець Тканинна 3од +2 інт 30зм",
#                 "Останній вирок Тканинна 3од +2 релігія 30зм",
#                 "Три стріли Легка 4од +2 здоров’я 50зм",
#                 "Крило півночі Легка 5од +2 спр 35зм",
#                 "Сталева цикада Легка 4од +30 мани 45зм",
#                 "Обладунок спектра Легка 4од +2 сили 35зм"],
#         "gods":
#             [
#                 "Архаїчний камінь Важка 17од +4 здоров’я 3пм",
#                 "Мародер Важка 20од +2 сили 4пм",
#                 "Відьмовський плащ Тканинна 3од +50 мани 2пм",
#                 "Північне сяйво Тканинна 2од +70 мани 3пм",
#                 "Зміїна луска Тканинна 3од +2 інт 2пм",
#                 "Синій місяць Тканинна 3од +2 релігії 150зм",
#                 "Парадокс Легка 4од +3 сили 2пм",
#                 "Страж забуття Легка 5од +3 здоров’я 3пм",
#                 "Кодзан-До Легка 4од +40 мани 3пм",
#                 "Сніжний дракон Легка 4од +2 удачі 3пм"],
#         "legendary":
#             [
#                 "Кривавий обладунок Важка 25од Ефект 150пм",
#                 "Небесна кара Важка 30од Ефект 170пм",
#                 "Приборкувач грому Тканинна 8од Ефект 120пм",
#                 "Серце глибин Тканинна 10од Ефект 150пм",
#                 "Печать демона Тканинна 6од Ефект 100пм",
#                 "Провідник душі Тканинна 7од Ефект 150пм",
#                 "Зустрічна комета Легка 15од Ефект 140пм",
#                 "Білий фантом Легка 10од Ефект 200пм",
#                 "Обладунки ворона Легка 12од Ефект 130пм",
#                 "Луска дракона Легка 17од Ефект 120пм",
#             ]
#     }
# }
#
#
# def process():
#     for mob, value in mobs.items():
#         if value["amount"]:
#             print(f"{mob}:")
#             for amount in range(value['amount']):
#                 sign = ri()
#                 # print(sign)
#                 for item, chance in value.items():
#                     if item != "amount":
#                         if sign in range(chance):
#                             if ri() > 50:
#                                 print(f"{item}: {choice(loot['weapon'][item])} weapon")
#                             else:
#                                 print(f"{item}: {choice(loot['armor'][item])} armor")
#                             break
#             print("\n")
#
#
# process()

### surname vars with tkinter ###
# from random import shuffle
# from tkinter import *
# root = Tk()
# root.eval('tk::PlaceWindow . center')
#
#
# def pressed():
#     r = 2
#     c = 0
#     splitted = entry.get().split()
#     rand_list = [num for num in range(1, len(splitted)+1)]
#     shuffle(rand_list)
#     for n in range(len(splitted)):
#         Label(text=splitted[n], font=("comic sans ms", 22)).grid(row=r, column=c, padx=15, pady=15)
#         Label(text=rand_list[n], font=("comic sans ms", 22)).grid(row=r, column=c+1, padx=15, pady=15)
#         r += 1
#
#
# entry = Entry(font=("Comic sans ms", 22))
# entry.grid(row=0, columnspan=2)
# button = Button(text="OK", command=pressed)
# button.grid(row=1, columnspan=2)
#
# mainloop()


### Calculator with loop with blinking ###
# from tkinter import *
#
# root = Tk()
#
# # root.title("Paint")
# # root.geometry("410x500+450+150")
#
#
# window_width = 410
# window_height = 550
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
#         return
#     if txt == "C":
#         clear()
#         return
#     if var.get() == "Error":
#         var.set("")
#     global global_txt
#     global_txt += txt
#     var.set(global_txt)
#
#
# def blink_in(txt):
#     global buts
#     buts[txt]['bg'] = "gray"
#
#
# def blink_out(event):
#     global buts
#     for k, v in buts.items():
#         if buts[k]['bg'] == "gray":
#             buts[k]['bg'] = 'snow'
#
#
# def val():
#     def button(txt, row, col):
#         global buts
#         buts[txt] = Button(text=txt, command=lambda: var_add_text(txt), bg="snow", font=("comic sans ms", 22))
#         buts[txt].grid(row=row, column=col, ipadx=20, ipady=15, padx=10, pady=5)
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

### TIC TAC TOE ###
# def show():
#     for row in board:
#         print(' '.join(row))
#
# def winner():
#     for row in board:
#         if all(cell == player for cell in row):
#             return True
#     for col in range(3):
#         if all(board[i][col] == player for i in range(3)):
#             return True
#     if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
#         return True
#
# board = [["-"] * 3 for _ in range(3)]
# player = "X"
# while True:
#     show()
#     row, col = map(int, input(f"{player} row and col (0 2): ").split())
#     if board[row][col] == "-":
#         board[row][col] = player
#         if winner():
#             show()
#             print(f"{player} wins")
#             break
#         player = "0" if player == "X" else "X"
#     else:
#         print("position taken")

### # with computer
# import random
#
#
# def show():
#     for row in board:
#         print(" ".join(row))
#
#
# def winner(player):
#     for row in board:
#         if all(cell == player for cell in row):
#             return True
#     for col in range(3):
#         if all(board[i][col] == player for i in range(3)):
#             return True
#
#     if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
#         return True
#
#
# def player_move(difficulty):
#     if player == 'X':
#         while True:
#             try:
#                 row, col = map(int, input("Enter row and column (0-2): ").split())
#                 if board[row][col] == '-':
#                     board[row][col] = player
#                     return
#                 else:
#                     print("That position is already taken!")
#             except ValueError:
#                 print("Please enter two numbers separated by a space.")
#     else:
#         if difficulty == 'easy':
#             while True:
#                 row = random.randint(0, 2)
#                 col = random.randint(0, 2)
#                 if board[row][col] == '-':
#                     print(f"Computer plays at row {row}, column {col}")
#                     board[row][col] = player
#                     return
#         elif difficulty == 'hard':
#             # Check for blocking moves
#             opponent = 'X' if player == 'O' else 'O'
#             for row in range(3):
#                 for col in range(3):
#                     if board[row][col] == '-':
#                         board[row][col] = opponent
#                         if winner(opponent):
#                             print(f"Computer plays at row {row}, column {col}")
#                             board[row][col] = player
#                             return
#                         else:
#                             board[row][col] = '-'
#
#             # Play in a strategic position
#             strategic_positions = [(1, 1), (0, 0), (0, 2), (2, 0), (2, 2)]
#             for row, col in strategic_positions:
#                 if board[row][col] == '-':
#                     print(f"Computer plays at row {row}, column {col}")
#                     board[row][col] = player
#                     return
#
#             # If no blocking, or strategic moves available, play randomly
#             while True:
#                 row = random.randint(0, 2)
#                 col = random.randint(0, 2)
#                 if board[row][col] == ' ':
#                     print(f"Computer plays at row {row}, column {col}")
#                     board[row][col] = player
#                     return
#
#
# board = [["-"] * 3 for _ in range(3)]
# player = "X"
# while True:
#     level = input("Level(easy|hard): ")
#     if level in ("easy", "hard"):
#         break
#     print("Invalid input")
#
# while True:
#     show()
#     player_move(level)
#     if winner(player):
#         show()
#         print(f"{player} wins")
#         break
#     player = "0" if player == "X" else "X"

# indexing
# duplicates

