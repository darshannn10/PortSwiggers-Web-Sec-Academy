# Lab 1: Unprotected admin functionality
This lab has an unprotected admin panel.

Solve the lab by deleting the user carlos.

## Solution
> Manual Exploitation
1. Go to the lab and view robots.txt by appending /robots.txt to the lab URL. Notice that the Disallow line discloses the path to the admin panel.
2. In the URL bar, replace /robots.txt with /administrator-panel to load the admin panel.
3. Delete carlos.
> Automating the process: [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/Access%20Control/lab-01/lab-01-script.py)

## Video Solution
[Sommer's YT Video](https://youtu.be/VJHauKQdtcA)
