#!/bin/bash

# Script to send a request to a URL and display the size of the response body in bytes

# Check if URL is provided as argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 [URL]"
    exit 1
fi

# Send request to the URL and store the response body in a temporary file
response=$(curl -sI "$1" | grep -i 'Content-Length' | awk '{print $2}')

# Display the size of the response body in bytes
echo "Response Body Size: $response bytes"
