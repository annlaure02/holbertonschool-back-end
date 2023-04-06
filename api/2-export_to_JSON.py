#!/usr/bin/python3
"""
    script to export data in the JSON format
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos_data = todos.json()
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users_data = users.json()

    for data in users_data:
        if int(argv[1]) == data.get("id"):
            user_id = data.get("id")
            username = data.get("username")

    list_dict = []

    for data in todos_data:
        dict1 = {}
        if int(argv[1]) == data.get("userId"):
            dict1["task"] = data.get("title")
            dict1["completed"] = data.get("completed")
            dict1["username"] = username
            list_dict.append(dict1)

    dict2 = {}
    dict2[user_id] = list_dict

    json_dict = json.dumps(dict2)
    with open(str(argv[1]) + ".json", "w") as file:
        file.write(json_dict)
