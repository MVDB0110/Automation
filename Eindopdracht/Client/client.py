from clientclasses import ComputerUsage
import time
import socket
import sys
import json
import configparser
import os

# Source 1: www.pythonprogramminglanguage.com

config_file = os.path.join(os.path.dirname(__file__), 'client.ini')
config = configparser.ConfigParser()
config.read(config_file)

host = config['GENERAL']['IP']
port = config['GENERAL']['Port']

print('> Creating socket')
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Probeer socket te maken
except socket.error:
    print('> Failed to create socket')
    sys.exit() # Stop script bij exception

print('> Connecting to server, ' + host)
try:
    s.connect((host, port)) # Probeer met server verbinding te maken.
    print("> Connected to",str(host),str(port))
except:
    print("> Cannot connect to server")
    sys.exit()

while True:
    try:
        x = ComputerUsage() # Roep class aan
        s.send(json.dumps(x.values()).encode('ascii')) # Maak een Json dump en codeer deze in ascii
        time.sleep(10) # Wacht tien seconden
    except socket.error:
        print('> Send failed')
        sys.exit()