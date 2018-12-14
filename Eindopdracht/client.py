from clientclasses import ComputerUsage
import time
import socket
import sys
import json

# Source 1: www.pythonprogramminglanguage.com

host = 'localhost'
port = 8888

# create socket
print('> Creating socket')
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('> Failed to create socket')
    sys.exit()

# Connect to remote server
print('> Connecting to server, ' + host)
try:
    s.connect((host, port))
    print("> Connected to",str(host),str(port))
except:
    print("> Cannot connect to server")
    sys.exit()

while True:
    try:
        x = ComputerUsage()
        s.send(json.dumps(x.values()).encode('ascii'))
        time.sleep(10)
    except socket.error:
        print('> Send failed')
        sys.exit()