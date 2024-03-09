# from random import shuffle
#
#
# def question(q, correct, wrong, *sols):
#     a = -1
#     global res_score
#     cor_sol = sols[0]
#     sols = list(sols)
#     shuffle(sols)
#     while a not in range(1, len(sols)+1):
#         print(q)
#         for z in range(len(sols)):
#             print(str(z + 1) + ")", sols[z])
#         try:
#             a = int(input("Your choice?\n"))
#         except ValueError:
#             print("Incorrect. Type of the nums above\n")
#     if a == sols.index(cor_sol) + 1:
#         print("\n" + correct)
#         res_score += 1
#     else:
#         print(wrong)
#         res_score += 0
#
#
# res_score = 0
#
# question("What did the Hermione`s cat to help friends to pass the Iva?",
#                       "yeap, the lever. No random throwing of the tree",
#                       "go reread the third book. it is really amazing part of story",
#                       "pulled the lever", "he cried to disarrange it",
#                       "he scrapped it", "he sang a song to sleep it")
#
#
# print("your score is:", res_score)

# # questions def remade
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
#     while user_ans not in range(1, len(sols)+1):
#         print(ques)
#         for z in range(len(sols)):
#             print(str(z+1) + ")", sols[z])
#         try:
#             user_ans = int(input())
#         except ValueError:
#             print(err)
#             continue
#         if len(sols) < user_ans or user_ans < 1:
#             print(err)
#             continue
#     if user_ans == sols.index(right_sol)+1:
#         print(ans, "\n")
#         sum_ans += 1
#     else:
#         print(wrong, "\n")
#
#
# sum_ans = 0
# question("What does Slughorn want to collect from Aragog after he dies?",
#                     "Yes, his venom has a high price on a black market",
#                     "No, it was his venom. It has a high price on a black market",
#                     "His venom", "His hair", "His blood", "His thorax"
#                     )
#
# question("Where does Mad-Eye Moody's eye wind up",
#                     "Yes, the ministry got his eye right after his death",
#                     "No, the ministry got his eye right after his death",
#                     "ON DOLORES UMBRIDGE'S OFFICE DOOR", "IN THE ROOM OF REQUIREMEN",
#                     "ON DUMBLEDORE'S DESK", "IN GRAWP'S STOMACH"
#                     )
#
# question("What makes a person feel better after seeing a Dementor??",
#                     "Yes, Try some chocolate. It will help",
#                     "No, better try some chocolate. It will help",
#                     "chocolate", "a nap", "treacle pudding", "chicken soup"
#                     )
# print("u got", sum_ans, "points")

# bot with questions with tkinter (tkinter questions)
from tkinter import *
from tkinter import messagebox


def create_window(ques, correct):
    def check_ans():
        global success, failed, checks

        if ent_ans.get() == correct:
            messagebox.showinfo(message="Вірно")
            success += 1
            window.destroy()
            return
        else:
            messagebox.showerror(message="Невірно")
            checks -= 1
            print(checks)

        if checks == 0:
            messagebox.showerror(message="Закінчились спроби")
            failed += 1
            window.destroy()
            return

    global checks
    checks = 3
    print(checks)

    window = Tk()
    window.title("┐(￣ヘ￣)┌")
    window.geometry("530x800+600+200")

    lbl_ques = Label(text=ques, font=("comic sans ms", 22, "bold", "underline"), relief="raised")
    ent_ans = Entry(font=("comic sans ms", 22, "bold", "underline"))
    but_ans = Button(text="OK", font=("arial", 22, "bold"), bg="white", foreground="red", command=check_ans)

    lbl_ques.pack()
    ent_ans.pack()
    but_ans.pack()

    mainloop()


success = 0
failed = 0

quess = {"ques1": "correct1",
         "ques2": "correct2",
         "ques3": "correct3",
         "4": "4"}

for ques, correct in quess.items():
    create_window(ques, correct)

print(f"success: {success}")
print(f"failed: {failed}")

