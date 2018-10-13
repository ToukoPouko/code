import time
# test
#Defining the Start Scenario
notAvailable = "That is not an action you could do right now."
userName = input("What do you want to be called as?: ")
def startScene():
    print("You hear water drops...")
    time.sleep(1)
    print("What will you do?")
    time.sleep(1)
    decision = input("Available actions: Open eyes, Keep sleeping, Do nothing: ")
    if decision.lower() == "open eyes":
        start1()
    elif decision.lower() == "keep sleeping":
        start2(1)
    elif decision.lower() == "do nothing":
        start3()
    else:
        print(notAvailable)
        startScene()

def start1():
    print("You open your eyes carefully...")
    time.sleep(1)
    print("The only thing you see is a small hole, because a small bit of sunlight is shining through it.")
    time.sleep(4)
    print("You don't know the place where you are. You don't remember anything else than your name, " + userName)
    time.sleep(4)
    print("What will you do?")
    time.sleep(1.5)
    decision = input("Available actions: Stand up, Sleep, Do nothing, Eat cake: ")
    if decision.lower() == "stand up":
        start4()
    elif decision.lower() == "sleep":
        print("You decide to get back to sleep")
        time.sleep(3)
        start2(2)
    elif decision.lower() == "do nothing":
        start3()
    elif decision.lower() == "eat cake":
        print("There was a cake next to you when you opened your eyes and you decided to eat it")
        print("The cake was so good that you fell asleep...")
        if achievement1 == False:
            print("Achievement got: The Cake is a lie")
        startScene()

    else:
        print(notAvailable)
        start1()

def start2(number):
    if number == 1:
        print("You keep sleeping...")
        time.sleep(2)
        startScene()
    elif number == 2:
        startScene()

def start3():
    print("You decided not to do anything, but you came too bored and fell asleep...")
    time.sleep(4)
    startScene()




startScene()
