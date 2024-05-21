#!/usr/bin/python3
"""
export data in the JSON format.

"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    if len(argv) <= 1:
        exit()
    try:
        user_id = int(argv[1])
    except ValueError:
        exit()

    _dict = {user_id: []}

    user_url = 'https://jsonplaceholder.typicode.com/users/' + str(user_id)
    user_name = requests.get(user_url).json().get('username')
    todos = requests.get(user_url + '/todos').json()

    for todo in todos:
        completed = todo.get('completed')
        title = todo.get('title')
        _dict[user_id].append({"task": title,
                               "completed": completed,
                               "username": user_name})
    with open('USER_ID.json', 'w') as js_file:
        json.dump(_dict, js_file)
