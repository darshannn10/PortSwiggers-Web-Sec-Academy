# Lab 2: Information disclosure on debug page
 
This lab contains a debug page that discloses sensitive information about the application. To solve the lab, obtain and submit the SECRET_KEY environment variable.

## Solution
> Manual Exploitation
1. With Burp running, browse to the home page.
2. Go to the "Target" > "Site Map" tab. Right-click on the top-level entry for the lab and select "Engagement tools" > "Find comments". Notice that the home page contains an HTML comment that contains a link called "Debug". This points to `/cgi-bin/phpinfo.php`.
3. In the site map, right-click on the entry for `/cgi-bin/phpinfo.php` and select "Send to Repeater".
4. In Burp Repeater, send the request to retrieve the file. Notice that it reveals various debugging information, including the `SECRET_KEY` environment variable.
5. Go back to the lab, click "Submit solution", and enter the `SECRET_KEY` to solve the lab.

> Automating the process: [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/Information%20Disclosure/lab-02/lab-02-script.py)

## Video Solution
[Sommer's YT Video](https://youtu.be/ulw2M_4JktU)
