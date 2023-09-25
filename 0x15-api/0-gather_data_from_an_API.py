#!/usr/bin/python3
"""Script that uses REST API for given employee returns to-do list information for employee ID"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    done_tasks = [i.get("title") for i in todos if i.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done_tasks), len(todos)))
    [print("\t {}".format(j)) for j in done_tasks]
