#!/usr/bin/python3
"""Return information about an employee's TODO list progress,
   then export data in the JSON format.
"""
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
    EmployeeName = response.json().get('username')

    ToDoUrl = api_url + "/todos"
    response = requests.get(ToDoUrl)
    tasks = response.json()
    json_dict = {EmployeeId: []}

    for task in tasks:
        json_dict[EmployeeId].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": EmployeeName
            })

    with open('{}.json'.format(EmployeeId), 'w', newline='') as data_file:
        json.dump(json_dict, data_file)
