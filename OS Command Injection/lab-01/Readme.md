# Lab 1: OS command injection, simple case
This lab contains an OS command injection vulnerability in the product stock checker.

The application executes a shell command containing user-supplied product and store IDs, and returns the raw output from the command in its response.

To solve the lab, execute the `whoami` command to determine the name of the current user.

## Solution
> Manual Exploitation
1. Use Burp Suite to intercept and modify a request that checks the stock level.
2. Modify the `storeID` parameter, giving it the value `1|whoami`.
3. Observe that the response contains the name of the current user.

> Automating the process: [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/OS%20Command%20Injection/lab-01/lab-01-script.py)

## Video Solution
[Rana Khalil's YT Video](https://youtu.be/GDUadTiXXVk)
[Sommer's YT Video](https://youtu.be/clUDnn66BR8)
