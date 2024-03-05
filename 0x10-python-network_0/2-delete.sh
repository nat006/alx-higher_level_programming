#!/bin/bash
# This script sends DELETE request to URL, displays the body of the response

if ["$#" - ne 1] then
echo "Usage: $0 URL"
exit 1
fi

response = $(curl - s - o / dev/null - w "%{http_code}" - X DELETE "$1")
if [$response - eq 200] then
curl - s - X DELETE "$1"
fi
