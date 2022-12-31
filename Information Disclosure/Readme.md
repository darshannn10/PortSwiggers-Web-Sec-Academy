# Information Disclosure

## What is information disclosure?
Information disclosure, also known as information leakage, is when a website unintentionally reveals sensitive information to its users. Depending on the context, websites may leak all kinds of information to a potential attacker, including:

- Data about other users, such as usernames or financial information
- Sensitive commercial or business data
- Technical details about the website and its infrastructure
The dangers of leaking sensitive user or business data are fairly obvious, but disclosing technical information can sometimes be just as serious. Although some of this information will be of limited use, it can potentially be a starting point for exposing an additional attack surface, which may contain other interesting vulnerabilities. The knowledge that you are able to gather could even provide the missing piece of the puzzle when trying to construct complex, high-severity attacks.

Occasionally, sensitive information might be carelessly leaked to users who are simply browsing the website in a normal fashion. More commonly, however, an attacker needs to elicit the information disclosure by interacting with the website in unexpected or malicious ways. They will then carefully study the website's responses to try and identify interesting behavior.

## What are some examples of information disclosure?
Some basic examples of information disclosure are as follows:

- Revealing the names of hidden directories, their structure, and their contents via a robots.txt file or directory listing
- Providing access to source code files via temporary backups
- Explicitly mentioning database table or column names in error messages
- Unnecessarily exposing highly sensitive information, such as credit card details
- Hard-coding API keys, IP addresses, database credentials, and so on in the source code
- Hinting at the existence or absence of resources, usernames, and so on via subtle differences in application behavior.

## Sources of information disclosure

- Web crawler files like `robots.txt` and `sitemap.yml` which can reveal hidden directories.
- Web server automatic directory listings (poorly configured web servers can reveal hidden directories).
- Developer commesn in source code
- Error messages providing too much information
- Debug data in the response
- User account pages with poor authorization controls
- Backup files which can leak the application source code
- Insecure build pipeline or web server configuration
- Version control history


## How do information disclosure vulnerabilities arise?
Information disclosure vulnerabilities can arise in countless different ways, but these can broadly be categorized as follows:

- Failure to remove internal content from public content.
- Insecure configuration of the website and related technologies.
- Flawed design and behavior of the application. 

## Techniques

Information disclosure can be triggered and detected by:

- `Fuzzing`: sending a large number of requests with varying inputs to see how the application behaves.
- `Scanning`: using a tool like [Burp Scanner](https://portswigger.net/burp/vulnerability-scanner) to test for and identify information leakage during browsing.
- `Causing errors`: attempting to cause error conditions in the application to see what information is revealed in the error messages.

## What is the impact of information disclosure vulnerabilities?
Information disclosure vulnerabilities can have both a direct and indirect impact depending on the purpose of the website and, therefore, what information an attacker is able to obtain. In some cases, the act of disclosing sensitive information alone can have a high impact on the affected parties. For example, an online shop leaking its customers' credit card details is likely to have severe consequences.

On the other hand, leaking technical information, such as the directory structure or which third-party frameworks are being used, may have little to no direct impact. However, in the wrong hands, this could be the key information required to construct any number of other exploits. The severity in this case depends on what the attacker is able to do with this information.

## Prevent

- Ensure all members of the service team know what information is and isn't considered sensitive so that it can be treated consistenly.
- Keep error messages generic and devoid of technical details.
- Disable stack trace and log output to the user in production.
- Audit code and build logs for sensitive information.
- Ensure production services have a secure configuration that strips as mush identifying information as possible from the responses (e.g. response header fingerprinting).
