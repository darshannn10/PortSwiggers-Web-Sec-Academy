# Lab 2: File path traversal, traversal sequences blocked with absolute path bypass

The application blocks traversal sequences but treats the supplied filename as being relative to a default working directory.

To solve the lab, retrieve the contents of the `/etc/passwd` file.

# Solution
> Manual Expliotation
1. Use Burp Suite to intercept and modify a request that fetches a product image.
2. Modify the `filename` parameter, giving it the value `/etc/passwd`.
3. Observe that the response contains the contents of the `/etc/passwd` file.
> Automating the process: [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/Directory%20Traversal/lab-02/lab-02-script.py)

## Video Solution
[Sommer's YT Video](https://youtu.be/jGyse5X9ltA)

