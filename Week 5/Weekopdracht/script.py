from smartcard import Smartcard

person_1_z = input("Van welke zijde voel je je op dit moment? ")
person_1_vl = input("Wat is je voorletter(s)? ")
person_1_tvl = input("Wat is je tussenvoegsel? ")
person_1_an = input("Wat is je achternaam? ")
person_1_bd = input("Op welke datum ben je geboren? ")

person_2_z = input("Van welke zijde voel je je op dit moment? ")
person_2_vl = input("Wat is je voorletter(s)? ")
person_2_tvl = input("Wat is je tussenvoegsel? ")
person_2_an = input("Wat is je achternaam? ")
person_2_bd = input("Op welke datum ben je geboren? ")

personal_ov_1 = Smartcard(person_1_z,person_1_vl,person_1_tvl,person_1_an,person_1_bd)
personal_ov_2 = Smartcard(person_2_z,person_1_vl,person_2_tvl,person_2_an,person_2_bd)

personal_ov_1.load(10)
personal_ov_2.load(10)

personal_ov_1.withdraw(5)
personal_ov_2.withdraw(15)