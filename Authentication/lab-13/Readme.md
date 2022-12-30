# Lab 13: Broken brute-force protection, multiple credentials per request

This lab is vulnerable due to a logic flaw in its `brute-force protection`. To solve the lab, brute-force Carlos's password, then access his account page.

Victim's username: `carlos`

[Candidate passwords](https://portswigger.net/web-security/authentication/auth-lab-passwords)

## Solution
> Manual Exploitation
1. With Burp running, investigate the login page. Notice that the POST /login request submits the login credentials in JSON format. Send this request to Burp Repeater.
2. In Burp Repeater, replace the single string value of the password with an array of strings containing all of the candidate passwords. For example:
```json
"username" : "carlos",
"password" : [
    "123456",
    "password",
    "qwerty"
    ...
]
```

3. Send the request. This will return a `302` response.
4. Right-click on this request and select `Show response in browser`. Copy the URL and load it in the browser. The page loads and you are logged in as `carlos`.
5. Click `My account` to access Carlos's account page and solve the lab.

> Automating the attack: [Script]()

# Video Solution
[Summer's YT Video](https://youtu.be/EuLhoEv3XYk)
