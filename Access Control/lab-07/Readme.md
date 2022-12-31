# Lab 7: User ID controlled by request parameter with data leakage in redirect
This lab contains an access control vulnerability where sensitive information is leaked in the body of a redirect response.

To solve the lab, obtain the API key for the user carlos and submit it as the solution.

You can log in to your own account using the following credentials: `wiener:peter`
## Solution
> Manual Exploitation
1. Log in using the supplied credentials and access your account page.
2. Send the request to Burp Repeater.
3. Change the "id" parameter to carlos.
4. Observe that although the response is now redirecting you to the home page, it has a body containing the API key belonging to carlos.
5. Submit the API key.

> Automating the process: [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/Access%20Control/lab-07/lab-07-script.py)

## Video Solution
[Sommer's YT Video]()
