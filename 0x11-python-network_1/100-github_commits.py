#!/usr/bin/python3
'''
    This script lists 10 commits (from the most recent to oldest)
    of the repository “rails” by the user “rails”.
'''
if __name__ == '__main__':
    import sys
    import requests

    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/' + owner + '/'\
          + repo + '/' + 'commits'
    headers = {
            'accept': 'application/vnd.github+json',
            'owner': owner,
            'repo': repo
            }

    r = requests.get(url, headers=headers)
    line_no = 0

    # com means commit, hard to shorten for pycodestyle length issues.
    for com in r.json():
        print("{}: {}".format(com['sha'], com['commit']['author']['name']))
        line_no += 1
        if line_no == 10:
            break
