#!/usr/bin/python3
"""
    script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress
"""
import csv
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

    file = open(str(argv[1]) + ".csv", "w", )
    csv_w = csv.writer(file, quoting=csv.QUOTE_ALL)

    for data in todos_data:
        list_csv = []
        if int(argv[1]) == data.get("userId"):
            task_completed_status = data.get("completed")
            task_title = data.get("title")
            list_csv.append(user_id)
            list_csv.append(username)
            list_csv.append(task_completed_status)
            list_csv.append(task_title)
            csv_w.writerow(list_csv)

    file.close()
