# Authentication vulnerabilities
Conceptually at least, authentication vulnerabilities are some of the simplest issues to understand. However, they can be among the most critical due to the obvious relationship between authentication and security. As well as potentially allowing attackers direct access to sensitive data and functionality, they also expose additional attack surface for further exploits. For this reason, learning how to identify and exploit authentication vulnerabilities, including how to bypass common protection measures, is a fundamental skill.

In this section, we'll look at some of the most common authentication mechanisms used by websites and discuss potential vulnerabilities in them. We'll highlight both inherent vulnerabilities in different authentication mechanisms, as well as some typical vulnerabilities that are introduced by their improper implementation. Finally, we'll provide some basic guidance on how you can ensure that your own authentication mechanisms are as robust as possible.

![password-reset-poisoning](https://user-images.githubusercontent.com/87711310/210082889-813fbe21-f8ee-4b7e-9510-e2eb2e404adf.svg)

## What is authentication?
Authentication is the process of verifying the identity of a given user or client. In other words, it involves making sure that they really are who they claim to be. At least in part, websites are exposed to anyone who is connected to the internet by design. Therefore, robust authentication mechanisms are an integral aspect of effective web security.

There are three authentication factors into which different types of authentication can be categorized:
- Something you know, such as a password or the answer to a security question. These are sometimes referred to as "knowledge factors".
- Something you have, that is, a physical object like a mobile phone or security token. These are sometimes referred to as "possession factors".
- Something you are or do, for example, your biometrics or patterns of behavior. These are sometimes referred to as "inherence factors".
Authentication mechanisms rely on a range of technologies to verify one or more of these factors.

## What is the difference between authentication and authorization?
Authentication is the process of verifying that a user really is who they claim to be, whereas authorization involves verifying whether a user is allowed to do something.

In the context of a website or web application, authentication determines whether someone attempting to access the site with the username Carlos123 really is the same person who created the account.

Once `Carlos123` is authenticated, his permissions determine whether or not he is authorized, for example, to access personal information about other users or perform actions such as deleting another user's account.

## How do authentication vulnerabilities arise?
Broadly speaking, most vulnerabilities in authentication mechanisms arise in one of two ways:

-The authentication mechanisms are weak because they fail to adequately protect against brute-force attacks.
-Logic flaws or poor coding in the implementation allow the authentication mechanisms to be bypassed entirely by an attacker. This is sometimes referred to as "broken authentication".
In many areas of web development, logic flaws will simply cause the website to behave unexpectedly, which may or may not be a security issue. However, as authentication is so critical to security, the likelihood that flawed authentication logic exposes the website to security issues is clearly elevated.

## What is the impact of vulnerable authentication?
The impact of authentication vulnerabilities can be very severe. Once an attacker has either bypassed authentication or has brute-forced their way into another user's account, they have access to all the data and functionality that the compromised account has. If they are able to compromise a high-privileged account, such as a system administrator, they could take full control over the entire application and potentially gain access to internal infrastructure.

Even compromising a low-privileged account might still grant an attacker access to data that they otherwise shouldn't have, such as commercially sensitive business information. Even if the account does not have access to any sensitive data, it might still allow the attacker to access additional pages, which provide a further attack surface. Often, certain high-severity attacks will not be possible from publicly accessible pages, but they may be possible from an internal page.

## Vulnerabilities in authentication mechanisms
A website's authentication system usually consists of several distinct mechanisms where vulnerabilities may occur. Some vulnerabilities are broadly applicable across all of these contexts, whereas others are more specific to the functionality provided.

We will look more closely at some of the most common vulnerabilities in the following areas:

- [Vulnerabilities in password-based login](https://portswigger.net/web-security/authentication/password-based)
- [Vulnerabilities in multi-factor authentication](https://portswigger.net/web-security/authentication/multi-factor)
- [Vulnerabilities in other authentication mechanisms](https://portswigger.net/web-security/authentication/other-mechanisms)

Note that several of the labs require you to enumerate usernames and brute-force passwords. To help you with this process, we've provided a shortlist of candidate [usernames](https://portswigger.net/web-security/authentication/auth-lab-usernames) and [passwords](https://portswigger.net/web-security/authentication/auth-lab-passwords) that you should use to solve the labs.

## Password based vulnerabilities
### Brute forcing

Use a tool like [Hydra](https://github.com/vanhauser-thc/thc-hydra) or [Burp Intruder](https://portswigger.net/burp/documentation/desktop/tools/intruder/using) to brute force a login form.  The tool will try a list of common usernames and passwords against the login form submission.

The following can all be used to perform user enumeration and hone the attack:

1. Error messages returned (Invalid username vs. Incorrect password)
1. Response times
1. Response status codes

This attack can be mitigated by IP based rate limiting, request throttling, account locking, MFA and CAPTCHAs.

```sh
# Brute force an https form POST submission
# You can get the $LOGIN_PATH and $FORM_SUBMIT_PAYLOAD using Burp Proxy or your browser's dev tools
hydra \
    -L "$FILE_WITH_USERNAMES" \
    -P "$FILE_WITH_PASSWORDS" \
    "$URL_OR_IP" \
    https-post-form "$LOGIN_PATH:$FORM_SUBMIT_PAYLOAD:$FAILURE_MESSAGE"

# Username and password list
hydra \
    -L usernames.list \
    -P passwords.list \
    web-security-academy.net \
    https-post-form "/login:username=^USER^&password=^PASS^:Invalid username"

# Known user and password list
hydra \
    -l the_big_cheese \
    -P passwords.list \
    web-security-academy.net \
    https-post-form "/login:username=^USER^&password=^PASS^:Invalid username"

# Known user and password list, checking for a 302 HTTP response code (success condition)
hydra \
    -l the_big_cheese \
    -P passwords.list \
    web-security-academy.net \
    https-post-form "/login:username=^USER^&password=^PASS^:S=302"
```

#### Considerations
- `Account locking`: can lead to user enumeration by indicating the account exists.  When an account is locked, the error message should remain generic.
- `Credential stuffing`: relies on people using the same password across multiple sites.  Uses a dictionary of `username:password` combinations and only tries each `username` once, thereby bypassing account locking.  This must be caught with rate limiting or throttling.
- `IP based rate limiting flaws`: if a successful login resets the rate limit counter, an attacker can bypass the rate limit by logging in with a valid account every `n` attempts.  Rate limiting should be unconditional for a set period based on the IP address.  This can be bypassed by using multiple IP addresses to conduct the attack.

## Multi-factor vulnerabilities

Vulnerabilities can include: 

- Checking the same factor twice (e.g. email based code) since this is only confirming the user knows their email login (both factors are "something you know").
- Using a weak factor (e.g. SMS based code) since this can be intercepted or fall victim to SIM card swapping.
- Second factor entry could be brute forced since it is usually a short number.
- Once login has succeeded and the second factor is requested, if there are flaws in the application logic, it may be possible to:
   - Bypass the second factor entirely by jumping directly to a page in the application.
   - User jump by altering the session cookie to login as a different user.

## Other vulnerabilities

- `Insecure password reset`:  allow an attacker to reset any user's password by guessing the reset link or altering the request to reset a different user's password.
- `Resetting passwords by mail`: sending a temporary password to a user's email address.  Email is considered insecure and there is a risk of that email being intercepted.  Only provide high-entropy password reset links by email.
- `Keeping users logged in`: relies on using a cookie.  If the cookie is insecure, an attacker can guess how to recreate it or alter a cookie for their own account to login as another user.  This can be mitigated by second factor verification.

### Keeping users logged in

A `remember me` cookie will include a value that can be used to authenticate the user.  As a result, it's susceptible to brute forcing if you can determine how the cookie value is generated.

```sh
# Remember me cookie example
Set-Cookie: stay-logged-in=d2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw;
```

Burp Proxy will automatically recognize the value as a base64 encoded string or you can decode it yourself:

```sh
# Decode the cookie value
echo "d2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw" | base64 -d
weiner:51dc30ddc473d43a6011e9ebba6ca770
```

You can then use the following tools to determine the hash type and check the result for a known value:

```sh
# Identify hash type
hashid -m "$HASH"
hash-identifier "$HASH"

# Generate a hash of differnt types to compare against a known hashed value.
# The `-n` is required to prevent printing the newline character
# which would alter the hash returned.
echo -n "foo" | openssl dgst -md5
echo -n "bar" | openssl dgst -sha256
```

Once you know the hashing, you can begin brute forcing the hashed value using [Burp Intruder (view solution)](https://portswigger.net/web-security/authentication/other-mechanisms/lab-brute-forcing-a-stay-logged-in-cookie).

## Tools
* [Hydra](https://github.com/vanhauser-thc/thc-hydra)
* [Burp Intruder](https://portswigger.net/burp/documentation/desktop/tools/intruder/using)


## Preventing attacks on your own authentication mechanisms

We have demonstrated several ways in which websites can be vulnerable due to how they implement authentication. To reduce the risk of such attacks on your own websites, there are several general principles that you should always try to follow.
1. Take care with user credentials
Even the most robust authentication mechanisms are ineffective if you unwittingly disclose a valid set of login credentials to an attacker. It should go without saying that you should never send any login data over unencrypted connections. Although you may have implemented HTTPS for your login requests, make sure that you enforce this by redirecting any attempted HTTP requests to HTTPS as well.

You should also audit your website to make sure that no username or email addresses are disclosed either through publicly accessible profiles or reflected in HTTP responses, for example.

2. Don't count on users for security
Strict authentication measures often require some additional effort from your users. Human nature makes it all but inevitable that some users will find ways to save themselves this effort. Therefore, you need to enforce secure behavior wherever possible.

The most obvious example is to implement an effective password policy. Some of the more traditional policies fall down because people crowbar their own predictable passwords into the policy. Instead, it can be more effective to implement a simple password checker of some kind, which allows users to experiment with passwords and provides feedback about their strength in real time. A popular example is the JavaScript library zxcvbn, which was developed by Dropbox. By only allowing passwords which are rated highly by the password checker, you can enforce the use of secure passwords more effectively than you can with traditional policies.

3. Prevent username enumeration
It is considerably easier for an attacker to break your authentication mechanisms if you reveal that a user exists on the system. There are even certain situations where, due to the nature of the website, the knowledge that a particular person has an account is sensitive information in itself.

Regardless of whether an attempted username is valid, it is important to use identical, generic error messages, and make sure they really are identical. You should always return the same HTTP status code with each login request and, finally, make the response times in different scenarios as indistinguishable as possible.

4. Implement robust brute-force protection
Given how simple constructing a brute-force attack can be, it is vital to ensure that you take steps to prevent, or at least disrupt, any attempts to brute-force logins.

One of the more effective methods is to implement strict, IP-based user rate limiting. This should involve measures to prevent attackers from manipulating their apparent IP address. Ideally, you should require the user to complete a CAPTCHA test with every login attempt after a certain limit is reached.

Keep in mind that this is not guaranteed to completely eliminate the threat of brute-forcing. However, making the process as tedious and manual as possible increases the likelihood that any would-be attacker gives up and goes in search of a softer target instead.

5. Triple-check your verification logic
As demonstrated by our labs, it is easy for simple logic flaws to creep into code which, in the case of authentication, have the potential to completely compromise your website and users. Auditing any verification or validation logic thoroughly to eliminate flaws is absolutely key to robust authentication. A check that can be bypassed is, ultimately, not much better than no check at all.

6. Don't forget supplementary functionality
Be sure not to just focus on the central login pages and overlook additional functionality related to authentication. This is particularly important in cases where the attacker is free to register their own account and explore this functionality. Remember that a password reset or change is just as valid an attack surface as the main login mechanism and, consequently, must be equally as robust.

7. Implement proper multi-factor authentication
While multi-factor authentication may not be practical for every website, when done properly it is much more secure than password-based login alone. Remember that verifying multiple instances of the same factor is not true multi-factor authentication. Sending verification codes via email is essentially just a more long-winded form of single-factor authentication.

SMS-based 2FA is technically verifying two factors (something you know and something you have). However, the potential for abuse through SIM swapping, for example, means that this system can be unreliable.

Ideally, 2FA should be implemented using a dedicated device or app that generates the verification code directly. As they are purpose-built to provide security, these are typically more secure.

Finally, just as with the main authentication logic, make sure that the logic in your 2FA checks is sound so that it cannot be easily bypassed.
