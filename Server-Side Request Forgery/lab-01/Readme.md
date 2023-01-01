## Solution
> Manuak Exploitation
1. Browse to `/admin` and observe that you can't directly access the admin page.
2. Visit a product, click "Check stock", intercept the request in Burp Suite, and send it to Burp Repeater.
3. Change the URL in the `stockApi` parameter to `http://localhost/admin`. This should display the administration interface.
4. Read the HTML to identify the URL to delete the target user, which is:
```
http://localhost/admin/delete?username=carlos
```
5. Submit this URL in the `stockApi` parameter, to deliver the SSRF attack.

> Automating the process
- [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/Server-Side%20Request%20Forgery/lab-01/lab-01-script.py)


## Video Solution
- [Rana Khalil's Solution](https://youtu.be/lMxCQcktifs)
- [Sommer's Solution](https://youtu.be/yblAc0upHC4)