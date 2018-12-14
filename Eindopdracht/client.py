from clientclasses import *
import time
import socket
import sys
import json

# Source 1: www.pythonprogramminglanguage.com

host = 'localhost'
port = 8891

# create socket
print('> Creating socket\n')
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('> Failed to create socket\n')
    sys.exit()

# Connect to remote server
print('> Connecting to server, ' + host + '\n')
try:
    s.connect((host, port))
    print("> Connected to",str(host),str(port))
except:
    print("> Cannot connect to server")

while True:
    try:
        x = ComputerUsage()
        s.send(json.dumps(x.values()).encode('ascii'))
        time.sleep(10)
    except socket.error:
        print('> Send failed\n')
        sys.exit()