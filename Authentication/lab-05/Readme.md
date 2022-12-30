# Lab 5: Username enumeration via response timing
This lab is vulnerable to username enumeration using its response times. To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page.

Your credentials: `wiener:peter`
[Candidate usernames](https://portswigger.net/web-security/authentication/auth-lab-usernames)
[Candidate passwords](https://portswigger.net/web-security/authentication/auth-lab-passwords)

## Solution
> Manual Exploitation
1. With Burp running, submit an invalid username and password, then send the `POST /login` request to Burp Repeater. Experiment with different usernames and passwords. Notice that your IP will be blocked if you make too many invalid login attempts.
2. Identify that the ``X-Forwarded-For` header is supported, which allows you to spoof your IP address and bypass the IP-based brute-force protection.
3. Continue experimenting with usernames and passwords. Pay particular attention to the response times. Notice that when the username is invalid, the response time is roughly the same. However, when you enter a valid username (your own), the response time is increased depending on the length of the password you entered.
4. Send this request to Burp Intruder and select the attack type to `Pitchfork`. Clear the default payload positions and add the `X-Forwarded-For` header.
5. Add payload positions for the `X-Forwarded-For` header and the `username` parameter. Set the password to a very long string of characters (about 100 characters should do it).
6. On the `Payloads` tab, select payload set 1. Select the Numbers payload type. Enter the range 1 - 100 and set the step to 1. Set the max fraction digits to 0. This will be used to spoof your IP.
7. Select payload set 2 and add the list of usernames. Start the attack.
8. When the attack finishes, at the top of the dialog, click Columns and select the `Response` received and `Response` completed options. These two columns are now displayed in the results table.
9. Notice that one of the response times was significantly longer than the others. Repeat this request a few times to make sure it consistently takes longer, then make a note of this username.
10. Create a new Burp Intruder attack for the same request. Add the `X-Forwarded-For` header again and add a payload position to it. Insert the username that you just identified and add a payload position to the `password` parameter.
11. On the `Payloads` tab, add the list of numbers in payload set 1 and add the list of passwords to payload set 2. Start the attack.
12. When the attack is finished, find the response with a 302 status. Make a note of this password.
13. Log in using the username and password that you identified and access the user account page to solve the lab.

> Automating the attack: [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/new/main/Authentication/lab-05/auth-lab-05.py)

# Video Solution
[Sommer's YT Video](https://youtu.be/RO5Wo5jjbWE)
