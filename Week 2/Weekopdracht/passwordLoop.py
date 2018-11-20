import hashlib
import sys

def passwdLoop():
    p = "326f13e25448c99ccae78b0afa1c84e6fae2d8a587976df3a86628ae"

    for i in range(65,90):
        letter1 = chr(i)
        for i2 in range(65,90):
            letter2 = chr(i2)
            for i3 in range(65,90):
                letter3 = chr(i3)
                ww = letter1 + letter2 + letter3
                if hashlib.sha224(ww.encode()).hexdigest() == p:
                    print("Je hebt het wachtwoord gevonden! Het was:",ww)
                    sys.exit()

                else:
                    print("Helaas, nog een poging. ", ww, " klopt niet")

def SHAloop():
    hash = 'f00bdeb2cd9da240a57c951fdf1bcba509fd0cd83c5e5ad9a669de12'
    for i in range(65,90):
        char = chr(i)
        char = char.encode()
        if hash == hashlib.sha224(char).hexdigest():
            print("Het wachtwoord is gevonden.")