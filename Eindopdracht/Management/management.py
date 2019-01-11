import socket
from _thread import start_new_thread
import json
import sqlite3
import configparser
import os
import syslog

def new_host(csocket,addr):
    print('> Verbonden met ' + str(addr[0]) + ':' + str(addr[1]))
    syslog.syslog(syslog.LOG_INFO, 'Verbonden met: '+str(addr[0])+':'+str(addr[1]))
    while True:
        db = sqlite3.connect(db_file)
        dbconn = db.cursor()
        data = conn.recv(1024)
        try: # Probeer data te decoderen en daarna te loaden met JSON
            data = json.loads(data.decode('ascii'))
        except: # Als de data niet te importeren is met JSON verbreek verbinding
            break;

        dbconn.execute('DELETE FROM computerusage WHERE hostname=?',(str(data[1]),)) # Haal eerdere data van deze host uit de database
        dbconn.execute('INSERT INTO computerusage VALUES(?,?,?,?,?,?)', (data[0],str(data[1]),data[2],data[3],data[4],data[5])) # Voeg daarna de nieuwe regel toe
        db.commit() # Maak de aanpassingen
        db.close()
    csocket.close() # Sluit verbinding
    syslog.syslog(syslog.LOG_INFO,'Verbinding verbroken met: '+str(addr[0])+':'+str(addr[1]))

config_file = os.path.join(os.path.dirname(__file__), 'server.ini')
config = configparser.ConfigParser()
config.read(config_file)

if config['GENERAL']['IP'] == 'All':
    host = '' # Alle beschikbare interfaces
else:
    host = config['GENERAL']['IP'] # IP/Hostname van config

port = config['GENERAL']['Port'] # Poort van config

db_file = config['DATABASE']['DatabaseFile']

syslog.openlog(logoption=syslog.LOG_PID, facility=syslog.LOG_DAEMON)
syslog.syslog(syslog.INFO,'Daemon geinitialiseerd.')

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Maak TCP socket
    s.bind((host, int(port))) # Probeer te luisteren op poort
    s.listen(10)
    print('> Socket luistert op poort: ' + str(port))
    syslog.syslog(syslog.LOG_INFO,'Daemon luistert op: '+str(port))
except socket.error as se:
    print("> Port is in gebruik.", se)
    syslog.syslog(syslog.LOG_ERR, "Port is in gebruik."+se)

db = sqlite3.connect(db_file) # Open database usage
dbconn = db.cursor()
dbconn.execute('CREATE TABLE IF NOT EXISTS computerusage (stamp REAL,hostname VARCHAR(30),cpercent REAL,mtotal REAL,musage REAL,mpercent REAL);') # Creeer tabel als hij niet bestaat
db.commit() # Maak aanpassingen
db.close() # Sluit database

while True:
    conn, addr = s.accept() # Wacht op connecties
    start_new_thread(new_host,(conn,addr)) # Voor elke client een nieuwe thread aanmaken

