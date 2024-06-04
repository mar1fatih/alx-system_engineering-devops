#!/usr/bin/python3
""" the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ Return the total number of subscribers """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    headers = {
            'User-Agent': "Mozilla/5.0"
            }
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code != 200 or res.json().get('data') is None:
        return 0
    else:
        subs = res.json().get('data')
        subs = subs.get('subscribers')
        return subs
