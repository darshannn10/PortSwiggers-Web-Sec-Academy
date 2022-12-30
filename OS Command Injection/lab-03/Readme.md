# Lab 3: Blind OS command injection with output redirection

This lab contains a blind OS command injection vulnerability in the feedback function.

The application executes a shell command containing the user-supplied details. The output from the command is not returned in the response. However, you can use output redirection to capture the output from the command. There is a writable folder at:
```
/var/www/images/
```
The application serves the images for the product catalog from this location. You can redirect the output from the injected command to a file in this folder, and then use the image loading URL to retrieve the contents of the file.

To solve the lab, execute the `whoami` command and retrieve the output.

## Solution
> Manual Exploitation
1. Use Burp Suite to intercept and modify the request that submits feedback.
2. Modify the `email` parameter, changing it to:
```
email=||whoami>/var/www/images/output.txt||
```
3. Now use Burp Suite to intercept and modify the request that loads an image of a product.
4. Modify the filename parameter, changing the value to the name of the file you specified for the output of the injected command: `filename=output.txt`
5. Observe that the response contains the output from the injected command.

> Automating the process: [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/OS%20Command%20Injection/lab-03/lab-03-script.py)

## Video Solution
[Rana Khalil's YT Video](https://youtu.be/4Wl9Ap8cmqQ)
[Sommer's YT Video](https://youtu.be/Cocf02tBZak)
