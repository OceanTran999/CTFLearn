![Chal](https://github.com/user-attachments/assets/589bbecc-a61f-4b3c-bce7-f9305000656f)


This challenge is such a very good challenge that I learned a lot, the hint of this challenge is using `UNION` command for `SQL Injection`. The `UNION` keyword enables you to execute one or more additional SELECT queries and append the results to the original query, which can extract the information from different databases. The attack will work if we know how many columns existing in the database. Therefore, firstly I used these `ORDER BY` commands to determine how many columns.
```
  1 ORDER BY 2
  1 ORDER BY 3
  1 ORDER BY 4
  1 ORDER BY 5
```

![1ORDER4](https://github.com/user-attachments/assets/de764d35-d275-46a7-b87c-fb86886283e4)


![1ORDER5](https://github.com/user-attachments/assets/95de1aad-b0e3-4c4e-a41f-2cb6b06ff67c)


The result of the last command will return the `0 result`, which we can conclude that our database has 4 columns. Now, we can use `UNION` command to extract more information with multiple `SELECT` command, I use `NULL` value to check if the number of `NULL` values are correct, the server will not give us the error message. So, I will use `version()` command to extract the version of SQL Server.

![version](https://github.com/user-attachments/assets/83d7bf2f-7390-4729-8c15-98a848552d80)


Nice! Now, I will use this command to extract all the databases:
```
  1 UNION SELECT (SELECT group_concat(table_name) FROM information_schema.tables WHERE table_schema=database()), NULL, NULL, NULL--
```
The `group_concat()` concatenates the results into a string `information_schema` is a database that stores data of other databases and `database()` will return the name of the current database.

![show_databases](https://github.com/user-attachments/assets/8644fa98-6317-44e9-9a17-881abb07817c)


Welp, I see the `w0w_y0u_f0und_m3` database can possibly contains the flag, so I will extract it and get the flag XD

![flag](https://github.com/user-attachments/assets/83bdc5eb-1628-4511-84ad-a7d63f3d0a7a)

# References:
- https://www.acunetix.com/blog/articles/exploiting-sql-injection-example/
- https://portswigger.net/web-security/sql-injection/union-attacks
- https://www.sqlinjection.net/union/
- https://www.w3schools.com/sql/sql_orderby.asp
- https://www.w3schools.com/sql/sql_union.asp
