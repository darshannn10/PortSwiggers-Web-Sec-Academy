# Lab 11: Method-based access control can be circumvented
This lab implements access controls based partly on the HTTP method of requests. You can familiarize yourself with the admin panel by logging in using the credentials administrator:admin.

To solve the lab, log in using the credentials wiener:peter and exploit the flawed access controls to promote yourself to become an administrator.
## Solution
> Manual Exploitation
1. Log in using the admin credentials.
2. Browse to the admin panel, promote carlos, and send the HTTP request to Burp Repeater.
3. Open a `private/incognito browser window`, and log in with the `non-admin credentials`.
4. Attempt to re-promote `carlos` with the non-admin user by copying that user's session cookie into the existing Burp Repeater request, and observe that the response says "Unauthorized".
5. Change the method from `POST` to `POSTX` and observe that the response changes to `missing parameter`.
6. Convert the request to use the `GET` method by right-clicking and selecting `Change request method`.
7. Change the username parameter to your username and resend the request.

> Automating the process: [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/Access%20Control/lab-11/lab-11-script.py)

## Video Solution
[Sommer's YT Video](https://youtu.be/H_xREdOq1yk)
