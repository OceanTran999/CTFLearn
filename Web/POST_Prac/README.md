![Chal](https://github.com/user-attachments/assets/964d3a87-e5e0-47f4-bf79-98738a5bfdd7)


Accessing the vulnerable web, I don't see anything except the hint seding the HTTP POST request

![Access_web](https://github.com/user-attachments/assets/98e045c0-fa48-4596-8183-54e53a68923d)


Using Burp, I see that it gives the credential of the `admin` user :), so we just need to use Python to create a HTTP request and get the flag.

![Burp](https://github.com/user-attachments/assets/8f19fcd4-5fae-4c89-bb5e-a60451f37a88)


![Flag](https://github.com/user-attachments/assets/311d8026-94c9-403a-87a3-e8500bc97dc8)
