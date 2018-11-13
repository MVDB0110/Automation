def doeIets(x):
    if x < 10:
        y = 10
    elif x >= 10 and x < 20:
        y="x tussen 10 en 20"
    else:
        y = "x groter dan 19"
    return y

getal = input("Geef een getal in: ")
z = doeIets(int(getal))
print(z)