#!/usr/bin/python3
"""display on the standard output the employee TODO list
   progress in this exact format
"""


import json
import requests
import sys

api = 'https://jsonplaceholder.typicode.com'
if __name__ == '__main__':
    file_name = 'todo_all_employees.json'
    users = requests.get('{}/users/'.format(api))
    users = users.json()
    emp_todos = {}
    for usr in users:
        emp_id = usr['id']
        todos = requests.get('{}/todos?userId={}'.format(api, emp_id))
        todos = todos.json()
        todos_copy = []
        for todo in todos:
            task = {'username': usr['username'],
                    'task': todo['title'],
                    'completed': todo['completed']
                    }
            todos_copy.append(task)
        emp_todos[str(emp_id)] = todos_copy
    with open(file_name, mode='w') as json_file:
        json.dump(emp_todos, json_file)
