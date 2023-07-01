#!/bin/bash
# sends a request to the URL at $1, displays the size of the body
curl -s "$1" | wc -c
