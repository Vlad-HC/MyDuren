import socket

ss = socket.socket()
HOST = '127.0.0.1'
name = input("Print your name")
ss.connect((HOST,10000))
ss.send(name.encode())
sn = ss.recv(1024)
sn = sn.decode()
print(sn ,':', 'join')

while True:
    mess:str
    mess = (ss.recv(1024)).decode()
    print(sn,":", mess)
    mess = input('Im')
    mess = mess.decode()
    ss.send(mess.encode())