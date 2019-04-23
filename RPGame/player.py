import random

class Player:
    def __init__(self):
        self.name = ""
        self.hp = 100
        self.gold = 100
        self.armor = 0
        self.aDmg = 25
        self.mDmg = 10
        self.critChance = 0.05
        self.critMult = 1.75

    def askName(self):
        print("Please enter your characters name:")
        self.name = input(">> ")

    def attack(self, target):
        chance = random.randint(0, 1) / 100
        damage = (self.aDmg * self.critMult) if chance <= self.critChance else self.aDmg
        target.hp -= damage

    def takeDamage(self, target):
        self.hp -= target.dmg


