import random
import time, sys

#made by PixeledGamer
#Rock Paper Scissors


print("Welcome to Rock, Paper, Scissors!")
time.sleep(2)
points = 0

print("Type 'stop' to stop playing")




def gameScene(score, decision):
    def quit(score):
        sys.exit("Your final score was: " + str(score))
    if decision.lower() != "stop":
        choice = input("Which will you choose; Rock, Paper or Scissors?: ")
        ai = random.choice(["Rock", "Paper", "Scissors"])
        points = score if score < 0 else 0


        if choice.lower() == "rock" or choice.lower() == "paper" or choice.lower() == "scissors":
            if choice.lower() == ai.lower():
                print("AI's choice was " + ai)
                print("It's a draw!")
                print("Your score is " + str(points) + " currently")
                time.sleep(3)
                gameScene(points, choice)
            elif choice.lower() == "rock" and ai.lower() == "paper":
                print("AI's choice was " + ai)
                print("The AI won. Better luck next time!")
                points = points - 1
                print("Your score is " + str(points) + " currently")
                time.sleep(3)
                gameScene(points, choice)
            elif choice.lower() == "rock" and ai.lower() == "scissors":
                print("AI's choice was " + ai)
                print("You won!")
                points = points + 1
                print("Your score is " + str(points) + " currently")
                time.sleep(3)
                gameScene(points, choice)
            elif choice.lower() == "paper" and ai.lower() == "rock":
                print("AI's choice was " + ai)
                print("You won!")
                points = points + 1
                print("Your score is " + str(points) + " currently")
                time.sleep(3)
                gameScene(points, choice)
            elif choice.lower() == "paper" and ai.lower() == "scissors":
                print("AI's choice was " + ai)
                print("The AI won. Better luck next time!")
                points = points - 1
                print("Your score is " + str(points) + " currently")
                time.sleep(3)
                gameScene(points, choice)
            elif choice.lower() == "scissors" and ai.lower() == "rock":
                print("AI's choice was " + ai)
                print("The AI won. Better luck next time!")
                points = points - 1
                print("Your score is " + str(points) + " currently")
                time.sleep(3)
                gameScene(points, choice)
            elif choice.lower() == "scissors" and ai.lower() == "paper":
                print("AI's choice was " + ai)
                print("You won!")
                points = points + 1
                print("Your score is " + str(points) + " currently")
                time.sleep(3)
                gameScene(points, choice)
        else:
            if choice.lower() == "stop":
                quit(points)
            else:
                print("That is not an valid action!")
                print("Your score is " + str(points) + " currently")
                gameScene(points, choice)

    elif decision.lower() == "stop":
        quit(points)

gameScene(points, "")
