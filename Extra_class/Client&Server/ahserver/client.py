import socket
import rsa
with open("public.pem","rb") as f:
    pk = f.read()
    public_key = rsa.PublicKey.load_pkcs1(pk)

host = '192.168.1.43'
port = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect( (host,port) )

while True:

    user_input =  str(input())
    if not user_input:
        break
    user_input =  user_input.encode('utf-8')
    enc = rsa.encrypt(user_input, public_key)

    s.sendall(enc)