import rsa
from rsa.key import PublicKey


(public, private) = rsa.newkeys(512)


with open("public.pem",'wb') as f:
    pk = rsa.PublicKey.save_pkcs1(public)
    f.write(pk)

with open("private.pem",'wb') as f:
    pk = rsa.PrivateKey.save_pkcs1(private)
    f.write(pk)


data = "hello".encode('utf-8')

enc = rsa.encrypt(data, public)

print(enc)

dec = rsa.decrypt(enc, private)

print(dec.decode('utf-8'))