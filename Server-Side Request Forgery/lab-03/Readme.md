# Lab 3: SSRF with blacklist-based input filter
This lab has a stock check feature which fetches data from an internal system.

To solve the lab, change the stock check URL to access the admin interface at `http://localhost/admin` and delete the user `carlos`.

The developer has deployed two weak anti-SSRF defenses that you will need to bypass.

# Solution
> Manual Exploitation
1. Visit a product, click "Check stock", intercept the request in Burp Suite, and send it to Burp Repeater.
2. Change the URL in the `stockApi` parameter to `http://127.0.0.1/` and observe that the request is blocked.
3. Bypass the block by changing the URL to: `http://127.1/
4. Change the URL to `http://127.1/admin` and observe that the URL is blocked again.
5. Obfuscate the `a` by `double-URL encoding` it to `%2561` to access the admin interface and delete the target user.
```
(%2561 -> %61 -> a)
```

> Automating the process
- [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/Server-Side%20Request%20Forgery/lab-03/lab-03-script.py)

## Video Solution
- [Rana Khalil's YT Video](https://youtu.be/vO0EqpX6PCQ)
- [Sommer's YT Video](https://youtu.be/y_lq8mfUwcs)
