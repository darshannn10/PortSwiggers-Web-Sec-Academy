# PortSwigger's Web-Security-Academy Writeups

This repo contains my write-ups and scripts for solving the [PortSwigger WebSecurity Academy](https://portswigger.net/web-security). I plan to vaguely follow the learning path provided by PortSwigger, however, I expect to skip some of the expert-level labs initially.

## Topics

### Server-side
1. [SQL injection](SQL-Injection/)
2. [Authentication](Authentication/)
3. [Directory traversal](Directory%20Traversal/)
4. [Command injection](OS%20Command%20Injection/)
5. [Business logic vulnerabilities](Business%20Logic%20Vulnerabilities/)
6. [Information disclosure](Information%20Disclosure)
7. [Access control](Access%20Control/)
8. [File upload vulnerabilities](File%20Upload%20Vulnerabilities/)
9. [Server-side request forgery (SSRF)](Server-Side%20Request%20Forgery/)
10. [XML external entity (XXE) injection](XXE%20Injection)


## License

The content of this repo are study notes based on PortSwigger's [Web Security Academy](https://portswigger.net/web-security).  They hold all rights to any content that is not my own.

## Setup
```sh
# Install Homebrew, VirtualBox, Vagrant and create a Kali VM
curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh | bash
brew bundle
vagrant up
```

Optionally, configure Chromium to trust the Burp CA certificate:

1. In the VM, open Burp's integrated Chromium browser.
2. Go to `http://burpsuite` and download the `cacert.der` certificate.
3. Go to `chrome://settings/certificates` and select `Authorities`.
4. Click `Import`, select `cacert.der`, and trust for web identies.
