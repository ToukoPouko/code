import random
from player import Player

class Enemy:
    def __init__(self, name, hp, dmg, gReward, xpReward):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.gReward = gReward
        self.xpReward = xpReward

    def attack(self, target):
        target.hp -= self.dmg
        print("The " + self.name + " attacked you and dealt " + str(self.dmg) + " damage")
