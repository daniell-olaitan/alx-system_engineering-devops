#!/usr/bin/python3
"""
Exports data from an API to a CSV file
"""


import csv
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    todos = requests.get(f"{url}/todos", params={'userId': sys.argv[1]}).json()
    username = requests.get(f"{url}/users/{sys.argv[1]}").json().get('name')

    with open("{}.csv".format(sys.argv[1]), mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            record = [sys.argv[1], username,
                      todo.get('completed'), todo.get('title')]

            csv_writer.writerow(record)
