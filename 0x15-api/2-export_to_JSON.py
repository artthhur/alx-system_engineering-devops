#!/usr/bin/python3
"""
This script displays information about an employee's TODO list progress and
exports it to JSON format.
"""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    user_name = user.get("username")
    todo = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": a.get("title"),
                "completed": a.get("completed"),
                "username": user_name
            } for a in todo]}, jsonfile)
