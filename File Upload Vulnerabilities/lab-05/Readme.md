# Lab 5: Web shell upload via obfuscated file extension
This lab contains a vulnerable image upload function. Certain file extensions are blacklisted, but this defense can be bypassed using a classic obfuscation technique.

To solve the lab, upload a basic PHP web shell, then use it to exfiltrate the contents of the file /home/carlos/secret. Submit this secret using the button provided in the lab banner.

You can log in to your own account using the following credentials: `wiener:peter`

## Solution
> Manual Exploitation
1. Log in and upload an image as your avatar, then go back to your account page.
2. In Burp, go to *Proxy > HTTP history* and notice that your image was fetched using a GET request to /files/avatars/<YOUR-IMAGE>. Send this request to Burp Repeater.
3. On your system, create a file called `exploit.php`, containing a script for fetching the contents of Carlos's secret. For example:
```php
<?php echo file_get_contents('/home/carlos/secret'); ?>
```
4. Attempt to upload this script as your avatar. The response indicates that you are only allowed to upload JPG and PNG files.
5. In Burp's proxy history, find the `POST /my-account/avatar` request that was used to submit the file upload. Send this to Burp Repeater.
6. In Burp Repeater, go to the tab for the `POST /my-account/avatar` request and find the part of the body that relates to your PHP file. In the `Content-Disposition` header, change the value of the filename parameter to include a `URL encoded null byte`, followed by the `.jpg` extension:
```php
filename="exploit.php%00.jpg"
```
7. Send the request and observe that the file was successfully uploaded. Notice that the message refers to the file as `exploit.php`, suggesting that the `null byte` and `.jpg` extension have been stripped.
8. Switch to the other Repeater tab containing the `GET /files/avatars/<YOUR-IMAGE>` request. In the path, replace the name of your image file with `exploit.php` and send the request. Observe that Carlos's secret was returned in the response.
9. Submit the secret to solve the lab.

> Automating the process
- [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/File%20Upload%20Vulnerabilities/lab-05/lab-05-script.py)
- [Shell](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/File%20Upload%20Vulnerabilities/lab-05/lab-05-shell.py)

