from cryptography.fernet import Fernet

def keygen(r):
    cp=[]
    for i in range(r):
        key = Fernet.generate_key()
        cp[i]=key[2:]
    return cp

#file = open('key.key', 'wb')
#file.write(key)
#file.close()
