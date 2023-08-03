#!/usr/bin/python3
"""Return information about an employee's TODO list progress,
   then export data in the CSV format.
"""
import csv
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

    data_set = []

    for task in tasks:  # Create each row and append to data_set list
        complete_status = task.get('completed')
        title = task.get('title')
        data_row = [EmployeeId, EmployeeName, complete_status, title]
        data_set.append(data_row)

    with open(f'{EmployeeId}.csv', 'w', newline='') as user_file:
        writer_obj = csv.writer(user_file, quoting=csv.QUOTE_ALL)
        writer_obj.writerows(data_set)
