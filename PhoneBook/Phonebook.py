import time, os

dir = os.path.dirname(__file__) # Path of the script
file_path = os.path.join(dir, "contacts.txt")


def main():
    while True:
        print("--------------------------------------")
        print("1. Add new person")
        print("2. View phonebook")
        print("3. Delete person")
        userInput = input(">>")

        try:
            userInput = int(userInput)
        except:
            print("Invalid input.")
            time.sleep(0.5)
            main()

        if userInput == 1:
            addPerson()
        elif userInput == 2:
            viewPhonebook()
        elif userInput == 3:
            deletePerson()
        else:
            print("Invalid input.")


def addPerson():
    name = input("Enter name: ")
    number = input("Enter number: ")
    address = input("Enter address: ")
    file = open(file_path, "a")
    file.write(name + "," + number + "," + address)
    file.close()


def viewPhonebook():
    file = open(file_path, "r")
    for line in file:
        print(line)
    return


def deletePerson():
    return


if __name__ == "__main__":
    main()