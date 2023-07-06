#!/usr/bin/python3
"""Script takes in a URL and an email, sends a POST request"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email parameter
    params = {'email': email}

    # Send the POST request and retrieve the response
    res = requests.post(url, data=params)

    print(res.text)
