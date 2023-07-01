#!/bin/bash
if [ -z "$1" ]; then echo "Please provide a URL as an argument."; exit 1; fi
response=$(mktemp); curl -s -o "$response" "$1"; size=$(wc -c < "$response"); echo "$size"; rm "$response"

