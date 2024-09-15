![Chal](https://github.com/user-attachments/assets/bd3d2092-fb10-450b-9308-4fa1ff4e3e2e)

Checking the program's protection, we can see that we can not use `ret2shellcode`, or `buffer overflow` to exploit in this challenge.

![checksec](https://github.com/user-attachments/assets/0aba7291-e371-4a27-85c3-52b7f237ae4f)


So.... how can we solve this challenge? Looking at the `func()`, we can see there's a `format string` vulnerability in `line 26`.

![func()](https://github.com/user-attachments/assets/ab3ebf04-d933-4684-b4b0-667b3f4e8fde)


Also, the program gives us the address of `victory()`, the address of the `buf` variable in the stack and the value of the `return address`. My first question is why the challenge gives us these credentials? After researching for a long time, I realized that we can overwrite the `return address` with the address of `buf` in the stack without overflowing the whole stack :D. First, we have to find the position of the `buf` using the multiple `%x` as the input of the program, this will print the value in the stack, and we can see our input is in the `7th`.

![run1](https://github.com/user-attachments/assets/46ff4cf6-4e4a-4f9e-af87-848dc412a318)


Great!!! What's next, in C, there's a special format string that can change the value in the stack, though we can not see it, and that is `%n`.

![fmtstr_n](https://github.com/user-attachments/assets/3bf2b370-a56c-4c0c-ac83-5509e8718d91)


Using `GDB`, we can see the `buf` is in `ebp-0x8c`, so I draw the stack to easily see:

![disas_func](https://github.com/user-attachments/assets/a6774aee-913b-4ce2-a5f3-5c087eab9a7e)


![stack](https://github.com/user-attachments/assets/4d9ef1ef-f5f3-47ea-afa0-5f6ab1805b4a)


With this, we will understand that the position of the `return address` is in `43th`. Using `%43$lx`, we can see that it has the same value with the return address ;)

![run2](https://github.com/user-attachments/assets/2c3cb01e-2cf9-4b85-b7cb-3b55f7bd6e74)


We can use different way to analyze the position of `return address`, for example we can use `gdb-peda` to observe the whole stack.

![disas_func2](https://github.com/user-attachments/assets/f2efb572-93c5-4ca5-9af6-59603cb418ce)


![disas_func3](https://github.com/user-attachments/assets/69d3a89b-3c2b-47a0-aa38-632a52bf1353)


Or using `radare2`:

![rdare2](https://github.com/user-attachments/assets/f039d1d5-3c49-479e-a1c7-8641c3623120)


We can see the `0xff88b1cc` in the stack is the value of `main()` address.

![rdare2_2](https://github.com/user-attachments/assets/f03d44ce-f7b6-4936-8a01-12443fd9f876)


Almost done here, now how can we overwrite the value of the return address? Welp, there are some values help us to overwrite the value in the stack. In this case, I will use `%x` format to overwrite the hexa value.

![fmtstr_o,u,x,X](https://github.com/user-attachments/assets/4567fb68-eeab-4ec0-9d2b-bb91698e24c7)


Here's my first payload, the `AAAA` is because our stack frame is 4 bytes due to this is `i386` structure, so we have to fulfill the stack frame. First we will calculate the address of `return address` using the address of `buf`, then we will overwrite the address with the `victory()` to get the flag. Easy right?

![payload](https://github.com/user-attachments/assets/5959682e-cd87-43a7-962f-b8ed31be8f37)


But wait.... why my return address is only 2 bytes?

![ret_addr](https://github.com/user-attachments/assets/02057122-9dd0-4940-be3d-0c94b0219ad7)


That's because I'm using the `%n`, it will overwrite whole value of the return address, so I have to find other format string to overwrite only 2 lower bytes. Looking at the table, I will use `%hn`.

![fmtstr_tablr](https://github.com/user-attachments/assets/df6be6e6-0af5-4f60-be40-ddf8ad6c573e)


![payload2](https://github.com/user-attachments/assets/641f6a5a-1bd6-4802-9914-6f81da8773d5)


And we got the flag !!!

![Flag](https://github.com/user-attachments/assets/71ff4983-c8a3-48f8-b7d9-6fd0b00fcdac)
