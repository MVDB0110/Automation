import datetime

class Smartcard():
    """Smartcard class voor OV passen"""

    card_serial = 0

    def __init__(self, geslacht, voorletters, tussenvoegsels, achternaam, geboortedatum):
        self.geslacht = geslacht
        self.voorletters = voorletters
        self.tussenvoegsels = tussenvoegsels
        self.achternaam = achternaam
        self.geboortedatum = geboortedatum
        self.creationdate = datetime.date.today()
        self.namecheck = Smartcard.__check_name(self)
        self.saldo = 0
        self.serial = Smartcard.card_serial
        Smartcard.card_serial +=1

    def __check_name(self):
        fullname = self.voorletters+self.tussenvoegsels+self.achternaam
        if len(fullname) <= 26:
            return "True"
        else:
            return "False"

    def load(self,hoeveelheid):
        """Laad saldo op pas"""
        self.saldo += hoeveelheid

    def withdraw(self, hoeveelheid):
        """Haal saldo van pas"""
        saldotest = self.saldo - hoeveelheid
        if saldotest < 0:
            self.saldo = saldotest
            print(self.voorletters + " " + self.tussenvoegsels + " " + self.achternaam + " heeft een negatief saldo.")
        else:
            self.saldo = saldotest

    def __str__(self):
        return self.voorletters + " " + self.tussenvoegsels + " " + self.achternaam
