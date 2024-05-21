n = int(input("Wpisz, ile liczb Fibbonacciego program ma ci podać: "))
f1 = 1
f2 = 1
r = 0
t = n - 3
if n == 1:
    print(f1)
elif n == 2:
    print(f1)
    print(f2)
elif n == 3:
    print(f1)
    print(f2)
    print(f1 + f2)
else:
    print(f1)
    print(f2)
    print(f1 + f2)
    while r < t:
        if r < t:
            f2 += f1
            f1 = f2 - f1
            print(f1 + f2)
            r += 1