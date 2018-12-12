import sqlite3

db='adresgegevens.db'
connection = sqlite3.connect(db)
conn = connection.cursor()

conn.execute('SELECT * FROM adresgegevens;')
data = conn.fetchall()

for line in data:
    print(line[0],line[1],line[2])