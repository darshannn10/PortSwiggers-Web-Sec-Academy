# Lab 10: Insecure direct object references
This lab stores user chat logs directly on the server's file system, and retrieves them using static URLs.

Solve the lab by finding the password for the user carlos, and logging into their account.

## Solution
> Manual Exploitation
1. Select the `Live chat` tab.
2. Send a message and then select `View transcript`.
3. Review the URL and observe that the transcripts are text files assigned a filename containing an incrementing number.
4. Change the filename to `1.txt` and review the text. Notice a password within the chat transcript.
5. Return to the main lab page and log in using the stolen credentials.

> Automating the process: [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/Access%20Control/lab-09/lab-09-script.py)

## Video Solution
[Intigriti-How to search for IDORs](https://youtu.be/jgbHaALms_Q)

[Sommer's YT Video](https://youtu.be/Sd8jL96H0hc)
