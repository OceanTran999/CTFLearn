![Chal](https://github.com/user-attachments/assets/36d45bbb-11fa-41f1-b702-7bad3208e208)


Accessing to the vulnerable website, I see that it said my `User-Agent` value is not correct.

![Access_Web](https://github.com/user-attachments/assets/f2503eca-2a99-438f-8242-f037c6581cb1)


Using BurpSuite, I see there's a hint in the comment, I think it can be the suitable value for `User-Agent`. After that, it gives us another hint about the `awesomesauce.com`. At first I don't understand it, after searching Google and reading the comments :), I see there's another field in HTTP Header I don't care much, it's the `Referer`. So, just adding this field with the url of second hint, we will get the flag. Here's the way I use to get the flag in using both Burp and curl ways.

![Burp](https://github.com/user-attachments/assets/aaacacc6-b843-4491-93c0-f7871aa04cc1)


![Flag_With_Burp](https://github.com/user-attachments/assets/6ade4b62-4971-409f-9f99-aa51f037e4ea)


![Flag_With_Curl](https://github.com/user-attachments/assets/267647f6-786f-46b8-924e-899777db8096)
