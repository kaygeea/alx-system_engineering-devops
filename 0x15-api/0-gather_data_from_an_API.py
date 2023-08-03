#!/usr/bin/python3
"""Return information about an employee's TODO list progress"""
import json
import requests
from sys import argv, exit


if __name__ == "__main__":
    EmployeeId = argv[1]
    try:
        EmployeeId = int(EmployeeId)
    except ValueError:
        print('Employee ID must be a number! Please check your input.')
        exit(1)
    api_url = f"https://jsonplaceholder.typicode.com/users/{EmployeeId}"

    response = requests.get(api_url)
    EmployeeName = response.json().get('name')

    ToDoUrl = api_url + "/todos"
    response = requests.get(ToDoUrl)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(EmployeeName, done, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
