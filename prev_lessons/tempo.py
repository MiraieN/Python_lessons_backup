class Char:
    def __init__(self, health):
        self.hp = health
        self.level = 0
        self.start_hp = self.hp
        print(f"HP:     {self.hp}")
        print(f"level:  {self.level}")

def fight():
    def level_up(creat):
        creat.level += 1
        hp_inc(creat)
        print(f"\nlevel: {creat.level}")


    def hp_inc(creat):
        creat.hp = creat.start_hp
        creat.hp += stats['hp']
        creat.start_hp = creat.hp
        print(f"hp:{creat.hp}")


new_Char = Char(100)

stats = {'hp': 5}

while new_Char.level != 10:
    level_up(new_Char)
