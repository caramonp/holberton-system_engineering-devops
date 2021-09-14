#!/usr/bin/python3
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
    tasks = []
    done_tasks = 0
    total_tasks = 0

    for info in response:
        if user_id == info.get('userId'):
                if info.get('completed') is True:
                    done_tasks += 1
                    tasks.append(info.get('title'))
                total_tasks += 1
        print("Employee {} is done with tasks({}/{}):"
              .format(user_name, done_tasks, total_tasks))

        for title in tasks:
            print('\t', title)
