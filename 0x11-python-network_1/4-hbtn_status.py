#!/usr/bin/python3
''' This script fetches the url https://alx-intranet.hbtn.io/status
    using the 'requests' package and displays the body of the
    response according to the required format.
'''

if __name__ == '__main__':
    import requests

    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
