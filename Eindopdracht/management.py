import socket
from _thread import start_new_thread
import json
import sqlite3

def new_host(csocket,addr):
    print('> Verbonden met ' + addr[0] + ':' + str(addr[1]))
    while True:
        db = sqlite3.connect('usage.sqlite')
        dbconn = db.cursor()
        data = conn.recv(1024)
        try:
            data = json.loads(data.decode('ascii'))
        except:
            break;

        dbconn.execute('DELETE FROM computerusage WHERE hostname=?',(str(data[1]),))
        dbconn.execute('INSERT INTO computerusage VALUES(?,?,?,?,?,?)', (data[0],str(data[1]),data[2],data[3],data[4],data[5]))
        db.commit()
        db.close()
    csocket.close()

HOST = '' # Alle beschikbare interfaces
PORT = 8888 # Willekeurige poort (denk aan firewall bij Windows Systemen)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(10)
    print('> Socket luistert op poort:',PORT)
except:
    print("> Port is in gebruik.")

db = sqlite3.connect('usage.sqlite')
dbconn = db.cursor()
dbconn.execute('CREATE TABLE IF NOT EXISTS computerusage (stamp REAL,hostname VARCHAR(30),cpercent REAL,mtotal REAL,musage REAL,mpercent REAL);')
db.commit()
db.close()

while True:
    # Wacht op connecties (blocking)
    conn, addr = s.accept()
    start_new_thread(new_host,(conn,addr))

