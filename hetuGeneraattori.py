import time


def start():
    print("Milloin olet syntynyt?")
    birthday = str(input("Kirjoita syntymäaika muodossa 01.01.2016 "))
    print(birthday[6:8])
    if not birthday.isalpha() and len(birthday) == 10:
        generate_hetu(birthday)
    else:
        print("Et kirjoittanut syntymäaikaasi oikein. Yritä uudelleen!")
        time.sleep(3)
        start()


def generate_hetu(birthday):
    day_and_month = (birthday[0:2], birthday[3:5])
    day_and_month = "".join(day_and_month)
    if birthday[6:7] == "2":
        year = "A"
    elif birthday[6:8] == "19":
        year = "-"
    else:
        year = "+"
    gender = input("Oletko mies vai nainen? ")
    nnn = []
    kohta = 0
    if gender.lower() == "nainen":
        kohta = 2
    elif gender.lower() == "mies":
        kohta = 3
    tiiviste = str((int(day_and_month) + int(year)) / 31)
    switch ((int(day_and_month) + int(year)) % 31:
    print(day_and_month)
    print(year)
    print(kohta)
    print(tiiviste)
    while kohta <= 899:
        possible_hetu = (day_and_month, year, str(kohta))
        possible_hetu = "".join(possible_hetu)
        nnn.append(possible_hetu)
        print(possible_hetu)
        kohta += 2


start()




