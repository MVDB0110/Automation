import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import configparser
import os

minions = []
mempercent = []
cpupercent = []

config_file = os.path.join(os.path.dirname(__file__), 'server.ini')
config = configparser.ConfigParser()
config.read(config_file)

db_file = config['DATABASE']['DatabaseFile']
db = sqlite3.connect(db_file) # Open SQlite database
dbconn = db.cursor()
dbconn.execute('SELECT * FROM computerusage') # Vraag alle velden uit de tabel computerusage
fetch = dbconn.fetchall()
for line in fetch:
    minions.append(line[1]) # Voeg hostname toe aan minions
    mempercent.append(line[5]) # Voeg percentage geheugengebruik toe aan mempercent
    cpupercent.append(line[2]) # Voeg percentage processorgebruik toe aan cpupercent

plt.rcdefaults()
fig, ax = plt.subplots() # Maak figuur 1

ybar = np.arange(len(minions)) # Vraag getal van objecten over y-as

ax.barh(minions, mempercent, align='center',color='red', ecolor='black') # Zet waarden figuur 1
ax.set_yticks(ybar) # Maak evenveel posities op y-as als objecten in minions
ax.set_yticklabels(minions) # Zet hostnames op y-as
ax.set(xlim=[0,100]) # Zet x-as van 0 tm 100
ax.invert_yaxis()
ax.set_xlabel('Percentage')
ax.set_title('Memory Usage')

plt.savefig('memory.png') # Sla geheugengebruik grafiek op

plt.rcdefaults()
fig2, ax2 = plt.subplots() # Maak figuur 2

ybar = np.arange(len(minions)) # Vraag getal van objecten over y-as

ax2.barh(minions, cpupercent, align='center',color='red', ecolor='black') # Zet gegevens in grafiek
ax2.set_yticks(ybar) # Maak evenveel posities op y-as als objecten in minions
ax2.set_yticklabels(minions) # Zet hostnames op y-as
ax2.set(xlim=[0,100]) # Zet x-as van 0 tm 100
ax2.invert_yaxis()
ax2.set_xlabel('Percentage')
ax2.set_title('CPU Usage')

plt.savefig('cpu.png') # Sla processorgebruik op.