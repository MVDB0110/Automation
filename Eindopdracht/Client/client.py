import time
import socket
import sys
import json
import configparser
import os
if os.name == 'posix': # Unix/Linux
    from clientclasses import ComputerUsage
if os.name == 'nt': # Windows
    import subprocess
    import psutil

# Source 1: www.pythonprogramminglanguage.com

config_file = os.path.join(os.path.dirname(__file__), 'client.ini') # Configfile
config = configparser.ConfigParser() # Configparser aanmaken
config.read(config_file) # Lees config

# Zet waarden uit logfile in variabele
host = config['GENERAL']['IP']
port = config['GENERAL']['Port']
scriptloc = config['WINDOWS']['ScriptLocation']

print('> Creating socket')
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Probeer socket te maken
except socket.error as se:
    print('> Failed to create socket', se)
    sys.exit() # Stop script bij exception

print('> Connecting to server, ' + host)
try:
    s.connect((host, int(port))) # Probeer met server verbinding te maken.
    print("> Connected to",str(host),str(port))
except socket.error as se:
    print("> Cannot connect to server\n", se)
    sys.exit()

while True:
    if os.name == 'posix':
        try:
            x = ComputerUsage() # Roep class aan
            s.send(json.dumps(x.values()).encode('ascii')) # Maak een Json dump en codeer deze in ascii
            time.sleep(10) # Wacht tien seconden
        except socket.error:
            print('> Send failed')
            sys.exit()
    if os.name == 'nt':
        try:
            pwsh = subprocess.Popen(['powershell.exe','-ExecutionPolicy','Unrestricted',scriptloc],stdout=subprocess.PIPE)
            output = pwsh.stdout.read()
        except:
            print("> Powershell script niet gevonden.")
        output = output.decode() # output komt gecodeerd binnen.
        output = output.splitlines() # output bestaat uit 5 regels waarvan 2 bruikbaar
        usage = [time.time(),socket.gethostname(),output[1],output[4],psutil.disk_usage(".").total,psutil.disk_usage(".").used,psutil.disk_usage(".").percent] # list maken van verschillende informatie
        try:
            s.send(json.dumps(output).encode('ascii'))  # Maak een Json dump en codeer deze in ascii
        except: # Als json niet gedumpt kan worden is er een send failed. Dan verbreekt de server de verbinding.
            print("> Send failed")
        time.sleep(10)  # Wacht tien seconden