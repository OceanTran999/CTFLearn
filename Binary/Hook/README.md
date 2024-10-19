![Chall](https://github.com/user-attachments/assets/4cc8101e-7991-4049-a5f8-5a8d9a6f7fe7)


At first, I thought that I can overwrite all the functions in `libc`, but I forgot that the program has the `Full RELRO`, which all the `GOT` will only has the `READ-ONLY` permission.

![checksec](https://github.com/user-attachments/assets/92deecce-067a-44ff-a97e-a0ae0e93c56f)


So, no `win()`, can not overwriting `GOT`, what should we do? Welp, reading the challenge, I see the `hook` keyword so I decide to search Google for this exploit, and I understand that there's an vulnerability for `GLIBC-2.31` that you can overwrite the `__malloc_hook()`, `__free_hook()` and `__realloc_hook()` which are used for debugging program for dynammic memory allocation. Using `manpage` to see these functions:

![man_hook](https://github.com/user-attachments/assets/5d96c16b-9230-4e3e-86af-7e1d00fae840)


Now we know the vulnerability, so what's next? I see that the program has `UAF` vulnerability because users can interact with freed chunks. Therefore, we can calculate these `hook()` functions due to giving `puts()`, to overwrite the address of the `next_chunk` and `malloc()` again to get that address, right? But in this writeup I am doing a `Double-Free` to get the shell in the target server.
First, I will `malloc()` and `free()` 2 chunks, then using `gdb-pwndbg` to check the freed `tcache_chunks`.

![gdb1](https://github.com/user-attachments/assets/d7394cee-3e2c-48a1-a313-7fc012976848)


Then, I will overwrite the `tcache's key`, which is used to check the `double-free` attack.

![gdb2](https://github.com/user-attachments/assets/c754e92c-696e-4edb-82ea-153fb9e55aa6)


`free()` again, and I just made `double-free` attack successfully. You can see the `tcache->count` is `3` while the `tcache_chunk` array only has 1 element `0x55555555b2c0` and it points to itself LOL XD.

![gdb3](https://github.com/user-attachments/assets/b5390fc2-e6fd-4823-8ac6-a9d24e1552f0)


Next, I will `malloc()` with the input is the address of `__free_hook()`, the chunk will `malloc()` and `free()` simultaneously, which you can see the `__free_hook()` is in the `tcache_chunk` now. Also, We have to `malloc()` again for the `0x55f121cc32c0`address, in this address you can set the `/bin/sh` string.

![gdb4](https://github.com/user-attachments/assets/ede2b507-00c5-41e1-92f7-5e1e1afd8a56)


Now the tcache's entry are pointing to the address of `__free_hook()`.

![gdb5](https://github.com/user-attachments/assets/2ef7a116-750f-4377-9c4b-3bee0be0e3f3)


I will `malloc()` again with input is `OOOOOOOO`.

![test_overwrite](https://github.com/user-attachments/assets/68f672c0-ea3f-40de-8e3b-6a6cf8dc706d)


And yeah, I finally did it. So we just overwrite this address with `system()`, and `free()` the chunk that has `/bin/sh` string, and we will get the shell.

![gdb6_Resultoverwrite](https://github.com/user-attachments/assets/f33a0821-45b9-49ca-8234-fd151636752b)


![Flag](https://github.com/user-attachments/assets/9ff09287-5244-49ef-8f34-427c1f3d803d)

# References:
- https://blog.quarkslab.com/heap-exploitation-glibc-internals-and-nifty-tricks.html
- https://adamgold.github.io/posts/basic-heap-exploitation-house-of-force/
