#!/usr/bin/python3
"""A module that sends a request to the URL
   and displays the body of the response"""
import urllib.request as request
import urllib.error
import sys

url = sys.argv[1]
try:
    with request.urlopen(url) as response:
        data = response.read().decode('utf-8')
        print(data)
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
