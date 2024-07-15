#!/usr/bin/python3
'''
    This script that takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id variable found
    in the response header, all by using the 'requests' package.
'''

if __name__ == '__main__':
    import sys
    import requests

    r = requests.get(sys.argv[1])
    if 'X-Request-Id' in r.headers:
        print(r.headers['X-Request-Id'])
