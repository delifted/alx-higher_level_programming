#!/usr/bin/python3
"""Script takes in a URL and an email, sends a POST request"""

import sys
from urllib import request, parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email parameter
    params = parse.urlencode({'email': email}).encode('utf-8')

    # Send the POST request and retrieve the response
    with request.urlopen(url, data=params) as response:
        body = response.read().decode('utf-8')

    print(body)
