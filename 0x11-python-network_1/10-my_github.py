#!/usr/bin/python3
'''
    This script takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id.
'''
if __name__ == '__main__':
    import sys
    import requests

    username = sys.argv[1]
    token = sys.argv[2]

    url = 'https://api.github.com/user'
    auth_headers = {
            'Accept': 'application/vnd.github+json',
            'Authorization': 'Bearer ' + token
            }

    r = requests.get(url, headers=auth_headers)

    if 'id' in r.json():
        print(r.json()['id'])
    else:
        print("None")
