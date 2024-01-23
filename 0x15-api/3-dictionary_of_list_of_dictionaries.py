#!/usr/bin/python3
"""
Gathers users data from an API and export to JSON
"""


import json
import requests

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    users = requests.get("{}/users".format(url)).json()

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump({
            u.get('id'): [{
                'username': u.get('username'),
                'task': t.get('title'),
                'completed': t.get('completed')
                } for t in requests.get("{}/todos".format(url),
                                        params={'userId': u.get('id')}).json()]
            for u in users}, jsonfile)