# ________________________________________________________________
# import random
# import time
#
#
# # function to center texts
# def center(txt):
#     return txt.center(50)
#
#
# def points(point, who):
#     if point == 1:
#         print(center(f'\n{who} have {point} point'))
#     else:
#         print(center(f'\n{who} have {point} points'))
#
#
# # meeting
# print(center("Hello!"))
# print(center("I am RSP bot, nice to meet you"))
# user_in = input(center("let's play a game, wanna start? (Y/N)\n")).lower()
# # cycling if no
# if user_in == "n" or user_in == "no":
#     print(center("hmm... maybe you could overthink?"))
#     print(center("I will give you time"))
#     for count in range(3, 0, -1):
#         print(f'{count}...')
#         time.sleep(1)
#     user_in = input(center("wanna start? (Y/N)\n")).lower()
#     if user_in == "y" or user_in == "yes":
#         print(center("Grrrand idea!"))
#
# #rules
# print(center("So, the rules:"))
# print(center("U pick one of these (rock, paper, scissors) and I pick randomly"))
#
#
# # generating items for game
# items = ["rock", "scissors", "paper"]
# random.shuffle(items)
# bot_score, user_score, count = 0, 0, -1
# item_pos = 0
#
# # main game
# while user_score != 3 or bot_score != 3:
#     count += 1
#     print(center(f'Round {count+1}'))
#     user_in = input("What would u pick? (R/S/P)\n").lower()
#     # if user_in == "show_items":
#     #     print(center("This game I will pick it next way:"))
#     #     for num in range(3):
#     #         print(center(f'{num+1} round: {items[num]}'))
#     #     user_in = input("So, what would u pick? (R/S/P)\n").lower()
#     poss_items = ("rock", "r", "paper", "p", "scissors", "s")
#
#     while user_in not in poss_items:
#         print(center("U typed it wrong. Try again"))
#         user_in = input("What would u pick? (R/S/P)").lower()
#
#     item_pos += 1
#     try:
#         print(center(f'I got {items[item_pos]}'))
#     except IndexError:
#         random.shuffle(items)
#         item_pos = 0
#         print(center(f'I got {items[item_pos]}'))
#
#     # checking if random got rock
#     if user_in in poss_items[0:2]:
#         if items[item_pos] == "rock":
#             print(center("We've got the same"))
#         elif items[item_pos] == "scissors":
#             user_score += 1
#         elif items[item_pos] == "paper":
#             bot_score += 1
#     # if paper
#     if user_in in poss_items[2:4]:
#         if items[item_pos] == "paper":
#             print(center("We've got the same"))
#         elif items[item_pos] == "rock":
#             user_score += 1
#         elif items[item_pos] == "scissors":
#             bot_score += 1
#     # if scissors
#     if user_in in poss_items[4:6]:
#         if items[item_pos] == "scissors":
#             print(center("We've got the same"))
#         elif items[item_pos] == "paper":
#             user_score += 1
#         elif items[item_pos] == "rock":
#             bot_score += 1
#
#     # printing points
#     points(user_score, "U")
#     points(bot_score, "I")
#
#     # if someone got 2 points first, finishing game
#     if user_score == 2 and bot_score != 2:
#         print(center("U won. Congratz!"))
#         break
#     if bot_score == 2 and user_score != 2:
#         print(center("I won. He-he"))
#         break
#
#     print(center("Let's go the next round"))
#
# # end check. The one with 3 points wins
# if user_score == 3 and bot_score != 3:
#     print(center("U won. Congratz!"))
# elif bot_score == 3 and user_score != 3:
#     print(center("I won. He-he"))


