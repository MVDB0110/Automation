import datetime

def maximumCijfer():
    lst = [8, 2, 3, -1, 7]
    return max(lst)

def geboortejaar():
    huidigejaar = 2018
    jaar = input("Wat is jou leeftijd jongeman/vrouw? ")
    jaar = int(jaar)
    return huidigejaar - jaar

def geboortejaarTime():
    date = datetime.datetime.now().date().year
    jaar = input("Wat is jou leeftijd jongeman/vrouw? ")
    jaar = int(jaar)
    return date - jaar

def withinRange():
    rng = range(1,100)
    invoer = int(input("Geef een cijfertje: "))
    if invoer in rng:
        return "Is in range."
    else:
        return "Niet in range."

def evenGetallen():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for cijfer in lst:
        if cijfer % 2 == 0:
            print("Even getal: " + str(cijfer))
        else:
            print("Oneven: " + str(cijfer))

def multiply():
    lst = [8, 2, 3, -1, 7]
    cijfer = 1
    for i in lst:
        cijfer = cijfer * i

    return cijfer

def reverse():
    str = "1234abcd"
    return str[::-1]

def prime():
    prime = int(input("Geef een getal: "))
    for i in range(2, prime):
        if (prime % i) == 0:
            return str(prime) + " is not a prime number"
            break
    else:
        return str(prime) + " is a prime number"

print(prime())