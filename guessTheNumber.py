# "Guess the Number" by Pixel
import time
import random
import os

print("Hello! What is your name?")
name = input()
print("Wow! " + name + ", That is a great name you got there!")
time.sleep(3)

def start():
    length = 101
    a = 0
    percent = 0
    while a < length:
        rint = random.randint(1, 6)
        randomTime = random.randint(1, 12)
        #os.system("reset")
        print("Randomizing number... " + str(percent) + "% complete")

        percent = percent + 1
        a = a + 1
        time.sleep(randomTime / 650)

    #os.system("clear")
    game(1, None)


def game(alku, num, ):
    # number = random.randint(1, 25)
    if alku == 1:
        number = random.randint(1, 10)
        num = number
        print("You can now start guessing.")
    guess = input()


    if guess.isdigit():
        if int(guess) == num:
            print("You guessed it!")
            time.sleep(2)
            start()
        else:
            print("Not that :)")
            game(0, num)
            game(0, num)
    else:
        print("That is not a valid number!")
        time.sleep(3)
        game(1, num)

start()