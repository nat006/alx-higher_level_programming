#!/usr/bin/python3

"""
Sends req to URL, disps body of rspns. If stat code >=400 it prints error msg
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
