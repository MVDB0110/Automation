import sqlite3
import random

db='getallen.db'

conn = sqlite3.connect(db)
c=conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS getallen (getal INTEGER);')

for i in range(1,1000):
    int = random.randint(1,499)
    c.execute('INSERT INTO getallen(getal) VALUES({})'.format(int))

conn.commit()

c.execute("SELECT * FROM getallen")
data = c.fetchall()

c.close()
conn.close()

lst = []

for line in data:
    lst.append(line[0])

gemid = sum(lst)
gemid = gemid / len(lst)

print("Het totaal is: ",sum(lst))
print("Het gemiddelde is: ",gemid)
print("Het laagste getal is: ",min(lst))
print("Het hoogste getal is: ",max(lst))