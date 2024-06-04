#!/usr/bin/python3
""" the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com' +\
          '/r/{}/about.json'.format(subreddit)

    headers = {
            'User-Agent': "Mozilla/5.0"
            }
    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        return 0
    else:
        subs = res.json()['data']['subscribers']
        return subs
