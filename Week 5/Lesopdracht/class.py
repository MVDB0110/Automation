import datetime

class Train():

    snelheid = 0

    def __init__(self, jaar, merk, organisatie):
        self.merk = merk
        self.bouwjaar = jaar
        self.organisatie = organisatie
        self.snelheid = Train.__versnellen()

    def __str__(self):
        return "Deze trein is gebouwd in " + str(self.bouwjaar) + " door " + self.merk + " en rijd voor " + self.organisatie + " en rijd " + str(self.snelheid) + " km/h"

    def __versnellen():
        snelheid = Train.snelheid + 1
        return snelheid

t1 = Train(1999,'VDL Berkhof','NS')
print(t1)