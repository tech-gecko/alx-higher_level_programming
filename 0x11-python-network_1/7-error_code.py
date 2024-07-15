#!/usr/bin/python3
''' This script takes in a URL, sends a request to the URL,
    displays the body of the response (decoded in utf-8) and
    handles HTTP Errors, using the 'requests' package.
'''

if __name__ == '__main__':
    import sys
    import requests

    req = requests.get(sys.argv[1])
    if req.status_code >= 400:
        print("Error code:", req.status_code)
    else:
        print(req.text)
