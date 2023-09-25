#!/usr/bin/python3
"""Script that exports to-do list information of all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    landing_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(landing_url + "users").json()

    with open("todo_all_employees.json", "w") as info_file:
        json.dump({
            i.get("id"): [{
                "task": j.get("title"),
                "completed": j.get("completed"),
                "username": i.get("username")
            } for j in requests.get(landing_url + "todos",
                                    params={"userId": i.get("id")}).json()]
            for i in users}, info_file)
