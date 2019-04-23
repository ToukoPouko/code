import random

class Player:
    def __init__(self):
        self.name = ""
        self.hp = 100
        self.gold = 100
        self.armor = 0
        self.aDmg = 25
        self.mDmg = 10

    def askName(self):
        print("Please enter your characters name:")
        self.name = input(">> ")
