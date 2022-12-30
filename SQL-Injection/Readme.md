# SQL Injection(SQLi)

[PortSwigger Lab](SQL%20Injection(SQLi)%2062d95bf98e564611b0846ece5df951ca/PortSwigger%20Lab%2030c6fc0b0fc740a2870ac594c470821a.md)

SQL injection is a web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database.

It allows an attacker to view data that they are not normally able to retrieve

- " SELECT * FROM v$version " → shows database version in Oracle
- " SELECT * FROM information_schema.tables  " → to list tables in the database

![Untitled](https://user-images.githubusercontent.com/87711310/205446962-457c75dc-7b49-49a4-9eae-c18825a25bfa.png)


## Impact

CIA triad is impacted
**C**onfidentilaity: view sensitive information
**I**ntegrity: alter data in database
**A**vaulability: Delete data in database

RCE to operating system

## Type of SQL Injections

![Untitled 1](https://user-images.githubusercontent.com/87711310/205446983-20f0c2a3-ee95-403f-8fe7-2fbc299ad4e3.png)

## In-band SQLi (Classic SQLi)

Same communication channel is used for the attack and the result of attack 

- Most common type
- Easy to exploit

### 1. Error-based SQLi

- in-band SQL Injection technique
- relies on error messages thrown by the database server to obtain information about the structure of the database
- Sometimes, error-based SQL injection alone is enough for an attacker to enumerate an entire database.

![Untitled 2](https://user-images.githubusercontent.com/87711310/205447004-2a15a713-27e6-4029-9c1a-8d23b92b9e2e.png)

### 2. Union-based SQLi

- leverages the UNION SQL operator to combine the results of two or more SELECT statements into a single result which is then returned as part of the HTTP response.

![Untitled 3](https://user-images.githubusercontent.com/87711310/205447005-75d8b05f-b173-48f0-9602-a6511486f3fe.png)

## Inferential (Blind)

- no data is actually transferred via the web application and the attacker would not be able to see the result of an attack in-band.
- Instead, an attacker is able to reconstruct the database structure by sending payloads, observing the web application’s response and the resulting behavior of the database server
- Takes longer to exploit

### 1. Boolean-based SQLi

- relies on sending an SQL query to the database which forces the application to return a different result depending on whether the query returns a TRUE or FALSE result

![Untitled 4](https://user-images.githubusercontent.com/87711310/205447011-c8e1fd45-5e00-4b68-9db4-7c35ad068099.png)

- Extract information from database

![https://imgur.com/iqm4l9N.png](https://imgur.com/iqm4l9N.png)

### 2. Time-based SQLi

- relies on sending an SQL query to the database which forces the database to wait for a specified amount of time (in seconds) before responding.
- The response time will indicate to the attacker whether the result of the query is TRUE or FALSE.
- Depending on the result, an HTTP response will be returned with a delay, or returned immediately.
- This allows an attacker to infer if the payload used returned true or false, even though no data from the database is returned.
- Typically slower attack
- **Example Query**:
If the first character of the administrator’s hashed password is an ‘a’, wait for 10
seconds.
→ response takes 10 seconds → first letter is ‘a’
→ response doesn’t take 10 seconds → first letter is not ‘a

## Out-of-Band SQLi

- not very common, mostly because it depends on features being enabled on the database server being used by the web application.
- Out-of-band SQL Injection occurs when an attacker is unable to use the same channel to launch the attack and gather results.
- Consists of triggering an OOB network connection to a system you control.
- Not common
- DNS, HTTP protocol used.

![Untitled 5](https://user-images.githubusercontent.com/87711310/205447180-6c05b902-8271-46e5-8781-a5856971aedc.png)

## **HOW TO FIND SQLI VULNERABILITIES?**

### **Finding SQLi Vulnerabilities
Depends on the perspective of testing.**

**1) Black-Box Testing Perspective**

- Map the application
- Fuzz the application
- Submit SQL-specific characters such as ' or ", and look for
errors or other anomalies
- Submit Boolean conditions such as OR 1=1 and OR 1=2,
and look for differences in the application's responses
- Submit payloads designed to trigger time delays when
executed within a SQL query, and look for differences in
the time taken to respond
- Submit OAST payloads designed to trigger an out-of-band
network interaction when executed within an SQL query,
and monitor for any resulting interactions

**2) White-Box Testing Perspective**

- Enable web server logging
- Enable database logging
- Map the application
- Visible functionality in the application
- Regex search on all instances in the code that talk to
the database
- Code review!
- Follow the code path for all input vectors
- Test any potential SQLi vulnerabilities

## **HOW TO EXPLOIT SQLI VULNERABILITIES?**

### **1) Exploiting Error-Based SQLi**

- Submit SQL-specific characters such as ' or ", and look for errors or other anomalies
- Different characters can give you different errors

### 2) Exploiting Union-Based SQLi

- There are two rules for combining the result sets of two queries by using UNION:
   • The number and the order of the columns must be the same in all queries
   • The data types must be compatible
- Exploitation:
• Figure out the number of columns that the query is making
• Figure the data types of the columns (mainly interested in string data)
• Use the UNION operator to output information from the database

- Determining the number of columns required in an SQL injection **UNION** attack using **ORDER BY**:

![Untitled 6](https://user-images.githubusercontent.com/87711310/205447184-99eaf92f-dea0-452e-a2cc-102db3c32a9b.png)

• Incrementally inject a series of ORDER BY clauses until you get an error or observe a
different behaviour in the application

![Untitled 7](https://user-images.githubusercontent.com/87711310/205447227-f5607657-dc6b-470e-a456-dfb539331282.png)


![Untitled 8](https://user-images.githubusercontent.com/87711310/205447231-a67c5ede-9e06-4e17-9a24-867edbbe6019.png)

- Determining the number of columns required in an SQL injection UNION attack using **NULL VALUES**:

![Untitled 9](https://user-images.githubusercontent.com/87711310/205447266-bae4c0df-6b5f-46d1-9ef9-4ff68abae10f.png)

- Incrementally inject a series of UNION SELECT payloads specifying a different number of null  values until you no longer get an error

![Untitled 10](https://user-images.githubusercontent.com/87711310/205447270-f688a481-2fa6-4e7d-a9c7-c5f9e3d351ac.png)

- Finding columns with a useful data type in an SQL injection UNION attack:
 • Probe each column to test whether it can hold string data by submitting a series of UNION SELECT payloads that place a string value into each column in turn

![Untitled 11](https://user-images.githubusercontent.com/87711310/205447272-aff048b0-aa80-40c1-8131-6927e01b9712.png)

- There are two rules for combining the result sets of two queries by using UNION:
   • The number and the order of the columns must be the same in all queries
   • The data types must be compatible
- Exploitation:
• Figure out the number of columns that the query is making
• Figure the data types of the columns (mainly interested in string data)
• Use the UNION operator to output information from the database

### 3)Exploiting Time-Based Blind SQLi

- Submit a payload that pauses the application for a specified period of time
- Write a program that uses conditional statements to ask the database a series of TRUE / FALSE questions and monitor response time

### 4) Exploiting Out-of-Band SQLi

- Submit OAST payloads designed to trigger an out-of-band network interaction when executed within an SQL query, and monitor for any resulting interactions
- Depending on SQL injection use different methods to exfil data
