import psutil
import time
import socket

class ComputerUsage():
    def __init__(self):
        memorydump = psutil.virtual_memory()
        self.mempercentage = memorydump[2]
        self.cpupercentage = psutil.cpu_percent(interval=0.4,percpu=False)
        self.hostname = socket.gethostname()
        self.stamp = time.time()
        self.disktotal = psutil.disk_usage(".").total
        self.diskusage = psutil.disk_usage(".").used
        self.diskpercent = psutil.disk_usage(".").percent
    def values(self):
        return [self.stamp,self.hostname,self.cpupercentage,self.mempercentage,self.disktotal,self.diskusage,self.diskpercent]

