#!/usr/bin/python3
"""
Exports an employee's TODO list to a JSON file named USER_ID.json.
"""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    base = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(base, employee_id)).json()
    todos = requests.get("{}/todos".format(base),
                         params={"userId": employee_id}).json()

    tasks = [{"task": t["title"],
              "completed": t["completed"],
              "username": user["username"]} for t in todos]

    with open("{}.json".format(employee_id), "w") as f:
        json.dump({employee_id: tasks}, f)
