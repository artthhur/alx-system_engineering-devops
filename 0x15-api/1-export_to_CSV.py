#!/usr/bin/python3
"""
This script displays information about an employee's TODO list progress and
exports it to a CSV file.
"""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todo = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        employee = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [employee.writerow(
            [user_id, username, a.get("completed"), a.get("title")]
         ) for a in todo]
