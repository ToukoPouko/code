''' Made by PixeledGamer '''

import string as str

def start():
    string = input('Input a string you want to reverse: ')
    print("")
    index = 0
    chars = list(string)
    newChars = list(string)
    for i in range(0, len(string)):
        newChars[i] = chars[len(chars)-1-i]
    print("".join(newChars))
    print("")
    start()
    
start()
