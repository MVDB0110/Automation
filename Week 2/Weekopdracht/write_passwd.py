import hashlib

def write():
    while True:
        password = input("Geef een wachtwoord op: ")
        if len(password) >= 8:
            break
        else:
            print("Geef een wachtwoord op van minimaal 8 karakters")
    hashpasswd = hashlib.new('sha512', password.encode())
    passwdFile = open('passwd.txt', mode='w')
    passwdFile.write(hashpasswd.hexdigest())
    passwdFile.close()