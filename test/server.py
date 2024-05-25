import socket


HOST = '127.0.0.1'
PORT = 10000
ns = socket.socket()
ns.bind((HOST,PORT))
ns.listen()
print('Server is working')
name = input('Print your name')

conn, add = ns.accept()

client = (conn.recv(1024)).decode()
print(client + 'join!')
conn.send(name.encode())

while True:
    mess = input('Im')
    conn.send(mess.encode())
    mess = conn.recv(1024)
    mess = mess.decode()
    print(client, ":", mess)
