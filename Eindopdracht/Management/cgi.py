#!/usr/bin/python3

import cgi
import cgitb
import sqlite3
import configparser
import os
import logging
import time
from cgiclasses import HorizontalBar

print("Content-type: text/html\n")

cgitb.enable()

logger = logging.getLogger(__name__) # Initieer logsysteem
logger.setLevel(logging.INFO) # Log alles boven en gelijk aan INFO
logfile = logging.FileHandler(os.path.join(os.path.dirname(__file__), 'cgi.log')) # Zet het in Log file cgi.log
format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') # Formatteer het op deze wijze
logfile.setFormatter(format) # Geef het format dat net gemaakt is aan
logger.addHandler(logfile) # Handler aanmaken voor logfile

minions = []
mempercent = []
cpupercent = []
diskpercent = []
htmlList = []

config_file = os.path.join(os.path.dirname(__file__), 'server.ini')
config = configparser.ConfigParser()
config.read(config_file)

db_file = config['DATABASE']['DatabaseFile']

try:
    db = sqlite3.connect(db_file) # Open SQlite database
    dbconn = db.cursor()
except:
    logger.error('Database bestand bestaat niet of kan niet worden gelezen.')

dbconn.execute('SELECT * FROM computerusage') # Vraag alle velden uit de tabel computerusage
fetch = dbconn.fetchall()
for line in fetch:
    minions.append(line[1]) # Voeg hostname toe aan minions
    mempercent.append(line[3]) # Voeg percentage geheugengebruik toe aan mempercent
    cpupercent.append(line[2]) # Voeg percentage processorgebruik toe aan cpupercent
    diskpercent.append(line[6]) # Voeg percentage hardeschijf toe aan diskpercent
    htmlList.append((line[0],line[1],line[2],line[3],round(line[4]/1024**3,2),round(line[5]/1024**3,2))) # Maak de lijst met alle minion informatie in de tabel later

cpu = HorizontalBar('CPU Usage','Percentage',minions,cpupercent,'red') # Maak horizontal bar
memory = HorizontalBar('Memory Usage','Percentage',minions,mempercent,'red') # Maak horizontal bar
disk = HorizontalBar('Disk Usage','Percentage',minions,diskpercent,'red') # Maak horizontal bar

cpu.plotPNG('cpu.png') # Sla processor plaatje op
memory.plotPNG('memory.png') # Sla processor plaatje op
disk.plotPNG('disk.png') # Sla processor plaatje op

print("<html>\n")
print("<header>\n")
print("<title>Management Website Tim en Mike</title>\n")
print("</header>\n")
print("<body>\n")
print("<div width='100%' align='center'><h1>Management Website</h1></div>\n")
print("<div align='center'>\n")
print("<img src='memory.png'>\n")
print("<img src='cpu.png'>\n")
print("<img src='disk.png'>\n")
print("</div>\n")
print("<table align='center' border='1'>\n")
print("<tr>\n")
print("<td align ='center'>Minion</td><td align ='center'>CPU usage</td><td align ='center'>Memory Usage</td><td align ='center'>Diskspace Total</td><td align ='center'>Diskspace In Use</td><td align ='center'>Date & Time</td>\n")
print("</tr>\n")
for minion in htmlList:
    if int(minion[2]) > 89: # Is CPU percentage over de 89? Dan wordt de kleur rood
        ccolor='#FF0000' # Rood
    else: # Anders groen
        ccolor='#00FF00' # Groen
    if int(minion[3]) > 89: # Is Memory percentage over de 89? Dan wordt de kleur rood
        mcolor='#FF0000' # Rood
    else: # Anders groen
        mcolor='#00FF00' # Groen
    print("<tr>\n")
    print("<td align ='center'>"+str(minion[1])+"</td><td bgcolor='"+ccolor+"' align ='center'>"+str(round(minion[2]))+"</td><td bgcolor='"+mcolor+"' align ='center'>"+str(round(minion[3]))+"</td><td align ='center'>"+str(minion[4])+"GB</td><td align ='center'>"+str(minion[5])+"GB</td><td align ='center'>"+str(time.ctime(minion[0]))+"</td>\n")
    print("</tr>\n")
print("</table>\n")
print("</body>\n")
print("</html>")
