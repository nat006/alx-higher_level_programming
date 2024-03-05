#!/bin/bash
# This script displays all HTTP methods accepted by the server for given URL

if ["$#" - ne 1] then
echo "Usage: $0 URL"
exit 1
fi

url = $1

options = $(curl - s - X OPTIONS - I $url | grep "Allow")
if [- n "$options"] then
echo "HTTP Methods accepted by the server for $url:"
echo "$options" | tr - d '\r'
else
echo "Server does not support OPTIONS method for $url"
fi
