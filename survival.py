from random import randint as rInt
from time import sleep as sleep

name = None
time = 2

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.hunger = 0
        self.speed = 1

    def stats(self):
        print('HP:  {}'.format(self.health))
        print('Hunger: {}'.format(self.hunger))
        #print('HP:  {}'.format(self.health))

    def update(self):
        


class Scene:
    def __init__(self, desc, choices, conses, cons_desc):
        self.desc = desc
        self.choices = choices
        self.conses = conses


    def run(self):
        clear()
        player.stats()
        print(self.desc)
        print('What will you do? ')
        print('1. {} | 2. {} | 3. {}'.format(choices[1], choices[2], choices[3]))
        choice = input()
        index = choice - 1
        con = conses[index]
        con_desc = cons_desc[index]
        print(con_desc)


def clear():
    for i in range(100):
        print(" ")
    return

def cont():
    input('Press ENTER to continue...')
    clear()
    return

def start():
    global name

    print('You wake up in a forest with a little headache.')
    cont()
    print('You don\'t remember how you got there or what your name is.')
    cont()
    print('You find an ID in your pocket and take a look at it.')
    cont()
    print('You notice a puddle on the ground next to you. You take the ID and compare the picture to the reflection of your face from the puddle')
    cont()
    print('The picture looks just like you. According to the ID, your name is ')
    name = input()
    clear()
    print('You stand up and start walking deeper in to the forest')
    cont()
    


player = Player(name)

start()
