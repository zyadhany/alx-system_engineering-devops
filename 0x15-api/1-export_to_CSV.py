#!/usr/bin/python3
""" get api to do """
import csv
import requests
import sys


def main():
    """ main function """

    id = sys.argv[1]
    name = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(id)).json()['username']
    tdos = requests.get("https://jsonplaceholder.typicode.com/todos/?userId={}"
                        .format(id)).json()

    with open('{}.csv'.format(id), 'w+') as file:
        for todo in tdos:
            info = '"{}","{}","{}","{}"\n'.format(
                id, name, todo.get('completed'), todo.get('title'))
            file.write(info)


if __name__ == "__main__":
    main()
