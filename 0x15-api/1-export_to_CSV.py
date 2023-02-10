#!/usr/bin/python3
"""
   Export data in the CSV format
"""


import csv
import requests
import sys

api = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    employ_id = sys.argv[1]
    file_name = '{}.csv'.format(employ)
    employ_info = requests.get('{}/users/{}'.format(api, employ_id))
    employ_info = employ_info.json()
    todos = requests.get('{}/todos?userId={}'.format(api, employ_id))
    todos = todos.json()
    with open(file_name, mode="w") as csv_file:
        export = csv.writer(csv_file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        for row in todos:
            export.writerow((row['userId'], user_info['username'],
                             row['completed'], row['title']))
