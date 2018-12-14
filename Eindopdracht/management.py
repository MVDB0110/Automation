import socket
from _thread import start_new_thread
import json

def new_host(csocket,addr):
    print('> Verbonden met ' + addr[0] + ':' + str(addr[1]))
    while True:
        file = open('usage.txt','a')
        data = conn.recv(1024)
        try:
            data = json.loads(data.decode('ascii'))
        except:
            break;
        file.write(str(data[0])+';'+str(data[1])+';'+str(data[2])+';'+str(data[3])+';'+str(data[4])+';'+str(data[5])+'\n')
        file.close()

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

while True:
    # Wacht op connecties (blocking)
    conn, addr = s.accept()
    start_new_thread(new_host,(conn,addr))

