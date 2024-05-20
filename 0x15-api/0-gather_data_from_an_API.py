#!/usr/bin/python3
"""
returns information about TODO list progress.

"""
import requests
from sys import argv

if __name__ == '__main__':

    Employee_name = None
    _list = []
    c = 0
    p = 0

    if len(argv) <= 1:
        exit()
    try:
        id = int(argv[1])
    except ValueError:
        exit()

    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    for item in response.json():
        if item.get('userId') == id:
            c += 1
            if item.get('completed') is True:
                p += 1
                _list.append(item.get('title'))

    response_2 = requests.get('https://jsonplaceholder.typicode.com/users')
    for item in response_2.json():
        if item.get('id') == id:
            Employee_name = item.get('name')

    if Employee_name:
        print('Employee {} is done with tasks({}/{}):'.format(Employee_name,
                                                              p, c))
        for item in _list:
            print('\t {}'.format(item))
