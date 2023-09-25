#!/usr/bin/python3
"""script that exports to-do list information
    for a given employee ID to JSON format."""

import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    landing_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(landing_url + "users/{}".format(user_id)).json()
    username = user.get("username")
    tasks = requests.get(landing_url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": j.get("title"),
                "completed": j.get("completed"),
                "username": username
            } for j in tasks]}, jsonfile)
