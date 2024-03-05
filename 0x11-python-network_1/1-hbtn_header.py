#!/usr/bin/python3

"""
Module sends rqst to URL, displays value of X-Rqst-Id var in response header
"""

import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))
