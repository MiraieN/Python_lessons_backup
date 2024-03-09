# video course Classes https://youtu.be/mDKM-JtUhhc?t=33030

## classes https://youtu.be/mDKM-JtUhhc?t=26039
#
# ## classes inheritance https://youtu.be/mDKM-JtUhhc?t=31294
class Monster:
    def __init__(self, energy, health):
        self.energy = energy
        self.health = health

    def reduce_energy(self, amount):
        self.energy -= amount

    def move(self, speed):
        print(f'The monster has moved with a speed of {speed}')

    def attack(self, amount):
        print(f"Monster damaged for {amount}")

class Scorpion(Monster):
    def __init__(self, speed, scorpion_health, scorpion_energy, poison_damage):
        # super().__init__(energy=scorpion_energy, health=scorpion_health)
        Monster.__init__(self, scorpion_energy, scorpion_health)
        self.speed = speed
        self.poison_damage = poison_damage
    # def __init__(self, poison_damage):
    #     self.poison_damage = poison_damage

    def attack(self):
        print(f"Scorpion attacked for {self.poison_damage} of poison damage")
        # return self.poison_damage


# m = Monster(10, 15)
# m.attack(15)
s = Scorpion(15, 10, 10, 5)
# s = Scorpion(50)
s.move(s.speed)
s.attack()
s.reduce_energy(10)
print(s.energy)
print(s.health)


# ## complex inheritance https://youtu.be/mDKM-JtUhhc?t=31834
# # mro https://youtu.be/mDKM-JtUhhc?t=32096
class Creature:
    def __init__(self, killable, **kwargs):
        self.killable = killable
        self.killed = False
        super().__init__(**kwargs)

    def kill(self):
        if self.killable:
            print("The creature is killed now")
            self.killed = True
        else:
            print("The creature is still alive")
class Monster:
    def __init__(self, energy, health, **kwargs):
        self.energy = energy
        self.health = health
        super().__init__(**kwargs)

    def reduce_energy(self, amount):
        self.energy -= amount
        return self.energy

    def move(self, speed):
        print(f'The monster has moved with a speed of {speed}')

    def attack(self, amount):
        print(f"Monster damaged for {amount}")

class Fish:
    def __init__(self, speed, has_scales, **kwargs):
        self.speed = speed
        self.has_scales = has_scales
        super().__init__(**kwargs)

    def swim(self):
        print(f'Fish is swimming at the speed of {self.speed}')


class Shark(Creature, Monster, Fish):
    def __init__(self,has_teeth, energy, health, speed, has_scales, killable):
        self.has_teeth = has_teeth
        super().__init__(energy = energy, health = health, speed = speed, has_scales = has_scales, killable=killable)

    def bite(self):
        if self.has_teeth:
            print(f'The shark bites with {10}')
        else:
            print('The shark swims away')
            self.swim()

lil_shark = Shark(False,
                  10,
                  15,
                  20,
                  False,
                  False)
big_shark = Shark(True,
                  8,
                  12,
                  15,
                  False,
                  True)

print(lil_shark.speed)
print(lil_shark.reduce_energy(1))
lil_shark.bite()
big_shark.bite()
lil_shark.attack(10)
lil_shark.kill()
big_shark.kill()
print(lil_shark.killable)

