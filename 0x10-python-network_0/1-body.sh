#!/bin/bash
# Takes a URL, sends GET request and displays response body
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q 200 && curl -s "$1"
