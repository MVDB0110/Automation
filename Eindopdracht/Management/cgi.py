#!/usr/bin/python3

import cgi
import cgitb
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import configparser
import os
import logging
from cgiclasses import HorizontalBar

print("Content-type: text/html\n")

cgitb.enable()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logfile = logging.FileHandler(os.path.join(os.path.dirname(__file__), 'cgi.log'))
format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logfile.setFormatter(format)
logger.addHandler(logfile)

minions = []
mempercent = []
cpupercent = []

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

cpu = HorizontalBar('CPU Usage','Percentage',minions,cpupercent,'red')
memory = HorizontalBar('Memory Usage','Percentage',minions,mempercent,'red')

cpu.plotPNG('cpu.png')
memory.plotPNG('memory.png')

print("<html>\n")
print("<header>\n")
print("<title>Management Website Tim en Mike</title>\n")
print("</header>\n")
print("<body>\n")
print("<div width='100%' align='center'><h1>Management Website</h1></div>\n")
print("<div align='center'>\n")
print("<img src='memory.png'>\n")
print("<img src='cpu.png'>\n")
print("</div>\n")
print("</body>\n")
print("</html>")
