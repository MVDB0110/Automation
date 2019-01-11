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
    def values(self):
        return [self.stamp,self.hostname,self.cpupercentage,self.mempercentage]

