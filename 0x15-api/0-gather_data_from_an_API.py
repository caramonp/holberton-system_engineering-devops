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

    todos_len = 0
    todos_arr = []
    for i in response:
        if i.get("completed"):
            todos_arr.append(i)
            todos_len += 1

    print("Employee {} is done with tasks({}/{}):".format(
          user_name, todos_len, len(response)))

    for i in todos_arr:
        print("\t {}".format(i.get("title")))
