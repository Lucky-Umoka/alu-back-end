#!/usr/bin/python3
"""
Using a REST API, returns the TODO list progress of an employee.
"""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    base = "https://jsonplaceholder.typicode.com"

    user = requests.get(f"{base}/users/{employee_id}").json()
    todos = requests.get(f"{base}/todos",
                         params={"userId": employee_id}).json()

    done = [t["title"] for t in todos if t["completed"]]
    total = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(
        user["name"], len(done), total))
    for title in done:
        print("\t {}".format(title))
