#!/usr/bin/python3
"""A module that list 10 commits
   (from the most recent to oldest) of a repository"""
import requests
import sys

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/" + owner + '/' + repo + '/commits'
    r = requests.get(url)
    for index, commit in enumerate(r.json()):
        if index > 9:
            break
        else:
            print('{}: {}'.format(commit['sha'],
                  commit['commit']['author']['name']))
