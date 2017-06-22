#!/usr/bin/env python
from socket import *
#from server import  PORT, BUFSIZ

HOST ="127.0.0.1"
PORT = 8010
BUFSIZ = 1024
ADDR =(HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)
while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data.encode('utf-8'))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))
tcpCliSock.close()
