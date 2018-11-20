import random

def dobbelsteen(min=1, max=6):
    variabel = random.randint(min,max) # Geef variabel een getal tussen minimaal en maximaal
    return variabel # Geef variabel terug

def yesno():
    variabel = random.choice(['yes', 'no'])  # Geef variabel yes of no mee
    return variabel # Geef variabel terug