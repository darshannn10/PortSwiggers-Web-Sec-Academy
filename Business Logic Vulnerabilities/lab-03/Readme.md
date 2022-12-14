# Lab 3: Inconsistent security controls
This lab's flawed logic allows arbitrary users to access administrative functionality that should only be available to company employees. To solve the lab, access the admin panel and delete Carlos.

## Solution
> Manual Exploitation
1. Open the lab then go to the "Target" > "Site map" tab in Burp. Right-click on the lab domain and select "Engagement tools" > "Discover content" to open the content discovery tool.
2. Click "Session is not running" to start the content discovery. After a short while, look at the "Site map" tab in the dialog. Notice that it discovered the path /admin.
3. Try and browse to /admin. Although you don't have access, the error message indicates that DontWannaCry users do.
4. Go to the account registration page. Notice the message telling DontWannaCry employees to use their company email address. Register with an arbitrary email address in the format:
```
anything@your-email-id.web-security-academy.net
```
You can find your email domain name by clicking the "Email client" button.

5. Go to the email client and click the link in the confirmation email to complete the registration.
6. Log in using your new account and go to the "My account" page. Notice that you have the option to change your email address. Change your email address to an arbitrary @dontwannacry.com address.
7. Notice that you now have access to the admin panel, where you can delete Carlos to solve the lab.

> Automating the process: [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/Business%20Logic%20Vulnerabilities/lab-03/lab-03-script.py)

## Video Solution
[Sommer's YT Video](https://youtu.be/wRVgU2Pnews)
