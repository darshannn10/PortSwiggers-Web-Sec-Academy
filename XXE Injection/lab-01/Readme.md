# Lab 1: Exploiting XXE using external entities to retrieve files
This lab has a "Check stock" feature that parses XML input and returns any unexpected values in the response.

To solve the lab, inject an XML external entity to retrieve the contents of the `/etc/passwd` file.

## Solution
> Manual Exploitation
1. Visit a product page, click "Check stock", and intercept the resulting POST request in Burp Suite.
2. Insert the following external entity definition in between the XML declaration and the `stockCheck` element:
```
<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
```
3. Replace the `productId` number with a reference to the external entity: `&xxe;`. The response should contain `Invalid product ID:` followed by the contents of the `/etc/passwd` file.

> Automating the process
- [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/XXE%20Injection/lab-01/lab-01-script.py)

## Video Solution
- [Sommer's Video](https://youtu.be/V5JE468z5zk)
- [Seven Seas Security's Video](https://youtu.be/71dZaGfOVqw)
