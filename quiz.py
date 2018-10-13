import random
import time

print("Welcome to the Ultimate Quiz!")
time.sleep(1)
name = input("What is your name? ")
print("Hello " + name + "!")
time.sleep(2)
list = []
file = open("QUESTIONS.txt", "r")

for line in file:
    list.append(line.split(","))


class Question:

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask_question(self):
        user_answer = input(self.question)
        if user_answer.lower() == self.answer.lower():
            print("You are right!")
            time.sleep(2)
        else:
            print("Sorry, wrong answer. The right answer was: ", self.answer)
            time.sleep(2)

# Add Questions Here
# Example: question_name = Question("Your question ", "Answer to the question")
q1 = Question(list[0[0]], list[0[1]])
q2 = Question("What is the most played game in Steam? ", "Dota 2")
q3 = Question("Who did you say you are at the start? ", name)

# Ask them here
# Example: question_name.ask_question()
q1.ask_question()
q2.ask_question()
q3.ask_question()



