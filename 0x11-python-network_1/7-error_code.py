#!/usr/bin/python3
"""A module that sends a request to the URL
   and displays the body of the response."""
import requests

url = sys.argv[1]
r = requests.get(url)
if r.status_code >= 400:
    print("Error code: {}".format(r.status_code))
else:
    print(r.text)
