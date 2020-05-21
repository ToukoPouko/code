import random

f = open("D:\\Koulu\\Matematiikka\\MA13\\file.txt")
rows = f.readlines()

def main():
    print("1. Add entry")
    print("2. Random entry")
    print("3. Print entries")
    print("4. Remove entry")
    option = input(">> ")
    if option == "1":
        add()
    elif option == "2":
        randomEntry()
    elif option == "3":
        printEntries()



def add():
    print("INPUT CODE")
    code = input(">> ")
    print("INPUT RATING")
    rating = input(">> ")
    f.append([code, rating])
    main()

def randomEntry():
    print(rows[random.randint(0,len(rows))])
    main()

def printEntries():
    print("Sorting method?")
    print("1. Code")
    print("2. Rating")
    option = input(">> ")
    if option == "1":
        for row in sorted(rows):
            print(row.split(",")[0], + ", " + row.split(",")[1])
    elif option == "2":
        newRow = []
        for row in rows:
            newRow.append(row.split(",")[0] + row.split(",")[1])
        print(newRow)
        for row in newRow.sort():
            print(row)
    main()
    

main()