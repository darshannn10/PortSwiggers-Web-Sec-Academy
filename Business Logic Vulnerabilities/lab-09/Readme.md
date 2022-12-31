# Lab 9: Authentication bypass via flawed state machine
This lab makes flawed assumptions about the sequence of events in the login process. To solve the lab, exploit this flaw to bypass the lab's authentication, access the admin interface, and delete Carlos.

You can log in to your own account using the following credentials: wiener:peter

## Solution
> Manual Exploitation
1. With Burp running, complete the login process and notice that you need to select your role before you are taken to the home page.
2. Use the content discovery tool to identify the `/admin` path.
3. Try browsing to `/admin` directly from the role selection page and observe that this doesn't work.
4. Log out and then go back to the login page. In Burp, turn on proxy intercept then log in.
5. Forward the `POST /login request`. The next request is `GET /role-selector`. Drop this request and then browse to the lab's home page. Observe that your role has defaulted to the `administrator` role and you have access to the admin panel.
6. Delete Carlos to solve the lab.
> Automating the process: [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/Business%20Logic%20Vulnerabilities/lab-09/lab-09-script.py)

## Video Solution
[Sommer's YT Video](https://youtu.be/55UvEQGK_pI)
