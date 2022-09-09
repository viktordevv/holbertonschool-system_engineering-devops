#!/usr/bin/python3
'''
Export to CSV
'''

import csv
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(argv[1])).json()
    todo = requests.get(url + 'todos', params={'userId': argv[1]}).json()
    with open('{}.csv'.format(argv[1]), 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            writer.writerow([argv[1], user.get('username'),
                             task.get('completed'), task.get('title')])