# _______________________________________________________________________________________
# import random
# import time
#
# center = lambda txt: txt.center(50)
#
#
# def points(point, who):
#     if point == 1:
#         print(center(f'\n{who} have {point} point'))
#     else:
#         print(center(f'\n{who} have {point} points'))
#
#
# # meeting
# print(center("Hello!"))
# print(center("I am RSP bot, nice to meet you"))
# user_in = input(center("let's play a game, wanna start? (Y/N)\n")).lower()
# # cycling if no
# while user_in == "n" or user_in == "no":
#     print(center("hmm... maybe you could overthink?"))
#     print(center("I will give you time"))
#     for count in range(3, 0, -1):
#         print(f'{count}...')
#         time.sleep(1)
#     user_in = input(center("wanna start? (Y/N)\n")).lower()
#     if user_in == "y" or user_in == "yes":
#         print(center("Grrrand idea!"))
#
# # rules
# print(center("So, the rules:"))
# print(center("U pick one of these (rock, paper, scissors) and I pick randomly"))
#
# # generating items for game
# items = ("rock", "scissors", "paper")
# bot_score, user_score, count = 0, 0, -1
# # item_pos = 0
# poss_items = ("rock", "r", "paper", "p", "scissors", "s")
#
# # main game
# while user_score != 3 or bot_score != 3:
#     count += 1
#     print(center(f'Round {count + 1}'))
#     user_in = input(center("What would u pick? (R/S/P)\n")).lower()
#
#     while user_in not in poss_items:
#         print(center("U typed it wrong. Try again"))
#         user_in = input(center("What would u pick? (R/S/P)\n")).lower()
#
#     bot_choice = random.choice(items)
#
#     print(center(f'I got {bot_choice}'))
#
#     # checking if random got rock
#     if user_in in poss_items[0:2]:
#         if bot_choice == "rock":
#             print(center("We've got the same"))
#         elif bot_choice == "scissors":
#             user_score += 1
#         elif bot_choice == "paper":
#             bot_score += 1
#     # if paper
#     if user_in in poss_items[2:4]:
#         if bot_choice == "paper":
#             print(center("We've got the same"))
#         elif bot_choice == "rock":
#             user_score += 1
#         elif bot_choice == "scissors":
#             bot_score += 1
#     # if scissors
#     if user_in in poss_items[4:6]:
#         if bot_choice == "scissors":
#             print(center("We've got the same"))
#         elif bot_choice == "paper":
#             user_score += 1
#         elif bot_choice == "rock":
#             bot_score += 1
#
#     # printing points
#     points(user_score, "U")
#     points(bot_score, "I")
#
#     # if someone got 2 points first, finishing game
#     if user_score == 2 and bot_score < 2:
#         print(center("U won. Congratz!"))
#         break
#     if bot_score == 2 and user_score < 2:
#         print(center("I won. He-he"))
#         break
#
#     print(center("Let's go the next round"))
#
# # end check. The one with 3 points wins
# if user_score == 3:
#     print(center("U won. Congratz!"))
# elif bot_score == 3:
#     print(center("I won. He-he"))


# _______________________________________________________
# from random import randint
# from time import sleep
#
#
# # CЛОЖНА!!!!!!!!!!!!!!!!!!
# class Stats:
#     def __init__(self, name, rang, hp, power, skill):
#         self.name = name
#         self.rang = rang
#         self.hp = hp
#         self.power = power
#         self.skill = skill
#
#     def print_info(self):
#         print("Имя: ", self.name)
#         print("Ранг: ", self.rang)
#         print("Здоровье: ", self.hp)
#         print("Максимальная сила: ", self.power)
#         print("Скилл: ", self.skill)
#
#
# def Attack_Power():
#     return randint(120, 2000)
#
#
# def attack(attacking, defence):
#     print("{0} атакует {1}".format(attacking.name, defence.name))
#     defence.hp -= Attack_Power()
#     print("Здоровье {0}: {1}".format(defence.name, defence.hp))
#
#
# class Character(Stats):
#     def emergence(self):
#         print("Засияли красные глаза...")
#         sleep(3)
#         print("Из тени выходит гуль")
#         sleep(5)
#         self.print_info()
#
#
# Kaneki_Ken = Character("Канеки Кен", "SSS+", randint(5000, 15000), randint(120, 2000), "Дединсайд")
# Nimura_Furyta = Character("Нимура Фурута", "SSS", randint(5000, 15000), randint(120, 2000),
#                           "отсутствие Дединсайта в крови")
# # ИСТОРИЯ
# print("Канеки Кен пошел уничтожать ядро Дракона,но ему перегородил путь Нимура Фунура.")
# sleep(5)
# print("Обстановка накаляется...")
# sleep(2)
# print("*Канеки наполнен решимостью")
# sleep(3)
# Kaneki_Ken.emergence()
# sleep(10)
# Nimura_Furyta.emergence()
# sleep(10)
# print("Битва Началась!")
# sleep(2)
# while (Nimura_Furyta.hp or Kaneki_Ken.hp) > 0:
#     attack(Kaneki_Ken, Nimura_Furyta)
#     Nimura_Furyta.hp -= Kaneki_Ken.power
#     sleep(3)
#     if Kaneki_Ken.hp <= 0:
#         sleep(3)
#         print("Нимура победил")
#         sleep(3)
#         print("*Ядро не было разрушено")
#         sleep(3)
#         print("*Человечество было заражено")
#         break
#     elif Nimura_Furyta.hp <= 0:
#         sleep(3)
#         print("Канеки победил")
#         sleep(3)
#         print("*Канеки побежал дальше и уничтожил ядро Дракона")
#         sleep(3)
#         print("*Канеки спас человечество")
#         break
#     attack(Nimura_Furyta, Kaneki_Ken)
#     Kaneki_Ken.hp -= Nimura_Furyta.power
#     sleep(3)
#     if Kaneki_Ken.hp <= 0:
#         sleep(3)
#         print("Нимура победил")
#         sleep(3)
#         print("*Ядро не было разрушено")
#         sleep(3)
#         print("*Человечество было заражено")
#         break
#     elif Nimura_Furyta.hp <= 0:
#         sleep(3)
#         print("Канеки победил")
#         sleep(3)
#         print("*Канеки побежал дальше, и уничтожил ядро Дракона")
#         sleep(3)
#         print("*Канеки спас человечество")
#         break

