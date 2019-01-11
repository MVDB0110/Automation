import socket
from _thread import start_new_thread
import json
import sqlite3
import configparser
import os
import logging

def new_host(csocket,addr):
    print('> Verbonden met ' + str(addr[0]) + ':' + str(addr[1]))
    logger.info('Verbonden met: '+str(addr[0])+':'+str(addr[1]))
    while True:
        db = sqlite3.connect(db_file) # Verbindt met database
        dbconn = db.cursor()
        data = conn.recv(1024) # Ontvang data
        try: # Probeer data te decoderen en daarna te loaden met JSON
            data = json.loads(data.decode('ascii'))
        except: # Als de data niet te importeren is met JSON verbreek verbinding
            break;

        dbconn.execute('DELETE FROM computerusage WHERE hostname=?',(str(data[1]),)) # Haal eerdere data van deze host uit de database
        dbconn.execute('INSERT INTO computerusage VALUES(?,?,?,?,?,?,?)', (data[0],str(data[1]),data[2],data[3],data[4],data[5],data[6])) # Voeg daarna de nieuwe regel toe
        db.commit() # Maak de aanpassingen
        db.close()
    csocket.close() # Sluit verbinding
    logger.info('Client: '+str(addr[0])+":"+str(addr[1])+' heeft de verbinding verbroken.')

config_file = os.path.join(os.path.dirname(__file__), 'server.ini')
config = configparser.ConfigParser()
config.read(config_file)

if config['GENERAL']['IP'] == 'All':
    host = '' # Alle beschikbare interfaces
else:
    host = config['GENERAL']['IP'] # IP/Hostname van config

port = config['GENERAL']['Port'] # Poort van config

db_file = config['DATABASE']['DatabaseFile']

logger = logging.getLogger(__name__) # Initieer logsysteem
logger.setLevel(logging.INFO) # Zet log level op INFO
logfile = logging.FileHandler(os.path.join(os.path.dirname(__file__), 'management.log')) # Geef de logfile aan
format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') # Geef het format aan
logfile.setFormatter(format) # Geef het format aan de formatter
logger.addHandler(logfile) # Handler aanmaken voor logfile
logger.info('Daemon geinitialiseerd')

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Maak TCP socket
    s.bind((host, int(port))) # Probeer te luisteren op poort
    s.listen(10)
    print('> Socket luistert op poort: ' + str(port))
    logger.info('Daemon luistert op: '+str(port))
except socket.error as se:
    print("> Port is in gebruik.", se)
    logger.error("Port is in gebruik."+se)

db = sqlite3.connect(db_file) # Open database usage
dbconn = db.cursor()
dbconn.execute('CREATE TABLE IF NOT EXISTS computerusage (stamp REAL,hostname VARCHAR(30),cpercent REAL,mpercent REAL,disktotal REAL,diskusage REAL,diskpercent);') # Creeer tabel als hij niet bestaat
db.commit() # Maak aanpassingen
db.close() # Sluit database

while True:
    conn, addr = s.accept() # Wacht op connecties
    start_new_thread(new_host,(conn,addr)) # Voor elke client een nieuwe thread aanmaken

