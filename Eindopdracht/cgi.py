import matplotlib.pyplot as plt
import numpy as np
import sqlite3

minions = []
mempercent = []
cpupercent = []

db = sqlite3.connect('usage.sqlite')
dbconn = db.cursor()
dbconn.execute('SELECT * FROM computerusage')
fetch = dbconn.fetchall()
for line in fetch:
    minions.append(line[1])
    mempercent.append(line[5])
    cpupercent.append(line[2])

plt.rcdefaults()
fig, ax = plt.subplots()

ybar = np.arange(len(minions))

ax.barh(minions, mempercent, align='center',color='red', ecolor='black')
ax.set_yticks(ybar)
ax.set_yticklabels(minions)
ax.set(xlim=[0,100])
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Percentage')
ax.set_title('Memory Usage')

plt.savefig('memory.png')

plt.rcdefaults()
fig2, ax2 = plt.subplots()

ybar = np.arange(len(minions))

ax2.barh(minions, cpupercent, align='center',color='red', ecolor='black')
ax2.set_yticks(ybar)
ax2.set_yticklabels(minions)
ax2.set(xlim=[0,100])
ax2.invert_yaxis()  # labels read top-to-bottom
ax2.set_xlabel('Percentage')
ax2.set_title('CPU Usage')

plt.savefig('cpu.png')