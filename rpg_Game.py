from time import sleep as sleep
from random import randint as rint

user_input = ""
drop_list = []

player_hp = 100
player_armor = 100
player_dmg = 10

class Mob:

    def __init__(self, name, hp, dmg, gold):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.gold = gold

    def take_dmg(self, p_dmg):
        if rint(1, 100) >= 9:
            self.hp -= p_dmg
            print("You hit the {0} with {1} damage!".format(self.name, p_dmg))
        elif rint(1, 100) <= 9:
            p_dmg += (0.635 * p_dmg)
            self.hp -= p_dmg
            print("You hit the {0} with a critical hit, dealing {1} damage!".format(self.name, p_dmg))
        return

    def attack(self, p_hp):
        p_hp -= self.dmg
        print("You took {0} damage from the {1}".format(self.dmg, self.name))
        return

    def destroy(self, p_gold):
        self.hp = 0
        p_gold += self.gold
        if rint(1, 100) <= 5:
            drop_item(self.name)
        print("You got {} gold!").format(p_gold)
        return


def drop_item(name):
    global user_input

    item = drop_list[rint(0, len(drop_list))]
    user_input = input("The {0} left a {1} on the ground. Do you want to pick it up?(Y/N):".format(name, item))
    if check_input("y"):
        append_to_inv(item)
    elif check_input("n"):
        user_choice()


def check_input(item):
    global user_input

    if user_input.lower() == item:
        return True
    else:
        return False


def empty():
    print("")
    return


def clear_screen():
    for i in range(1, 20):
        empty()
    return


def access_help():
    clear_screen()
    print("Choose one of the actions presented on the screen and select one of them")
    print("by typing the action after the \"What would you want to do?: \" message.")
    empty()
    empty()
    empty()
    input("Press ENTER to dismiss")
    user_choice()


def access_inv():

    '''Access the user inventory and load the current items'''

    try:
        inventory_file = open("user_inventory", "r")  # Open file if it exists
    except FileNotFoundError:
        inventory_file = open("user_inventory", "w")  # Create file if it doesn't exist

    # inventory = inventory_file.

    clear_screen()
    empty()
    empty()
    print()
    return


def access_travel():

    '''Access the travelling screen and load the current position on the map'''
    mob_encounter("Alajärvi")


def access_gear():

    '''Access the users gear and load the current gear'''


def user_choice():
    global user_input

    clear_screen()
    empty()
    empty()
    print("Type \"help\" anytime to access the help menu or \"settings\" to access the settings menu")
    empty()
    print("       Inventory    |    Gear  ")
    print("-"*40)
    print("       Travel       |    Exit  ")
    empty()
    user_input = input("What would you want to do?: ")

    if check_input("inventory"):
        access_inv()

    elif check_input("travel"):
        access_travel()

    elif check_input("gear"):
        access_gear()

    elif check_input("exit"):
        exit()

    elif check_input("help"):
        help()


def mob_encounter(destination):

    clear_screen()
    empty()
    if rint(1, 1) == 1:
        mob = skeleton
    print("While you were travelling to {0} you encountered a {1}".format(destination, mob.name))
    sleep(3)
    encounter_screen(mob)


def encounter_screen(mob):



#Init mobs

skeleton = Mob("Skeleton", 50, 15, 20)

user_choice()
