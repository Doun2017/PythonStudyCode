#!/usr/bin/env python

from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(bytes(data+'\n', 'utf-8'))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print (data)
    tcpCliSock.close()