# _______________________________________________________
# from time import sleep
# import random
#
#
# class Stats:
#     def __init__(self, name, power, health, crit_chance, crit_amplifier):
#         self.alive = True
#         self.name = name
#         self.power = power
#         self.hp = health
#         self.crit_chance = crit_chance
#         self.hp_at_start = self.hp
#         self.power_at_start = self.power
#         self.crit_amplifier = crit_amplifier
#         self.deaths = 0
#
#     def print_info(self):
#         print(f"Name: {self.name}")
#         print(f"Hit power: {self.name}")
#         print(f"Health: {self.name}")
#         print(f"Ult chance: {self.name}")
#
#     def power_default(self):
#         self.power = self.power_at_start
#
#     def dies(self):
#         self.alive = False
#         self.deaths += 1
#
#
# class Heroes(Stats):
#     def print_info(self):
#         print("\nThe new hero appears:")
#         super().print_info()
#
#
# class Enemies(Stats):
#     def print_info(self):
#         print("\nNew enemy spawned:")
#         super().print_info()
#
#
# knight = Heroes("Knight", 13, 105, 24, 1.5)
# wolf = Enemies("wolf", 8, 65, 36, 1.2)
# golem = Enemies("Golem", 12, 120, 6, 1.3)
#
#
# # main attack func (looped till one dies)
# def attacking(att, deff):
#     while att.hp > 0 or deff.hp > 0:
#         att.power_default()
#         crit_check(att)
#         sleep(0.3)
#         print(f"{att.name} attacks \n {att.power} damage!")
#         deff.hp -= int(att.power)
#         print(f"{deff.name} has {deff.hp} hp\n")
#         crit_check(deff)
#         sleep(0.3)
#         print(f"{deff.name} attacks \n  {deff.power} damage!")
#         att.hp -= int(deff.power)
#         print(f"{att.name} has {att.hp} hp\n")
#         if att.hp <= 0 and deff.hp <= 0:
#             print(f"{deff.name} dies")
#             deff.dies()
#             print(f"{att.name} dies")
#             att.dies()
#             break
#         elif att.hp <= 0:
#             print(f"{att.name} dies")
#             att.dies()
#             break
#         elif deff.hp <= 0:
#             print(f"{deff.name} dies")
#             deff.dies()
#             break
#
#
# # mult power bt crit amplifier if rand (1-100) in crit chance
# def crit_check(att):
#     if random.randint(1, 100) in range(1, att.crit_chance):
#         att.power *= att.crit_amplifier
#
#
# def door_picking():
#     print("\nU have 3 doors")
#     print("which door to open? (1/2/3)")
#
#     # incorrect type check
#     while True:
#         try:
#             sleep(1)
#             choose = int(input("Door number: "))
#             break
#         except ValueError:
#             print("it seems you've typed something wrong. Try again")
#         if choose not in rand_picks:
#             print("Error. Type (1/2/3)")
#
#     # shuffling list to pick from
#     random.shuffle(rand_picks)
#
#     # heal
#     if rand_picks[choose - 1] == 1:
#         print("\nYou've got an hp potion, grab your 30 hp")
#         print("A nice moment. Enjoy ^-^")
#         for _ in range(30):
#             # healed to max
#             if knight.hp_at_start == knight.hp:
#                 print("healed to max")
#                 break
#             print(f"\nYour health: {knight.hp}")
#             knight.hp += 1
#             sleep(0.1)
#
#         print("Your hp:", knight.hp)
#
#     # wolf
#     if rand_picks[choose - 1] == 2:
#         print("You've got an enemy: Wolf!.\nFight for your life!")
#         lucky_pick(knight, wolf)
#
#     # golem
#     if rand_picks[choose - 1] == 3:
#         print("You've got an enemy: Golem!.\nFight for your life!")
#         lucky_pick(knight, golem)
#
#
# # 0 or 1 roll
# def lucky_pick(hero, enemy):
#     lucky = random.randint(0, 1)
#     while True:
#         try:
#             print("Roll for first hit. 0/1")
#             user_num = int(input())
#             break
#         except ValueError:
#             print("it seems you've typed something wrong. Try again")
#     if user_num == lucky:
#         print("Lucky pick!")
#         attacking(hero, enemy)
#     else:
#         print("Unlucky =(")
#         attacking(enemy, hero)
#
#
# # results of deaths for end
# def deaths_count():
#     print(f"Wolf: {wolf.deaths} deaths" if wolf.deaths != 1 else f"Wolf: {wolf.deaths} death")
#     print(f"Golem: {golem.deaths} deaths" if golem.deaths != 1 else f"Golem: {golem.deaths} death")
#
#
# def end_speech():
#     if wolf.deaths < 1 and golem.deaths < 1:
#         print("Em.. Not bad I think..")
#     elif wolf.deaths > 0 and golem.deaths < 1:
#         print("Good journey. Not really  lucky thought")
#     elif wolf.deaths > 0 and golem.deaths < 1:
#         print("A great journey it was!")
#     print("\nResults:")
#     deaths_count()
#
#
# # prep picks to random
# rand_picks = [1, 2, 3]
#
# print("\nHello, traveler. Guide your hero to the win!")
# knight.print_info()
#
# while knight.hp > 0:
#     door_picking()
#
# end_speech()


