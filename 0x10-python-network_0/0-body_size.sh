#!/bin/bash

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
	echo "Please provide a URL as an argument."
	exit 1
fi

# Send the request and store the response in a temporary file
response=$(mktemp)
curl -s -o "$response" "$1"

# Get the size of the response in bytes
size=$(wc -c < "$response")

# Display the size of the response body
echo "Response body size: $size bytes"
