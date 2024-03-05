#!/bin/bash

# Bash script to send request to URL and display the size of the response body

# Check if URL argument is provided
if [-z "$1"] then
echo "Usage: $0 <URL>"
exit 1
fi

# Send request to URL and store response in a variable
response = $(curl - sI "$1")

# Extract Content-Length header from response
content_length = $(echo "$response" |
grep - i "Content-Length" |
awk '{print $2}')
