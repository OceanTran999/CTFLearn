![Challenge](https://github.com/OceanTran999/CTFLearn/assets/100577019/9cadfee0-39b8-4c8b-a238-a9fd342c948c)

![source](https://github.com/OceanTran999/CTFLearn/assets/100577019/9803296f-b3ee-4ebd-9003-5248e37230fe)

![Protection](https://github.com/OceanTran999/CTFLearn/assets/100577019/33ca6ff5-f9f2-4ad9-92cf-97d9ef6acb80)


In this challenge, we can see that the NX is enabled, means that we can't execute in the stack. Also, the challenge does not provide the `shell()` or `system()` to help us jump to obtain the shell. Therefore, we have to find a way to get it, and I will use Return Oriented Programming (ROP) to solve this.
First, we need to find the offset, I'll use `pattern_create` and `pattern_offset` of Metasploit to calculate offset.

![pattern_create](https://github.com/OceanTran999/CTFLearn/assets/100577019/88e9ff8f-faa1-4660-94c4-565b7d818d5f)

![disas_ask](https://github.com/OceanTran999/CTFLearn/assets/100577019/b7e23ae9-0d16-4664-a08f-98bda4020a50)


We can see, in top of the stack will have the value `Aa8A`, I will calculate it to know the offset.

![pattern_offset](https://github.com/OceanTran999/CTFLearn/assets/100577019/6f09d1b6-b9ab-4725-80dc-f03c02ed06ce)


Great!!! We know the offset. Now, what's next? Before we continue, we have to know what's ROP first.
- ROP (Return Oriented Programming) is the exploitation technique that allows attacker executes code to bypass NX (No-eXcutable) protection. In this techniquem attacker can gain the control to call stack so as to hijack the program control flow and execute machine instruction sequences which are available in memory, also called **gadget**, each **gadget** typically end with `ret` instruction (https://en.wikipedia.org/wiki/Return-oriented_programming).
- Why we use ROP? Welp, because we can not gain the shell as the challenge doesn't give us the function like `system()`. `shell()`, we have to call these function in C standard library or shared library in Linux aka libc. Therefore, to know the address of these function, we have to determine the version of libc that remote server uses first, and ROP will help us to fulfill. To get the libc version, we need to leak the address in GOT (Global Offset Table) which contains the correct address of functions that called in libc. Now, I'll give example to easy understand how ROP works.

Assuming that we have the address of gadget `pop rdi;ret;` is `0xabcdef` and we have a stack look like

![stack1](https://github.com/OceanTran999/CTFLearn/assets/100577019/a3f5f872-50d3-41db-8d9e-923f697434b3)


To let the program run the gadget, we need to make the return address point to the address of this gadget.

![stack2](https://github.com/OceanTran999/CTFLearn/assets/100577019/3061a462-5221-434d-9b3d-3842e67fb998)


When the `ask()` is done, the `$rsp` keeps going up (-4 or -8 bytes) to execute each code in gadget, for example the `pop rdi` means that it will save `AAAA` value to the `rdi` register.

![stack3](https://github.com/OceanTran999/CTFLearn/assets/100577019/ffa57d85-37c0-45f0-886d-8cdd2e7fb81f)


Finally, it will call `main()` thanks to `ret` instruction.

![stack4](https://github.com/OceanTran999/CTFLearn/assets/100577019/dd5354ee-04bb-492e-95d2-c8a6a269819e)


Ok. Now let's started! I will find the address of gadget and hope I will find the simplest one. I will use [ROPgadget](https://github.com/JonathanSalwan/ROPgadget) tool.

![debug1](https://github.com/OceanTran999/CTFLearn/assets/100577019/5c26d9e4-eac4-4007-bb79-fe2c1f65d597)


Noice :) I got the address of `pop rdi; ret` gadget.

![ROPgadget](https://github.com/OceanTran999/CTFLearn/assets/100577019/14223140-0fb6-4479-ba9c-4b97754fc154)


Here's my payload look likes:

>  offset + pop_rdi + GOT_address_of_function + puts@plt + main()

- pop_rdi: the gadget we found
- GOT_address_of_function: the address of function we need in GOT to get the version of libc in remote server.
- puts@plt: To call the `puts()` so we can see the address of GOT function, we can use other function such as `printf()`, etc to show the output and leak the address. We will call it in PLT section (use GDB to see the address).
- main(): exploit the vulnerable program again

We need to find at least 2 address for recognizing the libc version, I will use the address of `read()` and `puts()` in this challenge.

![leak](https://github.com/OceanTran999/CTFLearn/assets/100577019/ad75cde5-a15a-4b12-9151-1a5dd183ebda)


Yummy!!! Now I will use this address to find the libc version in https://libc.blukat.me/.

![libc_version](https://github.com/OceanTran999/CTFLearn/assets/100577019/cdaa763e-d7f1-4462-9d86-3fe74a2eddfe)


Since we know the libc address, we will easily calculate the address of `system()` and `/bin/sh` string to call `system("/bin/sh")` in order to gain the shell and get the flag.

![Flag](https://github.com/OceanTran999/CTFLearn/assets/100577019/6f1acc4d-8de9-49af-9ec8-122c8eef5900)
