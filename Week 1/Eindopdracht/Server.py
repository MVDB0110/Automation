import socket
import subprocess
import datetime

HOST = '' # Alle beschikbare interfaces
PORT = 8888 # Willekeurige poort (denk aan firewall bij Windows Systemen)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(10)
    print('> Socket luistert op poort:',PORT)
except:
    print("> Port is in gebruik.")

# Wacht op connecties (blocking)
conn, addr = s.accept()
# Er is een client verbonden met de server
print('> Verbonden met ' + addr[0] + ':' + str(addr[1]))

while True:
    conn.sendall(b'> Geef de presharedkey op: \n')
    conn.sendall(b'> ')
    key = conn.recv(1024)
    key = str(key.decode('ascii')).rstrip()
    if key == 'P@ssw0rd':
        conn.sendall(b'> Succesvol geauthenticeerd. \n')
        break

# De server meldt zich aan de client
conn.sendall(b'> Welkom Op Mijn Server, vertel me iets, dan zeg ik hetzelfde terug:\n')
conn.sendall(b'> ')

while True:
    log = open('logfile.txt', mode='a')

    # Wacht op input van de client en geef deze ook weer terug (echo service)
    data = conn.recv(1024)
    data=str(data.decode('ascii')).rstrip() # # Remove \r | \n | \r\n
    print('> Client data ontvangen: ' + data)

    if data == 'stop':
        print("> Socket is gesloten.")
        conn.close() # Verbreek de verbinding en sluit de socket
        s.close()
        log.close()
        break;

    elif data == "notepad":
        command = "open -a /Applications/TextEdit.app"
        conn.sendall(b"> Open Notepad \n")
        conn.sendall(b'> ')
        log.write(str(datetime.datetime.now()).split(' ')[0] + " " + str(datetime.datetime.now().time()).split('.')[0] + " " + command + "\n")
        subprocess.call(command, shell=True)

    elif data == "calc":
        command = "open -a /Applications/Calculator.app"
        conn.sendall(b"> Open Calculator \n")
        conn.sendall(b'> ')
        log.write(str(datetime.datetime.now()).split(' ')[0] + " " + str(datetime.datetime.now().time()).split('.')[0] + " " + command + "\n")
        subprocess.call(command, shell=True)

    else:
        conn.sendall(b"> Je Stuurde Mij Deze Data: " + data.encode())
        conn.sendall(b'\n')
        conn.sendall(b'> ')