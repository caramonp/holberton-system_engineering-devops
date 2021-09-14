#!/usr/bin/python3
"""[returns information in csv format]
"""
import csv
import requests
import sys


if __name__ == "__main__":

    todos_url = 'https://jsonplaceholder.typicode.com/todos/'
    response_todos = requests.get(todos_url)
    response = response_todos.json()

    user_url = 'https://jsonplaceholder.typicode.com/users/{}'
    users_id = requests.get(user_url.format(sys.argv[1]))
    response_id = users_id.json()

    user_name = response_id.get('name')
    user_id = response_id.get('id')

    with open('{}.csv'.format(sys.argv[1]), mode='w') as csv_id:
        j = csv.writer(csv_id, quoting=csv.QUOTE_ALL)

        for info in response:
            j.writerow([user_id, user_name, info.get('completed'),
                        info.get('title')])