# # морозиво сніжок
# from tkinter import *
# from tkinter.messagebox import showinfo
#
# window = Tk()
# window.title("┐(￣ヘ￣)┌")
# window.geometry("530x800+600+200")
#
#
# def create_click():
#     txt = ""
#     # if d1_var.get() == 1:
#     #     txt = txt + 'Морозиво "Казка"\n'
#     # if d2_var.get() == 1:
#     #     txt = txt + 'Морозиво з шоколадом\n'
#     # if d3_var.get() == 1:
#     #     txt = txt + 'Тістечко"Сніжок"\n'
#     # if d4_var.get() == 1:
#     #     txt = txt + 'Десерт "Білосніжка"\n'
#
#     # d = {d1: d1_var,
#     #      d2: d2_var}
#
#     for j, i in d.items():
#         if i.get() == 1:
#             txt += j['text'] + '\n'
#     d1['state'] = DISABLED
#     d2['state'] = DISABLED
#     d3['state'] = DISABLED
#     d4['state'] = DISABLED
#     if len(txt) == 0:
#         txt = "select smth"
#     showinfo("Замовлення", txt)
#     print(d1['text'])
#
#
# def clear_click():
#     # d1.deselect()
#     # d2.deselect()
#     # d3.deselect()
#     # d4.deselect()
#     for elem, e in d.items():
#         elem.deselect()
#
#
# def edit():
#     d1['state'] = NORMAL
#     d2['state'] = NORMAL
#     d3['state'] = NORMAL
#     d4['state'] = NORMAL
#
#
# def check_all():
#     d1.select()
#     d2.select()
#     d3.select()
#     d4.select()
#
#
# d1_var = IntVar()
# d2_var = IntVar()
# d3_var = IntVar()
# d4_var = IntVar()
#
# d1 = Checkbutton(text='Морозиво "Казка"', variable=d1_var)
# d2 = Checkbutton(text="Морозиво з шоколадом", variable=d2_var)
# d3 = Checkbutton(text='Тістечко"Сніжок"', variable=d3_var)
# d4 = Checkbutton(text='Десерт "Білосніжка"', variable=d4_var)
#
# d1.place(x=20, y=20)
# d2.place(x=20, y=50)
# d3.place(x=20, y=80)
# d4.place(x=20, y=110)
#
# btn = Button(text="Done", command=create_click)
# btn_clear = Button(text="Clear", command=clear_click)
# btn_edit = Button(text="Edit", command=edit)
# btn_all = Button(text="All", command=check_all)
#
# btn.pack()
# btn_clear.pack()
# btn_edit.pack()
# btn_all.pack()
#
# d = {d1: d1_var,
#      d2: d2_var}
#
# mainloop()
