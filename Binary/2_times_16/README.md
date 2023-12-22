![Chall](https://github.com/OceanTran999/CTFLearn/assets/100577019/dd5b76b7-11aa-43df-a661-e173a62434ef)


Here's file's protection

![Protection](https://github.com/OceanTran999/CTFLearn/assets/100577019/f6dc34b4-0a35-47f0-b958-4275954fb5dd)


`vuln()` and `main()`

![vuln_main](https://github.com/OceanTran999/CTFLearn/assets/100577019/1aa905a5-97eb-482a-b44a-3c791512a437)


`print_flag()`

![print_flag](https://github.com/OceanTran999/CTFLearn/assets/100577019/fa9c4a2d-70c6-4c4e-891f-13cc64deb950)


Next, I `disassemble vuln`
![disas_vuln](https://github.com/OceanTran999/CTFLearn/assets/100577019/6101194b-83b2-48a4-9173-0d0e0188fb7d)


Looking at the Assembly code, I think the stack will look like:
```44 bytes buffer + 4 bytes `ebp` + 4 bytes `print_flag()` + 4 bytes + 4 bytes `p1` + 4 bytes `p2````
Next, we will need the address of `print_flag()`

![print_flag](https://github.com/OceanTran999/CTFLearn/assets/100577019/fa9c4a2d-70c6-4c4e-891f-13cc64deb950)


`disassemble print_flag`, we can see the value of `p1` and `p2` variable

![disas_print_flag](https://github.com/OceanTran999/CTFLearn/assets/100577019/e26d06ae-6f4a-4783-9078-8fdea1c9888e)


![0xc0ffee-print_flag](https://github.com/OceanTran999/CTFLearn/assets/100577019/f292933f-999b-4ed5-a232-b350c4fb5b9b)


# Stack
Here's the stack I have to solve this challenge.

![Final_Stack](https://github.com/OceanTran999/CTFLearn/assets/100577019/ad6fd1dd-e77d-412d-811c-1f92b2d712b6)


Finally, we get the flaggg :D

![Flag](https://github.com/OceanTran999/CTFLearn/assets/100577019/a8003915-649b-45a8-a963-4a0dfa096c09)
