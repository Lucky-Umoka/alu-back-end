#!/usr/bin/python3
"""
Exports every employee's TODO list to todo_all_employees.json.
"""
import json
import requests


if __name__ == "__main__":
    base = "https://jsonplaceholder.typicode.com"

    users = requests.get("{}/users".format(base)).json()
    todos = requests.get("{}/todos".format(base)).json()

    usernames = {u["id"]: u["username"] for u in users}
    data = {str(uid): [] for uid in usernames}

    for t in todos:
        uid = t["userId"]
        data[str(uid)].append({"username": usernames[uid],
                               "task": t["title"],
                               "completed": t["completed"]})

    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
