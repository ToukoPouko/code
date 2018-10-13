import sys, os
import time, re

clear = lambda: os.system("cls" if os.name == "nt" else "clear")

def quit():
    clear()
    sys.exit("Bye bye!")


def gameScene():
    word = input("Type a word that you want the other player to guess: ")
    word = word.lower()
    guessWord = len(word) * "_"
    guessWord = list(guessWord)
    guessWord = ''.join(guessWord)

    clear()

    if word.lower() == "stop":
        quit()
    else:

        def startGuessing(wordatm):

            if wordatm != word.lower():
                guessWord = list(wordatm)
                print(wordatm)
                guess = input("Start guessing by typing in a letter: ")

                if guess.lower() != "stop" and guess.isdigit() == False:
                    if len(guess) >= 2 or len(guess) <= 0:
                        print("Type only 1 letter!")
                        time.sleep(1)
                        clear()
                        startGuessing(wordatm)
                    else:
                        for char in range(len(word)):
                            if guess.lower() == word[char]:
                                guessWord = list(guessWord)
                                guessWord[char] = guess.lower()
                                guessWord = ''.join(guessWord)
                                clear()
                                startGuessing(guessWord)

                elif guess.lower() == "stop":
                    quit()

            elif wordatm == word.lower():
                clear()
                print("You guessed the word!!")
                print(" ")
                print("The word was " + word.lower())
                print(" ")
                time.sleep(1)
                clear()
                gameScene()


        startGuessing(guessWord)



gameScene()
