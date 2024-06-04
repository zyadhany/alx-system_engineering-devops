#!/usr/bin/python3
""" redeat api"""
import json
import requests
import sys


def number_of_subscribers(subreddit):
    """reddit API, return number subscribers """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    client = requests.session()
    r = client.get(url, allow_redirects=False)
    if r.status_code == 200:
        return (r.json()["data"]["subscribers"])
    else:
        return(0)