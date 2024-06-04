#!/usr/bin/python3
'''
module for the Reddit api recurse function
'''
import requests


def recurse(subreddit, hot_list=[], nxt=None):
    '''recursively returns the top 10 subscribers '''
    headers = {'User-agent': 'test'}
    res = requests.get("https://www.reddit.com/r/{}/hot.json?after={}"
                       .format(subreddit, nxt), headers=headers)
    try:
        data = res.json().get('data')
    except Exception:
        return None
    nxt = data.get('after')
    posts = data.get('children')
    for post in posts:
        hot_list.append(post['data']['title'])
    if nxt:
        recurse(subreddit, hot_list, nxt)
    return hot_list
