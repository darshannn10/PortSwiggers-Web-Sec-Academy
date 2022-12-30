# Lab 3: SQL injection UNION attack, determining the number of columns returned by the query

This lab contains an SQL injection vulnerability in the `product category` filter. The results from the query are returned in the application's response, so you can use a `UNION` attack to retrieve data from other tables. The first step of such an attack is to `determine the number of columns` that are being returned by the query. You will then use this technique in subsequent labs to construct the full attack.

To solve the lab, determine the `number of columns` returned by the query by performing an SQL injection `UNION` attack that returns an additional row containing `null` values.

## Solution
> Manual Method
1. Use Burp Suite to intercept and modify the request that sets the product category filter.
2. Modify the `category` parameter, giving it the value `'+UNION+SELECT+NULL--`. Observe that an error occurs.\
3. Modify the `category` parameter to add an additional column containing a null value: ```'+UNION+SELECT+NULL,NULL--```
4. Continue adding null values until the error disappears and the response includes additional content containing the null values.
5. Alternatively, you can also use `ORDER BY` clause

> Scripting the Attack: [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/SQL-Injection/Lab-03/sqli-lab-03.py)

## Payload:
Normal: 

1. `' UNION SELECT NULL,NULL,NULL--`

2. `' ORDER BY 3--`
        
URL-Encoded: `%27+UNION+SELECT+NULL,NULL,NULL--`

## Video Solution
1. Manual: [Rana Khalil's Youtube video](https://youtu.be/umXGHbEyW5I)
2. Automating: [Rana Khalil's Youtube video](https://www.youtube.com/watch?v=fMPvCyD2v4w&list=PLuyTk2_mYISLaZC4fVqDuW_hOk0dd5rlf&index=3&ab_channel=RanaKhalil)
