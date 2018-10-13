''' Made by PixeledGamer '''

vowels = 'aeiouyäöå'
vowels = list(vowels)

def start():
    userText = input('Enter the text to get vowel count for. ')
    print('')
    chars = list(userText)
    count = 0
    for c in chars:
        for v in vowels:
            if c.lower() == v:
                count += 1
            else:
                continue
    print('There were ' + str(count) + ' vowels in your string')
    print('')
    start()


start()
    
    
