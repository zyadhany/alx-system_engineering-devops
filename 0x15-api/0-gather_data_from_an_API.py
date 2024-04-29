#!/usr/bin/python3
""" get api to do """
import requests
import sys


def main():
    """ main function """

    id = sys.argv[1]
    name = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(id)).json()['name']
    todo = requests.get("https://jsonplaceholder.typicode.com/todos/?userId={}"
                        .format(id)).json()

    done = []

    for task in todo:
        if task['completed'] is True:
            done.append(task['title'])

    print('Employee {} is done with tasks({}/{}):'
          .format(name, len(done), len(todo)))

    for task in done:
        print("\t", task, sep=" ")


if __name__ == "__main__":
    main()
