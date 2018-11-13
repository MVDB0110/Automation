import datetime

time = str(datetime.datetime.now().time()).split('.')[0]
date = str(datetime.datetime.now()).split(' ')[0]
print(date + " " + time)