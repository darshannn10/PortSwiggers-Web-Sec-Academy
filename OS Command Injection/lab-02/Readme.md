# Lab 2: Blind OS command injection with time delays

This lab contains a blind OS command injection vulnerability in the feedback function.

The application executes a shell command containing the user-supplied details. The output from the command is not returned in the response.

To solve the lab, exploit the blind OS command injection vulnerability to cause a 10 second delay.

## Solution
> Manual Exploitation
1. Use Burp Suite to intercept and modify the request that submits feedback.
2. Modify the `email` parameter, changing it to:
```
email=x||ping+-c+10+127.0.0.1||
```
3. Observe that the response takes 10 seconds to return.
> Automating the process: [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/OS%20Command%20Injection/lab-02/lab-02-script.py)

## Videoo Solution
[Rana Khalil's YT Video](https://youtu.be/YHQXfPWo1vI)
[Sommer's YT Video](https://youtu.be/sclkGjfyzLc)
