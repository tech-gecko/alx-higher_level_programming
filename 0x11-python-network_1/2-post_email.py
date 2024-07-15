#!/usr/bin/python3
'''
    This script takes in a URL and an email, sends a POST request to
    the URL with the email as a parameter, and displays the body
    of the response (decoded in utf-8).
'''

if __name__ == '__main__':
    import sys
    import urllib.parse
    import urllib.request

    url = sys.argv[1]
    email_dict = {'email': sys.argv[2]}
    email_data = urllib.parse.urlencode(email_dict)
    data = email_data.encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        body = response.read()

    print(body.decode('utf-8'))
