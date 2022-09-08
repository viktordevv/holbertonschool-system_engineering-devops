#!/usr/bin/python3
'''Gather data from an API'''
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(argv[1])).json()
    todo = requests.get(url + 'todos', params={'userId': argv[1]}).json()
    done = [task for task in todo if task.get('completed') is True]
    print('Employee {} is done with tasks({}/{}):'.format(
        user.get('name'), len(done), len(todo)))
    for task in done:
        print('\t {}'.format(task.get('title')))
