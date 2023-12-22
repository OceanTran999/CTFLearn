# Challenge 1: pwn simple rip

![Chal1](https://github.com/OceanTran999/CTFLearn/assets/100577019/0651b4ca-e025-44df-85a8-8a0113566268)


The `win()` in this challenge is not in the `main()`, so I have to make this vulnerable program jump to it. Here's the protection.

![Protection1](https://github.com/OceanTran999/CTFLearn/assets/100577019/464f27b1-35bb-4147-a57a-98bdbc0cd80a)


When run in the server, the return address is the red bytes and it is in Little Endian. My stack looks like: 60 bytes `buffer` + 4 bytes `win()`

![run1](https://github.com/OceanTran999/CTFLearn/assets/100577019/2f102182-6599-4fee-9ccb-85f25de645d5)


Finally, we just need the address of `win()` to get the flag.

![win1](https://github.com/OceanTran999/CTFLearn/assets/100577019/6088d154-f601-48fc-842b-b069b200a54a)


# Challenge 2: shell time

![Chal2](https://github.com/OceanTran999/CTFLearn/assets/100577019/c540459e-7e73-49e9-b4fa-1e0d1c5a23f4)


When looking at the challenge, I think it is the easy one :), but nahhh. In the vulnerable program, it does not have the address of `shell()` or `system()`. Looking at the hint, I think `ret2libc` is the way to solve this challenge (although it says that we do not need to ;)). Here's the protection

![Protection2](https://github.com/OceanTran999/CTFLearn/assets/100577019/0d6172ea-0dc4-4893-a5f9-7399852f0905)


Now, we need to find the address of `system()` and the address of string `/bin/sh` for `system("/bin/sh")`. Therefore, to get the address of `puts()` that run in the server program in order to get the version of libc, my payload is: 60 bytes `buffer` + 4 bytes `puts@plt` + 4 bytes `main()` (to run again the function after sending the PLT section) + 4 bytes `puts@got`.
After we get the address of `system()`, search the version of libc in https://libc.blukat.me/, use the `system()` to calculate the address of other function such as `system()`, `/bin/sh`.

![libc_version](https://github.com/OceanTran999/CTFLearn/assets/100577019/e7720613-3224-49ef-8071-5c9a6e4e5d4d)

![Calculate_addr](https://github.com/OceanTran999/CTFLearn/assets/100577019/0132db09-3f85-4427-b1c8-8ef17adee842)


The final step, my payload is: 60 bytes of `buffer` + 4 bytes `system()` + 4 bytes `exit()` + 4 bytes `/bin/sh`. Sending to the server and we will get the flag

![Flag](https://github.com/OceanTran999/CTFLearn/assets/100577019/f2f1c6c6-7067-44a7-a9aa-c2fdcbe4eeff)
