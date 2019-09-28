#!/usr/bin/env python

import socketserver
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        print ('...connected from:', self.client_address)
        str_to_send = '[%s] %s\n' % (
            ctime(), self.rfile.readline().strip().decode('utf-8'))
        self.wfile.write(bytes(str_to_send, 'utf-8'))

tcpSerSock = socketserver.TCPServer(ADDR, MyRequestHandler)
print ('waiting for connection...')
tcpSerSock.serve_forever()
