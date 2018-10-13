import random, time, string


def start():
    canAddChars = input("Allow special characters y/n")
    if canAddChars.lower() == "y" or canAddChars.lower() == "yes":
        canAddChars = True
    elif canAddChars.lower() == "n" or canAddChars.lower() == "no":
        canAddChars = False
    else:
        print("That is not a valid action")
        start()

    passLength = input("Password length: ")
    if passLength.isalpha() == False and int(passLength) >= 4:
        passLength = int(passLength)
    else:
        print("That is not a valid length")
        start()

    initialize_password_generation(canAddChars, passLength)


def initialize_password_generation(chars, length):
    if chars:
        generate_strong_password(length)
    elif not chars:
        generate_password(length)
    else:
        print("An Error has occured.")
        time.sleep(2.5)
        start()


def generate_password(length):
    password = list("x" * length)

    for i in range(length):
        randomInt = random.randint(1, 9)
        chance = random.randint(1, 2)
        randomLetter = random.choice(string.ascii_letters)
        if chance == 1:
            password[i] = str(randomInt)
        elif chance == 2:
            password[i] = randomLetter

    password = "".join(password)
    print(password)
    save_password_into_a_file(str(password).encode("utf-8"))


def generate_strong_password(length):
    password = list("x" * length)

    for i in range(length):
        randomInt = random.randint(1, 9)
        chance = random.randint(1, 3)
        randomLetter = random.choice(string.ascii_letters)
        randomChar = random.choice(string.punctuation)
        if chance == 1:
            password[i] = str(randomInt)
        elif chance == 2:
            password[i] = randomLetter
        elif chance == 3:
            password[i] = randomChar

    password = "".join(password)
    print(password)
    save_password_into_a_file(password)


def save_password_into_a_file(password):
    userChoice = input("Would you like to save the password in a file?")
    if userChoice.lower() == "yes" or userChoice.lower() == "y":
        with open("password.txt", "w") as file:
            file.write(str(password))


start()
