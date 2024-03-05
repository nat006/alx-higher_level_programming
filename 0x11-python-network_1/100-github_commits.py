#!/usr/bin/python3

"""
Script that lists 10 commits of a repository from a given user on GitHub
"""

import requests
import sys

repo = sys.argv[1]
owner = sys.argv[2]
url = f"https://api.github.com/repos/{owner}/{repo}/commits"
response = requests.get(url)
commits = response.json()
for commit in commits[:10]:
    sha = commit.get('sha')
    author = commit.get('commit').get('author').get('name')
    print(f"{sha}: {author}")
