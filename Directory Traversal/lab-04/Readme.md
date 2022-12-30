# Lab 4: File path traversal, traversal sequences stripped with superfluous URL-decode
This lab contains a file path traversal vulnerability in the display of product images.

The application blocks input containing path traversal sequences. It then performs a URL-decode of the input before using it.

To solve the lab, retrieve the contents of the `/etc/passwd` file.

## Solution
> Manual Exploitation
1. Use Burp Suite to intercept and modify a request that fetches a product image.
2. Modify the filename parameter, giving it the value:
```
..%252f..%252f..%252fetc/passwd
```
3. Observe that the response contains the contents of the /etc/passwd file.

> Automating the process: [Script]()

# Video Solution
[Sommer's YT video](https://youtu.be/7slk8nYGtY0)
