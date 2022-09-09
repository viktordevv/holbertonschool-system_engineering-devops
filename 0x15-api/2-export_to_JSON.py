#!/usr/bin/python3
'''
Export to JSON
'''

import json
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(argv[1])).json()
    todo = requests.get(url + 'todos', params={'userId': argv[1]}).json()
    with open('{}.json'.format(argv[1]), 'w') as jsonfile:
        json.dump({argv[1]: [{
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': user.get('username')
        } for task in todo]}, jsonfile)
