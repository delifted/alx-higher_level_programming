#!/usr/bin/python3
"""Script fetches url header id"""

from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = request.urlopen(url)
    header = response.headers
    x_request_id = header.get('X-Request-Id')
    print("{}".format(x_request_id))
