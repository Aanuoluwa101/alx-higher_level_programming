#!/usr/bin/python3
"""sends a POST request to http://0.0.0.0:5000/search_user
   with the letter as a parameter"""
import requests
import sys

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    r = requests.post(url, data={'q': q})
    try:
        data = r.json()
        if data:
            print('[{}] {}'.format(data['id'], data['name']))
        else:
            print('No result')
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')
