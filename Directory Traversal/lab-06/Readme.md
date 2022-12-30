# Lab 6: File path traversal, validation of file extension with null byte bypass
This lab contains a file path traversal vulnerability in the display of product images.

The application validates that the supplied filename ends with the expected file extension.

To solve the lab, retrieve the contents of the `/etc/passwd` file.

## Solution
> Manual Exploitation
1. Use Burp Suite to intercept and modify a request that fetches a product image.
2. Modify the filename parameter, giving it the value:
```
../../../etc/passwd%00.png
```
3. Observe that the response contains the contents of the /etc/passwd file.
> Automating the process: [Script]()

# Video Solution
[Summer's YT video](https://youtu.be/vFkrWxsWnoY)
