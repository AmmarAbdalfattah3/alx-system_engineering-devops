#!/usr/bin/python3
"""display on the standard output the employee TODO list
   progress in this exact format
"""


import sys
import requests

api = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    employ_id = sys.argv[1]
    employ_info = requests.get('{}/users/{}'.format(api, employ_id))
    employ_info = employ_info.json()
    todos = requests.get('{}/todos?userId={}'.format(api, employ_id))
    todos = todos.json()
    comp_todos = []
    for todo in todos:
        if todo['completed'] is True:
            comp_todos.append(todo)
    print("Employee {} is done with tasks({}/{}):".format(employ_info['name'],
          len(comp_todos), len(todos)))
    for todo in comp_todos:
        print("\t {}".format(todo['title']))
