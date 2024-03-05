#!/usr/bin/python3

"""
Takes URL, sends req to URL, displays value of var X-Req-Id in response header
"""

import requests
import sys

if __name__ == '__main':
    url = sys.argv[1]
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')
    print(request_id)
