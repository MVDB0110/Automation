import hashlib

def read():
    passwdFile = open('passwd.txt', mode='r')
    password = input("Wat is de geheime sleutel? ")
    hashpasswd = hashlib.new('sha512', password.encode())

    for line in passwdFile:
        if hashpasswd.hexdigest() == line:
            print("Wachtwoord OK")
        else:
            print("Wachtwoord FOUT")
