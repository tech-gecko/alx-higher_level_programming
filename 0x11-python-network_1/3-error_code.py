#!/usr/bin/python3
''' This script takes in a URL, sends a request to the URL,
    displays the body of the response (decoded in utf-8) and
    handles HTTP Errors.
'''

if __name__ == '__main__':
    import sys
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError

    req = Request(sys.argv[1])
    try:
        with urlopen(req) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
    else:
        pass
