#!/usr/bin/python3
"""
This script displays information about an employee's TODO list progress and
exports it to JSON format.
"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            c.get("id"): [{
                "task": a.get("title"),
                "completed": a.get("completed"),
                "username": c.get("username")
            } for a in requests.get(url + "todos",
                                    params={"userId": c.get("id")}).json()]
            for c in users}, jsonfile)
