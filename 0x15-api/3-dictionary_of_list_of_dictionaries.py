#!/usr/bin/python3
"""Retrieves TODO data of all employees via a REST API,
   then exports the data in JSON format.
"""
import json
import requests
from sys import argv, exit


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(api_url)
    employees = response.json()

    dictionary = {}
    for employee in employees:
        employeeId = employee.get('id')
        employeeName = employee.get('username')
        api_url = 'https://jsonplaceholder.typicode.com/users/{}'.\
            format(employeeId)
        api_url = api_url + '/todos/'
        response = requests.get(api_url)
        tasks = response.json()
        dictionary[employeeId] = []
        for task in tasks:
            dictionary[employeeId].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": employeeName
            })
    with open('todo_all_employees.json', 'w') as data_file:
        json.dump(dictionary, data_file)
