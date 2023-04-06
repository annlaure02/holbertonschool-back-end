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

    dict2 = {}

    for data in users_data:
        user_id = data.get("id")
        username = data.get("username")
        list_dict = []
        for other_data in todos_data:
            if other_data.get("userId") == user_id:
                dict1 = {}
                dict1["username"] = username
                dict1["task"] = other_data.get("title")
                dict1["completed"] = other_data.get("completed")
                list_dict.append(dict1)
        dict2[user_id] = list_dict

    json_dict = json.dumps(dict2)
    with open("todo_all_employees.json", "w") as file:
        file.write(json_dict)
