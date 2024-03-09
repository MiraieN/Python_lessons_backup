import tkinter as tk
from random import randint as r


class Creature:
    def __init__(self, name, health, damage, accuracy, dodge, armor, crit_chance, crit_amplifier, diplomacy):
        self.name = name
        self.hp = health
        self.dmg = damage
        self.acc = accuracy
        self.dodge = dodge
        self.armor = armor
        self.crit_chance = crit_chance
        self.crit_amp = crit_amplifier
        self.speak = diplomacy

        self.health_max = self.hp
        self.dmg_start = self.dmg
        self.acc_start = self.acc
        self.dodge_start = self.dodge
        self.armor_start = self.armor
        self.crit_chance_start = self.crit_chance
        self.crit_amp_start = self.crit_amp
        self.speak_at_start = self.speak
        # print(f"{self.name} created")

    def __str__(self):
        print(f"{self.name} created")


class Hero(Creature):
    def __init__(self, name, health, damage, accuracy, dodge, armor, crit_chance, crit_amplifier, diplomacy):
        super().__init__(name, health, damage, accuracy, dodge, armor, crit_chance, crit_amplifier, diplomacy)

    def __str__(self):
        return f"{self.name} created"


# for pos in "first", "second":
#     print(f'''Hello, {pos} player. Choose your class:
#                                                 1. Warrior
#                                                 2. Robber
#                                                 3. Scientist
#                                                 4. Multispeaker
#                                                 ''')
player1 = ''
player2 = ''


def choose_class_pl1(name):
    match name:
        case "Warrior":
            player1 = Hero("Warrior", 100, 10, 40, 20, 50, 22, 30, 5)
        case "Robber":
            player1 = Hero("Robber", 70, 15, 60, 60, 30, 33, 30, 5)
        case "Scientist":
            player1 = Hero("Scientist", 50, 20, 80, 70, 70, 44, 30, 5)
        case "Multispeaker":
            player1 = Hero("Multispeaker", 70, 10, 60, 40, 30, 33, 30, 30)
    label_pl1.config(text=player1)


def choose_class_pl2(name):
    match name:
        case "Warrior":
            player2 = Hero("Warrior", 100, 10, 40, 20, 50, 22, 30, 5)
        case "Robber":
            player2 = Hero("Robber", 70, 15, 60, 60, 30, 33, 30, 5)
        case "Scientist":
            player2 = Hero("Scientist", 50, 20, 80, 70, 70, 44, 30, 5)
        case "Multispeaker":
            player2 = Hero("Multispeaker", 70, 10, 60, 40, 30, 33, 30, 30)
    label_pl2.config(text=player2)


def destroy_all_widgets():
    for widg in root.grid_slaves():
        widg.destroy()


# name, health, damage, accuracy, dodge, armor, crit_chance, crit_amplifier, diplomacy
dragon = Creature("Dragon", r(150, 220), r(30, 50), r(50, 80), r(5, 15), 0, r(10, 20), r(150, 250), 0)

root = tk.Tk()
root.title("DnD")

window_width = 800
window_height = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)
root.attributes('-alpha', 0.8)
root.attributes('-topmost', 1)  # stay at top
# root.iconbitmap('2.ico')

loginInput = tk.StringVar()
passInput = tk.StringVar()

label_classes = tk.Label(text='''Hello players. Choose your classes:''',
                         font=("Calibri", 16, "bold"))
label_pl1 = tk.Label(text="Player 1", font=("Calibri", 16, "bold"))
label_pl2 = tk.Label(text="Player 2", font=("Calibri", 16, "bold"))
button_warrior = tk.Button(text="Warrior", command=lambda: choose_class_pl1("Warrior"), font=("Calibri", 16, "bold"))
button_warrior_2 = tk.Button(text="Warrior", command=lambda: choose_class_pl2("Warrior"), font=("Calibri", 16, "bold"))
button_robber = tk.Button(text="Robber", command=lambda: choose_class_pl1("Robber"), font=("Calibri", 16, "bold"))
button_robber_2 = tk.Button(text="Robber", command=lambda: choose_class_pl2("Robber"), font=("Calibri", 16, "bold"))

button_ok = tk.Button(text="OK", command=destroy_all_widgets, font=("Calibri", 16, "bold"))

label_classes.grid(row=0, column=0)
label_pl1.grid(row=1, columnspan=3, sticky="w", padx=70, pady=20)
label_pl2.grid(row=1, columnspan=7, sticky="e", padx=70, pady=20)
button_warrior.grid(row=2, columnspan=1, sticky="w", padx=70, pady=20)
button_robber.grid(row=3, columnspan=1, sticky="w", padx=70, pady=20)

button_warrior_2.grid(row=2, column=2, columnspan=2, sticky="e", padx=70, pady=20)
button_robber_2.grid(row=3, column=2, columnspan=2, sticky="e", padx=70, pady=20)

button_ok.grid(row=6, columnspan=4, padx=70, pady=20)


root.mainloop()

# stats = {"hp": 0,
#              "dmg": 0,
#              "acc": 0,
#              "dodge": 0,
#              "armor": 0,
#              "crit_chance": 0,
#              "crit_amp": 0}
