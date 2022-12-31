# Lab 2: Unprotected admin functionality with unpredictable URL
This lab has an unprotected admin panel. It's located at an unpredictable location, but the location is disclosed somewhere in the application.

Solve the lab by accessing the admin panel, and using it to delete the user carlos.

## Solution
> Manual Exploitation
1. Review the lab home page's source using Burp Suite or your web browser's developer tools.
2. Observe that it contains some JavaScript that discloses the URL of the admin panel.
3. Load the admin panel and delete carlos.
> Automating the process: [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/Access%20Control/lab-02/lab-02-script.py)

## Video Solution
[Sommer's YT Video](https://youtu.be/mml8SlN2Or4)
