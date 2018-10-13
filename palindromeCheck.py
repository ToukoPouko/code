''' Made by PixeledGamer '''

def start():
    string = input('Input a string you want to be checked: ')
    print('')
    chars = list(string)
    newChars = list(string)
    for i in range(0, len(string)):
        newChars[i] = chars[len(chars)-1-i]
    newString = "".join(newChars)
    if newString.lower() == string.lower():
        print('That string is a palindrome')
    else:
        print('That string is not a palindrome')
    print('')
    start()


start()
