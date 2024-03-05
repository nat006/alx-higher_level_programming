#!/usr/bin/python3

"""
Mod sends POST rqst to URL w/ email as para, displays rspnse decoded in utf-8
"""

import urllib.parse
import urllib.request
import sys

if __name__ == '__main':
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
