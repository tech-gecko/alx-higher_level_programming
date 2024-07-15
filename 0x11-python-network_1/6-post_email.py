#!/usr/bin/python3
'''
    This script takes in a URL and an email, sends a POST request to
    the URL with the email as a parameter, and displays the body
    of the response (decoded in utf-8) all with 'requests'.
'''

if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]
    email_dict = {'email': sys.argv[2]}

    r = requests.post(url, data=email_dict)

    print(r.text)
