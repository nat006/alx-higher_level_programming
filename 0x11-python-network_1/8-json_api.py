#!/usr/bin/python3

"""
This script takes letter, sends POST request to http://0.0.0.0:5000/search_user
with the letter as parameter, and displays the id and name if the JSON is valid
"""

import requests
import sys

if __name__ == '__main__':
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {'q': q}
    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        data = response.json()
        if data:
            print(f"[{data.get('id')}] {data.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
