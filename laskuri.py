import math, time


print("1. Rocket League")
print("2. CS:GO")
print("3. Rainbow Six Siege")
print("4. Star Wars: BattleFront 2")
peli = int(input("Valitse yllä olevista yksi. "))
if peli == 1:
    score = int(input("Paljonko SCORE oli lopussa?"))
    moves = score * (score / 2) / 10000
    moves = math.floor(moves)
    print("Sinun pitää tehdä", moves, "liikettä yhteensä")
    time.sleep(20)
