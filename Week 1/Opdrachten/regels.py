file = open('regels.txt', mode='r')
i=0
for line in file:
    i+=1
    print(str(i) + " " + line)