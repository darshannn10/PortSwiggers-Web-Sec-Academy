# Business logic vulnerabilities :bug:

![logic-flaws](https://user-images.githubusercontent.com/87711310/210128355-32eb2093-a10e-4ba8-a68d-e793a7613183.jpg)

## What are business logic vulnerabilities?
Business logic vulnerabilities are flaws in the design and implementation of an application that allow an attacker to elicit unintended behavior. This potentially enables attackers to manipulate legitimate functionality to achieve a malicious goal. These flaws are generally the result of failing to anticipate unusual application states that may occur and, consequently, failing to handle them safely.
Logic flaws are often invisible to people who aren't explicitly looking for them as they typically won't be exposed by normal use of the application. However, an attacker may be able to exploit behavioral quirks by interacting with the application in ways that developers never intended.

One of the main purposes of business logic is to enforce the rules and constraints that were defined when designing the application or functionality. Broadly speaking, the business rules dictate how the application should react when a given scenario occurs. This includes preventing users from doing things that will have a negative impact on the business or that simply don't make sense.

Flaws in the logic can allow attackers to circumvent these rules. 

Logic-based vulnerabilities can be extremely diverse and are often unique to the application and its specific functionality. Identifying them often requires a certain amount of human knowledge, such as an understanding of the business domain or what goals an attacker might have in a given context. This makes them difficult to detect using automated vulnerability scanners. As a result, logic flaws are a great target for bug bounty hunters and manual testers in general.

## How do business logic vulnerabilities arise?
Business logic vulnerabilities often arise because the design and development teams make flawed assumptions about how users will interact with the application. These bad assumptions can lead to inadequate validation of user input.

Ultimately, this means that when an attacker deviates from the expected user behavior, the application fails to take appropriate steps to prevent this and, subsequently, fails to handle the situation safely.
Logic flaws are particularly common in overly complicated systems that even the development team themselves do not fully understand

## What is the impact of business logic vulnerabilities?
The impact of business logic vulnerabilities can, at times, be fairly trivial. It is a broad category and the impact is highly variable. However, any unintended behavior can potentially lead to high-severity attacks if an attacker is able to manipulate the application in the right way. For this reason, quirky logic should ideally be fixed even if you can't work out how to exploit it yourself. There is always a risk that someone else will be able to.

Fundamentally, the impact of any logic flaw depends on what functionality it is related to, for example: 
- If the flaw is in the authentication mechanism, this could have a serious impact on your overall security.
- Flawed logic in financial transactions can obviously lead to massive losses for the business through stolen funds, fraud, and so on.

## Examples of Businness Logic Vulnerabilities
### Excessive trust in client-side controls
Assuming that requests will only come through the user interface and be subjected to client-side validation.  Easily bypassed by tools like Burp Suite.

### Failing to handle unconventional input
Bugs triggered by receiving user input that is not of the expected type or within the expected range (e.g. a negative number when only positive values are expected).  This must be caught with input and business logic validation.

### Making flawed assumptions about user behavior
Assuming that users will interact predictably.  This can include:
- Not following an expected workflow sequence; 
- Not providing all required input; and
- Not remaining trustworthy after initial authentication.

### Providing an encryption oracle
Occurs when user provided input is then returned as cipher text to the user.  This can allow the attacker to determine the encryption algorithm and key used by the application.

## Tips
- Look for all requests that submit input to the server and check if there is adequate server-side validation.
- Submit input that satisfies validation, but is outside of expected ranges (e.g. negative numbers in a scenario where they do not make sense).
- Attempt to bypass sections of workflows (skip ahead to the end).

## Prevent
1. Make sure all developers and testers understand the application logic.
1. Validate all user inputs.
1. Write clear, simple code that is easy to understand and test.
1. Break complex logic into smaller, simpler functions and ensure each function is thoroughly tested.
