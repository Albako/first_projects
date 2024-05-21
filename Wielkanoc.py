print("Program podaje datę wielkanocy w latach od 325 do 2200.")
w = 0
x = 0
y = 0
z = True
while z:
    w = int(input("Podaj rok, w którym chcesz sprawdzić datę wielkanocy: "))
    if w < 1583 and w >= 325:
        x = 15
        y = 6
        z = False
    elif w >= 1583 and w < 1700:
        x = 22
        y = 2
        z = False
    elif w >= 1700 and w < 1800:
        x = 23
        y = 3
        z = False
    elif w >= 1800 and w < 1900:
        x = 23
        y = 4
        z = False
    elif w >= 1900 and w < 2100:
        x = 24
        y = 5
        z = False
    elif w >= 2100 and w <= 2200:
        x = 24
        y = 6
        z = False
    else:
        print("Program nie jest w stanie podać daty wielkanocy w latach powyżej 2200 roku, ani poniżej 325 roku.")
a = w % 19
b = w % 4
c = w % 7
d = (19 * a + x) % 30
e = (2 * b + 4 * c + 6 * d + y) % 7
f = 22 + d + e
if f > 31:
    k = f - 31
    print(f"Wielkanoc w roku {w} wypada {k} kwietnia")
else:
    print(f"Wielkanoc w roku {w} wypada {f} marca")

