#!/usr/bin/python3
"""[returns information in json format]
"""
import json
import requests
import sys


if __name__ == "__main__":

    todos_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'
    response_todos = requests.get(todos_url.format(sys.argv[1]))
    response = response_todos.json()

    user_url = 'https://jsonplaceholder.typicode.com/users/{}'
    users_id = requests.get(user_url.format(sys.argv[1]))
    response_id = users_id.json()

    user_name = response_id.get('username')
    user_id = response_id.get('id')

    to_dict = {user_id: [{"task": i.get('title'),
                          "completed": i.get('completed'),
                          "username": user_name} for i in response]}

    with open("{}.json".format(sys.argv[1]), mode="w") as the_json:
        json.dump(to_dict, the_json)
