#!/usr/bin/python3
'''
    This script takes in a letter and sends a POST request to
    'http://0.0.0.0:5000/search_user' with the letter as a parameter,
    according to the requirements given.
'''

if __name__ == '__main__':
    import sys
    import requests

    url = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) == 1:
        letter_dict = {'q': ''}
    else:
        letter_dict = {'q': sys.argv[1]}

    r = requests.post(url, data=letter_dict)

    try:
        json = r.json()
        if json == {}:
            print("No result")
        else:
            print("[{}] {}".format(json['id'], json['name']))
    except ValueError:
        print("Not a valid JSON")
