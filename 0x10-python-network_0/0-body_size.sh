#!/bin/bash

# Bash script to send request to URL and display size of the response body

# Check if URL argument is provided
if [-z "$1"] then
echo "Usage: $0 <URL>"
exit 1
fi

url = $1
response = $(curl - sI "$url" | grep - i content-length | awk '{print $2}')
if [-z "$response"] then
echo "Error: Could not get the content length of the response"
exit 1
fi

echo "Size of the response body: $response bytes"
