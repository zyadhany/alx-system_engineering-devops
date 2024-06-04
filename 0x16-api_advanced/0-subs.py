#!/usr/bin/python3
""" redeat api"""
import json
import requests
import sys

def number_of_subscribers(subreddit):
    """reddit API, return number subscribers """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    client = requests.get(url, headers=headers)
    
    if client.status_code == 200:
        return client.json()["data"]["subscribers"]
    else:
        return 0
