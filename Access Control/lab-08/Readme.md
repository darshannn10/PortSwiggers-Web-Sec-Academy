# Lab 8: User ID controlled by request parameter with password disclosure
This lab has user account page that contains the current user's existing password, prefilled in a masked input.

To solve the lab, retrieve the administrator's password, then use it to delete carlos.

You can log in to your own account using the following credentials: `wiener:peter`

## Solution
> Manual Exploitation
1. Log in using the supplied credentials and access the user account page.
2. Change the `id` parameter in the URL to `administrator`.
3. View the response in Burp and observe that it contains the administrator's password.
4. Log in to the administrator account and delete `carlos`.

> Automating the process: [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/Access%20Control/lab-08/lab-08-script.py)

## Video Solution
[Sommer's YT Video](https://youtu.be/erLHrDmf2gE)
