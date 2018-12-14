import matplotlib.pyplot as plt
import numpy as np
import sqlite3

minions = []
percentage = []

db = sqlite3.connect('usage.sqlite')
dbconn = db.cursor()
dbconn.execute('SELECT * FROM computerusage')
fetch = dbconn.fetchall()
for line in fetch:
    minions.append(line[1])
    percentage.append(line[5])

plt.rcdefaults()
fig, ax = plt.subplots()

# Example data

ybar = np.arange(len(minions))

ax.barh(minions, percentage, align='center',color='red', ecolor='black')
ax.set_yticks(ybar)
ax.set_yticklabels(minions)
ax.set(xlim=[0,100])
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Percentage')
ax.set_title('Memory Usage')

plt.show()