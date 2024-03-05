#!/bin/bash
# Sends GET request to URL, displays body of response for 200 status code

response = $(curl - s - o / dev/null - w "%{http_code}" $1)
if [$response - eq 200] then
curl - s $1
fi
