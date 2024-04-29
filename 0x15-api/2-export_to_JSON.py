#!/usr/bin/python3
""" get api to do """
import json
import requests
import sys


def main():
    """ main function """

    id = sys.argv[1]
    name = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(id)).json()['username']
    tdos = requests.get("https://jsonplaceholder.typicode.com/todos/?userId={}"
                        .format(id)).json()

    with open('{}.json'.format(id), 'w+') as file:
        tasks = []
        for todo in tdos:
            task = {"task": todo.get("title"),
                    "completed": todo.get("completed"), "username": name}
            tasks.append(task)
        file.write(json.dumps({id: tasks}))


if __name__ == "__main__":
    main()
