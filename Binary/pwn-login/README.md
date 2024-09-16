This challenge is very good that it takes more than an hour for me to learn new thing :D. First, here's program protection.

![chall](https://github.com/user-attachments/assets/0795d781-f6a7-4e5d-940b-5decc2d59a7f)


Let's analysis the program:
- The `login` using `malloc()` to create a user with a pointer called `curr` and save the its data on the heap.
- The `sign_out` will `free()` the user's data on the heap. However, it does not reset all the user's data.
- `print_flag` will give you the real flag if you are **admin(admin != 0)**, otherwise it will gives the `fake_flag`.
- `Lock_user` will backup the pointer `curr` with another pointer called `save`.
- `Restore_user` will use the backup pointer `save` to the `curr` and change the value `save` to **NULL**.

So, I use `gdb-peda` and see that the `Username` is saved at `0x5555556032a8`.

![gdb1](https://github.com/user-attachments/assets/d165a5dc-2ffe-4664-ab03-cabc879d1924)


Next, I will `free()` the current user, looking at the memory again, it seems that the first 8 bytes only freed.

![sign_out](https://github.com/user-attachments/assets/d204b23f-500d-4c94-a2f1-af13b77e2f74)


In the `print_flag()`, there's a `strdup()` function, checking the `man page`, I understand that it will return a pointer to a new `fake_flag` string, also, it will save this string in the heap thanks to the `malloc()`.

![strdup](https://github.com/user-attachments/assets/46c0767f-79fa-401d-8b10-75f0de6c81a7)

 
To easy understand, let's input the fake flag with `DDDDDDDDEEEEEEEEFFFFFFFF` and check the heap memory again.

![fakeflag1](https://github.com/user-attachments/assets/2da7e267-205e-41d2-9fa1-3b54493537c6)


It seems it's located at `0x5555556032e0` on the heap. Hmmmmm... so, if my length of fake flag is equal to the `curr`'s, I can make a `Use After Free(UAF)` Attack, right?

![fake_flag2](https://github.com/user-attachments/assets/8139e24e-bb01-46f4-9461-37c13ad2c1a5)


And yes, the program really has the `UAF` vulnerability, so, I can create a fake flag with its size between `32-40`, I will overwrite the value in the `curr`.

![fake_flag3](https://github.com/user-attachments/assets/834a158e-676d-4383-a1d6-974c47c58a9b)


But, butttt, we're not done yet. The program will check if the `curr != NULL` to give the real flag, but we already signed out, what should we do? Welp, we can `lock()` the current user before `sign_out`, and `restore()` after giving the fake flag. Call `print_flag()` once again and we will get the real flag :D

![flag](https://github.com/user-attachments/assets/b8e8bdf0-1e3a-484b-8761-1b472c85cdd0)
