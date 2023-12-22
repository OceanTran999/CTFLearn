![Code](https://github.com/OceanTran999/CTFLearn/assets/100577019/d7d3a0f9-1bdf-4cc2-a84e-bf58dbf560a4)


In this challenge, the `vuln()` is in the `main()`, so we do not have to overwrite this function. And this challenge must run in the server to solve.

![Input](https://github.com/OceanTran999/CTFLearn/assets/100577019/3d673aaa-1a5c-444d-b45d-1360a7dfeef8)


We can see that, the return address is the red one, which is `0xdeadbeef`, we just change this address to the `win()` to get the flag. Here's the stack: 48 bytes `buff` + 4 bytes `win()`

![Flag](https://github.com/OceanTran999/CTFLearn/assets/100577019/ffe87b68-51a5-459c-b9f3-f590bae37332)
