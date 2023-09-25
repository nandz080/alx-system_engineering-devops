#!/usr/bin/python3
"""Script that uses REST API to exports to-do list
    information for a given employee ID to CSV format."""

import csv
import requests
import sys

if __name__ == '__main__':
    employeeId = sys.argv[1]
    landing_url = "https://jsonplaceholder.typicode.com/users"
    url = landing_url + "/" + employeeId

    response = requests.get(url)
    username = response.json().get('username')

    url_todo = url + "/todos"
    response = requests.get(url_todo)
    tasks = response.json()

    with open('{}.csv'.format(employeeId), 'w') as file:
        for t in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employeeId, username, t.get('completed'),
                               t.get('title')))
