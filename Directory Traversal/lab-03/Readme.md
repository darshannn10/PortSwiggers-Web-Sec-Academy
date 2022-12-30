# Lab 3: File path traversal, traversal sequences stripped non-recursively
This lab contains a file path traversal vulnerability in the display of product images.

The application strips path traversal sequences from the user-supplied filename before using it.

To solve the lab, retrieve the contents of the `/etc/passwd` file.

## Solution
> Manual Exploitation
1. Use Burp Suite to intercept and modify a request that fetches a product image.
2. Modify the filename parameter, giving it the value:
```
....//....//....//etc/passwd
```
3. Observe that the response contains the contents of the /etc/passwd file.
> Automating the process: [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/Directory%20Traversal/lab-03/lab-03-script.py)

# Video Solution
[Sommer's Youtube Video](https://youtu.be/bydjunJhZaE)
