#!/usr/bin/python3
"""
gathers data from an API
"""


import requests
from sys import argv

if __name__ == '__main__':
    if argv[1].isdigit():
        id = int(argv[1])
        user_url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
        todos_url = f'https://jsonplaceholder.typicode.com/todos'
        r = requests.get(user_url)
        name = r.json().get('name')
        r = requests.get(todos_url)
        todos = r.json()
        if name is not None:
            titles = []
            total = 0
            total_done = 0
            for todo in todos:
                if id == todo.get("userId"):
                    total += 1
                    if todo.get("completed"):
                        total_done += 1
                        titles.append(todo.get("title"))

            print("Employee {} is done with tasks({}/{}):".format(
                name, total_done, total))
            for title in titles:
                print("\t {}".format(title))
