import random

class Player:
    def __init__(self):
        self.name = ""
        self.level = 1
        self.hp = 100
        self.gold = 100
        self.armor = 0
        self.aDmg = 25
        self.mDmg = 10
        self.critChance = 0.1
        self.critMult = 1.75


    def askName(self):
        print("Please enter your characters name:")
        self.name = input(">> ")
        print("Welcome " + self.name + " to the game!")

    def attack(self, target):
        chance = random.randint(0, 100) / 100
        print(str(chance))
        damage = (self.aDmg * self.critMult) if chance <= self.critChance else self.aDmg
        target.hp -= damage
        print("Hit " + target.name + " dealing " + str(damage) + " damage")
        print("The " + target.name + " has now " + str(target.hp) + " HP")

    '''def takeDamage(self, target):
        self.hp -= target.dmg'''
