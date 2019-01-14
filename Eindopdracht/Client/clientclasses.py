import psutil
import time
import socket

class ComputerUsage():
    def __init__(self):
        memorydump = psutil.virtual_memory() # Vraag memory gegevens op
        self.mempercentage = memorydump[2] # Vraag percentage van het memory dat in gebruik is
        self.cpupercentage = psutil.cpu_percent(interval=0.9,percpu=False) # Vraag het percentage van de gehele CPU over een interval van 0.4
        self.hostname = socket.gethostname() # Vraag hostname van de minion op
        self.stamp = time.time() # Vraag timestamp op
        self.disktotal = psutil.disk_usage(".").total # Vraag het totale schijf volume op
        self.diskusage = psutil.disk_usage(".").used # Vraag het gerbuikte schijf volume op
        self.diskpercent = psutil.disk_usage(".").percent # Vraag het percentage hiervan op
    def values(self):
        return [self.stamp,self.hostname,self.cpupercentage,self.mempercentage,self.disktotal,self.diskusage,self.diskpercent]

