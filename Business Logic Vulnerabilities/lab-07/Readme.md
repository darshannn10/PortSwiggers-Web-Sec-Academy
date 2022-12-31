# Lab 7: Weak isolation on dual-use endpoint
This lab makes a flawed assumption about the user's privilege level based on their input. As a result, you can exploit the logic of its account management features to gain access to arbitrary users' accounts. To solve the lab, access the administrator account and delete Carlos.

You can log in to your own account using the following credentials: `wiener:peter`

## Solution
> Manual Exploitation
1. With Burp running, log in and access your account page.
2. Change your password.
3. Study the `POST /my-account/change-password` request in Burp Repeater.
4. Notice that if you remove the `current-password` parameter entirely, you are able to successfully change your password without providing your current one.
5. Observe that the user whose password is changed is determined by the `username` parameter. Set `username=administrator` and send the request again.
6. Log out and notice that you can now successfully log in as the `administrator` using the password you just set.
7. Go to the admin panel and delete Carlos to solve the lab.

> Automating the process: [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/Business%20Logic%20Vulnerabilities/lab-07/lab-07-script.py)

## Video Solution
[Sommer's YT Video](https://youtu.be/--d7Hl-lBzM)
