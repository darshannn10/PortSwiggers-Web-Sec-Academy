# Lab 5: User ID controlled by request parameter
This lab has a horizontal privilege escalation vulnerability on the user account page.

To solve the lab, obtain the API key for the user carlos and submit it as the solution.

You can log in to your own account using the following credentials: `wiener:peter`

## Solution
> Manual Exploitation
1. Log in using the supplied credentials and go to your account page.
2. Note that the URL contains your username in the "id" parameter.
3. Send the request to Burp Repeater.
4. Change the `id` parameter to `carlos`.
5. Retrieve and submit the API key for `carlos`
> Automating the process: [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/Access%20Control/lab-05/lab-05-script.py)

## Video Solution
[Sommer's YT Video](https://youtu.be/pv5PfMbe_7k)
