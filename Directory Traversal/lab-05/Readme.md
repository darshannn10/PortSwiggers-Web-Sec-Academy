# Lab 5: File path traversal, validation of start of path

This lab contains a file path traversal vulnerability in the display of product images.

The application transmits the full file path via a request parameter, and validates that the supplied path starts with the expected folder.

To solve the lab, retrieve the contents of the /etc/passwd file.

## Solution
> Manual Exploitation
1. Use Burp Suite to intercept and modify a request that fetches a product image.
2. Modify the `filename` parameter, giving it the value:
```
/var/www/images/../../../etc/passwd
```
3. Observe that the response contains the contents of the `/etc/passwd` file.

> Automating the process: [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/Directory%20Traversal/lab-05/lab-05-script.py)

# Video Solution
[Sommer's YT Playlist](https://youtu.be/9ym9W88oS7w)
