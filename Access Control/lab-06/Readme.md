# Lab: User ID controlled by request parameter, with unpredictable user IDs

This lab has a horizontal privilege escalation vulnerability on the user account page, but identifies users with GUIDs.

To solve the lab, find the GUID for carlos, then submit his API key as the solution.

You can log in to your own account using the following credentials: `wiener:peter`

## Solution
> Manual Exploitation
1. Find a blog post by `carlos`.
2. Click on `carlos` and observe that the URL contains his user ID. Make a note of this ID.
3. Log in using the supplied credentials and access your account page.
4. Change the `id` parameter to the saved user ID.
5. Retrieve and submit the API key.

> Automating the process: [Script](https://github.com/darshannn10/PortSwiggers-Web-Sec-Academy/blob/main/Access%20Control/lab-06/lab-06-script.py)

## Video Solution
[Sommer's YT Video](https://youtu.be/KMM4VkXVdjw)
