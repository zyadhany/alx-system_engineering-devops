#!/usr/bin/python3
""" get api to do """
import json
import requests
import sys


def main():
    """ main function """

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    info = {}

    for user in users:
        id = user['id']
        name = user['username']
        tdos = requests.get(
            "https://jsonplaceholder.typicode.com/todos/?userId={}"
            .format(id)).json()
        tasks = []
        for todo in tdos:
            task = {"task": todo.get("title"),
                    "completed": todo.get("completed"), "username": name}
            tasks.append(task)
        info[id] = tasks

    with open('{}.json'.format(id), 'w+') as file:
        file.write(json.dumps(info))


if __name__ == "__main__":
    main()
