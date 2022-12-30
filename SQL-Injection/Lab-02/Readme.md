# Lab 2: SQL injection vulnerability allowing login bypass

This lab contains an SQL injection vulnerability in the login function.

To solve the lab, perform an SQL injection attack that logs in to the application as the administrator user.



## Solution
>  Manually
1. Use Burp Suite to intercept and modify the login request.
2. Modify the username parameter, giving it the value: `administrator'--`

> Scripting the Attack:   [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/SQL-Injection/Lab-02/sqli-lab-02.py)

## Video Solution:
1. Manually: [Rana Khalil's Youtube Video](https://youtu.be/ML3aGaloczI)
2. Scripting: [Rana Khalil's Youtube Video](https://www.youtube.com/watch?v=fMPvCyD2v4w&list=PLuyTk2_mYISLaZC4fVqDuW_hOk0dd5rlf&index=3&ab_channel=RanaKhalil)
