import random

class Enemy:
    def __init__(self, name, hp, dmg, gReward, xpReward):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.gReward = gReward
        self.xpReward = xpReward

    def attack(self, target):
        chance = random.randint(0, 1) / 100
        damage = (self.aDmg * self.critMult) if chance <= self.critChance else self.aDmg
        target.hp -= damage

    def takeDamage(self, target):
        chance = random.randint(0, 100) / 100
        damage = (target.dmg * self.critMult) if chance <= self.critChance else target.dmg
        self.hp -= damage


