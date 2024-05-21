#!/usr/bin/python3
"""
export data in the CSV format.

"""

import requests
from sys import argv


if __name__ == '__main__':
    if len(argv) <= 1:
        exit()
    try:
        id = int(argv[1])
    except ValueError:
        exit()

    _url = 'https://jsonplaceholder.typicode.com/'
    username = requests.get(_url + 'users/' + str(id)).json().get('username')
    todos = requests.get(_url + 'users/' + str(id) + '/todos').json()

    with open('{}.csv'.format(id), 'w') as cvs:
        for todo in todos:
            title = todo.get('title')
            completed = todo.get('completed')

            cvs.write('"{}","{}","{}","{}"\n'.format(id,
                                                     username,
                                                     completed,
                                                     title))
