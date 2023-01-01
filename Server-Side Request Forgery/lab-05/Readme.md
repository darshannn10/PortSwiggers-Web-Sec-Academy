# Lab 5: Blind SSRF with out-of-band detection

This site uses analytics software which fetches the URL specified in the Referer header when a product page is loaded.

To solve the lab, use this functionality to cause an HTTP request to the public Burp Collaborator server.

## Solution
> Manual Exploitation
1. Visit a product, intercept the request in Burp Suite, and send it to Burp Repeater.
2. Go to the Repeater tab. Select the Referer header, right-click and select "Insert Collaborator Payload" to replace the original domain with a Burp Collaborator generated domain. Send the request.
3. Go to the Collaborator tab, and click "Poll now". If you don't see any interactions listed, wait a few seconds and try again, since the server-side command is executed asynchronously.
4. You should see some DNS and HTTP interactions that were initiated by the application as the result of your payload.

> Automating the process
- [Script]()

## Video Solution
- [Rana Khalil's Video](https://youtu.be/GAQFQhdrM1M)
- [Sommer's Video](https://youtu.be/lL6Msbkwhyk)
