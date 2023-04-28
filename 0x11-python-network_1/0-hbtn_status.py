#!/usr/bin/python3
"""A module that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request as request

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    with request.urlopen(url) as response:
        data = response.read()
        print('Body response:\n\t- type: {}\n\t- \
content: {}\n\t- utf8 content: {}'
              .format(data.__class__, data,
                      data.decode('utf-8')))
