z = True
z1 = True
o = []
while z1:
    a = int(input("Podaj liczbę arabską, którą chcesz przerobić na liczbę rzymską: "))
    if a >= 4000:
        print("Błąd! Podana warotość musi być mniejsza od 4000.")
    elif a <= 0:
        print("Błąd! Podana warotość musi być większa niż 0.")
    else:
        a1 = a
        z1 = False
while z:
    if a >= 1000 and a < 4000:
        a -= 1000
        o.append("M")
    elif a >= 900 and a < 1000:
        a -= 900
        o.append("CM")
    elif a >= 500 and a < 900:
        a -= 500
        o.append("D")
    elif a >= 400 and a < 500:
        a -= 400
        o.append("CD")
    elif a >= 100 and a < 400:
        a -= 100
        o.append("C")
    elif a >= 90 and a < 100:
        a -= 90
        o.append("XC")
    elif a >= 50 and a < 90:
        a -= 50
        o.append("L")
    elif a >= 40 and a < 50:
        a -= 40
        o.append("XL")
    elif a >= 10 and a < 40:
        a -= 10
        o.append("X")
    elif a >= 9 and a < 10:
        a -= 9
        o.append("IX")
    elif a >= 5 and a < 9:
        a -= 5
        o.append("V")
    elif a >= 4 and a < 5:
        a -= 4
        o.append("IV")
    elif a >= 1 and a < 4:
        a -= 1
        o.append("I")
    else:
        z = False

print(f"Liczba {a1} po rzymsku to:")
print(''.join(map(str, o)))