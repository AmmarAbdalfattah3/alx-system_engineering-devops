#!/usr/bin/python3
"""display on the standard output the employee TODO list
   progress in this exact format
"""


import json
import requests
import sys

api = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    employ_id = sys.argv[1]
    file_name = '{}.json'.format(employ_id)
    employ_info = requests.get('{}/users/{}'.format(api, employ_id))
    employ_info = employ_info.json()
    todos = requests.get('{}/todos?userId={}'.format(api, employ_id))
    todos = todos.json()
    all_tasks = {}
    user_todos = []
    for task in todos:
        tasks = {'task': task.get('title'),
                 'completed': task.get('completed'),
                 'username': employ_info.get('username')}
        user_todos.append(tasks)
    all_tasks[str(employ_id)] = user_todos
    with open(file_name, mode="w") as json_file:
        json.dump(all_tasks, json_file)
