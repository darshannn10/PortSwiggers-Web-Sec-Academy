# Lab 1: File path traversal, simple case
This lab contains a file path traversal vulnerability in the display of product images.

To solve the lab, retrieve the contents of the `/etc/passwd` file.

## Solution
> Manual Exploitation
1. Use Burp Suite to intercept and modify a request that fetches a product image.
2. Modify the filename parameter, giving it the value:
```bash
../../../etc/passwd
```
3. Observe that the response contains the contents of the /etc/passwd file.

> Automating the process: [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/Directory%20Traversal/lab-01/lab-01-script.py)

# Video Solution
[Sommer's Youtube Video](https://youtu.be/3CyrBt0E8AA)
