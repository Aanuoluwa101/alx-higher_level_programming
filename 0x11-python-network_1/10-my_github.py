#!/usr/bin/python3
"""A module that takes a user's GitHub credentials (username and password)
   and uses the GitHub API to display the user's id"""
import requests
import sys

username = sys.argv[1]
psswd = sys.argv[2]
url = "https://api.github.com/users/" + username
token = 'Bearer ' + psswd
headers = {'Authorization': token,
           'X-GitHub-Api-Version': '2022-11-28'}
r = requests.get(url, headers=headers)
data = r.json()
print(data['id'])
