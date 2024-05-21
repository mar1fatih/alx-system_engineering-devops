#!/usr/bin/python3
"""
Records all tasks from all employees.

"""
import json
import requests
from sys import argv


if __name__ == '__main__':

    _dict = {}

    _url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(_url).json()

    for usr in users:
        user_id = usr.get('id')
        user_name = usr.get('username')
        _url = "https://jsonplaceholder.typicode.com/users/" + str(user_id)
        user_tasks = requests.get(_url + '/todos').json()
        _dict[user_id] = []

        for user in user_tasks:
            completed = user.get('completed')
            title = user.get('title')
            _dict[user_id].append({"task": title,
                                   "completed": completed,
                                   "username": user_name})

    with open('todo_all_employees.json', 'w') as f:
        json.dump(_dict, f)
