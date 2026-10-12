#!/usr/bin/python3
"""
Exports an employee's TODO list to a CSV file named USER_ID.csv.
"""
import csv
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    base = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(base, employee_id)).json()
    todos = requests.get("{}/todos".format(base),
                         params={"userId": employee_id}).json()

    with open("{}.csv".format(employee_id), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow([employee_id, user["username"],
                             t["completed"], t["title"]])
