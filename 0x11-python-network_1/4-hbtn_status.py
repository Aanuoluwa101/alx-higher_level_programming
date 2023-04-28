#!/usr/bin/python3
"""A module that fetches https://alx-intranet.hbtn.io/status"""
import requests

r = requests.get('https://alx-intranet.hbtn.io/status')
txt = r.text
print('Body response:\n\t- type: {}\n\t- content: {}'
      .format(txt.__class__, txt))
