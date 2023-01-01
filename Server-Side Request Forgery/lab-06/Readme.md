# Lab 6: SSRF with whitelist-based input filter
This lab has a stock check feature which fetches data from an internal system.

To solve the lab, change the stock check URL to access the admin interface at http://localhost/admin and delete the user carlos.

The developer has deployed an anti-SSRF defense you will need to bypass

# Solution
> Manual Exploitation
1. Visit a product, click "Check stock", intercept the request in Burp Suite, and send it to Burp Repeater.
2. Change the URL in the stockApi parameter to `http://127.0.0.1/` and observe that the application is parsing the URL, extracting the hostname, and validating it against a whitelist.
3. Change the URL to `http://username@stock.weliketoshop.net/` and observe that this is accepted, indicating that the URL parser supports embedded credentials.
4. Append a # to the username and observe that the URL is now rejected.
5. Double-URL encode the `#` to `%2523` and observe the extremely suspicious "Internal Server Error" response, indicating that the server may have attempted to connect to "username".
6. To access the admin interface and delete the target user, change the URL to:
```
http://localhost:80%2523@stock.weliketoshop.net/admin/delete?username=carlos
```
> Automating the process
- [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/Server-Side%20Request%20Forgery/lab-06/lab-06-script.py)

## Video Solution
- [Rana Khalil's Video](https://youtu.be/EJhxTN0T_UM)
- [Sommer's Video](https://youtu.be/CsV8Huq6wkc)
