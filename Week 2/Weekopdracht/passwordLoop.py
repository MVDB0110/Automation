import hashlib

p = "326f13e25448c99ccae78b0afa1c84e6fae2d8a587976df3a86628ae"

for i in range(100):
    letter1 = chr(i)
    for i2 in range(100):
        letter2 = chr(i2)
        for i3 in range(100):
            letter3 = chr(i3)
            ww = letter1 + letter2 + letter3
            if hashlib.sha224(ww.encode()).hexdigest() == p:
                print("Je hebt het wachtwoord gevonden! Het was:",ww)
                break

            else:
                print("Helaas, nog een poging (poging",i,")")