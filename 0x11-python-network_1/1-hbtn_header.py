#!/usr/bin/python3
"""A module that sends a request to the URL
   and displays the value of the X-Request-Id variable
   found in the header of the response"""
import urllib.request as request
import sys

url = sys.argv[1]
with request.urlopen(url) as response:
    data = response.headers
    print(data['X-Request-Id'])
