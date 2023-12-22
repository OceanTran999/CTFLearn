![Chal](https://github.com/OceanTran999/CTFLearn/assets/100577019/a17d43cf-8f89-48e7-94d1-afbd5ed1906a)

Here's the protection of vulnerable file

![Protection](https://github.com/OceanTran999/CTFLearn/assets/100577019/c2f35a03-0cbd-42df-bbd9-23f340505b92)


Here's the source code I have:

![Code](https://github.com/OceanTran999/CTFLearn/assets/100577019/ae6385b7-0eb6-463b-94ca-cf5ce04ad57d)


It can be seen that, in `vuln()`, we can utilize format string due to `printf(buf)`. Let's run the file.

![Run](https://github.com/OceanTran999/CTFLearn/assets/100577019/f0548057-37e1-4d23-9309-dbdb930f54d2)


The 11th %p is the address of `main()`, which also the return address of the `vuln()`. Next, I will `disassemble vuln`. In the `xor` and `mv`, I think that might be the address of Canary/Cookie value, which is in `rbp-0x8`. Before juming to the `main()`, the Canary/Cookies value will save to the RAX register, and check if the value is correct, if not, the program will be crashed.

![rbp-0x8_XOR](https://github.com/OceanTran999/CTFLearn/assets/100577019/54159da0-5bdb-4dc4-b081-c3d4568fe94d)


![rbp-0x8_je](https://github.com/OceanTran999/CTFLearn/assets/100577019/d9390748-35b4-4389-88d9-c0c3cb4dce32)


I will use GDB Debugger to set the breakpoint on `printf()` after the first `gets()` and address `0x401324` in `vuln()`.

![breakpoint](https://github.com/OceanTran999/CTFLearn/assets/100577019/85de8098-07ba-4278-adbb-0c8858d29ec0)


Great!!! Now we can see the return address of `vuln()` in `main()`.

![main_retaddr](https://github.com/OceanTran999/CTFLearn/assets/100577019/4394afbf-cbef-4f79-8962-74f30e1f1bd6)


Jumping to `0x401324`, I get RAX register's value.

![rax1](https://github.com/OceanTran999/CTFLearn/assets/100577019/3f3e33ec-79cd-440d-9ee2-c892752a1019)

We know that the offset of `buf` is 24 and the canary is in the position 9th in stack. Now we will debug again with the input is `%9$lx`:

![breakpoint_2](https://github.com/OceanTran999/CTFLearn/assets/100577019/1779e176-5cda-4d1e-8447-29c2a9c04516)


And we will see the value of `buf` and RAX register are same.

![rax2](https://github.com/OceanTran999/CTFLearn/assets/100577019/457d29fd-4d8e-4cc2-9b12-b37f92a1de42)

![equal_rax2](https://github.com/OceanTran999/CTFLearn/assets/100577019/127449f0-a27c-4cff-af45-94d017c29487)


Finally, we just need the address of `print_flag()`

![addr_print_flag()](https://github.com/OceanTran999/CTFLearn/assets/100577019/c6b6dff6-c618-4420-86ee-ab94acf62712)


# Stack
I will have stack for this challenge.

![stack](https://github.com/OceanTran999/CTFLearn/assets/100577019/c03f2a7d-e26c-40e1-b7c8-a300444c097f)


However, it works in local version, when I submit to server, I can't get the flag. Therefore I choose different address to jump to, which is `0x40121B`. And I finally get the flag.

![IDA_Pro](https://github.com/OceanTran999/CTFLearn/assets/100577019/0e4f6b76-d69a-4e04-b95e-333a7e3a55c4)


![Flag](https://github.com/OceanTran999/CTFLearn/assets/100577019/8ff63582-732c-432d-95cf-dd595338f452)
