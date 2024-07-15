#!/usr/bin/python3
''' This script fetches URLs from a resource, and returns...
 ...results according to the format required.
'''

if __name__ == '__main__':
    import urllib.request
    with urllib.request.urlopen('https://intranet.hbtn.io/status')\
         as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf-8 content: {}".format(body.decode('utf-8')))
